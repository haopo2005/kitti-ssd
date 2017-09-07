#-*- coding: UTF-8 -*- 
import os
import sys

if __name__ == "__main__":
	rootdir = sys.argv[1]
	os.system('cd '+rootdir)
	a = 3999
	list = os.listdir(rootdir) 
	for i in range(0,len(list)):
		path = os.path.join(rootdir,list[i])
		sub_list = os.listdir(path)
		sub_list = sorted(sub_list)
		for j in range(0,len(sub_list)):
			sub_path = os.path.join(path,sub_list[j]) #jpg
			houzhui = sub_path.split('.')[1]
			if houzhui == 'jpg':
				os.system('cp '+ sub_path +' /home/jst/share/project/HUST/images/' + str(a)+".jpg")
				sub_txt = sub_path.split('.')[0]+".txt"
				os.system('cp '+ sub_txt +' /home/jst/share/project/HUST/labels/' + str(a)+".txt")
				a = a + 1
				print a
