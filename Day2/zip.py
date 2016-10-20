import glob
import zipfile

pyfiles=glob.glob("*.py")
z=zipfile.ZipFile("D:\myzip1.zip","w", zipfile.ZIP_DEFLATED)
for file in pyfiles:
    z.write(file)
z.close()
