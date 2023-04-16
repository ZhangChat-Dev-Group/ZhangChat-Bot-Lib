# ZhangChat Bot Lib
**小张聊天室机器人库** - From ee For https://chat.zhangsoft.cf/

## Update Record 更新记录
**2023.02.28 uwu.1.00**  
- First Edition	初版

## Easy to use 使用方法
**If you use TestBot 如果你用TestBot**
- Open TestBot.py 打开TestBot.py
- Change [Set] 更改 [设置]
- Run with Python 用Python运行

**Change Color 改变颜色**  
`self.chat.send("changecolor",<color>)`

**Change Nick 改变昵称**  
`self.chat.send("changenick",<nick>)`

**Send Chat 发送消息**  
`self.chat.send("chat",<text>)`

**Send Emote 发送状态**  
`self.chat.send("emote",<text>)`

**Invite User 邀请用户**  
`self.chat.send("invite",<nick>,<channel>)`

**Join Channel 加入频道**  
`self.chat.send("join",<channel>,<nick>,<password>,<token>,<head>)`

**Send Whisper 发送私聊**  
`self.chat.send("whisper",<nick>,<text>)`

**Close Connection 退出连接**  
`self.chat.send("leave")`
