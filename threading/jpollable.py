# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
一个比较巧妙的轮询多线程队列方法：利用隐藏的环回（loopback）网络连接。

针对每个想要轮询的队列（或任何对象），创建一对互联的socket。然后对其中一个
socket执行写操作，以此表示数据存在。另一个socket就传递给select()或者类似的
函数来轮询数据。
'''
from  __future__ import unicode_literals
try:
	import queue
except ImportError:
	import Queue as queue
import socket
import os
import select
import threading
import time


class PollableQueue(queue.Queue, object):
	'''
	一个轮询多线程队列方法
	'''
	def __init__(self):
		super(PollableQueue, self).__init__()

		if os.name == "posix":
			self._putsocket, self._getsocket = socket.socketpair()
		else:
			server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			server.bind(("localhost", 0))
			server.listen(1)
			self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self._putsocket.connect(server.getsockname())
			self._getsocket, _ = server.accept()
			server.close()

	def fileno(self):
		'''
		此方法使得这个队列可以用类似select()这样的函数来轮询。
		基本上，fileno()方法只是暴露出底层由get()函数所使用的socket的文件描述符。
		'''
		return self._getsocket.fileno()

	def put(self, item):
		'''
		在将数据放入队列之后，对其中一个socket写入一个字节的数据。
		'''
		super(PollableQueue, self).put(item)
		self._putsocket.send(b'x')

	def get(self):
		'''
		当要把数据从队列中取出时，此方法就从另一个socket中把一个字节读取出来。
		'''
		self._getsocket.recv(1)
		return super(PollableQueue, self).get()


def consumer(queues):
	'''
	定义一个消费者，用来再多个队列上监视是否有数据到来。
	'''
	while True:
		can_read, _, _ = select.select(queues, [], [])
		for r in can_read:
			item = r.get()
			print(item.name, item.add())



class Test():
	'''
	测试类，作为传入的对象进行测试
	'''
	def __init__(self, a=0, f=""):
		self.a = a
		self.b = 100
		self.name = str(a) + f

	def add(self):
		return self.a + self.b



if __name__ == "__main__":
	q1 = PollableQueue()
	q2 = PollableQueue()

	t = threading.Thread(target=consumer, args=([q1, q2], ))
	t.daemon = True
	t.start()

	# 下面属于生产者，测试

	q1.put(Test(127))
	time.sleep(1)
	q1.put(Test(15))
	time.sleep(1)
	q2.put(Test(36))
	time.sleep(1)
	q2.put(Test(1))
	time.sleep(1)
	q1.put(Test(99))

	# i = 1
	# n = 0
	# while True:
	# 	if i > 30:
	# 		i = 0
	#
	# 	if i != 0:
	# 		q1.put(Test(i))
	#
	# 	if i > 15:
	# 		q2.put(Test(n, f="2222222222"))
	# 		n += 1
	# 	i += 1
	#
	# 	if n > 27:
	# 		break
	#
	# 	time.sleep(0.2)





