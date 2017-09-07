#-*- coding: UTF-8 -*- 
import os
import sys

if __name__ == "__main__":
	rootdir = sys.argv[1]
	os.system('cd '+rootdir)
	list = os.listdir(rootdir) 
	for i in range(0,len(list)):
		path = os.path.join(rootdir,list[i])
		shit = path.split('.')[0].split('/')
		#print shit
		filename = '/home/jst/share/project/HUST/acc_labels/'+ shit[len(shit)-1] + '.txt'
		#print filename
		file_obj = open(path, 'r')
		content = file_obj.read()
		if len(content) == 0:
			file_obj.close()
			img_Name= '/home/jst/share/project/HUST/images/' + shit[len(shit)-1]+'.jpg'
			os.remove(path)
			os.remove(img_Name)
		else:
			ff = open(filename, 'w+')
			shit2 = content.strip().split('\r\n')
			#print shit2
			for line in shit2:
				info = line.split(' ')
				#print info
				x = float(info[0])
				y = float(info[1])
				w = float(info[2])
				h = float(info[3])
				
				x1 = x 
				y1 = y
				x2 = x+w
				y2 = y+h
				class_index = 0
				if x2>160:
					x2 = 160
				if y2>120:
					y2 = 120				
				ff.write(str(class_index)+' '+str(x1)+' '+str(y1)+' '+str(x2)+' '+str(y2)+'\n')
			file_obj.close()
			ff.close()
		
