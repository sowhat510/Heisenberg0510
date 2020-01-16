"""
正则表达式功能扩展
"""
import re

s = """Hello
北京
"""

# 只匹配ascii
# regex = re.compile(r'\w+',flags=re.A)

# 忽略字母大小写
# regex = re.compile(r"[a-z]+",flags=re.I)

# 让.可以匹配换行
# regex = re.compile(r".+",flags=re.S)

# 让^ $ 分别能匹配每一行的开头结尾位置
regex = re.compile(r"^北京",flags=re.M|re.A)

l = regex.findall(s)
print(l)

