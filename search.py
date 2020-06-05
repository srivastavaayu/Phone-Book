from Tkinter import *
from tkMessageBox import *
import  sqlite3
def search1():
    con=sqlite3.Connection('phone_data')
    cur=con.cursor()
    ##cur.execute('select * from phone p inner join pnumber p1 on p.id=p1.id inner join email e on e.id=p1.id')
    ##temp=cur.fetchall()
    ###print temp


    root2=Tk()
    root2.title('Search')
    def fetch(* args):
        #print 'hi'
        a=lb.curselection()
        b=lb.get(a)
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
        #print b
        c= b[0]
        #print b
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
        if len(c2)!=0:
            c2=c2[0]
        if len(c3)!=0:
            c3=c3[0]
        #print c1,c2,c3
        lb.delete(0,END)
        lb1=Listbox(root2,width=95,height=25)
        #lb.insert(END,0)
        k=c1[1]
        k='First Name : ' +k
        lb1.insert(END,k)
        k=c1[2]
        k='Middle Name : ' +k
        lb1.insert(END,k)
        k=c1[3]
        k='Last Name : ' +k
        lb1.insert(END,k)
        k=c1[4]
        k='Company Name : ' +k
        lb1.insert(END,k)
        k=c1[5]
        k='Address : ' +k
        lb1.insert(END,k)
        k=c1[6]
        k='City : ' +k
        lb1.insert(END,k)
        k=c1[7]
        k='Pin Code : ' +k
        lb1.insert(END,k)
        k=c1[8]
        k='Website URL : ' +k
        lb1.insert(END,k)
        k=c1[9]
        k='Date of Birth : ' +k
        lb1.insert(END,k)
        k=c2[2]
        k= 'Number : '+str(k)
        lb1.insert(END,k)
        k=c2[1]
        k='Type :'+k
        lb1.insert(END,k)
        k=c3[2]
        k='Email :'+k
        lb1.insert(END,k)
        k=c3[1]
        k='Type :'+k
        lb1.insert(END,k)
        def delete():
            #print a
            cur.execute(' delete from phone where id =(?)',a)
            lb.delete(0,END)
            con.commit()
            showinfo('Removed','Successfully Deleted From Contacts')
            root2.destroy()
        lb1.grid(row=5,column=0,columnspan=5)
        Button(root2,text='Delete',command=delete).grid(row=8,column=2)
           
        
    def close():
        root2.destroy()
    root2.geometry('582x582')
    Label(root2,text='Searching Phone Book',font='times 20 bold italic ',fg='green').grid(row=1,column=1,columnspan=3)
    Label(root2).grid(row=2,column=0)
    Label(root2,text='Enter the Name',font="times 15 ").grid(row=3,column=0)
    e=Entry(root2,width=25)
    e.grid(row=3,column=1,columnspan=5)
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
    root2.bind('<ButtonRelease-1>',fetch)
    root2.bind('<Button-2>', fetch) 
    root2.bind('<Button-3>', fetch) 
    root2.bind('<Double 1>', fetch) 
    lb.grid(row=5,column=0,columnspan=5)
    Label(root2,text='select name  and press right click or double click to see all deatails').grid(row=6,column=1)
    Label(root2).grid(row=7,column=0)
    #Button(root2,text='Fetch Details',command=fetch).grid(row=7,column=1)
    Button(root2,text='Close',command=close).grid(row=8,column=0)











    #con.commit()
    #con.close()
    root2.mainloop()


