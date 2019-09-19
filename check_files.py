
import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(575, 200))
        self.master.title('Check Files')
        self.master.config(bg="lightgrey")

        self.varfName = StringVar()
        self.varlName = StringVar()



        self.txtfName = Entry(self.master,text=self.varfName, width=28, font=("Helvetica",16),fg="black",bg="white")
        self.txtfName.grid(row=0, column=2,padx=(50,0), pady=(40,0))

        self.txtlName = Entry(self.master,text=self.varlName, width=28, font=("Helvetica",16),fg="black",bg="white")
        self.txtlName.grid(row=1, column=2,padx=(50,0), pady=(10,0))

        self.btnSubmit = Button(self.master, text="Browse...", width=18, height=1, command=self.submit)
        self.btnSubmit.grid(row=0, column=1,padx=(20,0), pady=(40,0), sticky=NW)

        self.btnSubmit = Button(self.master, text="Browse...", width=18, height=1, command=self.submit)
        self.btnSubmit.grid(row=1, column=1,padx=(20,0), pady=(10,0), sticky=NW)

        self.btnSubmit = Button(self.master, text="Check for files...", width=18, height=3, command=self.submit)
        self.btnSubmit.grid(row=2, column=1,padx=(20,0), pady=(10,0), sticky=NW)

        self.btnCancel = Button(self.master, text="Close Program", width=18, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=2,padx=(0,0), pady=(0,0), sticky=SE)

    def submit(self):
        fn = self.varfname.get()
        ln = self.varlname.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln)) 

    def cancel(self):
        self.master.destroy()
        

    
        










if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
