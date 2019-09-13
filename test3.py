import sqlite3

conn = sqlite3.connect('test3.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_myFiles ( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                fileNames text NOT NULL)")     
    conn.commit()
conn.close()

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

for file in fileList:
    if file.endswith(".txt"):
        conn = sqlite3.connect('test3.db')

        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_myFiles(fileNames) VALUES (?)", 
                (file,))
            conn.commit()
        conn.close()
        print(file)


       

