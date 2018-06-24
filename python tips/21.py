#coding:utf-8

"""
desc: open function
author: ben
date: 2018-05-17
"""

# ## most
# f = open('test.txt', 'r+')
# j = f.read()
# f.close()

## with
# with open('test.txt', 'r+') as f:
#     j = f.read()


#打开一个文件，并确定它是否是JPG文件
import io

with open('photo.jpg', 'rb') as inf:
    jpgdata = inf.read()

if jpgdata.startswith(b'\xff\xd8'):
    text = u'This is a JPEG file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8') as outf:
    outf.write(text % len(jpgdata))