__author__ = 'Cq'
"""
    解析简单的xml文档
"""

# 使用标准库工具xml.etree.ElementTree，中的parse函数解析
from xml.etree.ElementTree import parse


# parse(source, parse=None)
f = open('demo.xml')

et = parse(f)

# 根节点
root = et.getroot()
print(et.getroot().tag)
print(et.getroot().attrib)
print(et.getroot().text)

# 子元素
for e in root:
    print(e.get('name'))
    print(e.tag)

# 寻找子元素
root.find('aaa')
root.findall('aaa')  # 列表
items = root.iterfind('aaa')  # 生成器对象

for i in items:
    print(i.tag)

# 获取所有元素的列表
# iter(e_name)
l = list(root.iter())
print(l)

# 添加匹配条件
root.findall('aaa/*')
root.findall('./*')
root.findall('//aaa')  # 任意节点下的aaa元素
root.findall('//aaa/..')  # 任意节点下的aaa元素的父元素
root.findall('aaa[@name]')  # 当前节点下的带有name属性的aaa元素
root.findall('aaa[@name=bob]')  # 当前节点下的带有name属性等于bob的aaa元素
root.findall('aaa[bbb]')  # 当前节点下的aaa中必须用bbb元素的节点
root.findall('aaa[bbb="text"]')  # 当前节点下的aaa中必须用bbb元素的文本等于text的节点
root.findall('aaa[1]')  # 当前节点下的aaa元素列表的第一个，1开始
root.findall('aaa[last()]')  # 当前节点下的aaa元素列表的倒数第一个

