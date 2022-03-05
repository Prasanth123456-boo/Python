f = open("obank.py", "r")
countlines=0
for line in f.readlines():
    countlines=countlines+1
    print('number of lines:',countlines)
f.close()
