import tkinter as tk
from tkinter import *
from tabulate import tabulate
from beautifultable import BeautifulTable
from tkinter import font  as tkfont
root = tk.Tk()



file = open('data.txt')
lines = file.read().splitlines()
dict = {}

keyname = []
keyaddress = []
keyemail = []
keydob = []
keysalary = []
valuename = []
valueaddress = []
valueemail = []
valuedob = []
valuesalary = []

j = 0
for line in lines:
    keyname.append('name' + str(j))
    keyaddress.append('address' + str(j))
    keyemail.append('email' + str(j))
    keydob.append('dob' + str(j))
    keysalary.append('salary' + str(j))
    valuename.append('')
    valueaddress.append('')
    valueemail.append('')
    valuedob.append('')
    valuesalary.append('')
    j+=1

i = 0
for line in lines:
    valuename[i] = line.split(',')[0]
    valueaddress[i] = line.split(',')[1]
    valueemail[i] = line.split(',')[2]
    valuedob[i] = line.split(',')[3]
    valuesalary[i] = line.split(',')[4]
    dict[keyname[i]] = valuename[i]
    dict[keyaddress[i]] = valueaddress[i]
    dict[keyemail[i]] = valueemail[i]
    dict[keydob[i]] = valuedob[i]
    dict[keysalary[i]] = valuesalary[i]
    i+=1

print(dict)


class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.pack()
        self.master.title("Data Center")
        self.master.tk_setPalette(background="#ececec")

        tk.Message(self, text="Search Personal Information",
                   font='System 1 bold',
                   justify='left',
                   aspect=800).pack(pady=(15, 0))
        container=tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)



        x=(self.master.winfo_screenwidth()-
           self.master.winfo_reqwidth())/2

        y=(self.master.winfo_screenheight()-
           self.master.winfo_reqheight())/3

        self.master.geometry("800x500".format(x,y))

        self.master.config(menu=tk.Menu(self.master))


        self.frames = {}
        for F in (StartPage, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()




tempArr={}

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=20, pady=15, anchor='w')

        #For Name Label and Entry
        tk.Label(dialog_frame, text="Name").grid(row=0, column=0, sticky='w')
        self.name_input = tk.Entry(dialog_frame, background='white', width=24)
        self.name_input.grid(row=0, column=1, sticky='w')
        self.name_input.focus_set()

        #For Address Label andn Entry
        tk.Label(dialog_frame, text="Address").grid(row=1, column=0, sticky='w')
        self.addr_input = tk.Entry(dialog_frame, background='white', width=24)
        self.addr_input.grid(row=1, column=1, sticky='w')

        #for Email Label and Entry
        tk.Label(dialog_frame,text='Email').grid(row=0,column=2,sticky='w')
        self.mail_input=tk.Entry(dialog_frame,background='white',width=24)
        self.mail_input.grid(row=0,column=3,sticky='w')

        #for Salary Label and Entry
        tk.Label(dialog_frame, text='Salary').grid(row=1, column=2, sticky='w')
        self.Salary_input = tk.Entry(dialog_frame, background='white', width=24)
        self.Salary_input.grid(row=1, column=3, sticky='w')


        button_frame = tk.Frame(self)   #Creating a container for buttons
        button_frame.pack(padx=15, pady=(0, 15), anchor='e')

        #Showing All Button - to show all information
        tk.Button(button_frame,text='Show All',command=self.ShowAll).pack(side='left')


        #Button that when click it will search the input/will call the method "Click_Ok"
        tk.Button(button_frame, text="G0", default='active',
                  command=self.click_ok).pack(side='right')

        #Clear Button- to delete any text inside TextBox
        self.ClearBtn = Button(button_frame, text='Clear', command=lambda: self.clear()).pack(anchor='e')


        #Button to edit information, it will go the PageTwo Class
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Edit Information",
                           command=lambda :controller.show_frame("PageTwo"))
        button.pack()

        self.text = Text(root, width=100, height=15, bg='white')
        self.text.pack()

    #This method is to print out all the data inside the text file
    def ShowAll(self):
        table = BeautifulTable()
        table.column_headers = ["Name", "Address", "Email", "D.O.B", "Salary"]
        for i in range(j):
            Name = valuename[i]
            Addr = valueaddress[i]
            Email = valueemail[i]
            Dob = valuedob[i]
            salar = valuesalary[i]
            table.append_row([Name, Addr, Email, Dob, salar])

        self.text.insert(END,table)



    #This method is to clear any text inside the text box when the button is clicked
    def clear(self):
        self.text.delete(1.0, END)


    def click_ok(self):
        #print(self.name_input.get())
        #print (self.addr_input.get())
        info = Listall.information
        KeyName = info(self.name_input.get())
        KeyAddr = info(self.addr_input.get())
        KeyEmail=info(self.mail_input.get())
        KeySalar=info(self.Salary_input.get())

        if KeyName == True:
            for i in range(13):
                if valuename[i] == self.name_input.get():
                    self.text.insert(END, self.listInfo(i))
                    print("Valid")
        elif KeyAddr==True:
            for i in range(13):
                if valueaddress[i] == self.addr_input.get():
                    self.text.insert(END, self.listInfo(i))
                    print("Valid")

        elif KeyEmail==True:
            for i in range(13):
                if self.mail_input.get() == valueemail[i]:
                    self.text.insert(END, self.listInfo(i))
                    print("Valid")
        elif KeySalar==True:
            for i in range(13):
                if valuesalary[i] == self.Salary_input.get():
                    self.text.insert(END, self.listInfo(i))
                    print("Valid")
        else:
            print("Not valid")
            self.text.insert(END, "\t\tSORRY 404 NOT FOUND !!\n")

    def listInfo(self,num):

        PageTwo.listInfoedit(self,num)
        Name = valuename[num]
        Addr = valueaddress[num]
        Email = valueemail[num]
        Dob = valuedob[num]
        salar = valuesalary[num]

        table = BeautifulTable()
        table.column_headers = ["Name", "Address", "Email", "D.O.B", "Salary"]
        print(Name, Addr, Email, Dob,salar)
        table.append_row([Name, Addr, Email, Dob, salar])
        return table


