#-*- coding: UTF-8 -*- 
import os
import sys

if __name__ == "__main__":
	rootdir = sys.argv[1]
	os.system('cd '+rootdir)
	list = os.listdir(rootdir) 
	for i in range(0,len(list)):
		path = os.path.join(rootdir,list[i])#label
		shit = path.split('.')[0].split('/')
		img_Name= '/home/jst/share/project/HUST/images/' + shit[len(shit)-1]+'.jpg'#image
		os.system('./verify_image '+path+' '+img_Name+' '+str(i)+'.jpg')
		
