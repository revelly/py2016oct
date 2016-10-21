print("Day 3")


import os
#from os.path import join, getsize
for root, dirs, files in os.walk('D:\\projects\\py2016oct'):
    for file in files:
        if file.endswith(".py"):
            filename = os.path.join(root, file)
            print("File name: {}, filesize: {}".format(filename, os.stat(filename).st_size))
