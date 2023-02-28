# -*- coding: UTF-8 -*-

'''
[Main] ZhangChat Bot Lib	[主要] 小张聊天室机器人库
Author: PAPEREE				作者：纸片君ee(PAPEREE)
Version: uwu.1.00			版本：uwu.1.00
Date: 2023.02.28			日期：2023.02.28

How to use?					如何使用？
U can see the README.md		你可以看看README.md文档
'''

from websocket import WebSocket
from json import dumps,loads
from sys import exit

class ZhangChat:
	def __init__(self,*args):

		# Create ws socket 创建ws套接字
		self.ws=WebSocket()

		# Connect ws address 连接ws地址
		self.ws.connect("wss://chat.zhangsoft.cf/ws")

		# Add args to global value 将args添加到全局变量
		self.args=args

		# Join channel 加入频道
		self.send("join",*args)

	def leave(self):
			
		# End ws connection 结束ws连接
		self.ws.close()

	def send(self,cmd,*args):

		# If cmd is leave 如果cmd是leave
		if cmd=="leave":
			self.leave()

			# End the process 结束进程
			exit(0)

		else:
			# All cmd type 所有的cmd类型
			cmds={"changecolor":["color"],"changenick":["nick"],"chat":["text"],"emote":["text"],"invite":["nick","to"],"join":["channel","nick","password","token","head"],"whisper":["nick","text"]}
		
			# Zip and convert to dict 压缩并转换为字典 ← 什么极限写法
			data=dict(zip(cmds[cmd],args))

			# Add cmd to pack 单独加cmd参数
			data["cmd"]=cmd

			# If have head when join 如果有头像参数
			if cmd=="chat" and self.args[-1]:

				# Add head to pack 向包中添加头像
				data["head"]=self.args[-1]

			# Send pack 向聊天室发包
			self.ws.send(dumps(data))

	def recv(self):

		# Load data and return 接收数据并输出
		return loads(self.ws.recv())