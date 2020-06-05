from Tkinter import *
import  sqlite3
from tkMessageBox import *
from edit import edit1
from search import *
from intro import *
root=Tk()
con=sqlite3.Connection('phone_data')
cur=con.cursor()
#introd()


def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    #r1.deselect()
    #r2.deselect()
    #r3.deselect()
    #r4.deselect()
    #r5.deselect()


#                                SQLITE 3

#cur.execute('drop table phone')
cur.execute('create table if not exists phone(id int primary key,fname varchar(20),mname varchar(20),lname varchar(20),company varchar(20),address varchar(20),city varchar(20),pin varchar(20),website varchar(20),dob date)')
cur.execute('create table if not exists pnumber(id int,type varchar(10),num number(13),foreign key(id) references phone(id) on delete cascade)')
cur.execute('create table if not exists email(id int ,type varchar(20),email_id varchar(30),foreign key(id) references phone(id) on delete cascade)')
cur.execute("PRAGMA foreign_keys = ON")
##cur.execute('select * from phone p inner join pnumber p1 on p.id=p1.id inner join email e on e.id=p1.id')
##temp=cur.fetchall()
##print temp
#cur.execute('drop table phone')
def data(l,num,em):
    #print l
    cur.execute("insert into phone values(?,?,?,?,?,?,?,?,?,?)",l)
    cur.execute('select * from phone')
    #print cur.fetchall()
    #print num,len(num),num[2]
    if len(num)==2:
        f=''
        num.append(f)
    cur.execute("insert into pnumber values(?,?,?)",num)
    cur.execute("select * from pnumber")
    #print cur.fetchall()
    #print em ,len(em)
    cur.execute("insert into email values(?,?,?)",em)
    #cur.execute("select * from email")
    #print cur.fetchall()
##    cur.execute('select * from phone p inner join pnumber p1 on p.id=p1.id inner join email e on e.id=p1.id')
##    temp=cur.fetchall()
##    #listb(temp)
    con.commit()
    showinfo('Save','Successfully Saved')
    clear()
    

            
def save():
    cur.execute('select max(id) from phone')
    m=cur.fetchall()
    m=m[0][0]
    m=m+1
    l=[]
    l.append(m)
    a=e1.get()
    l.append(a)
    a=e2.get()
    l.append(a)
    a=e3.get()
    l.append(a)
    a=e4.get()
    l.append(a)
    a=e5.get()
    l.append(a)
    a=e6.get()
    l.append(a)
    a=e7.get()
    l.append(a)
    a=e8.get()
    l.append(a)
    a=e9.get()
    temp=0
    temp1=0
    if a!='':
        if a[2]!='-' or a[5]!='-':
            showinfo('Error','Date Format Error')
            temp=-1
        else:
            l.append(a)
    else:
        a=''
        l.append(a)
        
    num=[]
    num.append(m)
    if v1.get()==1:
        c='Office'
        num.append(c)
    elif v1.get()==2:
        c='Home'
        num.append(c)
    elif v1.get()==3:
        c='Mobile'
        num.append(c)
    else:
        d='Null'
        num.append(d)
    b=e10.get()
    if len(b)!=0:
        if b.isdigit():    
            num.append(b)
        else:
            showinfo('Error','Number should be in integer')
            temp1=-1
            
    em=[]
    em.append(m)
    if v2.get()==1:
        c='Office'
        em.append(c)
    elif v2.get()==2:
        c='Personal'
        em.append(c)
    else :
        d='Null'
        em.append(d)
    c=e11.get()
    em.append(c)
    if temp==0 and temp1==0:
        data(l,num,em)



#                               GUI 
root.title('Phone Book')
#root.geometry('500x400')

#photo
a=PhotoImage(file='a.gif')
a=a.subsample(7,7)
Label(root,image=a).grid(row=0,column=1)

#entry details
Label(root,text='First Name').grid(row=1,column=0)                         
e1=Entry(root)                                                         # e1=first name
e1.grid(row=1,column=1)
Label(root,text='Middle Name').grid(row=2,column=0)
e2=Entry(root)                                                         # e2=middle name
e2.grid(row=2,column=1)
Label(root,text='Last Name').grid(row=3,column=0)
e3=Entry(root)                                                         # e3=last name
e3.grid(row=3,column=1)
Label(root,text='     Company Name               ').grid(row=4,column=0)
e4=Entry(root)                                                         # e4=company name
e4.grid(row=4,column=1)
Label(root,text='Address').grid(row=5,column=0)
e5=Entry(root)                                                          # e5=Address
e5.grid(row=5,column=1)
Label(root,text='City').grid(row=6,column=0)
e6=Entry(root)                                                          #e6=city
e6.grid(row=6,column=1)
Label(root,text='Pin Code').grid(row=7,column=0)
e7=Entry(root)                                                          #e7=pin code
e7.grid(row=7,column=1)
Label(root,text='Website URL').grid(row=8,column=0)
e8=Entry(root)                                                         # e8=website
e8.grid(row=8,column=1)
Label(root,text='Date of Birth').grid(row=9,column=0)
e9=Entry(root)                                                         # e9=birthdate
e9.grid(row=9,column=1)
Label(root,text='dd-mm-yyyy').grid(row=9,column=2)
#RadioButtons
Label(root,text=' Select Phone Type:',font='times 18 bold italic').grid(row=10,column=0)
v1=IntVar()
r1=Radiobutton(root,text='Office',variable=v1,value=1)
r1.grid(row=10,column=1)
r2=Radiobutton(root,text='Home',variable=v1,value=2)
r2.grid(row=10,column=2)
r3=Radiobutton(root,text='Mobile',variable=v1,value=3)
r3.grid(row=10,column=3)
Label(root,text='Phone Number').grid(row=11,column=0)
e10=Entry(root)                                                         #e10=phone number
e10.grid(row=11,column=1)
#Button(root,text='+').grid(row=11,column=2)
v2=IntVar()
Label(root,text=' Select Email Type:',font='times 18 bold italic').grid(row=12,column=0)
r4=Radiobutton(root,text='Office',variable=v2,value=1)
r4.grid(row=12,column=1)
r5=Radiobutton(root,text='Personal',variable=v2,value=2)
r5.grid(row=12,column=2)
Label(root,text='Email id').grid(row=13,column=0)
e11=Entry(root)                                                           #e11=email id
e11.grid(row=13,column=1)
#Button(root,text='+').grid(row=13,column=2)

#Buttons
Label(root).grid(row=14,column=0)
Button(root,text='Save',command=save).grid(row=15,column=0)
Button(root,text='Search',command=search1).grid(row=15,column=1)

Button(root,text='Edit',command=edit1).grid(row=15,column=2)
def close():
    root.destroy()
Button(root,text='Close',command=close).grid(row=15,column=3)
Label(root).grid(row=16,column=0)






















root.mainloop()
