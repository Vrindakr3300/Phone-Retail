from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
import mysql.connector as conn

def mobdet():
    newscreen1=Tk()
    newscreen1.geometry("1000x800")
    p=c1.get()
    p1=tk.Label(newscreen1,text=p,bg="pink",fg="black",height="5",width="55")
    p1.config(font=("Shizuru",30))
    p1.place(x=0,y=0,relwidth=1)
    newscreen1.config(bg="lightsteelblue3")
    Frame1=Frame(newscreen1,bg="green")
    Frame1.place(x=-100,y=300)
    if p=="oppo":
        conn1=conn.connect(host="localhost",user="root",password="@vrindakr051204",database="phones") 
        cursor=conn1.cursor();
        query='select * from phonesav where company = %s'
        t=(p,)
        cursor.execute(query,t)
        s=cursor.fetchall()
        for i in s:
            print(i)
        k1=0
        for i in s:
            for j in range(len(i)):
                e= Label(Frame1,text=i[j],width=30,fg="black",bg="#90EE90",font=('Arial',10),borderwidth=2,relief='ridge')
                e.grid(row=k1,column=j)
            k1=k1+1
    elif p=="samsung":
        conn1=conn.connect(host="localhost",user="root",password="@vrindakr051204",database="phones") 
        cursor=conn1.cursor();
        query='select * from phonesav where company = %s'
        t=(p,)
        cursor.execute(query,t)
        s=cursor.fetchall()
        for i in s:
            print(i)
        k1=0
        for i in s:
            for j in range(len(i)):
                e= Label(Frame1,text=i[j],width=30,fg="black",bg="#90EE90",font=('Arial',10),borderwidth=2,relief='ridge')
                e.grid(row=k1,column=j)
            k1=k1+1
    elif p=="apple":
        conn1=conn.connect(host="localhost",user="root",password="@vrindakr051204",database="phones") 
        cursor=conn1.cursor();
        query='select * from phonesav where company = %s'
        t=(p,)
        cursor.execute(query,t)
        s=cursor.fetchall()
        for i in s:
            print(i)
        k1=0
        for i in s:
            for j in range(len(i)):
                e= Label(Frame1,text=i[j],width=30,fg="black",bg="#90EE90",font=('Arial',10),borderwidth=2,relief='ridge')
                e.grid(row=k1,column=j)
            k1=k1+1
            
    Frame2=Frame(newscreen1)
    Frame2.place(x=10,y=250)        
    p2=tk.Label(Frame2,text="Enter the mobile serial no. you want to buy:",compound=LEFT,font=("Shizuru",15,"bold")).grid(row=11,column=0,padx=40,pady=10)
    global n2
    n2=tk.StringVar() 
    global c2
    c2=Entry(Frame2,width=25,textvariable=n2)
    c2.grid(column=2,row=11)

    Frame3=Frame(newscreen1)
    Frame3.place(x=600,y=430)
    b1=tk.Button(Frame3,text='BUY',compound=LEFT,font=('Arial',20,'bold'),command=bought).grid(row=15,column=8,padx=50,pady=10)

def bought():
    p2=c2.get()
    mydb=conn.connect(host="localhost",user="root",passwd="@vrindakr051204",database="phones")
    mycursor=mydb.cursor()
    query="delete from phonesav where s_no=%s"
    pp=(p2,)
    mycursor.execute(query,pp)
    mydb.commit()
    messagebox.showinfo("Your product is bought:D")  

 
def avrcd():
    newscreen=Tk()
    newscreen.geometry("1000x800")
    p1=tk.Label(newscreen,text="AVAILABLE MOBILES",bg="pink",fg="black",height="5",width="55") 
    p1.config(font=("Shizuru",30))
    p1.place(x=0,y=0,relwidth=1)
    newscreen.config(bg="lightsteelblue3")
    Frame1=Frame(newscreen,bg="green")
    Frame1.place(x=400,y=400)
    p2=tk.Label(Frame1,text="mobile companies:",compound=LEFT,font=("Shizuru",20,"bold")).grid(row=11,column=0,padx=50,pady=10)
    global n1
    n1=tk.StringVar()
    global c1
    c1=ttk.Combobox(Frame1,width=27,textvariable=n1)
    c1['values']=('oppo','apple','samsung')
    c1.grid(column=2,row=11)
    b1=tk.Button(Frame1,text='VIEW',compound=LEFT,font=('Arial',20,'bold'),command=mobdet).grid(row=12,column=2,padx=50,pady=10)

