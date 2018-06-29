__author__ = 'Cq'

"""
    调整字符串中文本的格式
"""
import re

# 调整日期的格式
with open('message.log') as f:
    # res = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', f.read())
    res = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', f.read())

print(res)