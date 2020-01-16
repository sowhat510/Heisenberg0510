"""
match对象属性
"""
import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
obj = regex.search('abcdefgh') # match对象

print(obj.lastgroup) # 最后一组名
print(obj.lastindex) # 最后一组序号
print(obj.span()) # 匹配内容位置 s[0:6]
print(obj.groupdict()) # 获取捕获组字典
print(obj.group('pig')) # 获取内容