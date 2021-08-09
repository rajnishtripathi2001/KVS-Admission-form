# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 03:56:31 2020

@author: rajnish
"""


import tkinter as t
from tkinter import *
from tkinter import messagebox as msg
import tkinter.font as tkFont
import mysql.connector as con
from mysql.connector import Error


def login():
    
    x=User.get()
    y=Passwd.get()  
    
    try:
           
       if len(x) == 0 and len(y) == 0:
        
           msg.showerror("Login Exeption","Please fill in the Missing Info")
    
       elif len(x) == 0 and len(y) != 0:
        
           msg.showerror("Login Exeption","Please Enter the Username")
        
       elif len(x) != 0 and len(y) == 0:
        
           msg.showerror("Login Exeption","Please Enter the Password")
        
       else:
           conn = con.connect(host='localhost',user=x,passwd=y)
        
           if conn.is_connected():
               print('Connected to MySQL database')
                   
               def devloperinfo():
                   msg.showinfo("Developer's Information","This application is developed by Rajnish Tripathi worked incorporated with Codiopy\n\nDeveloper's Contact\n     Rajnish Tripathi (Batch 2019-20)\n     rajnishtripathi2001@gmail.com\n     https://codiopy.blogspot.com ")
    
               def submitp1():
        
                   def submitp2():
            
                       def submitp3():
                
                           def submitp4():
                    
                               def submitp5():
                                                                  
                                   U=Us
                                   P=Ps
                        
                                   E1=d1
                                   E2=e23.get()
                                   E3=e24.get()
                                   E4=e25.get()
                                   E5=e26.get()
                                   E6=e27.get()
                                   E7=e28.get()
                            
                                   mydb=con.connect(host='localhost',user=U,passwd=P,database="admi_form")
                                   cur=mydb.cursor()
                                   
                                   stt2="insert into academic(srno,last_school,last_school_was,last_exam_result,percentage,admi_to_class,subject_proposed) VALUES({},'{}','{}','{}','{}','{}','{}')".format(E1,E2,E3,E4,E5,E6,E7)
                                
                                   cur.execute(stt2)
                                   mydb.commit()
                                
                                   top5.destroy()
                                
                                   msg.showinfo("Submitted","Congratulations Your Form has submitted Successfuly\n Now only Admission Administrator Can modify your details")
                               
                               Us=U
                               Ps=P
                            
                               d1=c1
                               d2=e17.get()
                               d3=e18.get()
                               d4=e19.get()
                               d5=e20.get()
                               d6=e21.get()
                               d7=e22.get()
                            
                               mydb=con.connect(host="localhost",user=Us,passwd=Ps,database="admi_form")
                               cur=mydb.cursor()
                        
                                    
                               stt="insert into official(srno,trnsf_certi_date,basic_pay_on_1st_apr,no_of_trnf,trns_certificate,reservation,aadhar_no) VALUES({},'{}','{}','{}','{}','{}','{}')".format(d1,d2,d3,d4,d5,d6,d7)
                    
                    
                               cur.execute(stt)
                               mydb.commit()
        
                               top4.destroy()
                                        
                               top5=t.Tk()
                           
                               top5.title("Addmission Form page 5")
                               top5.config(bg="silver")
                               top5.geometry("1000x690")
                               top5.resizable(0,0)
                               top5.iconbitmap('kvs.ico')
                            
                               fontStyle = tkFont.Font(family="Lucida Grande", size=20)
                               fontStyle2 = tkFont.Font(family="arial", size=10)
                            
                               page1=t.Label(top5,text="(5)")
                               page1.config(font=fontStyle,bg="black",fg='white')
                               page1.place(x=450,y=190)
                                
                               title1=t.Label(top5,text="केंद्रीय विद्यालय, आर.डी.यस.ओ., लखनऊ \nKendriya Vidyalaya, R.D.S.O.,Lucknow")
                               title1.config(font=fontStyle,bg="silver",fg='black')
                               title1.place(x=280,y=10)
                        
                               title2=t.Label(top5,text="प्रवेश के लिय प्रार्थना-पत्र \nAPPLICATION FOR ADMISSION")
                               title2.config(font=fontStyle,bg='silver',fg='black')
                               title2.place(x=280,y=90)
                            
                               line=t.Label(top5,text="_____________________________________________________")
                               line.config(font=fontStyle,bg='silver',fg='black')
                               line.place(x=90,y=153)
                            
                               l23=t.Label(top5,text="24. अन्तिम विद्यालय व कक्षा जहां पढा हो Name and address of the school last attended with class")
                               l23.config(font=fontStyle2,bg='silver',fg='black')
                               l23.place(x=10,y=250)
                            
                               e23=t.Entry(top5,width=40)
                               e23.place(x=35,y=280)
                    
                               l24=t.Label(top5,text="25. क्या यह केंद्रीय विद्यालय था या मान्यता प्राप्त/ अमान्यता प्राप्त विद्यालय था Whether it was a Kendriya Vidyalaya, Recognised/Unrecognised School")
                               l24.config(font=fontStyle2,bg='silver',fg='black')
                               l24.place(x=10,y=320)
            
                               e24=t.Entry(top5,width=40)
                               e24.place(x=35,y=350)
                                
                               l25=t.Label(top5,text="26. विगत परीक्षा परिणाम Result of last examination")
                               l25.config(font=fontStyle2,bg='silver',fg='black')
                               l25.place(x=10,y=390)
                
                               e25=t.Entry(top5,width=40)
                               e25.place(x=320,y=390)      
                
                               l26=t.Label(top5,text="27. अंको का प्रतिशत Percentage of marks")
                               l26.config(font=fontStyle2,bg='silver',fg='black')
                               l26.place(x=10,y=430)
                
                               e26=t.Entry(top5,width=40)
                               e26.place(x=260,y=430)
                
                               l27=t.Label(top5,text="28. जिस कक्षा प्रवेश चाहिए Class to which addmission is sought")
                               l27.config(font=fontStyle2,bg='silver',fg='black')
                               l27.place(x=10,y=470)
                
                               e27=t.Entry(top5,width=40)
                               e27.place(x=375,y=470)
                
                               l28=t.Label(top5,text="29. लिये जाने वाले प्रस्तावित विषय Subject proposed to offer")
                               l28.config(font=fontStyle2,bg='silver',fg='black')
                               l28.place(x=10,y=510)
                
                               e28=t.Entry(top5,width=40)
                               e28.place(x=350,y=510)
                            
                               Button4=t.Button(top5,text="Submit Your Form",command=submitp5)
                               Button4.place(x=690,y=610)
                                           
                               top5.mainloop()

                           U=Us
                           P=Ps
            
                           c1=b1
                           c2=e121.get()
                           c3=e122.get()
                           c4=e123.get()
                           c5=e131.get(1.0,END)
                           c6=e132.get(1.0,END)
                           c7=e14.get()
                           c8=e15.get()
                           c9=e16.get()
                
                           C=c2+" YEARS "+c3+" MONTH "+c4+" DAY"
                
                           mydb=con.connect(host="localhost",user=U,passwd=P,database="admi_form")
                           cur=mydb.cursor()                    
                                        
                           stt="insert into extra(srno,age_on_first_apr,addr_offic_mother,addr_offic_father,mother_tounge,home_town,state) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(c1,C,c5,c6,c7,c8,c9)
                    
                           cur.execute(stt)
                           mydb.commit()
                        
                           top3.destroy()
        #-------------------------------------------------------------------------                
                           top4=t.Tk()
                    
                           top4.title("Addmission Form page 4")
                           top4.config(bg="silver")
                           top4.geometry("1000x690")
                           top4.resizable(0,0)
                           top4.iconbitmap('kvs.ico')
            
                           fontStyle = tkFont.Font(family="Lucida Grande", size=20)
                           fontStyle2 = tkFont.Font(family="arial", size=10)
                           
                           page1=t.Label(top4,text="(4)")
                           page1.config(font=fontStyle,bg="black",fg='white')
                           page1.place(x=450,y=190)
        
                           title1=t.Label(top4,text="केंद्रीय विद्यालय, आर.डी.यस.ओ., लखनऊ \nKendriya Vidyalaya, R.D.S.O.,Lucknow")
                           title1.config(font=fontStyle,bg="silver",fg='black')
                           title1.place(x=280,y=10)
        
                           title2=t.Label(top4,text="प्रवेश के लिय प्रार्थना-पत्र \nAPPLICATION FOR ADMISSION")
                           title2.config(font=fontStyle,bg='silver',fg='black')
                           title2.place(x=280,y=90)
                            
                           line=t.Label(top4,text="_____________________________________________________")
                           line.config(font=fontStyle,bg='silver',fg='black')
                           line.place(x=90,y=153)        
                    
#===========================================================================================                
        
                           l17=t.Label(top4,text="18. स्थानान्तर प्रमाण-पत्र की संख्या व तिथि / No. & Date of transfer certificate")
                           l17.config(font=fontStyle2,bg='silver',fg='black')
                           l17.place(x=10,y=250)
                
                           e17=t.Entry(top4,width=40)
                           e17.place(x=440,y=250)
        
                           l18=t.Label(top4,text="19. मूल वेतन सम्बध्द वर्ष की 1 अप्रैल को / Basic pay as on 1st April of the year")
                           l18.config(font=fontStyle2,bg='silver',fg='black')
                           l18.place(x=10,y=290)
        
                           e18=t.Entry(top4,width=40)
                           e18.place(x=465,y=290)
                    
                           l19=t.Label(top4,text="20. 7 वर्षो मे हुए स्थानान्तरणो की संख्या / No. on transfers during last 7 years")
                           l19.config(font=fontStyle2,bg='silver',fg='black')
                           l19.place(x=10,y=330)
                        
                           e19=t.Entry(top4,width=10)
                           e19.place(x=445,y=330) 
                        
                           l20=t.Label(top4,text="21. क्या स्थानान्तर प्रमाण-पत्र संलग्न हैं ? / Whether the the transfer certificate is attached ?")
                           l20.config(font=fontStyle2,bg='silver',fg='black')
                           l20.place(x=10,y=370)
                        
                           e20=t.Entry(top4,width=40)
                           e20.place(x=520,y=370)
                        
                           l21=t.Label(top4,text="22. क्या विद्यार्थी अनुसूचित जाति/जनजाति/अन्य पिछङा वर्ग से है ? / Whether the student belongs to scheduled Caste/Tribe/OBC")
                           l21.config(font=fontStyle2,bg='silver',fg='black')
                           l21.place(x=10,y=410)
                
                           e21=t.Entry(top4,width=20)
                           e21.place(x=720,y=410)
                        
                           l22=t.Label(top4,text="23. विद्यार्थी का आधार कार्ङ नo. / Aadhar Card No. of Student")
                           l22.config(font=fontStyle2,bg='silver',fg='black')
                           l22.place(x=10,y=450)
                
                           e22=t.Entry(top4,width=20)
                           e22.place(x=360,y=450)
                        
                           Button3=t.Button(top4,text="Next Page",command=submitp4)
                           Button3.place(x=690,y=610)
                        
                           top4.mainloop()
                           
                       Us=U
                       Ps=P
                            
                       mydb=con.connect(host="localhost",user=Us,passwd=Ps,database="admi_form")
                       cur=mydb.cursor()      
                        
                       b1=a1
                       b2=e71.get()
                       b3=e72.get()
                       b4=e8.get()
                       b5=e9.get()
                       b6=e10.get(1.0,END)
                       b7=e11.get(1.0,END)

                       stt="insert into contact(srno,occ_mother,occ_father,mobile,email,full_addres,local_guardian) VALUES({},'{}','{}','{}','{}','{}','{}')".format(b1,b2,b3,b4,b5,b6,b7)

                       cur.execute(stt)
                       mydb.commit()

                       top2.destroy()
                        
                       top3=t.Tk()
                       top3.title("Addmission Form page 3")
                       top3.config(bg="silver")
                       top3.geometry("1000x690")
                       top3.resizable(0,0)
                       top3.iconbitmap('kvs.ico')
                
                       fontStyle = tkFont.Font(family="Lucida Grande", size=20)
                       fontStyle2 = tkFont.Font(family="arial", size=10)
            
                       page1=t.Label(top3,text="(3)")
                       page1.config(font=fontStyle,bg="black",fg='white')
                       page1.place(x=450,y=190)
                            
                       title1=t.Label(top3,text="केंद्रीय विद्यालय, आर.डी.यस.ओ., लखनऊ \nKendriya Vidyalaya, R.D.S.O.,Lucknow")
                       title1.config(font=fontStyle,bg="silver",fg='black')
                       title1.place(x=280,y=10)
                        
                       title2=t.Label(top3,text="प्रवेश के लिय प्रार्थना-पत्र \nAPPLICATION FOR ADMISSION")
                       title2.config(font=fontStyle,bg='silver',fg='black')
                       title2.place(x=280,y=90)
                            
                       line=t.Label(top3,text="_____________________________________________________")
                       line.config(font=fontStyle,bg='silver',fg='black')
                       line.place(x=90,y=153)
                    
                       l12=t.Label(top3,text="13. आयु (प्रसंगाधीन वर्ष की 1 अप्रैल को) Age of 1 April of the year")
                       l12.config(font=fontStyle2,bg='silver',fg='black')
                       l12.place(x=10,y=220)
                            
                       l121=t.Label(top3,text="Year")
                       l121.config(font=fontStyle2,bg='silver',fg='black')
                       l121.place(x=30,y=260)
                        
                       e121=t.Entry(top3,width=5)
                       e121.place(x=70,y=260)
            
                       l122=t.Label(top3,text="Month")
                       l122.config(font=fontStyle2,bg='silver',fg='black')
                       l122.place(x=120,y=260)
                        
                       e122=t.Entry(top3,width=5)
                       e122.place(x=170,y=260)
            
                       l123=t.Label(top3,text="Days")
                       l123.config(font=fontStyle2,bg='silver',fg='black')
                       l123.place(x=210,y=260)
                       
                       e123=t.Entry(top3,width=5)
                       e123.place(x=250,y=260)            
                            
                       l13=t.Label(top3,text="14. कार्यालय का नाम,पूरा पता व दूरभाष संख्या")
                       l13.config(font=fontStyle2,bg='silver',fg='black')
                       l13.place(x=10,y=290)
                        
                       l131=t.Label(top3,text="पिता/Father")
                       l131.config(font=fontStyle2,bg='silver',fg='black')
                       l131.place(x=30,y=320)
                        
                       e131=t.Text(top3,width=15,height=5)
                       e131.place(x=100,y=320)
                       
                       l132=t.Label(top3,text="माता/Mother")
                       l132.config(font=fontStyle2,bg='silver',fg='black')
                       l132.place(x=230,y=320)
                        
                       e132=t.Text(top3,width=15,height=5)
                       e132.place(x=310,y=320)
                        
                       l14=t.Label(top3,text="15. मातृ भाषा/Mother toungue")
                       l14.config(font=fontStyle2,bg='silver',fg='black')
                       l14.place(x=10,y=420)
                
                       e14=t.Entry(top3,width=20)
                       e14.place(x=180,y=420)
                        
                       l15=t.Label(top3,text="16. गृह नगर Home Town")
                       l15.config(font=fontStyle2,bg='silver',fg='black')
                       l15.place(x=10,y=460)
                    
                       e15=t.Entry(top3,width=20)
                       e15.place(x=170,y=460)                 
                        
                       l16=t.Label(top3,text="17. राज्य State")
                       l16.config(font=fontStyle2,bg='silver',fg='black')
                       l16.place(x=10,y=500)
                    
                       e16=t.Entry(top3,width=20)
                       e16.place(x=170,y=500)                   
                        
                       Button3=t.Button(top3,text="Next Page",command=submitp3)
                       Button3.place(x=690,y=610)
                        
                       top3.mainloop()

                   U=user
                   P=passwd
                    
                   mydb=con.connect(host="localhost",user=U,passwd=P,database="admi_form")
                   cur=mydb.cursor()
                
                   a1=int(e1.get())
                   a2=e2.get()
                   a3=e3.get()
                   a4=e4.get()
                   a5=e51.get()
                   a6=e52.get()
                   a7=e6.get()      
                
                   st="insert into personal(srno,studname,DOB,nationality,mother_name,father_name,blood_group) VALUES({},'{}','{}','{}','{}','{}','{}')".format(a1,a2,a3,a4,a5,a6,a7)
                 
                   cur.execute(st)
                   mydb.commit()

                   top.destroy()
                    
                   top2=t.Tk()
                   top2.title("Addmission Form page 2")
                   top2.config(bg="silver")
                   top2.geometry("1000x660")
                   top2.resizable(0,0)
                   top2.iconbitmap('kvs.ico')
             
                   fontStyle = tkFont.Font(family="Lucida Grande", size=20)
                   fontStyle2 = tkFont.Font(family="arial", size=10)
                    
                   page1=t.Label(top2,text="(2)")
                   page1.config(font=fontStyle,bg="black",fg='white')
                   page1.place(x=450,y=190)
        
                   title1=t.Label(top2,text="केंद्रीय विद्यालय, आर.डी.यस.ओ., लखनऊ \nKendriya Vidyalaya, R.D.S.O.,Lucknow")
                   title1.config(font=fontStyle,bg="silver",fg='black')
                   title1.place(x=280,y=10)
                    
                   title2=t.Label(top2,text="प्रवेश के लिय प्रार्थना-पत्र \nAPPLICATION FOR ADMISSION")
                   title2.config(font=fontStyle,bg='silver',fg='black')
                   title2.place(x=280,y=90)
                    
                   line=t.Label(top2,text="_____________________________________________________")
                   line.config(font=fontStyle,bg='silver',fg='black')
                   line.place(x=90,y=153)
                
                   l71=t.Label(top2,text="7. व्यवसाय माता Occupation Mother ")
                   l71.config(font=fontStyle2,bg='silver',fg='black')
                   l71.place(x=10,y=250)
                    
                   e71=t.Entry(top2,width=25)
                   e71.place(x=231,y=250)
        
                   l72=t.Label(top2,text="8. व्यवसाय पिता Occupation Father")
                   l72.config(font=fontStyle2,bg='silver',fg='black')
                   l72.place(x=10,y=290)
                
                   e72=t.Entry(top2,width=25)
                   e72.place(x=231,y=290)
                    
                   l8=t.Label(top2,text="9. मोबाइल ऩo. Mobile Number")
                   l8.config(font=fontStyle2,bg='silver',fg='black')
                   l8.place(x=10,y=330)
                   
                   e8=t.Entry(top2,width=20)
                   e8.place(x=225,y=330)
                
                   l9=t.Label(top2,text="10. E-mail")
                   l9.config(font=fontStyle2,bg='silver',fg='black')
                   l9.place(x=10,y=370)
                    
                   e9=t.Entry(top2,width=40)
                   e9.place(x=100,y=370)
                    
                   l10=t.Label(top2,text="11. पू्र्ण आवासीय पता Full Residential Address")
                   l10.config(font=fontStyle2,bg='silver',fg='black')
                   l10.place(x=10,y=410)
                            
                   e10=t.Text(top2,width=40,height=5)
                   e10.place(x=20,y=440)
                   
                   l11=t.Label(top2,text="12. स्थानीय अभिभावक का पता (यदि हो) Name and Address of local guardian (if any)")
                   l11.config(font=fontStyle2,bg='silver',fg='black')
                   l11.place(x=350,y=410)
        
                   e11=t.Text(top2,width=40,height=5)
                   e11.place(x=370,y=440)
                    
                   Button2=t.Button(top2,text="Next Page",command=submitp2)
                   Button2.place(x=690,y=580)
                    
                   top2.mainloop()
                       
               user=User.get()
               passwd=Passwd.get()
                
               root.destroy()
                
               top=t.Tk()
               top.title("Addmission Form page 1")
               top.config(bg="silver")
               top.geometry("1000x660")
               top.resizable(0,0)
                
               top.iconbitmap('kvs.ico')
            
               fontStyle = tkFont.Font(family="Lucida Grande", size=20)
               fontStyle2 = tkFont.Font(family="arial", size=10)
            
               page1=t.Label(top,text="(1)")
               page1.config(font=fontStyle,bg="black",fg='white')
               page1.place(x=450,y=190)
        
               title1=t.Label(top,text="केंद्रीय विद्यालय, आर.डी.यस.ओ., लखनऊ \nKendriya Vidyalaya, R.D.S.O.,Lucknow")
               title1.config(font=fontStyle,bg="silver",fg='black')
               title1.place(x=280,y=10)
        
               title2=t.Label(top,text="प्रवेश के लिय प्रार्थना-पत्र \nAPPLICATION FOR ADMISSION")
               title2.config(font=fontStyle,bg='silver',fg='black')
               title2.place(x=280,y=90)
        
               line=t.Label(top,text="_____________________________________________________")
               line.config(font=fontStyle,bg='silver',fg='black')
               line.place(x=90,y=153)
                        
               b1=t.Button(top,text="i",command=devloperinfo)
               b1.config(bg="black",fg="white",width=2,font='arial')
               b1.place(x=965,y=8)

                        
               l1=t.Label(top,text="क्रम संं  Sr.No.")
               l1.config(font=fontStyle2,bg='silver',fg='black')
               l1.place(x=10,y=230)
                        
               e1=t.Entry(top,width=20)
               e1.place(x=100,y=230)
                        
               l2=t.Label(top,text="1. विद्यार्थी का नाम  Name of Student")
               l2.config(font=fontStyle2,bg='silver',fg='black')
               l2.place(x=10,y=270)
                        
               e2=t.Entry(top,width=70)
               e2.place(x=215,y=270)
                        
               l3=t.Label(top,text="2. जन्म तिथि Date of Birth (yyyy/mm/dd)")
               l3.config(font=fontStyle2,bg='silver',fg='black')
               l3.place(x=10,y=310)
                        
               e3=t.Entry(top,width=25)
               e3.place(x=240,y=310)
                        
               l4=t.Label(top,text="3. राष्ट्रीयता Nationality")
               l4.config(font=fontStyle2,bg='silver',fg='black')
               l4.place(x=10,y=350)
                        
               e4=t.Entry(top,width=20)
               e4.place(x=140,y=350)
                       
               l5=t.Label(top,text="4. माता-पिता का विवरण Details of Parents :")
               l5.config(font=fontStyle2,bg='silver',fg='black')
               l5.place(x=10,y=385)
                        
               l51=t.Label(top,text="(i) पूरा नाम Full Name माता/Mother")
               l51.config(font=fontStyle2,bg='silver',fg='black')
               l51.place(x=30,y=415)
                    
               e51=t.Entry(top,width=20)
               e51.place(x=230,y=415)
                        
               l52=t.Label(top,text="पिता/Father")
               l52.config(font=fontStyle2,bg='silver',fg='black')
               l52.place(x=360,y=415)
                        
               e52=t.Entry(top,width=20)
               e52.place(x=435,y=415)
                        
               l6=t.Label(top,text="5. विद्यार्थी का रक्त समूह Blood Group of Student ")
               l6.config(font=fontStyle2,bg='silver',fg='black')
               l6.place(x=10,y=450)
                        
               e6=t.Entry(top,width=20)
               e6.place(x=290,y=450)    
                
               Button1=t.Button(top,text="Next Page",command=submitp1)
               Button1.place(x=690,y=620)
                
               top.mainloop()  
        
    except Error as e:
        
        sttq="Acess Denied : Password or Username is wrong \n"+str(e)
        msg.showerror("Db error",sttq)
               
root=t.Tk()
root.title("KVS Admission")
root.geometry("300x200")
root.resizable(0,0)
root.config(bg="black")
root.iconbitmap('kvs.ico')

L1=t.Label(root,text="Login To Database",font="Arial",fg="white",bg="black",relief='ridge',cursor='target')
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