def selldata():
    newscreen=Tk()
    newscreen.geometry("1000x800")
    p1=tk.Label(newscreen,text="Enter the details of your mobile",bg="pink",fg="black",height="5",width="55")
    p1.config(font=("Shizuru",30))
    p1.place(x=0,y=0,relwidth=1)
    newscreen.config(bg="lightsteelblue3")
    Frame1=Frame(newscreen,bg="green")
    Frame1.place(x=400,y=400)

    Frame2=Frame(newscreen)
    Frame2.place(x=10,y=250)
    p2=tk.Label(Frame2,text="s_no.: ",compound=LEFT,font=("Shizuru",15,"bold")).grid(row=11,column=0,padx=40,pady=10)
    global n2
    n2=tk.StringVar()
    global c2
    c2=Entry(Frame2,width=25,textvariable=n2)
    c2.grid(column=2,row=11)
        
    Frame3=Frame(newscreen)
    Frame3.place(x=10,y=330)
    p3=tk.Label(Frame3,text="Mobile companies:",compound=LEFT,font=("Shizuru",15,"bold")).grid(row=11,column=0,padx=40,pady=10)
    global n3
    n3=tk.StringVar()
    global c3
    c3=ttk.Combobox(Frame3,width=25,textvariable=n3)
    c3['values']=('oppo','apple','samsung')
    c3.grid(column=3,row=11)
    
    Frame4=Frame(newscreen)
    Frame4.place(x=10,y=410)
    p4=tk.Label(Frame4,text="Colour:",compound=LEFT,font=("Shizuru",15,"bold")).grid(row=11,column=0,padx=40,pady=10)
    global n4
    n4=tk.StringVar()
    global c4
    c4=ttk.Combobox(Frame4,width=25,textvariable=n4)
    c4['values']=('Grey','Lavender','Black','Rose Gold','Blue','Green','Gold','Graphite')
    c4.grid(column=3,row=11)

    Frame5=Frame(newscreen)
    Frame5.place(x=10,y=490)
    p5=tk.Label(Frame5,text="Phone model: ",compound=LEFT,font=("Shizuru",15,"bold")).grid(row=11,column=0,padx=40,pady=10)
    global n5
    n5=tk.StringVar()
    global c5
    c5=Entry(Frame5,width=25,textvariable=n5)
    c5.grid(column=2,row=11)

    Frame6=Frame(newscreen)
    Frame6.place(x=10,y=570)
    p6=tk.Label(Frame6,text="Ram & Storage & Camera:",compound=LEFT,font=("Shizuru",15,"bold")).grid(row=11,column=0,padx=40,pady=10)
    global n6
    n6=tk.StringVar()
    global c6
    c6=ttk.Combobox(Frame6,width=25,textvariable=n6)
    c6['values']=('3&128& 12+12','5&256& 12+24',' 10& 83 & 48+2+2','3&32 & 50+48+64')
    c6.grid(column=3,row=11)

    Frame7=Frame(newscreen)
    Frame7.place(x=10,y=650)
    p7=tk.Label(Frame7,text="Price: ",compound=LEFT,font=("Shizuru",15,"bold")).grid(row=11,column=0,padx=40,pady=10)
    global n7
    n7=tk.StringVar()
    global c7
    c7=Entry(Frame7,width=25,textvariable=n7)
    c7.grid(column=2,row=11)


    Frame8=Frame(newscreen)
    Frame8.place(x=600,y=430)
    b1=tk.Button(Frame8,text='SAVE',compound=LEFT,font=('Arial',20,'bold'),command=mobdata).grid(row=15,column=8,padx=50,pady=10)

def mobdata():
    p1=c2.get()
    p2=c3.get()
    p3=c4.get()
    p4=c5.get()
    p5=c6.get()
    p6=c7.get()
    mydb=conn.connect(host="localhost",user="root",passwd="@vrindakr051204",database="phones")
    mycursor=mydb.cursor()
    query="insert into phonesav values (%s,%s,%s,%s,%s,%s)"
    pp=(p1,p2,p3,p4,p5,p6)
    mycursor.execute(query,pp)
    mydb.commit()
    messagebox.showinfo("Your record is saved :D")
    
    
    
   
    

screen = Tk()
screen.geometry("1000x800")
screen.title("The Phone Shop")
p=Label(text="The Phone Shop",bg="#7FFFD4",fg="#00008B",height="5",width="55")
p.config(font=("Shizuru",30))
p.grid(row=0,column=1,padx=50,pady=10)
btn1=tk.Button(screen,text="BUY",height="5",width="39",bg="#50C878",fg="White",command=avrcd)
btn1.grid(row=13,column=1,padx=50,pady=10)
btn2=tk.Button(screen,text="SELL",height="5",width="39",bg="#50C878",fg="White",command=selldata)
btn2.grid(row=15,column=1,padx=50,pady=10)
btn3.grid(row=17,column=1,padx=50,pady=10)
screen.config(bg="lightsteelblue3")
screen.mainloop()



