
import tkinter
from tkinter import *
from tkinter import filedialog
import os

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600, 100))
        self.master.title('Check Files')
        self.master.config(bg="lightgrey")

        self.varfName = StringVar()
        self.varlName = StringVar()
        



        self.txtfName = Entry(self.master,text=self.varfName, width=30, font=("Helvetica",16),fg="black",bg="white")
        self.txtfName.grid(row=0, column=2,padx=(50,0), pady=(10,0))        


        self.btnSubmit = Button(self.master, text="Check for files...", width=18, height=2, command=self.submit)
        self.btnSubmit.grid(row=0, column=1,padx=(20,0), pady=(10,0), sticky=NW)

        self.btnCancel = Button(self.master, text="Close Program", width=18, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=2,padx=(0,0), pady=(0,0), sticky=SE)

       

    def submit(self):
        currdir = os.getcwd()
        tempdir = filedialog.askdirectory(initialdir=currdir, title='Please select a directory')
        self.txtfName.insert(0,tempdir)
        
        

    def cancel(self):
        self.master.destroy()
        

    
        










if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
