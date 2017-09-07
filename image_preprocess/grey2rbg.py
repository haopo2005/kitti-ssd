#-*- coding: UTF-8 -*- 
import os
import sys
from PIL import Image 

if __name__ == "__main__":
	rootdir = sys.argv[1]
	list = os.listdir(rootdir) 
	for i in range(0,len(list)):
		image_path = os.path.join(rootdir,list[i])
		new_img = '/home/jst/share/new/'+image_path.split('.')[0]+'.jpg'
		img = Image.open(image_path)
		img = img.convert("RGB")
		img.save(new_img)
		#print new_img
