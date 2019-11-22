from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import csv
import pandas as pd
def add():
  x=0
  l=''
  with open("F:\Assignment\Contacts.csv","r") as d:
    csvread=csv.reader(d)
    for line in csvread:
       if n2.get() in line:
          x+=1
          l=line[1]
  if x == 0 or l!=p2.get() or (x ==0 and l!=p2.get()):
     messagebox.showerror("Error","Invalid Username\Password")
  else:
    window=Tk()
    window.title("WELCOME!!! "+n2.get())
    window.geometry("4000x2000")
    
    ac=Label(window,text="Add Contacts--->")
    ac.grid(column=10,row=0)
    
    nm=Label(window,text="Name")
    nm.grid(column=10,row=5)
    global name
    name=Entry(window)
    name.grid(column=15,row=5)
    pn=Label(window,text="Phone No")
    pn.grid(column=10,row=10)
    global ph
    ph=Entry(window)
    ph.grid(column=15,row=10)
    g=Label(window,text="Gender")
    g.grid(column=10,row=15)
    global gg
    gg=IntVar()
    m=Radiobutton(window,text="Male",variable=gg,value=1)
    m.grid(column=15,row=15)
    f=Radiobutton(window,text="Female",variable=gg,value=2)
    f.grid(column=20,row=15)
    dob=Label(window,text="Date of Birth")
    dob.grid(column=10,row=20)
    month=['Select','January','February','March','April','May','June','July','August','September','October','November','December']
    global tkm
    tkm=StringVar(window)
    tkm.set('Select')
    mh=OptionMenu(window,tkm,*month)
    mh.grid(column=12,row=20)
    global date
    date=Spinbox(window,from_=1,to=31,width=4)
    date.grid(column=15,row=20)
    global year
    year=Spinbox(window,from_=1930,to=2019,width=9)
    year.grid(column=20,row=20)
    y=int(year.get())
    def datecheck():
        m31=['January','March','May','July','August','October','December']
        m30=['April','June','September','November']
        if tkm.get() in m31:
            if int(date.get())<=31:
                return True
            else:
                return False
        elif tkm.get() in m30:
            if int(date.get())<=30:
                return True
            else:
                return False
        elif tkm.get() == 'February':
            if (y%4==0 and y%100!=0) and y%400==0:
                if int(date.get())<=29:
                    return True
                else:
                    return False
            else:
                if int(date.get())<=28:
                    return True
                else:
                    return False
    
    def save():
        if gg.get() == 1:
            a='Male'
        else:
            a='Female'
        dd=str(date.get())+"th "+tkm.get()+" "+str(year.get())
        if len(ph.get()) == 10 and datecheck():
            l=name.get()+","+str(ph.get())+","+a+","+dd+"\n"
            with open('F:\Assignment\Contacts.csv',"a") as f:
                f.write(l)
        else:
            messagebox.showerror("Error","Incorrect values")
    
    bt=Button(window,text="Save",command=save)
    bt.grid(column=15,row=25)
    sc=Label(window,text="        Search Contacts-->")
    sc.grid(column=70,row=0)
    bn=Label(window,text="         By Name")
    bn.grid(column=70,row=5)
    global ne
    ne=Entry(window)
    ne.grid(column=71,row=5)
    res=Label(window,text="      Result-->")
    res.grid(column=70,row=25)
    sr= Text(window,width = 30,height=10)
    sr.grid(row = 30,column= 71,columnspan=2)

    def search():
        ds=pd.read_csv("F:\Assignment\Contacts.csv")
        x=len(ne.get())
        sr.insert(END, "Name \t \t Phone Number\n")
        a=0
        for i in range(len(ds)):
            b=ds['Name'][i]
            b=b[:x]
        #b.lower()
            if b==ne.get():
                a+=1
                sr.insert(END,"------------------------------\n")
                sr.insert(END,ds['Name'][i])
                sr.insert(END,"\t \t")
                sr.insert(END,ds['Phone Number'][i])
                sr.insert(END,"\t      \t")
                sr.insert(END,"\n")
        if a==0:
            messagebox.showerror("OOPS","No Contacts Found")
                
    bt1=Button(window,text="Search",command=search)
    bt1.grid(column=71,row=15)
    sm=Label(window,text="Send messages-->")
    sm.grid(column=70,row=60)
    snm=Label(window,text="Name")
    snm.grid(column=70,row=70)
    k=Entry(window)
    k.grid(column=71,row=70)
    me=Label(window,text="Message")
    me.grid(column=70,row=80)
    m=Entry(window,width=50)
    m.grid(column=71,row=80)
    
    def msg():
        ds=pd.read_csv("F:\Assignment\Contacts.csv")
        userlog=ds[ds["Name"]==k.get()]
        a=len(userlog)
        if a==1:
            l=n2.get()+"-"+k.get()+"-"+m.get()+"\n"
            a=open("F:\Assignment\Sent.txt","a")
            a.write(l)
        else:
            messagebox.showwarning("Yikes","Name not found")
            
    send=Button(window,text="Send",command=msg)
    send.grid(column=71,row=120)
    mr=Label(window,text="Messages recieved-->")
    mr.grid(column=10,row=60)
    rec= scrolledtext.ScrolledText(window,width=30,height=10)
    rec.grid(column=15,row=80)
    f=open("F:\Assignment\Sent.txt","r")
    for i in f:
        l=i.split("-")
        if l[1] == n2.get():
            rec.insert(END,l[0])
            rec.insert(END,":\n")
            rec.insert(END,"\t"+l[2])
    
    def clear():
       with open("F:\Assignment\Sent.txt", "r") as f:
        lines = f.readlines()
        for i in lines:
          l=i.split("-")
          if l[1] == n2.get():
            lines.remove(i)
       with open("F:\Assignment\Sent.txt", "w") as new_f:
          for line in lines:        
            new_f.write(line)
        
    clear=Button(window,text="Clear",command=clear)
    clear.grid(column=15,row=150)
    window.mainloop()
root=Tk()
root.title("Login")
root.geometry("300x200")
l1=Label(root,text="Sign in!",font=("ArialBold",50))
l1.grid(column=7,row=1)
n1=Label(root,text="Name")
n1.grid(column=6,row=3,sticky=W)
p1=Label(root,text="Phone Number")
p1.grid(column=6,row=4,sticky=W)
n2=Entry(root)
n2.grid(column=7,row=3,sticky=W)
p2=Entry(root,show="*")
p2.grid(column=7,row=4,sticky=W)
bt=Button(root,text="Login",command=add)
bt.grid(column=7,row=6)
root.mainloop()

