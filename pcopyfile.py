file1=input("ënter the source file to be copied")
file2=input("ënter the destination file :")
fr=open(file1,"r")
fw=open(file2,"w")
for line in fr.readlines():
 fw.write(line)
fr.close()
fw.close()
print("1 file copied")
