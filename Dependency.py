# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:22:11 2020

@author: rajni
"""
import tkinter as t
import mysql.connector as con
from mysql.connector import Error


def login():
    
    x=User.get()
    y=Passwd.get()
        
    conn = None
    
    try:
        
        if len(x) == 0 and len(y) == 0:
        
            t.messagebox.showerror("Login Exeption","Please fill in the Missing Info")
    
        elif len(x) == 0 and len(y) != 0:
        
            t.messagebox.showerror("Login Exeption","Please Enter the Username")
        
        elif len(x) != 0 and len(y) == 0:
        
            t.messagebox.showerror("Login Exeption","Please Enter the Password")
        
        else:
            conn = con.connect(host='localhost',user=x,passwd=y)
        
            if conn.is_connected():
                print('Connected to MySQL database')
    
    
                def cdb():
                    
                    try:
                        
                        U=u
                        P=p
        
                        mydb=con.connect(host='localhost',user=U,passwd=P)
                    
                        if mydb.is_connected():
                    
                            cur=mydb.cursor()
                        
                            cdb="create database admi_form"
                    
                            cur.execute(cdb)
                    
                            mydb.commit()
                            
                    except Error as e:
                        
                        t.messagebox.showerror("Db error",e)
                        
        
                def ctb():
                    
                    try:
                        
        
                        U=u
                        P=p
                        
                        mydb=con.connect(host='localhost',user=U,passwd=P,database="admi_form")
    
                        if mydb.is_connected():
                            
    
                            cur=mydb.cursor()
                            
                            ctb1="create table personal(srno int(10) primary key,studname varchar(25),DOB date,nationality varchar(15),mother_name varchar(50),father_name varchar(50),blood_group varchar(5))"
                            
                            cur.execute(ctb1)
                            
                            ctb2="create table contact(srno int(10) primary key,occ_mother varchar(80),occ_father varchar(80),mobile varchar(15),email varchar(30),full_addres varchar(100),local_guardian varchar(100))"
                            
                            cur.execute(ctb2)
                            
                            ctb3="create table extra(srno int(10) primary key,age_on_first_apr varchar(25),addr_offic_mother varchar(100),addr_offic_father varchar(100),mother_tounge varchar(25),home_town varchar(25),state varchar(25))"
                            
                            cur.execute(ctb3)
                            
                            ctb4="create table academic(srno int(10) primary key,last_school varchar(100),last_school_was varchar(25),last_exam_result varchar(25),percentage varchar(25),admi_to_class varchar(25),subject_proposed varchar(60))"
                            
                            cur.execute(ctb4)
                            
                            ctb5="create table official(srno int(10) primary key,trnsf_certi_date varchar(25),basic_pay_on_1st_apr varchar(10),no_of_trnf varchar(10),trns_certificate varchar(10),reservation varchar(10),aadhar_no varchar(50))"
                            
                            cur.execute(ctb5)
                    
                            mydb.commit()
                            
                            top.destroy()
                      
                    except Error as e:
                        
                        t.messagebox.showerror("Db error",e)
                    
#-------------------------------------------------------------------------------   
    
                u=User.get()
                p=Passwd.get()
    
                root.destroy()
                
                top=t.Tk()
                top.title("Dependency")
                top.geometry("230x100")
                top.resizable(0,0)
                
                a=t.Button(top,text="Create Database",command=cdb)
                a.place(x=10,y=10)
                
                b=t.Button(top,text="Create Tables",command=ctb)
                b.place(x=10,y=50)
            
                top.mainloop()

    except Error as e:
        
        sttq="Acess Denied : Password or Username is wrong \n \n"+str(e)
        t.messagebox.showerror("Db error",sttq)

    finally:
        
        if conn is not None and conn.is_connected():
            conn.close()

        
root=t.Tk()
root.title("Dependency Builder")
root.geometry("300x200")
root.resizable(0,0)
root.config(bg="black")

L1=t.Label(root,text="MYSQL GUI VERSION",font="Arial",fg="white",bg="black",relief='ridge',cursor='target')
L1.place(x=70,y=10)

l2=t.Label(root,text="User",fg="white",bg="black",font="arial",relief='ridge' )
l2.place(x=10,y=55)
    
User=t.Entry(root,width=20)
User.place(x=70,y=55)
    
l3=t.Label(root,text="Password",fg="white",bg="black",font="arial",relief='ridge')
l3.place(x=10,y=95)
    
Passwd=t.Entry(root,width=20,show="*")
Passwd.place(x=100,y=95)
    
b1=t.Button(root,text="Login",command=login)
b1.place(x=200,y=150)

root.mainloop()