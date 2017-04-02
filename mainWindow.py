# coding=gbk
# auth : ocean

import pika
import sys
from PyQt4 import QtGui, QtScript


# ######################### ������ #########################
credentials = pika.PlainCredentials('guest', 'guest')

# ����rabbit��������localhost�Ǳ�����������������������޸�Ϊip��ַ��

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.39', 5672, '/', credentials))

# ����Ƶ��
channel = connection.channel()

# ������Ϣ���У���Ϣ������������н��д��ݡ��������Ϣ���͵������ڵĶ��У�rabbitmq�����Զ������Щ��Ϣ��������в����ڣ��򴴽�
channel.queue_declare(queue='hello',durable=True)
channel.exchange_declare(exchange='logs_fanout',type='fanout')

# exchange -- ��ʹ�����ܹ�ȷ�е�ָ����ϢӦ�õ��ĸ�����ȥ��
# ����в�����ֵ routing_key�Ƕ����� body��Ҫ���������
channel.basic_publish(exchange='test.test',
                      routing_key='hello',
                      body='Hello World!')

print("���ͳɹ�")

# �������Ѿ�flush������Ϣ�Ѿ�ȷ�Ϸ��͵���RabbitMQ�У��ر�����
connection.close()


# ########################## ������ ##########################
credentials = pika.PlainCredentials('admin', 'admin')
# ���ӵ�rabbitmq������
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.103',5672,'/',credentials))
channel = connection.channel()

# ������Ϣ���У���Ϣ������������н��д��ݡ�������в����ڣ��򴴽�
channel.queue_declare(queue='wzg',durable=True)


# ����һ���ص�������������ߵĻص��������ǽ���Ϣ��ӡ������
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# ����rabbitmqʹ��callback��������Ϣ
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

 # no_ack=True��ʾ�ڻص������в���Ҫ����ȷ�ϱ�ʶ

print(' [*] Waiting for messages. To exit press CTRL+C')

# ��ʼ������Ϣ������������״̬������������Ϣ�Ż����callback���д�����ctrl+c�˳���
channel.start_consuming()