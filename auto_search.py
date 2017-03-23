#coding=utf-8

import os,sys
import pyperclip
import webbrowser
import time

while(True):
    key_old=pyperclip.paste()
    #print(key_old+"...")
    time.sleep(0.1)
    #webbrowser.open("https://www.baidu.com/s?wd="+key_old)
    #time.sleep(10)
    key_new=pyperclip.paste()
    #print("old:"+key_old)
    #print("new:"+key_new)
    if (key_new != key_old and key_new != "" ):
        webbrowser.open("https://www.baidu.com/s?wd=" + key_new)
        time.sleep(0.1)
    #else:
    #    print("相同,不需要搜索")
        #webbrowser.open("https://www.baidu.com/s?wd=" + key_new)
        #webbrowser.open("https://www.google.com.hk/search?newwindow=1&safe=strict&site=&source=hp&q" + key_new)
