import threading,requests  # 导入两个模块 安装。pip install requests
from ks import *    #导入模块ks 无需insatll
# 监听消息实例 通过消息来判断
def msgdata():
    msger = jtxx()                   #回调内部方法。如pycharm报红色字体。可以忽视。照样运行
    for data in msger:               #打印方法
        print(data)                  #这里回调所有消息。可以直接使用
        if data[0]=="msgdp":         #消息内容
            if data[5]=="0":         # 1代表发送消息 0代表收到消息
                if data[2].find("@chatroom") != -1:  # 群里发的消息
                    print("群里发的消息")
                if data[2][0:3].find("gh_") != -1:   #公众号收到的消息
                    print("公众号消息")
                if data[2].find("@chatroom") == -1 and data[2][0:3].find("gh_") == -1: #排除 群里发的消息 公众号收到的消息
                    print("私人消息")
                    fxx(data[2], "发送成功")#发送消息 data[2]=微信id  text[0:100]=请求后的消息
threading.Thread(target=msgdata).start()#多线程收消息 处理
input("启动微信")

