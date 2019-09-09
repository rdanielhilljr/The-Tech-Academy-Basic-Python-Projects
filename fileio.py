import os

fName = 'Hello.txt'

fPath = 'C:\\Users\\dnybo\\py-drill'

for file in os.listdir(fPath):
    if file.endswith(".txt"):
        print(os.path.join(fPath, file))


for file in os.listdir(fPath):
    if file.endswith(".txt"):
        print(os.path.getmtime(fPath))








