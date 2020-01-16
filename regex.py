"""
re模块使用
"""
import re

# 目标字符串
s = "Alex:1995,Sunny:1996"
pattern = r"(\w+):(\d+)"

# 使用re直接调用
l = re.findall(pattern,s)
print(l)

# 使用compile对象
regex = re.compile(pattern)
l = regex.findall(s,0,13)  # 截取匹配目标s[0:13]
print(l)


# 字符串切割
l = re.split(r':|,',s)
print(l)

# 字符串替换
s = re.sub(r',',';;',s)
print(s)






