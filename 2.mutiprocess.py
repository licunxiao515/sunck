from multiprocessing import Process,Manager,Queue
import time

def foo(i,q):
	q.put(i)


if __name__ == '__main__':
	print(time.ctime())
	q = Queue()

	pro_list = []
	for i in range(10):
		p = Process(target=foo,args=(i,q))
		p.start()
		pro_list.append(p)

	for pro in pro_list:
		pro.join()

	while not q.empty():
		print(q.get())

	print(time.ctime())