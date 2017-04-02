# coding=utf-8
__author__ = 'lihy'
import sys
import  pika
import execjs

from time import ctime,sleep
from PyQt4 import QtCore, QtGui
import datetime

# MQUtil工具类
class MQUtils:

    #初始化操作
    def __init__(self,mainWindowObj):
        self._conn_result = None
        # 发送结果对象
        self._send_result = {}
        # 消费消息数量
        self._consumeMsgCount = 0
        # 消费处理异常数量
        self._consumeErrorMsgCount = 0
        # 消费处理的脚本内容
        self._scriptBody = None
        # 保存转发的服务器配置信息
        self._sc_server_info = None
        # 转发服务器连接
        self._sc_connection = None
        # 发送服务器连接
        self._send_connection = None
        # 当前发送channel
        self._current_send_channel = None
        # 当前监听chnaanel
        self._current_listen_channnel = None
        # 是否停止
        self._stopFlag = False
        # 主窗口对象
        self._mainWindowObj = mainWindowObj

    # 连接MQ服务器
    def connMQServer(self,server,port,vhost,credentials):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters( server , int(port), vhost , credentials))
            connection.close()
            self._conn_result = True
        except Exception ,e:
            self._conn_result = False

    # 得到连接结果
    def getConnResult(self):
        return self._conn_result

    # 得到发送结果
    def getSendResult(self):
        return self._send_result

    # 得到发送Channel
    def getCurrentSendChannel(self,server,port,vhost,credentials,exchangeType,exchangeName,QueueName,rKey):

        # 当前发MQ连接
        if ( self._send_connection == None ):
            self._send_connection = pika.BlockingConnection( pika.ConnectionParameters(
                                                                         server,
                                                                         int(port),
                                                                         vhost ,
                                                                         credentials
                                                                     ))
            # 连接重连，则channel置空
            self._current_send_channel = None

        if (self._current_send_channel == None):
            # 创建频道
            self._current_send_channel = self._send_connection.channel()

            # 声明消息队列，消息将在这个队列中进行传递。如果将消息发送到不存在的队列，rabbitmq将会自动清除这些消息。如果队列不存在，则创建
            self._current_send_channel.queue_declare(queue= QueueName,durable=True)
            self._current_send_channel.exchange_declare(exchange=exchangeName,type=exchangeType)

            # 将队列与exchange进行绑定
            self._current_send_channel.queue_bind(exchange=exchangeName,queue=QueueName,routing_key=rKey)

        return self._current_send_channel

    # 发送MQ消息
    def sendMessage(self,server,port,vhost,credentials,exchangeType,exchangeName,QueueName,rKey,msgBody,sendCount):
        try:
            #connection = pika.BlockingConnection(pika.ConnectionParameters( server , int(port), vhost , credentials))
            # 得到频道
            channel = self.getCurrentSendChannel(server,port,vhost,credentials,exchangeType,exchangeName,QueueName,rKey)

            # 声明消息队列，消息将在这个队列中进行传递。如果将消息发送到不存在的队列，rabbitmq将会自动清除这些消息。如果队列不存在，则创建
            # channel.queue_declare(queue=QueueName,durable=True)
            # channel.exchange_declare(exchange=exchangeName,type=exchangeType)

            # 将队列与exchange进行绑定
            # channel.queue_bind(exchange=exchangeName,queue=QueueName,routing_key=rKey)

            # 向队列插入数值 routing_key是队列名 body是要插入的内容
            _stime = datetime.datetime.now().second
            for i in range(sendCount):
                channel.basic_publish(exchange= exchangeName,
                                      routing_key=rKey,
                                      body=msgBody)

                statusText = u"已发送:" + str(i+1) + u"耗时：" + str( datetime.datetime.now().second -_stime ) + u"秒"

                # print statusText
                self.updateMainWindowStatus(statusText,1)

                # 更新主界面，防止死掉
                if i % 10 == 0:
                    self._mainWindowObj._app.processEvents()

            # connection.close()
            self._mainWindowObj.sendMsgBtn.setDisabled(False);
            self._send_result['send_result'] = 'ok'
            self._send_result['send_count'] = sendCount
            print(u"发送完成")
        except Exception ,e:
            print e
            self._send_result['send_result'] = 'fail'
            self._send_result['error_msg'] = repr(e)

    # 回复MQ消息
    def replyMessage(self,msgBody):
        try:
            channel  = self.getSCSendChannel()
            # 转发消息
            channel.basic_publish(exchange= self._sc_server_info['exchangeName'],
                                      routing_key=self._sc_server_info['rtkey'],
                                      body=msgBody)
        except Exception ,e:
            print repr(e)

    # 停止监听
    def stop(self):
        self._stopFlag = True

    # 停止当前监听
    def stopListenMessage(self):
        if self._current_listen_channnel != None:
            try:
                self._current_listen_channnel.stop_consuming()
            except Exception ,e:
                print u"停止监听失败,ErrorMsg:"+repr(e)

    # 监听动作处理
    def ListenMessage(self,server,port,vhost,credentials,listenQueue,scriptBody,sc_server_info):
        self._stopFlag = False
        self._scriptBody = scriptBody
        self._sc_server_info = sc_server_info

        # 链接rabbit
        connection = pika.BlockingConnection(pika.ConnectionParameters(server,port,vhost,credentials))
        # 创建频道
        self._current_listen_channnel = connection.channel()
        # 如果生产者没有运行创建队列，那么消费者创建队列
        # channel.queue_declare(queue = listenQueue , durable = True)
        #以ACK模式接收
        self._current_listen_channnel.basic_consume(self.recvMessage,
                              queue  = listenQueue,
                              no_ack = False)

        print(' [*] Waiting for messages. ')
        self._current_listen_channnel.start_consuming()

    # 得到转发的服务连接
    def getSCSendChannel(self):
        if ( self._sc_connection == None ):
            self._sc_connection = pika.BlockingConnection( pika.ConnectionParameters(
                                                                         self._sc_server_info['server'],
                                                                         int( self._sc_server_info['port'] ),
                                                                         self._sc_server_info['vhost'] ,
                                                                         pika.PlainCredentials(
                                                                                                self._sc_server_info['uname'],
                                                                                                self._sc_server_info['upass']
                                                                                                )
                                                                     ) )

        # 创建频道
        channel = self._sc_connection.channel()

        # 声明消息队列，消息将在这个队列中进行传递。如果将消息发送到不存在的队列，rabbitmq将会自动清除这些消息。如果队列不存在，则创建
        channel.queue_declare(queue=self._sc_server_info['queueName'],durable=True)
        channel.exchange_declare(exchange=self._sc_server_info['exchangeName'],type=self._sc_server_info['exchangeType'])

        # 将队列与exchange进行绑定
        channel.queue_bind(exchange=self._sc_server_info['exchangeName'],queue=self._sc_server_info['queueName'],routing_key=self._sc_server_info['rtkey'])
        return channel

    # 更新主界面状态栏 kind==0是消费状态，1是发送状态
    def updateMainWindowStatus(self,statusText,kind):
         if self._mainWindowObj!=None and int(kind) == 0:
             labelObj = self._mainWindowObj.findChild(QtGui.QLabel,QtCore.QString.fromUtf8("consumer_label"))
             labelObj.setText(statusText)
             labelObj.update()
         else:
             labelObj = self._mainWindowObj.findChild(QtGui.QLabel,QtCore.QString.fromUtf8("sender_label"))
             labelObj.setText(statusText)
             labelObj.update()

    # 消息消费处理
    def recvMessage(self,ch, method, properties, body):
        if self._stopFlag == True:
            self.stopListenMessage()
            return

        # 消费计数器
        self._consumeMsgCount += 1
        bodyMsg = body.decode('utf8')

        # 调用消费逻辑进行处理
        try:
            ctx = execjs.compile( self._scriptBody )
            # 将消费的信息传入脚本函数中进行处理
            ret_value = ctx.call("MsgCallback",bodyMsg)
            print ret_value

            # 处理完成后，是否发送到其他队列中
            if self._sc_server_info['is_recv_sendflag'] == False:
                self.replyMessage( ret_value )

            # 确认消费
            ch.basic_ack(delivery_tag = method.delivery_tag)
            # 更新主界面，防止死掉
            self._mainWindowObj._app.processEvents()

        except Exception as err:
            self._consumeErrorMsgCount += 1
            print unicode(repr(err))

        statusText = u"已消费:" + str(self._consumeMsgCount) +u" 消费异常数:" + str(self._consumeErrorMsgCount)
        self.updateMainWindowStatus(statusText,0)
        print statusText
