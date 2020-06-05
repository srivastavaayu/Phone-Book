from Tkinter import *
from tkMessageBox import *
import  sqlite3
def edit1():
    con=sqlite3.Connection('phone_data')
    cur=con.cursor()
    ##cur.execute('select * from phone p inner join pnumber p1 on p.id=p1.id inner join email e on e.id=p1.id')
    ##temp=cur.fetchall()
    ###print temp


    root2=Tk()
    root2.title('Edit')


    def edit(* args):
        def save():
    ##        b
    ##        b.append(e1.get())
    ##        b.append(e2.get())
    ##        b.append(e3.get())
    ##        print b
    ##        cur.execute('select id from phone where fname like (?) and mname like(?) and lname like(?)',b)
    ##        i=cur.fetchall()
    ##        print i
    ##        k=i[0][0]
    ##        print k
            c=''
            #print  'abhi ', v1.get(),v4.get()
            t1=0
            t2=0
            if v1.get()==1:
                c='Office'
            elif v1.get()==2:
                c='Home'
            elif v1.get()==3:
                c='Mobile'
##            else:
##                showinfo('Error','Please choose one option')
##                t1=2
            d=''
            if v4.get()==1:
                d='Office'
            elif v4.get()==2:
                d='Personal'
##            else:
##                showinfo('Error','Please choose one option')
##                t2=2
            if t1==0 and t2==0:
                fname=e1.get()
                mname=e2.get()
                lname=e3.get()
                company=e4.get()
                add=e5.get()
                city=e6.get()
                pin=e7.get()
                web=e8.get()
                dob=e9.get()

                cur.execute('update  phone set fname =(?),mname=(?),lname=(?),company=(?),address=(?),city=(?),pin=(?),website=(?),dob=(?) where id =(?)',(fname,mname,lname,company,add,city,pin,web,dob,b))
                cur.execute('update pnumber set type=(?),num=(?) where id =(?)',(c,e10.get(),b))
                cur.execute('update email set type=(?),email_id=(?) where id =(?)',(d,e11.get(),b))
                con.commit()
                showinfo('Save','Saved Successfully')
                root.destroy()
                root2.destroy()
            #print 'success'
        
            
        #print 'hi'
        a=lb.curselection()
        b=lb.get(a)
        #print b
        c= b[0]
        #print b
        g=[]
        s=''
        for w in b:
            if w!=' ':
                s=s+w
            else:
                g.append(s)
                s=''
        b=g      
        cur.execute('select id from phone where fname like (?) and mname like(?) and lname like(?)',b)
        i=cur.fetchall()
        a=i[0]
        b=a[0]
        #print b
        cur.execute('select * from phone where id = (?)',a)
        c1= cur.fetchall()
        cur.execute('select * from pnumber where id = (?)',a)
        c2= cur.fetchall()
        cur.execute('select * from email where id = (?)',a)
        c3= cur.fetchall()
        #print c1,c2,c3
        c1=c1[0]
        #print len(c2),len(c3)
        if len(c2)!=0:
            c2=c2[0]
        if len(c3)!=0:
            c3=c3[0]
        print c2,c3
        w=5
        q=6
        if c3[1]=='Office':
            q=1
        elif c2[1]=='Personal':
            q=2


    #     GUI 

        root=Tk()
        root.title('Edit')
        Label(root,text='First Name').grid(row=1,column=0)                         
        e1=Entry(root)                                                         # e1=first name
        e1.insert(0,c1[1])
        e1.grid(row=1,column=1)
        Label(root,text='Middle Name').grid(row=2,column=0)
        e2=Entry(root)                                                         # e2=middle name
        e2.insert(0,c1[2])
        e2.grid(row=2,column=1)

        Label(root,text='Last Name').grid(row=3,column=0)
        e3=Entry(root)                                                         # e3=last name
        e3.insert(0,c1[3])
        e3.grid(row=3,column=1)

        Label(root,text='     Company Name               ').grid(row=4,column=0)
        e4=Entry(root)                                                         # e4=company name
        e4.insert(0,c1[4])
        e4.grid(row=4,column=1)

        Label(root,text='Address').grid(row=5,column=0)
        e5=Entry(root)                                                          # e5=Address
        e5.insert(0,c1[5])
        e5.grid(row=5,column=1)

        Label(root,text='City').grid(row=6,column=0)
        e6=Entry(root)                                                          #e6=city
        e6.insert(0,c1[6])
        e6.grid(row=6,column=1)

        Label(root,text='Pin Code').grid(row=7,column=0)
        e7=Entry(root)                                                          #e7=pin code
        e7.insert(0,c1[7])
        e7.grid(row=7,column=1)

        Label(root,text='Website URL').grid(row=8,column=0)
        e8=Entry(root)                                                         # e8=website
        e8.insert(0,c1[8])
        e8.grid(row=8,column=1)

        Label(root,text='Date of Birth').grid(row=9,column=0)
        e9=Entry(root)                                                         # e9=birthdate
        e9.insert(0,c1[9])
        e9.grid(row=9,column=1)

        Label(root,text='  dd-mm-yyyy').grid(row=9,column=2)
        #RadioButtons
        Label(root,text=' Select Phone Type:',font='times 18 bold italic').grid(row=10,column=0)
        v1=IntVar()
        t=0
        print c2[1]
        if c2[1]=='Office':
            t=1
            print 'hi',t
        elif c2[1]=='Home':
            t=2
        elif c2[1]=='Personal':
            t=3
        r1=Radiobutton(root,text='Office',variable=v1,tristatevalue=0,value=1)
        r1.grid(row=10,column=1)
        r2=Radiobutton(root,text='Home',variable=v1,tristatevalue=0,value=2)
        r2.grid(row=10,column=2)
        r3=Radiobutton(root,text='Mobile',variable=v1,tristatevalue=0,value=3)
        r3.grid(row=10,column=3)
        v1.set(t)
        Label(root,text='Phone Number').grid(row=11,column=0)
        e10=Entry(root)                                                         #e10=phone number
        e10.insert(0,c2[2])
        e10.grid(row=11,column=1)
        #Button(root,text='+').grid(row=11,column=2)

        v4=IntVar()

        Label(root,text=' Select Email Type:',font='times 18 bold italic').grid(row=12,column=0)
        r4=Radiobutton(root,text='Office',variable=v4,tristatevalue=0,value=1)
        r4.grid(row=12,column=1)
        r5=Radiobutton(root,text='Personal',variable=v4,tristatevalue=0,value=2)
        r5.grid(row=12,column=2)
        v4.set(q)
        Label(root,text='Email id').grid(row=13,column=0)
        e11=Entry(root)                                                           #e11=email id
        e11.insert(0,c3[2])
        e11.grid(row=13,column=1)
        #Button(root,text='+').grid(row=13,column=2)

        #Buttons
        Label(root).grid(row=14,column=0)
        Button(root,text='Save',command=save).grid(row=15,column=1)
    ##    Button(root,text='Search',command=search).grid(row=15,column=1)
    ##    Button(root,text='Close').grid(row=15,column=2)
    ##    Button(root,text='Edit').grid(row=15,column=3)
    ##    Label(root).grid(row=16,column=0)
            
        
    def close():
        root2.destroy()
    root2.geometry('600x600')
    Label(root2,text='Searching Phone Book',font='times 20 bold italic ',fg='green').grid(row=1,column=1,columnspan=3)
    Label(root2).grid(row=2,column=0)
    Label(root2,text='Enter the Name').grid(row=3,column=0)
    e=Entry(root2)
    e.grid(row=3,column=1)
    Label(root2).grid(row=4,column=0)
    lb=Listbox(root2,width=95,height=25,selectmode=SINGLE)
    def ins(* args):
        lb.delete(0,END)
        a=e.get()
        b=["%"+a+"%","%"+a+"%","%"+a+"%"]
        c=cur.execute('select fname,mname,lname from phone where fname like (?) or mname like (?) or lname like (?) order by fname',b)
        for i in c:
            flag=i[0]+' '+i[1]+' '+i[2]+' '
            lb.insert(END,flag)

    root2.bind('<KeyPress>',ins)
    root2.bind('<Button-2>', edit) 
    root2.bind('<Button-3>', edit) 
    root2.bind('<Double 1>', edit) 
    lb.grid(row=5,column=0,columnspan=5)
    Label(root2).grid(row=6,column=0)
    #Button(root2,text='Fetch Details',command=fetch).grid(row=7,column=1)
    Button(root2,text='Close',command=close).grid(row=7,column=1)
    #Button(root2,text='Edit',command=edit).grid(row=7,column=2)











    
    root2.mainloop()

