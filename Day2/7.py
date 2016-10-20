words=["India\n","is\n","my\n","country\n"]
f=open("sample1.txt","a")
f.writelines(words)
f.flush() #forces python to write into the file immediately
f.close()
