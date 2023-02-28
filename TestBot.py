# -*- coding: UTF-8 -*-

'''
[Demo] Only My Test Bot 	[演示] 只是我的测试机器人
Author: PAPEREE				作者：纸片君ee(PAPEREE)
Version: uwu.1.00			版本：uwu.1.00
Date: 2023.02.28			日期：2023.02.28

How to use?					如何使用？
U can see the README.md		你可以看看README.md文档
'''

from ZhangChat import *

class TestBot:
	def __init__(self):

		# [Set] [设置] channel:频道 nick:昵称 password:密码 token:密匙 head:头像
		self.join={"channel":"你的昵称","nick":"你的昵称","password":"你的密码","token":"你的密匙","head":"你的头像"}

		# Connect chatroom and join channel 连接聊天室并加入频道
		self.chat=ZhangChat(*self.join.values())

		# Start to receive data 开始接收数据
		self.pack()

	def pack(self):

		# Loop execution 循环执行
		while True:

			# Save loaded data 储存接收数据
			data=self.chat.recv()

			# Determine cmd type 判断cmd类型
			if data.get("cmd")=="chat":

				# If text is in list 如果text内容在列表里
				if data.get("text") in ["uwu","uvu"]:

					# Send user nick 发送用户昵称
					self.chat.send("chat",data.get("nick"))

					# End connection 结束连接
					self.chat.send("leave")

if __name__=="__main__":

	# First start 首先执行
	TestBot()