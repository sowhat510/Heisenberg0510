"""
生成match对象
"""
import re

s = "今年是2020年，我18岁的目标是体重140斤"
pattern = r"\d+"

# 得到匹配结果的迭代对象
# it = re.finditer(pattern,s)
# for i in it:
#     print(i)

# 完全匹配
obj = re.fullmatch(r'.+',s)
print(obj)

# 匹配开头
obj = re.match(r'\w+',s)
print(obj)

# 只匹配一处
obj = re.search(pattern,s)
print(obj)





