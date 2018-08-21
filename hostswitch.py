# -*- coding:utf-8 -*-  
import sys

hostsSrc='/private/etc/hosts'
configSrc='./config/hosts.conf'
hostsStart = '#hostsStart'
hostsEnd = '#hostsEnd'

#openfile函数：以只读方式打开文件，并返回所有文件内容
def openfile(fileSrc):
	with open(fileSrc,'r') as fileContent:
		return fileContent.read()
		 		
#now函数：显示当前hosts文件的配置
def now():
	hostsContent = openfile(hostsSrc)
	print((hostsContent[hostsContent.index(hostsStart)+11:hostsContent.index(hostsEnd)]).rstrip('\n'))

#show函数：显示当前所有的配置详情
def show():
	print('\n\033[0;36;40m*********************\nShow the hosts list!\n*********************\033[0m\n')
	configContent = openfile(configSrc)
	for configlist in configContent.split('*'):	
		print('\033[0;32;40mConfID:'+(configlist.split('#')[1])+'\033[0m')
		print('\033[0;32;40mDescribe:'+(configlist.split('#')[3])+'\033[0m')
		print((configlist.split('#')[4]).lstrip('\n'))

#switch函数：切换hosts配置	
def switch(x):
	#读取新旧配置文件
	configContent = openfile(configSrc)
	hostsContent = openfile(hostsSrc)
	
	#判断序列是否越界，如果越界终止写入配置
	if x<= len(configContent.split('*')):
		print('\n\033[0;36;40mChoose config number='+str(x)+'\033[0m')
		print(configContent.split('*')[x-1].split('#')[4].rstrip('\n').lstrip('\n'))
		#写入配置文件
		with open('/private/etc/hosts', "r+") as f:
			read_data = f.read()
			f.seek(0)
			f.truncate()   #清空文件
			f.write(hostsContent.replace(hostsContent[hostsContent.index(hostsStart):hostsContent.index(hostsEnd)+9],hostsStart+'\n'+configContent.split('*')[x-1].split('#')[4].lstrip('\n')+hostsEnd))
	else:
		print("\033[0;31;40mIncorrect parameter\033[0m")
	

if sys.argv[1] == 'now':
	now()
elif sys.argv[1] =='show':
	show()
elif sys.argv[1] == 'switch':
	try:
		switch(int(sys.argv[2]))
	except:
		print("\033[0;31;40mIncorrect parameter\033[0m")
else:
	print('\033[0;31;40mCommand not found\033[0m')

