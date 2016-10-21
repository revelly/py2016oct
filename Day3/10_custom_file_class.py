import os
class MyFile:
    def __init__(self, path):
        self.file = open(path)
        self.filepath=path
    def getsize(self):
        return os.stat(self.filepath).st_size
    def linecount(self):
        return len(self.file.readlines())
    def firstline(self):
        return open(self.filepath).readlines()[0].strip()
    def lastline(self):
        return open(self.filepath).readlines()[len(open(self.filepath).readlines())-1].strip()
    def nthline(self, n):
        return open(self.filepath).readlines()[n-1].strip()
    def close(self):
        print("File got closed")
        self.file.close()

        
myfile=MyFile("D:/projects/py2016oct/Day3/abc.txt")
print(myfile.getsize())
print(myfile.linecount())
print(myfile.firstline())
print(myfile.lastline())
print(myfile.nthline(6))
myfile.close()
