"""
 有一个列表
['Joy1','8848','06>5','HI-33','Koii','3306']
筛选出列表内各项中只包含数字字符的，打印出来
"""
import re

l = ['Joy1','8848','06>5','HI-33','Koii','3306']

for i in l:
    data = re.findall('^[0-9]*$',i)
    if data:
        print(data)

for i in l:
    data = re.findall("[^0-9]",i)
    if not data:
        print(i)

# 匹配大写字母开头单词
s = "Hi,Jame. I am working NBA CBD"
data = re.findall("[A-Z]+[a-z]*",s)
print(data)


# 匹配所有数字
s = "22  -15  1/2  45% 6"
data = re.findall("-?[0-9]+/?[1-9]*%?",s)
print(data)


# 匹配邮箱
s = "wangwc@tedu.cn"
data = re.search(r'\w+@\w+\.(cn|com)',s).group()
print(data)

# 匹配IP地址
s = '192.168.1.25'
data = re.search(r'(\d{1,3}\.?){4}',s).group()
print(data)




