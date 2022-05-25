from tkinter import *
root=Tk()
root.geometry("1000x1000")
root.title("Encapsulation")

label1=Label(root,text="Name")
label1.place(relx=0.4, rely=0.1,anchor=CENTER)

inputbox=Entry(root)
inputbox.place(relx=0.5,rely=0.1,anchor=CENTER)

label2=Label(root,text="Password")
label2.place(relx=0.4, rely=0.2,anchor=CENTER)

inputbox1=Entry(root)
inputbox1.place(relx=0.5,rely=0.2,anchor=CENTER)

label3=Label(root,text="Captcha")
label3.place(relx=0.4, rely=0.3,anchor=CENTER)

inputbox2=Entry(root)
inputbox2.place(relx=0.5,rely=0.3,anchor=CENTER)

label4=Label(root)
label4.place(relx=0.5, rely=0.5,anchor=CENTER)

label5=Label(root)
label5.place(relx=0.5, rely=0.6,anchor=CENTER)

label6=Label(root)
label6.place(relx=0.5, rely=0.7,anchor=CENTER)


class names():
    def __init__(self):
        self.__name="James"
        self.__password="p00p"
        self.captcha="37"
    def showscore(self):
        label4["text"]="Names: "+self.__name
        label5["text"]="Password: "+self.__password
        label6["text"]="Captcha: "+self.captcha
obj1=names()   
     
def update():
    obj1.name=inputbox.get()
    obj1.password=inputbox1.get()
    obj1.captcha=inputbox2.get()



button1=Button(root,text="Update Login Details", command=update)
button1.place(relx=0.4, rely=0.4,anchor=CENTER)

button2=Button(root,text="Show Profile", command=obj1.showscore)
button2.place(relx=0.6, rely=0.4,anchor=CENTER)


root.mainloop()