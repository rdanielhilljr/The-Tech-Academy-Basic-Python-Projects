
import tkinter
from tkinter import *
from tkinter import filedialog
import os
import shutil
import sqlite3

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 500))
        self.master.title('Check Files')
        self.master.config(bg="lightgrey")

        self.varfName = StringVar()
        self.varlName = StringVar()
       


        self.txtfName = Entry(self.master,text=self.varfName, width=30, font=("Helvetica",16),fg="black",bg="white")
        self.txtfName.grid(row=0, column=2,padx=(50,0), pady=(10,0))

        self.txtlName = Entry(self.master,text=self.varlName, width=30, font=("Helvetica",16),fg="black",bg="white")
        self.txtlName.grid(row=1, column=2,padx=(50,0), pady=(10,0))


        self.btnSubmit = Button(self.master, text="Source Directory...", width=18, height=2, command=self.submit)
        self.btnSubmit.grid(row=0, column=1,padx=(20,0), pady=(10,0), sticky=NW)

        self.btnSubmit2 = Button(self.master, text="Destination Directory...", width=18, height=2, command=self.submit2)
        self.btnSubmit2.grid(row=1, column=1,padx=(20,0), pady=(10,0), sticky=NW)

        self.btnSubmit3 = Button(self.master, text="Check Files...", width=18, height=2, command=self.checkFiles)
        self.btnSubmit3.grid(row=2, column=1,padx=(20,0), pady=(10,0), sticky=NW)

        self.btnCancel = Button(self.master, text="Close Program", width=18, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=2,padx=(0,0), pady=(0,0), sticky=SE)

       

    def submit(self):
        currdir = os.getcwd()
        tempdir = filedialog.askdirectory(initialdir=currdir, title='Please select a source directory')
        self.txtfName.insert(0,tempdir)
        

    def submit2(self):
        currdir = os.getcwd()
        tempdir2 = filedialog.askdirectory(initialdir=currdir, title='Please select a destination directory')
        self.txtlName.insert(0,tempdir2)

    def checkFiles(self):
        conn = sqlite3.connect('test4.db')

        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_myFiles ( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                fileNames text NOT NULL, time text NOT NULL)")     
            conn.commit()
            
        conn = sqlite3.connect('test4.db')
        with conn:
            cur = conn.cursor()
            print(self.txtlName.get())
            for file in os.listdir(self.txtfName.get()):
                if file.endswith(".txt"):
                    print(file)
                    abpath = os.path.join(self.txtfName.get(), file)
                    mTime = os.path.getmtime(abpath)
                    print(mTime)
                    shutil.move( abpath, self.txtlName.get())
                    cur.execute("INSERT INTO tbl_myFiles(fileNames, time) VALUES (?, ?)", (file, mTime))
                    conn.commit()
        conn.close()
            

        
        
        

    def cancel(self):
        self.master.destroy()
        

    
        










if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
