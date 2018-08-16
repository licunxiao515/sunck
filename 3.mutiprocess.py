from multiprocessing import Process,Manager

def foo(i,dic):
	dic[i] = i


if __name__ == "__main__":
	manager = Manager()
	dic = manager.dict()
	pro_list = []
	for i in range(10):
		p = Process(target=foo,args=(i,dic))
		p.start()
		pro_list.append(p)
	for pro in pro_list:
		pro.join()

	print(pro_list)



