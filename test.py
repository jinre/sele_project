# coding:utf-8
import os

file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "smtp_text\\qq.ini")
a = open(file_path, "r")
s = a.readline()
a.close()
s1 = s.split("|")
for i in s1:
    if i != "":
        sl = i
        print i