class Listall(tk.Frame):
    a=0
    def __init__(self,parent,controller):
        self.controller=controller

    def information(self):

        for i in range(13):
            Name = valuename[i]
            Addr = valueaddress[i]
            Email = valueemail[i]
            Dob = valuedob[i]
            salar = valuesalary[i]
            if Name == self:
                return True
            elif Addr==self:
                return True
            elif Email==self:
                return True
            elif salar==True:
                return True
        return False



#All this codes are the duplication of the Class StartPage
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=20, pady=15, anchor='w')

        tk.Label(dialog_frame, text="Name").grid(row=0, column=0, sticky='w')

        # Name
        tk.Label(dialog_frame, text="Name").grid(row=0, column=0, sticky='w')
        self.name_input = tk.Entry(dialog_frame, background='white', width=24)
        self.name_input.grid(row=0, column=1, sticky='w')
        self.name_input.focus_set()

        # Address
        tk.Label(dialog_frame, text="Address").grid(row=1, column=0, sticky='w')
        self.addr_input = tk.Entry(dialog_frame,text='addre',background='white', width=24)
        self.addr_input.grid(row=1, column=1, sticky='w')

        # Email
        tk.Label(dialog_frame, text='Email').grid(row=0, column=2, sticky='w')
        self.mail_input = tk.Entry(dialog_frame,text='mail', background='white', width=24)
        self.mail_input.grid(row=0, column=3, sticky='w')

        # Salary
        tk.Label(dialog_frame, text='Salary').grid(row=1, column=2, sticky='w')
        self.Salary_input = tk.Entry(dialog_frame,text='300', background='white', width=24)
        self.Salary_input.grid(row=1, column=3, sticky='w')

        button_frame = tk.Frame(self)
        button_frame.pack(padx=15, pady=(0, 15), anchor='e')

        tk.Button(button_frame, text="Update", default='active',
                  command=self.click_ok).pack(side='right')

        tk.Button(button_frame, text="cancel",
                  command=self.click_cancel).pack(side='right')

        button = tk.Button(self, text="",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        self.text = Text(root, width=100, height=15, bg='white')
        self.text.pack()


    def click_ok(self):
        KeyName=self.name_input.get()
        KeyAddr=self.addr_input.get()
        KeyEmail=self.mail_input.get()
        KeySalar=self.Salary_input.get()

        if KeyName !=None:
            for i in range(13):
                Name = valuename[i]
                if Name == self.name_input.get():
                    self.text.insert(END, self.listInfoedit(i))

                    print("Valid")

        elif KeyAddr!=None:
            for i in range(13):
                Name = valueaddress[i]
                if Name == self.addr_input.get():
                    self.text.insert(END, self.listInfoedit(i))
                    print("Valid")

        elif KeyEmail!=None:
            for i in range(13):
                Name = valueemail[i]
                if Name == self.mail_input.get():
                    self.text.insert(END, self.listInfoedit(i))
                    print("Valid")
        elif KeySalar!=None:
            for i in range(13):
                Name = valuesalary[i]
                if Name == self.Salary_input.get():
                    self.text.insert(END, self.listInfo(i))
                    print("Valid")
        else:
            print("Not valid")
            self.text.insert(END, "\t\tSORRY 404 NOT FOUND !!\n")

    def click_cancel(self):
        self.master.destroy()

    def listInfoedit(self, num):
        Name=self.name_input.get()
        Addre=self.addr_input.get()
        Emai=self.mail_input.get()
        Salar=self.Salary_input.get()

        for i in range(num + 1):
            if Name != None:
                valuename[i]=Name

            elif Addre != None:
                valueaddress[i]=Addre

            elif Emai != None:
                valueemail[i]=Emai

            elif Salar!= None:
                valuesalary[i]=Salar
            else:
                print("Not valid")
                self.text.insert(END, "\t\tNo Udpates were done !!\n")

        return None






if __name__=='__main__':
    root=tk.Tk()
    root.option_add('*tearOff',False)
    app = App(root)
    # subprocess.call(['/usr/bin/osascript','-e','tell app "Finder" to set frontmost of process "Python" to true'])
    app.mainloop()







