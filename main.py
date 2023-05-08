import tkinter as tk;from tkinter import *;import pandas as hira;import csv;import msvcrt

import os;import pwinput;import bcrypt;from tkinter import ttk,messagebox,Tk,Label;from PIL import Image,ImageTk
global date,month,year;date=12;month=12;year=2022
def signout(x,y):
   x.place_forget();x.pack_forget()
   sino = Label(window,text="Signing you OUT",font=("broadway",50));sino.place(x=500,y=175);sino.after(1500,lambda:sino.destroy())
   y.after(1500,lambda:y.place(x=700,y=350))
def justthisonce(p,q,r):
   r.place_forget();r.pack_forget()
   p.pack()
   q.pack()
def justforthat(r,s,t):
   t.pack_forget();t.place_forget()
   s.pack_forget();s.place_forget()
   t.pack();r.pack()
def mainmenui(x,y,n):
   x.place_forget();x.pack_forget()
   y.place_forget();y.pack_forget()
   n.place(x=500,y=50)
def mainmenu(x,y):
   x.pack_forget()
   x.place_forget()
   y.place(x=700,y=350)
def clicked_admin():
      windowframe.place_forget()
      window.title("Welcome Admin.")
      login = Frame(window);login.place(x=700,y=350)
      option = Label(login,text='\n PRISON ADMIN \n\n\nPlease login to continue\n\n\n');option.pack()
      option.after(900,lambda:login.place_forget())
      newframe1 = Frame(window);
      usern = Label(newframe1,text="Username");usern.pack()
      username=Entry(newframe1);username.pack()
      passw = Label(newframe1,text="Password");passw.pack()
      passwi=Entry(newframe1,show="*");passwi.pack()
      newframe1.after(1000,lambda:newframe1.place(x=700,y=350))
      def gainAccess(useren,passwo): 
         Username = useren.get()
         Password = passwo.get()
         if not len(Username or Password) < 1:
               if True:
                  db = open("cred_admin.txt", "r")
                  d = []
                  f = []
                  for i in db:
                     a,b = i.split(",")
                     b = b.strip()
                     c = a,b
                     d.append(a)
                     f.append(b)
                     data = dict(zip(d, f))
                  try:
                     if Username in data:
                        hashed = data[Username].strip('b')
                        hashed = hashed.replace("'", "")
                        hashed = hashed.encode('utf-8')
                        try:
                           if bcrypt.checkpw(Password.encode(), hashed):
                              messagebox.showinfo("Login Successful",f"Welcome {Username}")
                              newframe1.place_forget()
                              admin_panel = Frame(window);admin_panel.after(1000,lambda:admin_panel.place(x=700,y=350))
                              def staff_pan(): 
                                 admin_panel.place_forget()
                                 staffad = Frame(window);staffad.place(x=700,y=350)
                                 ok = Label(staffad,text="WELCOME TO THE STAFF MENU\n\n\nMAIN MENU\n\n");ok.pack()
                                 def addst(y):
                                    def add_get(x):
                                       id = x.get()
                                       addsta.pack_forget();addsta.place_forget()
                                       adding = Frame(window);adding.pack()
                                       joid = Label(adding,text=f"USING ID {id}");joid.pack()
                                       namel = Label(adding,text="ENTER THE FULL NAME:");namel.pack()
                                       namee = Entry(adding);namee.pack()
                                       genl = Label(adding,text="ENTER THE GENDER(male/female):");genl.pack()
                                       gene = Entry(adding);gene.pack()
                                       dobl = Label(adding,text="ENTER DATE OF BIRTH: ");dobl.pack()
                                       dobe = Entry(adding);dobe.pack()
                                       addressl = Label(adding,text="ENTER RESIDENTIAL ADDRESS:");addressl.pack()
                                       addresse = Entry(adding);addresse.pack()
                                       desigl = Label(adding,text="ENTER THE DESIGNATION AT THE PRISON: ");desigl.pack()
                                       desige = Entry(adding);desige.pack()
                                       hiredatel = Label(adding,text="ENTER THE DATE OF JOINING THE PRISON: ");hiredatel.pack()
                                       hiredatee = Entry(adding);hiredatee.pack()
                                       salaryl = Label(adding,text="ENTER THE SALARY AMOUNT: ");salaryl.pack()
                                       salarye= Entry(adding);salarye.pack()
                                       econtactl = Label(adding,text="ENTER NAME OF EMERGENCY CONTACT: ");econtactl.pack()
                                       econtacte=Entry(adding);econtacte.pack()
                                       erell = Label(adding,text="ENTER RELATION OF EMERGENCY CONTACT WITH STAFF: ");erell.pack()
                                       erele= Entry(adding);erele.pack()
                                       enuml = Label(adding,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT: ");enuml.pack()
                                       enume= Entry(adding);enume.pack()
                                       def addbe():
                                          df = hira.read_csv("stf_rec.csv")
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'name'] = namee.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'gen'] = gene.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'dob'] = dobe.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'address'] = addresse.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'desig'] = desige.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'hired date'] = hiredatee.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'salary'] = salarye.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'econtact'] = econtacte.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'erel'] = erele.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'enum'] = enume.get()
                                          df.to_csv("stf_rec.csv", index=False)
                                          added = Label(adding,text="YOUR RECORD IS ADDED... ");added.pack()
                                          adding.after(3000,lambda:[adding.pack_forget(),adding.place_forget()])
                                          y.after(3000,lambda:y.place(x=700,y=350)) 
                                       cont = Button(adding,text="Done Adding",cursor='plus',command=addbe);cont.pack()
                                       back=Button(adding,text="Go back",cursor='plus',command=lambda:mainmenu(adding,staffad));back.pack()
                                    y.place_forget()
                                    addsta = Frame(window);addsta.pack()
                                    df = hira.read_csv("stf_rec.csv")
                                    with open('stf_ids.txt') as openfileobject:
                                       count = 0
                                       flag = 0
                                       for line in openfileobject:
                                          temp = df.loc[count, 'name']
                                          #print(temp)
                                          if temp == '0':
                                             flag = 1  
                                             lines = line
                                             lines = lines.strip('\n')
                                             tell = Label(addsta,text=f"THE EXISTING ID {lines} IS FREE TO USE.");tell.pack()
                                          count += 1
                                          line = line.strip('\n')
                                          #print(line)
                                       if flag == 1:
                                          tello = Label(addsta,text=f"WOULD YOU LIKE TO USE ANY OF THESE IDS(y/n)?");tello.pack()
                                          telloe = Entry(addsta);telloe.pack()
                                          def neeche(x):  
                                             if x.get() == 'y' or x.get() == 'Y':
                                                idl = Label(addsta,text="WHICH ID WOULD YOU LIKE TO USE?");idl.pack()
                                                ide = Entry(addsta);ide.pack()
                                                continu = Button(addsta,text="CONTINUE",cursor='plus',command=lambda:add_get(ide));continu.pack()
                                                back=Button(addsta,text="Go back",cursor='plus',command=lambda:mainmenu(addsta,staffad));back.pack()
                                             elif x.get()=='n' or x.get()=='N':
                                                   addsta.pack_forget();addsta.place_forget()
                                                   adding = Frame(window);adding.pack()
                                                   id = str(line[0]+line[1]+chr(ord(line[2])+1))
                                                   joid = Label(adding,text=f"USING ID {id}");joid.pack()
                                                   namel = Label(adding,text="ENTER THE FULL NAME:");namel.pack()
                                                   namee = Entry(adding);namee.pack()
                                                   genl = Label(adding,text="ENTER THE GENDER(male/female):");genl.pack()
                                                   gene = Entry(adding);gene.pack()
                                                   dobl = Label(adding,text="ENTER DATE OF BIRTH: ");dobl.pack()
                                                   dobe = Entry(adding);dobe.pack()
                                                   addressl = Label(adding,text="ENTER RESIDENTIAL ADDRESS:");addressl.pack()
                                                   addresse = Entry(adding);addresse.pack()
                                                   desigl = Label(adding,text="ENTER THE DESIGNATION AT THE PRISON: ");desigl.pack()
                                                   desige = Entry(adding);desige.pack()
                                                   hiredatel = Label(adding,text="ENTER THE DATE OF JOINING THE PRISON: ");hiredatel.pack()
                                                   hiredatee = Entry(adding);hiredatee.pack()
                                                   salaryl = Label(adding,text="ENTER THE SALARY AMOUNT: ");salaryl.pack()
                                                   salarye= Entry(adding);salarye.pack()
                                                   econtactl = Label(adding,text="ENTER NAME OF EMERGENCY CONTACT: ");econtactl.pack()
                                                   econtacte=Entry(adding);econtacte.pack()
                                                   erell = Label(adding,text="ENTER RELATION OF EMERGENCY CONTACT WITH STAFF: ");erell.pack()
                                                   erele= Entry(adding);erele.pack()
                                                   enuml = Label(adding,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT: ");enuml.pack()
                                                   enume= Entry(adding);enume.pack()
                  
                                                   def addb():
                                                      with open('stf_rec.csv', mode='a') as file:
                                                         writerr = csv.writer(
                                                            file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                                         writerr.writerow(
                                                            [id, namee.get(), gene.get(), dobe.get(), addresse.get(), desige.get(), hiredatee.get(), salarye.get(), econtacte.get(), erele.get(), enume.get()])
                                                      db = open("stf_ids.txt", "a")
                                                      db.write(id+"\n")
                                                      adding.pack_forget();adding.place_forget()
                                                      added = Label(window,text="YOUR RECORD IS ADDED... ",font=("broadway",33));added.pack()
                                                      added.after(1500,lambda:added.destroy())
                                                      y.after(3000,lambda:y.place(x=700,y=350))  
                                                   cont = Button(adding,text="Done Adding",cursor='plus',command=addb);cont.pack()
                                                   back=Button(adding,text="Go back",cursor='plus',command=lambda:mainmenu(adding,staffad));back.pack() 
                                          contin = Button(addsta,text="CONTINUE",command=lambda:neeche(telloe));contin.pack() 
                                       else:
                                          addsta.pack_forget();addsta.place_forget()
                                          adding = Frame(window);adding.pack()
                                          id = str(line[0]+line[1]+chr(ord(line[2])+1))
                                          joid = Label(adding,text=f"USING ID {id}");joid.pack()
                                          namel = Label(adding,text="ENTER THE FULL NAME:");namel.pack()
                                          namee = Entry(adding);namee.pack()
                                          genl = Label(adding,text="ENTER THE GENDER(male/female):");genl.pack()
                                          gene = Entry(adding);gene.pack()
                                          dobl = Label(adding,text="ENTER DATE OF BIRTH: ");dobl.pack()
                                          dobe = Entry(adding);dobe.pack()
                                          addressl = Label(adding,text="ENTER RESIDENTIAL ADDRESS:");addressl.pack()
                                          addresse = Entry(adding);addresse.pack()
                                          desigl = Label(adding,text="ENTER THE DESIGNATION AT THE PRISON: ");desigl.pack()
                                          desige = Entry(adding);desige.pack()
                                          hiredatel = Label(adding,text="ENTER THE DATE OF JOINING THE PRISON: ");hiredatel.pack()
                                          hiredatee = Entry(adding);hiredatee.pack()
                                          salaryl = Label(adding,text="ENTER THE SALARY AMOUNT: ");salaryl.pack()
                                          salarye= Entry(adding);salarye.pack()
                                          econtactl = Label(adding,text="ENTER NAME OF EMERGENCY CONTACT: ");econtactl.pack()
                                          econtacte=Entry(adding);econtacte.pack()
                                          erell = Label(adding,text="ENTER RELATION OF EMERGENCY CONTACT WITH STAFF: ");erell.pack()
                                          erele= Entry(adding);erele.pack()
                                          enuml = Label(adding,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT: ");enuml.pack()
                                          enume= Entry(adding);enume.pack()

                                          def addb():
                                             with open('stf_rec.csv', mode='a') as file:
                                                writerr = csv.writer(
                                                   file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                                writerr.writerow(
                                                   [id,namee.get(), gene.get(), dobe.get(), addresse.get(), desige.get(), hiredatee.get(), salarye.get(), econtacte.get(), erele.get(), enume.get()])
                                             db = open("stf_ids.txt", "a")
                                             db.write(id+"\n")
                                             adding.pack_forget();adding.place_forget()
                                             added = Label(window,text="YOUR RECORD IS ADDED... ",font=("broadway",33));added.pack()
                                             added.after(1500,lambda:added.pack_forget())
                                             y.after(3000,lambda:y.place(x=700,y=350))
                                          cont = Button(adding,text="Done Adding",cursor='plus',command=addb);cont.pack()
                                          back=Button(adding,text="Go back",cursor='plus',command=lambda:mainmenu(adding,staffad));back.pack()
                                 add = Button(staffad,text="ADD RECORD",cursor='plus',command=lambda:addst(staffad));add.pack()
                                 def searchst():
                                    staffad.place_forget();staffad.pack_forget()
                                    searst= Frame(window);searst.pack()
                                    sit = Label(searst,text="HERE IS THE SEARCHING MENU");sit.pack()
                                    def show():
                                       file = open('stf_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                          if row == []:
                                             continue
                                          if row[0] == "id":
                                             pass
                                          elif row[1] == "0":
                                             pass
                                          else:
                                             pid = Label(searst,text=f"STAFF'S ID IS: {row[0]}");pid.pack()
                                             pna = Label(searst,text=f"NAME: {row[1]}");pna.pack()
                                             pde = Label(searst,text=f"DESIGNATION: {row[5]}");pde.pack()
                                       choice = Label(searst,text="WHICH RECORD WOULD YOU LIKE TO SEARCH?");choice.pack()
                                       idel = Label(searst,text="ENTER STAFF ID:");idel.pack();ide=Entry(searst);ide.pack()
                                       def dekho(ach):
                                          ids = ach.get()
                                          if len(ids) < 3:
                                             messagebox.showerror("ERROR","Please enter complete ID.")
                                          else:
                                             file = open('stf_rec.csv', mode='r')
                                             reader = csv.reader(file)
                                             flag = 0
                                             for row in reader:
                                              #skipping empty rows
                                                if row==[]:
                                                     continue
                                                if ids in row:
                                                   searst.pack_forget();searst.place_forget()
                                                   neb=Frame(window);neb.pack()
                                                   dek = Label(neb,text="HERE IS THE COMPLETE RECORD OF STAFF.");dek.pack()
                                                   flag += 1
                                                   joidh = Label(neb,text=f"SHOWING RECORD AGAINST ID {row[0]}");joidh.pack()
                                                   nameh = Label(neb,text=f"NAME: {row[1]}");nameh.pack()
                                                   genderh =Label(neb,text=f"GENDER: {row[2]}");genderh.pack()
                                                   bipl = Label(neb,text=f"DATE OF BIRTH: {row[3]}");bipl.pack()
                                                   ader=Label(neb,text=f"ADDRESS: {row[4]}");ader.pack()
                                                   desi =Label(neb,text=f"DESGINATION: {row[5]}");desi.pack()
                                                   jobh = Label(neb,text=f"JOB JOINING DATE: {row[6]}");jobh.pack()
                                                   salh=Label(neb,text=f"STAFF'S SALARY IS: {row[7]}");salh.pack()
                                                   ecoe =Label(neb,text=f"EMERGENCY CONTACT: {row[8]}");ecoe.pack()
                                                   relh = Label(neb,text=f"RELATION WITH EMERGENCY CONTACT: {row[9]}");relh.pack()
                                                   pnum =Label(neb,text=f"PHONE NUMBER OF EMERGENCY CONTACT: {row[10]}");pnum.pack()
                                                   back = Button(neb,text="GO BACK",command=lambda:mainmenu(neb,searst));back.pack()
                                             if flag == 0:
                                                
                                                messagebox.showerror("ERROR","NO RECORD MATCHING TO THIS ID EXISTS.")

                                       aage = Button(searst,text="SEARCH",cursor='plus',command=lambda:dekho(ide));aage.pack()
                                    press = Button(searst,text="PRESS TO VIEW THE LIST OF STAFF IDS.",command=show);press.pack()
                                    back = Button(searst,text="GO BACK",command=lambda:mainmenu(searst,staffad));back.pack() 
                                 search = Button(staffad,text="SEARCH RECORD",cursor='plus',command=searchst);search.pack()
                                 def editt():
                                    staffad.pack_forget();staffad.place_forget()
                                    stafed=Frame(window);stafed.pack()
                                    aaiye = Label(stafed,text="WELCOME TO THE EDITING MENU");aaiye.pack()
                                    def don():
                                       file = open('stf_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                           if row == []:
                                                  continue
                                           # print(row)
                                           if row[0] == "id":
                                                  pass
                                           elif row[1] == "0":
                                                pass
                                           else:
                                                diko=Label(stafed,text=f"STAFF'S ID IS:  {row[0]}\nNAME: {row[1]}\nDESIGNATION: {row[5]}");diko.pack()
                                       lel=Label(stafed,text="WHICH RECORD WOULD YOU LIKE TO EDIT(Enter ID)?");lel.pack()
                                       le = Entry(stafed);le.pack()
                                       
                                                
                                       def okies(anti):
                                                   id=anti.get()
                                                   if len(id)<3:
                                                      messagebox.showerror("INVALID ID","Please enter complete ID.")
                                                   else:
                                                      file = open('stf_rec.csv', mode='r')
                                                      reader = csv.reader(file)
                                                      flag = 0
                                                      for row in reader:
                                              #skipping empty rows
                                                         if row==[]:
                                                           continue
                                                         
                                                         if id in row:
                                                            flag += 1
                                                            stafed.pack_forget();stafed.place_forget()
                                                            rer = Frame(window);rer.pack()
                                                            optiom = Frame(window);optiom.pack()
                                                            rerw=Label(rer,text="YOUR OLD RECORD WAS AS: ");rerw.pack()
                                                            dek = Label(rer,text="HERE IS THE COMPLETE RECORD OF STAFF.");dek.pack()
                                                            joidh = Label(rer,text=f"SHOWING RECORD AGAINST ID {row[0]}");joidh.pack()
                                                            nameh = Label(rer,text=f"NAME: {row[1]}");nameh.pack()
                                                            genderh =Label(rer,text=f"GENDER: {row[2]}");genderh.pack()
                                                            bipl = Label(rer,text=f"DATE OF BIRTH: {row[3]}");bipl.pack()
                                                            ader=Label(rer,text=f"ADDRESS: {row[4]}");ader.pack()
                                                            desi =Label(rer,text=f"DESGINATION: {row[5]}");desi.pack()
                                                            jobh = Label(rer,text=f"JOB JOINING DATE: {row[6]}");jobh.pack()
                                                            salh=Label(rer,text=f"STAFF'S SALARY IS: {row[7]}");salh.pack()
                                                            ecoe =Label(rer,text=f"EMERGENCY CONTACT: {row[8]}");ecoe.pack()
                                                            relh = Label(rer,text=f"RELATION WITH EMERGENCY CONTACT: {row[9]}");relh.pack()
                                                            pnum =Label(rer,text=f"PHONE NUMBER OF EMERGENCY CONTACT: {row[10]}");pnum.pack()
                                                            opti=Label(rer,text="WHAT WOULD YOU LIKE TO EDIT?");opti.pack()
                                                            def chnna():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("stf_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER NAME:");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  name = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+(int(id[0])*260) +
                                                                     (int(id[1])*26)+ord(id[2])-65, 'name'] = name
                                                                  df.to_csv("stf_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            nam = Button(optiom,text="NAME",cursor='plus',command=chnna);nam.pack()
                                                            def geno():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("stf_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER GENDER(male/female)");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  gen = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+(int(id[0])*260) +
                                                                     (int(id[1])*26)+ord(id[2])-65, 'gen'] = gen
                                                                  df.to_csv("stf_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            gen=Button(optiom,text="GENDER",cursor='plus',command=geno);gen.pack()
                                                            def chdob():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("stf_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER DATE OF BIRTH");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  dob = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'dob'] = dob
                                                                  df.to_csv("stf_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            bod=Button(optiom,text="DATE OF BIRTH",cursor='plus',command=chdob);bod.pack()
                                                            def chadd():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("stf_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER RESIDENTIAL ADDRESS");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  address = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'address'] = address
                                                                  df.to_csv("stf_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            addr=Button(optiom,text="ADDRESS",cursor='plus',command=chadd);addr.pack()
                                                            def chddes():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("stf_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER THE DESIGNATION AT THE PRISON");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  desig = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'desig'] = desig
                                                                  df.to_csv("stf_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            desin=Button(optiom,text="DESIGNATION",cursor='plus',command=chddes);desin.pack()
                                                            def doko():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("stf_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER THE DATE OF JOINING THE PRISON");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  hiredate = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'hired date'] = hiredate
                                                                  df.to_csv("stf_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            dojo= Button(optiom,text="DATE OF JOINING",cursor='plus',command=doko);dojo.pack()
                                                            def salm():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("stf_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER THE SALARY AMOUNT");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  salary = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'salary'] = salary
                                                                  df.to_csv("stf_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            saala= Button(optiom,text="SALARY",cursor='plus',command=salm);saala.pack()
                                                            def emcom():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("stf_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER NAME OF EMERGENCY CONTACT");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  econtact = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'econtact'] = econtact
                                                                  df.to_csv("stf_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            emoh=Button(optiom,text="EMERGENCY CONTACT",cursor='plus',command=emcom);emoh.pack()
                                                            def chrelo():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("stf_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER RELATION OF EMERGENCY CONTACT WITH STAFF");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  erel = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'erel'] = erel
                                                                  df.to_csv("stf_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            relo=Button(optiom,text="RELATION WITH EMERGENCY CONTACT",cursor='plus',command=chrelo);relo.pack()
                                                            def chcon():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("stf_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  enum = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) + ord(id[2])-65, 'enum'] = enum
                                                                  df.to_csv("stf_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            conta=Button(optiom,text="CONTACT NO. OF EMERGENCY CONTACT",cursor='plus',command=chcon);conta.pack()
                                                            def aawa():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("stf_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo1 = Label(cnan,text="ENTER STAFF NAME");nameo1.pack()
                                                               nam1 = Entry(cnan);nam1.pack()

                                                               nameo2 = Label(cnan,text="ENTER GENDER (Male/Female)");nameo2.pack()
                                                               nam2 = Entry(cnan);nam2.pack()

                                                               nameo3 = Label(cnan,text="ENTER DATE OF BIRTH");nameo3.pack()
                                                               nam3 = Entry(cnan);nam3.pack()

                                                               nameo4 = Label(cnan,text="ENTER RESIDENTIAL ADDRESS");nameo4.pack()
                                                               nam4 = Entry(cnan);nam4.pack()

                                                               nameo5 = Label(cnan,text="ENTER THE DESIGNATION AT THE PRISON");nameo5.pack()
                                                               nam5 = Entry(cnan);nam5.pack()

                                                               nameo6 = Label(cnan,text="ENTER THE DATE OF JOINING THE PRISON");nameo6.pack()
                                                               nam6 = Entry(cnan);nam6.pack()

                                                               nameo7 = Label(cnan,text="ENTER THE SALARY AMOUNT");nameo7.pack()
                                                               nam7 = Entry(cnan);nam7.pack()

                                                               nameo8 = Label(cnan,text="ENTER NAME OF EMERGENCY CONTACT");nameo8.pack()
                                                               nam8 = Entry(cnan);nam8.pack()

                                                               nameo9 = Label(cnan,text="ENTER RELATION OF EMERGENCY CONTACT WITH STAFF");nameo9.pack()
                                                               nam9 = Entry(cnan);nam9.pack()

                                                               nameo10 = Label(cnan,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT");nameo10.pack()
                                                               nam10 = Entry(cnan);nam10.pack()
                                                               def chjo(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
                                                                  name=a1.get();gen=a2.get();dob=a3.get();address=a4.get();desig=a5.get();hiredate=a6.get();salary=a7.get();econtact=a8.get();erel=a9.get();enum=a10.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) + ord(id[2])-65, 'name'] = name
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'gen'] = gen
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'dob'] = dob
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) + ord(id[2])-65, 'address'] = address
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'desig'] = desig
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'hired date'] = hiredate
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'salary'] = salary
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2]) -65, 'econtact'] = econtact
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'erel'] = erel
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'enum'] = enum
                                                                  df.to_csv("stf_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:chjo(nam1,nam2,nam3,nam4,nam5,nam6,nam7,nam8,nam9,nam10));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            wrec = Button(optiom,text="WHOLE RECORD",cursor='plus',command=aawa);wrec.pack()
                                                            Back=Button(optiom,text="GO BACK TO MAIN MENU",cursor='plus',command=lambda:mainmenui(optiom,rer,stafed));Back.pack()

                                                      if flag == 0:
                                                         messagebox.showerror("ERROR","NO RECORD MATCHING TO THIS ID EXISTS.")              
                                       dal = Button(stafed,text="GET DATA",cursor='plus',command=lambda:okies(le));dal.pack()
                                    dabaiye = Button(stafed,text="PRESS TO VIEW THE LIST OF STAFF IDS",cursor='plus',command=don);dabaiye.pack()                  
                                    
                                    back=Button(stafed,text="EXIT",cursor='plus',command=lambda:mainmenu(stafed,staffad));back.pack()


                                    
                                    
                                 edit = Button(staffad,text="EDIT RECORD",cursor='plus',command=editt);edit.pack()
                                 def viewst():
                                    staffad.place_forget();staffad.pack_forget()
                                    viewpanel=Frame(window);viewpanel.pack()
                                    wlo=Label(viewpanel,text="WELCOME TO THE VIEWING MENU");wlo.pack()
                                    def krobhai():
                                       kro.pack_forget()
                                       file = open('stf_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                          if row[0] == "id":
                                             pass
                                          elif row==[]:
                                           continue  
                                          elif row[1]=='0':
                                             continue
                                          else:
                                           recor = Label(viewpanel,text=f"SHOWING RECORD AGAINST ID {row[0]}\nNAME {row[1]}\nGENDER: {row[2]}\nDATE OF BIRTH: {row[3]}\nADDRESS: {row[4]}\nDESGINATION: {row[5]}\nJOB JOINING DATE: {row[6]}\nSTAFF'S SALARY IS: {row[7]}\nEMERGENCY CONTACT: {row[8]}\nRELATION WITH EMERGENCY CONTACT: {row[9]}\nPHONE NUMBER OF EMERGENCY CONTACT: {row[10]}\n\n");recor.pack()
                                    

                                    kro = Button(viewpanel,text="PRESS TO VIEW ALL THE STAFF RECORDS.",cursor='plus',command=krobhai);kro.pack()
                                    back=Button(viewpanel,text="PRESS TO EXIT THE VIEWING MENU.",cursor='plus',command=lambda:mainmenu(viewpanel,staffad));back.pack()                           
                                 view= Button(staffad,text="VIEW RECORD",cursor='plus',command=viewst);view.pack()
                                 def deleteit():
                                    staffad.pack_forget();staffad.place_forget()
                                    delmen = Frame(window);delmen.pack()
                                    oks = Label(delmen,text="HERE IS THE DELETING MENU");oks.pack()
                                    def printo():
                                       file = open('stf_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                       # skipping empty rows causing errors
                                              if row == []:
                                                     continue
                                              # print(row)
                                              if row[0] == "id":
                                                     pass
                                              elif row[1] == "0":
                                                     pass
                                              else:
                                                     stfi=Label(delmen,text=f"STAFF'S ID IS: {row[0]}\nNAME: {row[1]}\nDESIGNATION: {row[5]}") ;stfi.pack() 
                                       joi = Label(delmen,text="ENTER THE STAFF'S ID YOU WANT TO DELETE:");joi.pack()
                                       joidd = Entry(delmen);joidd.pack() 
                                       def dodo(ids):
                                          id = ids.get()
                                          if len(id) < 3:
                                             messagebox.showerror("ERROR","Please enter complete ID.")
                                          else:
                                             file = open('stf_rec.csv', mode='r')
                                             reader = csv.reader(file)
                                             flag = 0
                                             for row in reader:
                                              #skipping empty rows
                                                if row==[]:
                                                     continue
                                                if id in row:
                                                   delmen.pack_forget();delmen.place_forget()
                                                   deko = Frame(window);deko.pack()
                                                   dikhao = Label(deko,text="SHOWING THE WHOLE RECORD OF STAFF.");dikhao.pack()
                                                   dek = Label(deko,text="HERE IS THE COMPLETE RECORD OF STAFF.");dek.pack()
                                                   flag += 1
                                                   joidh = Label(deko,text=f"SHOWING RECORD AGAINST ID {row[0]}");joidh.pack()
                                                   nameh = Label(deko,text=f"NAME: {row[1]}");nameh.pack()
                                                   genderh =Label(deko,text=f"GENDER: {row[2]}");genderh.pack()
                                                   bipl = Label(deko,text=f"DATE OF BIRTH: {row[3]}");bipl.pack()
                                                   ader=Label(deko,text=f"ADDRESS: {row[4]}");ader.pack()
                                                   desi =Label(deko,text=f"DESGINATION: {row[5]}");desi.pack()
                                                   jobh = Label(deko,text=f"JOB JOINING DATE: {row[6]}");jobh.pack()
                                                   salh=Label(deko,text=f"STAFF'S SALARY IS: {row[7]}");salh.pack()
                                                   ecoe =Label(deko,text=f"EMERGENCY CONTACT: {row[8]}");ecoe.pack()
                                                   relh = Label(deko,text=f"RELATION WITH EMERGENCY CONTACT: {row[9]}");relh.pack()
                                                   pnum =Label(deko,text=f"PHONE NUMBER OF EMERGENCY CONTACT: {row[10]}");pnum.pack()
                                                   quwe = Label(deko,text="ARE YOU SURE YOU WANT TO DELETE THE RECORD?");quwe.pack()
                                                   def dhaade():
                                                      df = hira.read_csv("stf_rec.csv")
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) + ord(id[2])-65, 'name'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'gen'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'dob'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) + ord(id[2])-65, 'address'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'desig'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'hired date'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'salary'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2]) -65, 'econtact'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'erel'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'enum'] = '0'
                                                      df.to_csv("stf_rec.csv", index=False)
                                                      messagebox.showinfo("SUCCESS","ID deleted successfully")
                                                      deko.pack_forget();deko.place_forget()
                                                      delmen.pack()
                                                   yay = Button(deko,text="YES",cursor='plus',command=dhaade);yay.pack()
                                                   back = Button(deko,text="NO",command=lambda:mainmenu(deko,delmen));back.pack()
                                             if flag == 0:
                                                
                                                messagebox.showerror("ERROR","NO RECORD MATCHING TO THIS ID EXISTS.")

                                       con = Button(delmen,text="VIEW",cursor='plus',command=lambda:dodo(joidd));con.pack()
                                       back=Button(delmen,text="EXIT",cursor='plus',command=lambda:mainmenu(delmen,staffad));back.pack()

                                    prin = Button(delmen,text="PRESS TO VIEW THE LIST OF STAFF IDS.",cursor='plus',command=printo);prin.pack()
                                                                   
                                 delete = Button(staffad,text="DELETE RECORD",cursor='plus',command=deleteit);delete.pack()
                                 back=Button(staffad,text="EXIT",cursor='plus',command=lambda:mainmenu(staffad,admin_panel));back.pack()
                                 
                              staff = Button(admin_panel,text="STAFF",cursor='plus',command=staff_pan);staff.pack()
                              
                              def prisopa():
                                 admin_panel.place_forget()
                                 staffad = Frame(window);staffad.place(x=700,y=350)
                                 ok = Label(staffad,text="WELCOME TO THE PRISONER MENU\n\n\nMAIN MENU\n\n");ok.pack()
                                 def addst(y):
                                    def add_get(x):
                                       id = x.get()
                                       addsta.pack_forget();addsta.place_forget()
                                       adding = Frame(window);adding.pack()
                                       joid = Label(adding,text=f"USING ID {id}");joid.pack()
                                       namel = Label(adding,text="ENTER THE FULL NAME:");namel.pack()
                                       namee = Entry(adding);namee.pack()
                                       genl = Label(adding,text="ENTER THE GENDER(male/female):");genl.pack()
                                       gene = Entry(adding);gene.pack()
                                       dobl = Label(adding,text="ENTER AGE");dobl.pack()
                                       dobe = Entry(adding);dobe.pack()
                                       addressl = Label(adding,text="ENTER WEIGHT(kg)");addressl.pack()
                                       addresse = Entry(adding);addresse.pack()
                                       desigl = Label(adding,text="ENTER HEIGHT");desigl.pack()
                                       desige = Entry(adding);desige.pack()
                                       hiredatel = Label(adding,text="ENTER HAIRCOLOUR");hiredatel.pack()
                                       hiredatee = Entry(adding);hiredatee.pack()
                                       salaryl = Label(adding,text="ENTER EYECOLOUR");salaryl.pack()
                                       salarye= Entry(adding);salarye.pack()
                                       crime = Label(adding,text="ENTER CRIME");crime.pack()
                                       crimee= Entry(adding);crimee.pack()
                                       spaat = Label(adding,text="ENTER THE CRIME SPOT");spaat.pack()
                                       spaate= Entry(adding);spaate.pack()
                                       court = Label(adding,text="ENTER COURT");court.pack()
                                       courte= Entry(adding);courte.pack()
                                       conla = Label(adding,text="ENTER THE CONVICT'S LAWYER");conla.pack()
                                       conlae= Entry(adding);conlae.pack()
                                       convic = Label(adding,text="ENTER CONVICTION");convic.pack()
                                       convice= Entry(adding);convice.pack()
                                       puns = Label(adding,text="ENTER THE DATE PUNISHMENT STARTED AT");puns.pack()
                                       punse= Entry(adding);punse.pack()
                                       punen = Label(adding,text="ENTER THEDATE PUNISHMENT ENDS AT");punen.pack()
                                       punene= Entry(adding);punene.pack()
                                       econtactl = Label(adding,text="ENTER NAME OF EMERGENCY CONTACT: ");econtactl.pack()
                                       econtacte=Entry(adding);econtacte.pack()
                                       erell = Label(adding,text="ENTER RELATION OF EMERGENCY CONTACT WITH PRISONER: ");erell.pack()
                                       erele= Entry(adding);erele.pack()
                                       enuml = Label(adding,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT: ");enuml.pack()
                                       enume= Entry(adding);enume.pack()
                                       def addbe():
                                          df = hira.read_csv("pri_rec.csv")
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'name'] = namee.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'gen'] = gene.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'age'] = dobe.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'weight'] = addresse.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'height'] = desige.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'hc'] = hiredatee.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'ec'] = salarye.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'crime'] = crimee.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                   ord(id[2])-65, 'crime spot'] = spaate.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'court'] = court.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'lawyer'] = conlae.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                 ord(id[2])-65, 'conviction'] = convice.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                 ord(id[2])-65, 'starting date'] = punse.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                 ord(id[2])-65, 'ending date'] = punene.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2]) -
                                                 65, 'emergency contact'] = econtacte.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                 ord(id[2])-65, 'relation'] = erele.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                 ord(id[2])-65, 'contact'] = enume.get()
                                          df.to_csv("pri_rec.csv", index=False)
                                          added = Label(adding,text="YOUR RECORD IS ADDED... ");added.pack()
                                          adding.after(3000,lambda:[adding.pack_forget(),adding.place_forget()])
                                          y.after(3000,lambda:y.place(x=700,y=350)) 
                                       cont = Button(adding,text="Done Adding",cursor='plus',command=addbe);cont.pack()
                                       back=Button(adding,text="Go back",cursor='plus',command=lambda:mainmenu(adding,staffad));back.pack()
                                    y.place_forget()
                                    addsta = Frame(window);addsta.pack()
                                    df = hira.read_csv("pri_rec.csv")
                                    with open('pri_ids.txt') as openfileobject:
                                       count = 0
                                       flag = 0
                                       for line in openfileobject:
                                          temp = df.loc[count, 'name']
                                          #print(temp)
                                          if temp == '0':
                                             flag = 1  
                                             lines = line
                                             lines = lines.strip('\n')
                                             tell = Label(addsta,text=f"THE EXISTING ID {lines} IS FREE TO USE.");tell.pack()
                                          count += 1
                                          line = line.strip('\n')
                                          #print(line)
                                       if flag == 1:
                                          tello = Label(addsta,text=f"WOULD YOU LIKE TO USE ANY OF THESE IDS(y/n)?");tello.pack()
                                          telloe = Entry(addsta);telloe.pack()
                                          def neeche(x):  
                                             if x.get() == 'y' or x.get() == 'Y':
                                                idl = Label(addsta,text="WHICH ID WOULD YOU LIKE TO USE?");idl.pack()
                                                ide = Entry(addsta);ide.pack()
                                                continu = Button(addsta,text="CONTINUE",cursor='plus',command=lambda:add_get(ide));continu.pack()
                                                back=Button(addsta,text="Go back",cursor='plus',command=lambda:mainmenu(addsta,staffad));back.pack()
                                             elif x.get()=='n' or x.get()=='N':
                                                   addsta.pack_forget();addsta.place_forget()
                                                   adding = Frame(window);adding.pack()
                                                   id = str(line[0]+line[1]+chr(ord(line[2])+1))
                                                   joid = Label(adding,text=f"USING ID {id}");joid.pack()
                                                   namel = Label(adding,text="ENTER THE FULL NAME:");namel.pack()
                                                   namee = Entry(adding);namee.pack()
                                                   genl = Label(adding,text="ENTER THE GENDER(male/female):");genl.pack()
                                                   gene=Entry(adding);gene.pack()
                                                   dobl = Label(adding,text="ENTER AGE");dobl.pack()
                                                   dobe = Entry(adding);dobe.pack()
                                                   addressl = Label(adding,text="ENTER WEIGHT(kg)");addressl.pack()
                                                   addresse = Entry(adding);addresse.pack()
                                                   desigl = Label(adding,text="ENTER HEIGHT");desigl.pack()
                                                   desige = Entry(adding);desige.pack()
                                                   hiredatel = Label(adding,text="ENTER HAIRCOLOUR");hiredatel.pack()
                                                   hiredatee = Entry(adding);hiredatee.pack()
                                                   salaryl = Label(adding,text="ENTER EYECOLOUR");salaryl.pack()
                                                   salarye= Entry(adding);salarye.pack()
                                                   crime = Label(adding,text="ENTER CRIME");crime.pack()
                                                   crimee= Entry(adding);crimee.pack()
                                                   spaat = Label(adding,text="ENTER THE CRIME SPOT");spaat.pack()
                                                   spaate= Entry(adding);spaate.pack()
                                                   court = Label(adding,text="ENTER COURT");court.pack()
                                                   courte= Entry(adding);courte.pack()
                                                   conla = Label(adding,text="ENTER THE CONVICT'S LAWYER");conla.pack()
                                                   conlae= Entry(adding);conlae.pack()
                                                   convic = Label(adding,text="ENTER CONVICTION");convic.pack()
                                                   convice= Entry(adding);convice.pack()
                                                   puns = Label(adding,text="ENTER THE DATE PUNISHMENT STARTED AT");puns.pack()
                                                   punse= Entry(adding);punse.pack()
                                                   punen = Label(adding,text="ENTER THEDATE PUNISHMENT ENDS AT");punen.pack()
                                                   punene= Entry(adding);punene.pack()
                                                   econtactl = Label(adding,text="ENTER NAME OF EMERGENCY CONTACT: ");econtactl.pack()
                                                   econtacte=Entry(adding);econtacte.pack()
                                                   erell = Label(adding,text="ENTER RELATION OF EMERGENCY CONTACT WITH PRISONER: ");erell.pack()
                                                   erele= Entry(adding);erele.pack()
                                                   enuml = Label(adding,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT: ");enuml.pack()
                                                   enume= Entry(adding);enume.pack()
                  
                                                   def addb():
                                                      with open('pri_rec.csv', mode='a') as file:
                                                         writerr = csv.writer(
                                                            file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                                         writerr.writerow(
                                                            [id, namee.get(), gene.get(), dobe.get(), addresse.get(), desige.get(), hiredatee.get(), salarye.get(), crimee.get(),spaate.get(),courte.get(),conlae.get(),convice.get(),punse.get(),punene.get(),econtacte.get(), erele.get(), enume.get()])
                                                      db = open("pri_ids.txt", "a")
                                                      db.write(id+"\n")
                                                      adding.pack_forget();adding.place_forget()
                                                      added = Label(window,text="YOUR RECORD IS ADDED... ",font=("broadway",33));added.pack()
                                                      added.after(1500,lambda:added.destroy())
                                                      y.after(3000,lambda:y.place(x=700,y=350))  
                                                   cont = Button(adding,text="Done Adding",cursor='plus',command=addb);cont.pack()
                                                   back=Button(adding,text="Go back",cursor='plus',command=lambda:mainmenu(adding,staffad));back.pack() 
                                          contin = Button(addsta,text="CONTINUE",command=lambda:neeche(telloe));contin.pack() 
                                       else:
                                          addsta.pack_forget();addsta.place_forget()
                                          adding = Frame(window);adding.pack()
                                          id = str(line[0]+line[1]+chr(ord(line[2])+1))
                                          joid = Label(adding,text=f"USING ID {id}");joid.pack()
                                          namel = Label(adding,text="ENTER THE FULL NAME:");namel.pack()
                                          namee = Entry(adding);namee.pack()
                                          genl = Label(adding,text="ENTER THE GENDER(male/female):");genl.pack()
                                          gene = Entry(adding);gene.pack()
                                          dobl = Label(adding,text="ENTER AGE");dobl.pack()
                                          dobe = Entry(adding);dobe.pack()
                                          addressl = Label(adding,text="ENTER WEIGHT(kg)");addressl.pack()
                                          addresse = Entry(adding);addresse.pack()
                                          desigl = Label(adding,text="ENTER HEIGHT");desigl.pack()
                                          desige = Entry(adding);desige.pack()
                                          hiredatel = Label(adding,text="ENTER HAIRCOLOUR");hiredatel.pack()
                                          hiredatee = Entry(adding);hiredatee.pack()
                                          salaryl = Label(adding,text="ENTER EYECOLOUR");salaryl.pack()
                                          salarye= Entry(adding);salarye.pack()
                                          crime = Label(adding,text="ENTER CRIME");crime.pack()
                                          crimee= Entry(adding);crimee.pack()
                                          spaat = Label(adding,text="ENTER THE CRIME SPOT");spaat.pack()
                                          spaate= Entry(adding);spaate.pack()
                                          court = Label(adding,text="ENTER COURT");court.pack()
                                          courte= Entry(adding);courte.pack()
                                          conla = Label(adding,text="ENTER THE CONVICT'S LAWYER");conla.pack()
                                          conlae= Entry(adding);conlae.pack()
                                          convic = Label(adding,text="ENTER CONVICTION");convic.pack()
                                          convice= Entry(adding);convice.pack()
                                          puns = Label(adding,text="ENTER THE DATE PUNISHMENT STARTED AT");puns.pack()
                                          punse= Entry(adding);punse.pack()
                                          punen = Label(adding,text="ENTER THEDATE PUNISHMENT ENDS AT");punen.pack()
                                          punene= Entry(adding);punene.pack()
                                          econtactl = Label(adding,text="ENTER NAME OF EMERGENCY CONTACT: ");econtactl.pack()
                                          econtacte=Entry(adding);econtacte.pack()
                                          erell = Label(adding,text="ENTER RELATION OF EMERGENCY CONTACT WITH PRISONER: ");erell.pack()
                                          erele= Entry(adding);erele.pack()
                                          enuml = Label(adding,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT: ");enuml.pack()
                                          enume= Entry(adding);enume.pack()

                                          def addb():
                                             with open('pri_rec.csv', mode='a') as file:
                                                writerr = csv.writer(
                                                   file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                                writerr.writerow(
                                                   [id, namee.get(), gene.get(), dobe.get(), addresse.get(), 
                                                   desige.get(), hiredatee.get(), salarye.get(), crimee.get(),spaate.get(),courte.get(),
                                                   conlae.get(),convice.get(),punse.get(),punene.get(),econtacte.get(), erele.get(), enume.get()])
                                             db = open("pri_ids.txt", "a")
                                             db.write(id+"\n")
                                             dbi=open('pri_att.csv','a')
                                             dbi.write(id)
                                             adding.pack_forget();adding.place_forget()
                                             added = Label(window,text="YOUR RECORD IS ADDED... ",font=("broadway",33));added.pack()
                                             added.after(1500,lambda:added.pack_forget())
                                             y.after(3000,lambda:y.place(x=700,y=350))
                                          cont = Button(adding,text="Done Adding",cursor='plus',command=addb);cont.pack()
                                          back=Button(adding,text="Go back",cursor='plus',command=lambda:mainmenu(adding,staffad));back.pack()
                                 add = Button(staffad,text="ADD RECORD",cursor='plus',command=lambda:addst(staffad));add.pack()
                                 def searchst():
                                    staffad.place_forget();staffad.pack_forget()
                                    searst= Frame(window);searst.pack()
                                    sit = Label(searst,text="HERE IS THE SEARCHING MENU");sit.pack()
                                    def show():
                                       file = open('pri_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                          if row == []:
                                             continue
                                          if row[0] == "id":
                                             pass
                                          elif row[1] == "0":
                                             pass
                                          else:
                                             pid = Label(searst,text=f"PRISONER'S ID IS: {row[0]}");pid.pack()
                                             pna = Label(searst,text=f"NAME: {row[1]}");pna.pack()
                                             pde = Label(searst,text=f"CRIME: {row[8]}");pde.pack()
                                       choice = Label(searst,text="WHICH RECORD WOULD YOU LIKE TO SEARCH?");choice.pack()
                                       idel = Label(searst,text="ENTER PRISONER ID:");idel.pack();ide=Entry(searst);ide.pack()
                                       def dekho(ach):
                                          ids = ach.get()
                                          if len(ids) < 3:
                                             messagebox.showerror("ERROR","Please enter complete ID.")
                                          else:
                                             file = open('pri_rec.csv', mode='r')
                                             reader = csv.reader(file)
                                             flag = 0
                                             for row in reader:
                                              #skipping empty rows
                                                if row==[]:
                                                     continue
                                                if ids in row:
                                                   searst.pack_forget();searst.place_forget()
                                                   neb=Frame(window);neb.pack()
                                                   dek = Label(neb,text="HERE IS THE COMPLETE RECORD OF PRISONER.");dek.pack()
                                                   flag += 1
                                                   joidh = Label(neb,text=f"SHOWING RECORD AGAINST ID {row[0]}");joidh.pack()
                                                   nameh = Label(neb,text=f"NAME: {row[1]}\tGENDER: {row[2]}\tAGE: {row[3]}\tWEIGHT: {row[4]}");nameh.pack()
                                                   desi =Label(neb,text=f"HEIGHT: {row[5]}\tHAIRCOLOUR: {row[6]}\tEYECOLOUR: {row[7]}\tCRIME: {row[8]}\nCRIME SPOT: {row[9]}\tCOURT: {row[10]}\tCONVICT\'S LAWYER: {row[11]}\tCONVICTION: {row[12]}");desi.pack()
                                                   relh = Label(neb,text=f"STARTING DATE OF PUNISHMENT: {row[13]}\tENDING DATE OF PUNISHMENT: {row[14]}");relh.pack()
                                                   pnum =Label(neb,text=f"NAME OF EMERGENCY CONTACT: {row[15]}\tRELATION WITH EMERGENCY CONTACT: {row[16]}\tPHONE NUMBER OF EMERGENCY CONTACT: {row[17]}");pnum.pack()
                                                   back = Button(neb,text="GO BACK",command=lambda:mainmenu(neb,searst));back.pack()
                                             if flag == 0:
                                                
                                                messagebox.showerror("ERROR","NO RECORD MATCHING TO THIS ID EXISTS.")

                                       aage = Button(searst,text="SEARCH",cursor='plus',command=lambda:dekho(ide));aage.pack()
                                    press = Button(searst,text="PRESS TO VIEW THE LIST OF PRISONER IDS.",command=show);press.pack()
                                    back = Button(searst,text="GO BACK",command=lambda:mainmenu(searst,staffad));back.pack() 
                                 search = Button(staffad,text="SEARCH RECORD",cursor='plus',command=searchst);search.pack()
                                 def editt():
                                    staffad.pack_forget();staffad.place_forget()
                                    stafed=Frame(window);stafed.pack()
                                    aaiye = Label(stafed,text="WELCOME TO THE EDITING MENU");aaiye.pack()
                                    def don():
                                       file = open('pri_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                           if row == []:
                                                  continue
                                           # print(row)
                                           if row[0] == "id":
                                                  pass
                                           elif row[1] == "0":
                                                continue
                                           else:
                                                diko=Label(stafed,text=f"PRISONER'S ID IS:  {row[0]}\nNAME: {row[1]}\nCRIME: {row[8]}");diko.pack()
                                       lel=Label(stafed,text="WHICH RECORD WOULD YOU LIKE TO EDIT(Enter ID)?");lel.pack()
                                       le = Entry(stafed);le.pack()
                                       
                                                
                                       def okies(anti):
                                                   id=anti.get()
                                                   if len(id)<3:
                                                      messagebox.showerror("INVALID ID","Please enter complete ID.")
                                                   else:
                                                      file = open('pri_rec.csv', mode='r')
                                                      reader = csv.reader(file)
                                                      flag = 0
                                                      for row in reader:
                                              #skipping empty rows
                                                         if row==[]:
                                                           continue
                                                         elif id in row and row[1]=='0':
                                                            flag+=1
                                                            messagebox.showinfo("DELETED ID","NO RECORD EXISTS")
                                                         if id in row and row[1]!='0':
                                                            flag += 1
                                                            stafed.pack_forget();stafed.place_forget()
                                                            rer = Frame(window);rer.pack()
                                                            optiom = Frame(window);optiom.pack()
                                                            rerw=Label(rer,text="YOUR OLD RECORD WAS AS: ");rerw.pack()
                                                            dek = Label(rer,text="HERE IS THE COMPLETE RECORD OF PRISONER.");dek.pack()
                                                            joidh = Label(rer,text=f"SHOWING RECORD AGAINST ID {row[0]}");joidh.pack()
                                                            nameh = Label(rer,text=f"NAME: {row[1]}\tGENDER: {row[2]}\tAGE: {row[3]}\tWEIGHT: {row[4]}");nameh.pack()
                                                            desi =Label(rer,text=f"HEIGHT: {row[5]}\tHAIRCOLOUR: {row[6]}\tEYECOLOUR: {row[7]}\tCRIME: {row[8]}");desi.pack()
                                                            jobh = Label(rer,text=f"CRIME SPOT: {row[9]}\tCOURT: {row[10]}\tCONVICT\'S LAWYER: {row[11]}\tCONVICTION: {row[12]}");jobh.pack()
                                                            pnum =Label(rer,text=f"STARTING DATE OF PUNISHMENT: {row[13]}\tENDING DATE OF PUNISHMENT: {row[14]}\tRELATION WITH EMERGENCY CONTACT: {row[15]}\tPHONE NUMBER OF EMERGENCY CONTACT: {row[16]}");pnum.pack()
                                                            def chnna():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER NAME:");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  name = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+(int(id[0])*260) +
                                                                     (int(id[1])*26)+ord(id[2])-65, 'name'] = name
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            nam = Button(optiom,text="NAME",cursor='plus',command=chnna);nam.pack()
                                                            def geno():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER GENDER(male/female)");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  gen = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+(int(id[0])*260) +
                                                                     (int(id[1])*26)+ord(id[2])-65, 'gen'] = gen
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            gen=Button(optiom,text="GENDER",cursor='plus',command=geno);gen.pack()
                                                            def chdob():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER AGE");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  dob = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'age'] = dob
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            bod=Button(optiom,text="AGE",cursor='plus',command=chdob);bod.pack()
                                                            def chadd():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER WEIGHT");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  address = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'weight'] = address
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            addr=Button(optiom,text="WEIGHT",cursor='plus',command=chadd);addr.pack()
                                                            def chddes():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER HEIGHT");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  desig = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'height'] = desig
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            desin=Button(optiom,text="HEIGHT",cursor='plus',command=chddes);desin.pack()
                                                            def doko():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER HAIRCOLOUR");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  hiredate = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'hc'] = hiredate
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            dojo= Button(optiom,text="HAIRCOLOUR",cursor='plus',command=doko);dojo.pack()
                                                            def salm():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER EYECOLOUR");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  salary = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'ec'] = salary
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            saala= Button(optiom,text="EYECOLOUR",cursor='plus',command=salm);saala.pack()
                                                            def emcom():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER CRIME");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  econtact = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'crime'] = econtact
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            emoh=Button(optiom,text="CRIME",cursor='plus',command=emcom);emoh.pack()
                                                            def chrelo():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER CRIME SPOT");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  erel = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'crime spot'] = erel
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            relo=Button(optiom,text="CRIME SPOT",cursor='plus',command=chrelo);relo.pack()
                                                            def chreloo():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER COURT");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  erel = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'court'] = erel
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            relo=Button(optiom,text="COURT",cursor='plus',command=chreloo);relo.pack()
                                                            def chreloe():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER CONVICT'S LAWYER");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  erel = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'lawyer'] = erel
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            relo=Button(optiom,text="CONVICT'S LAWYER",cursor='plus',command=chreloe);relo.pack()
                                                            def chreloi():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER CONVICTION");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  erel = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'conviction'] = erel
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            relo=Button(optiom,text="CONVICTION",cursor='plus',command=chreloi);relo.pack()
                                                            def chrelomo():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER STARTING DATE OF PUNISHMENT");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  erel = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'starting date'] = erel
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            relo=Button(optiom,text="STARTING DATE OF PUNISHMENT",cursor='plus',command=chrelomo);relo.pack()
                                                            def chrelohi():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER ENDING DATE OF PUNISHMENT");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  erel = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'ending date'] = erel
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            relo=Button(optiom,text="ENDING DATE OF PUNISHMENT",cursor='plus',command=chrelohi);relo.pack()
                                                            def chconopi():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER NAME OF EMERGENCY CONTACT");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  enum = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) + ord(id[2])-65, 'emergency contact'] = enum
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            conta=Button(optiom,text="NAME OF EMERGENCY CONTACT",cursor='plus',command=chconopi);conta.pack()
                                                            
                                                            def chconopr():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER RELATION OF EMERGENCY CONTACT WITH PRISONER");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  enum = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) + ord(id[2])-65, 'relation'] = enum
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(rer,cnan,optiom));peo.pack()
                                                            conta=Button(optiom,text="RELATIONWITH PRISONER",cursor='plus',command=chconopr);conta.pack()
                                                            
                                                            def chcon():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  enum = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) + ord(id[2])-65, 'contact'] = enum
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(rer,cnan,optiom));peo.pack()
                                                            conta=Button(optiom,text="EMERGENCY NUMBER",cursor='plus',command=chcon);conta.pack()
                                                            def aawa():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               rer.pack_forget();rer.place_forget()
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo1 = Label(cnan,text="ENTER PRISONER NAME");nameo1.pack()
                                                               nam1 = Entry(cnan);nam1.pack()

                                                               nameo2 = Label(cnan,text="ENTER GENDER (Male/Female)");nameo2.pack()
                                                               nam2 = Entry(cnan);nam2.pack()

                                                               nameo3 = Label(cnan,text="ENTER AGE");nameo3.pack()
                                                               nam3 = Entry(cnan);nam3.pack()

                                                               nameo4 = Label(cnan,text="ENTER WEIGHT");nameo4.pack()
                                                               nam4 = Entry(cnan);nam4.pack()

                                                               nameo5 = Label(cnan,text="ENTER HEIGHT");nameo5.pack()
                                                               nam5 = Entry(cnan);nam5.pack()

                                                               nameo6 = Label(cnan,text="ENTER HAIRCOLOUR");nameo6.pack()
                                                               nam6 = Entry(cnan);nam6.pack()

                                                               nameo7 = Label(cnan,text="ENTER EYECOLOUR");nameo7.pack()
                                                               nam7 = Entry(cnan);nam7.pack()

                                                               nameo8 = Label(cnan,text="ENTER CRIME");nameo8.pack()
                                                               nam8 = Entry(cnan);nam8.pack()

                                                               nameo9 = Label(cnan,text="ENTER CRIME SPOT");nameo9.pack()
                                                               nam9 = Entry(cnan);nam9.pack()

                                                               nameo10 = Label(cnan,text="ENTER COURT");nameo10.pack()
                                                               nam10 = Entry(cnan);nam10.pack()

                                                               nameo100 = Label(cnan,text="ENTER THE CONVICT'S LAWYER");nameo100.pack()
                                                               nam11 = Entry(cnan);nam11.pack()

                                                               nameo12 = Label(cnan,text="ENTER CONVICTION");nameo12.pack()
                                                               nam12 = Entry(cnan);nam12.pack()

                                                               nameo13 = Label(cnan,text="ENTER THE DATE PUNISHMENT STARTED AT");nameo13.pack()
                                                               nam13 = Entry(cnan);nam13.pack()

                                                               nameo14 = Label(cnan,text="ENTER THEDATE PUNISHMENT ENDS AT");nameo14.pack()
                                                               nam14 = Entry(cnan);nam14.pack()

                                                               nameo15 = Label(cnan,text="ENTER NAME OF EMERGENCY CONTACT");nameo15.pack()
                                                               nam15 = Entry(cnan);nam15.pack()

                                                               nameo16 = Label(cnan,text="ENTER RELATION OF EMERGENCY CONTACT WITH PRISONER");nameo16.pack()
                                                               nam16 = Entry(cnan);nam16.pack()

                                                               nameo17 = Label(cnan,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT");nameo17.pack()
                                                               nam17 = Entry(cnan);nam17.pack()
                                                               

                                                               def chjo(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17):
                                                                  name=a1.get();gen=a2.get();age=a3.get();wei=a4.get();hei=a5.get()
                                                                  hc=a6.get();ec=a7.get();crime=a8.get();spot=a9.get();court=a10.get()
                                                                  lyr=a11.get();sazaa=a12.get();start_date=a13.get();end_date=a14.get();econtact=a15.get();erel=a16.get();enum=a17.get()
                                                                  df = hira.read_csv("pri_rec.csv")

                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'name'] = name
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'gen'] = gen
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'age'] = age
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'weight'] = wei
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'height'] = hei
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'hc'] = hc
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'ec'] = ec
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'crime'] = crime
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'crime spot'] = spot
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'court'] = court
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'lawyer'] = lyr
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'conviction'] = sazaa
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'starting date'] = start_date
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'ending date'] = end_date
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2]) -
                                                                         65, 'emergency contact'] = econtact
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'relation'] = erel
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'contact'] = enum
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:chjo(nam1,nam2,nam3,nam4,nam5,nam6,nam7,nam8,nam9,nam10,nam11,nam12,nam13,nam14,nam15,nam16,nam17));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justthisonce(rer,optiom,cnan));peo.pack()
                                                            wrec = Button(optiom,text="WHOLE RECORD",cursor='plus',command=aawa);wrec.pack()
                                                            Back=Button(optiom,text="GO BACK TO MAIN MENU",cursor='plus',command=lambda:mainmenui(optiom,rer,stafed));Back.pack()

                                                      if flag == 0:
                                                         messagebox.showerror("ERROR","NO RECORD MATCHING TO THIS ID EXISTS.")              
                                       dal = Button(stafed,text="GET DATA",cursor='plus',command=lambda:okies(le));dal.pack()
                                    dabaiye = Button(stafed,text="PRESS TO VIEW THE LIST OF PRISONER IDS",cursor='plus',command=don);dabaiye.pack()                  
                                    
                                    back=Button(stafed,text="EXIT",cursor='plus',command=lambda:mainmenu(stafed,staffad));back.pack()

  
                                 edit = Button(staffad,text="EDIT RECORD",cursor='plus',command=editt);edit.pack()
                                 def viewst():
                                    staffad.place_forget();staffad.pack_forget()
                                    viewpanel=Frame(window);viewpanel.pack()
                                    wlo=Label(viewpanel,text="WELCOME TO THE VIEWING MENU");wlo.pack()
                                    def krobhai():
                                       kro.pack_forget()
                                       file = open('pri_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                          if row[0] == "id":
                                             pass
                                          
                                          elif row[1]=='0':
                                             continue
                                          else:
                                           recor = Label(viewpanel,text=f"SHOWING RECORD AGAINST ID {row[0]}\nNAME: {row[1]}\tGENDER: {row[2]}\tAGE: {row[3]}\tWEIGHT: {row[4]}\nHEIGHT: {row[5]}\tHAIRCOLOUR: {row[6]}\tEYECOLOUR: {row[7]}\tCRIME: {row[8]}\nCRIME SPOT: {row[9]}\tCOURT: {row[10]}\tCONVICT\'S LAWYER: {row[11]}\tCONVICTION: {row[12]}\nSTARTING DATE OF PUNISHMENT: {row[13]}\tENDING DATE OF PUNISHMENT: {row[14]}\nNAME OF EMERGENCY CONTACT: {row[15]}\tRELATION WITH PRISONER: {row[16]}\tEMERGENCY CONTACT NUMBER: {row[17]}");recor.pack()
                                    

                                    kro = Button(viewpanel,text="PRESS TO VIEW ALL THE PRISONER RECORDS.",cursor='plus',command=krobhai);kro.pack()
                                    back=Button(viewpanel,text="PRESS TO EXIT THE VIEWING MENU.",cursor='plus',command=lambda:mainmenu(viewpanel,staffad));back.pack()                           
                                 view= Button(staffad,text="VIEW RECORD",cursor='plus',command=viewst);view.pack()
                                 def deleteit():
                                    staffad.pack_forget();staffad.place_forget()
                                    delmen = Frame(window);delmen.pack()
                                    oks = Label(delmen,text="HERE IS THE DELETING MENU");oks.pack()
                                    def printo():
                                       file = open('pri_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                       # skipping empty rows causing errors
                                              if row == []:
                                                     continue
                                              # print(row)
                                              if row[0] == "id":
                                                     pass
                                              elif row[1] == "0":
                                                     pass
                                              else:
                                                     stfi=Label(delmen,text=f"PRISONER'S ID IS: {row[0]}\nNAME: {row[1]}\nCRIME: {row[8]}") ;stfi.pack() 
                                       joi = Label(delmen,text="ENTER THE PRISONER'S ID YOU WANT TO DELETE:");joi.pack()
                                       joidd = Entry(delmen);joidd.pack() 
                                       def dodo(ids):
                                          id = ids.get()
                                          if len(id) < 3:
                                             messagebox.showerror("ERROR","Please enter complete ID.")
                                          else:
                                             file = open('pri_rec.csv', mode='r')
                                             reader = csv.reader(file)
                                             flag = 0
                                             for row in reader:
                                              #skipping empty rows
                                                if row==[]:
                                                     continue
                                                
                                                if id in row:
                                                   delmen.pack_forget();delmen.place_forget()
                                                   deko = Frame(window);deko.pack()
                                                   dikhao = Label(deko,text="SHOWING THE WHOLE RECORD OF PRISONER.");dikhao.pack()
                                                   dek = Label(deko,text="HERE IS THE COMPLETE RECORD OF PRISONER.");dek.pack()
                                                   flag += 1
                                                   joidh = Label(deko,text=f"SHOWING RECORD AGAINST ID {row[0]}");joidh.pack()
                                                   nameh = Label(deko,text=f"NAME: {row[1]}\tGENDER: {row[2]}\tAGE: {row[3]}\tWEIGHT: {row[4]}");nameh.pack()
                                                   desi =Label(deko,text=f"HEIGHT: {row[5]}\tHAIRCOLOUR: {row[6]}\tEYECOLOUR: {row[7]}\tCRIME: {row[8]}\nCRIME SPOT: {row[9]}\tCOURT: {row[10]}\tCONVICT\'S LAWYER: {row[11]}\tCONVICTION: {row[12]}");desi.pack()
                                                   relh = Label(deko,text=f"STARTING DATE OF PUNISHMENT: {row[13]}\tENDING DATE OF PUNISHMENT: {row[14]}");relh.pack()
                                                   pnum =Label(deko,text=f"NAME OF EMERGENCY CONTACT: {row[15]}\tRELATION WITH EMERGENCY CONTACT: {row[16]}\tPHONE NUMBER OF EMERGENCY CONTACT: {row[17]}");pnum.pack()
                                                   def dhaade():
                                                      df = hira.read_csv("pri_rec.csv")
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                            ord(id[2])-65, 'name'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                            ord(id[2])-65, 'gen'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'age'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'weight'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'height'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'hc'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'ec'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'crime'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'crime spot'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'court'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'lawyer'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'conviction'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'starting date'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'ending date'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'markofid'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'bloodgrp'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'med'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'disb'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'alrgs'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'covid'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'emergency contact'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'relation'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                             ord(id[2])-65, 'contact'] = '0'
                                                      df.to_csv("pri_rec.csv", index=False)
                                                      messagebox.showinfo("SUCCESS","ID deleted successfully")
                                                      deko.pack_forget();deko.place_forget()
                                                      delmen.pack()
                                                   yay = Button(deko,text="YES",cursor='plus',command=dhaade);yay.pack()
                                                   back = Button(deko,text="NO",command=lambda:mainmenu(deko,delmen));back.pack()
                                             if flag == 0:
                                                
                                                messagebox.showerror("ERROR","NO RECORD MATCHING TO THIS ID EXISTS.")

                                       con = Button(delmen,text="VIEW",cursor='plus',command=lambda:dodo(joidd));con.pack()
                                       back=Button(delmen,text="EXIT",cursor='plus',command=lambda:mainmenu(delmen,staffad));back.pack()

                                    prin = Button(delmen,text="PRESS TO VIEW THE LIST OF PRISONER IDS.",cursor='plus',command=printo);prin.pack()
                                                                   
                                 delete = Button(staffad,text="DELETE RECORD",cursor='plus',command=deleteit);delete.pack()
                                 back=Button(staffad,text="EXIT",cursor='plus',command=lambda:mainmenu(staffad,admin_panel));back.pack()
                                 
                              priso = Button(admin_panel,text="PRISONER",cursor='plus',command=prisopa);priso.pack()
                              def guardi():
                                 admin_panel.place_forget()
                                 staffad = Frame(window);staffad.place(x=700,y=350)
                                 ok = Label(staffad,text="WELCOME TO THE GUARDS MENU\n\n\nMAIN MENU\n\n");ok.pack()
                                 def addst(y):
                                    def add_get(x):
                                       id = x.get()
                                       addsta.pack_forget();addsta.place_forget()
                                       adding = Frame(window);adding.pack()
                                       joid = Label(adding,text=f"USING ID {id}");joid.pack()
                                       namel = Label(adding,text="ENTER THE FULL NAME:");namel.pack()
                                       namee = Entry(adding);namee.pack()
                                       genl = Label(adding,text="ENTER THE GENDER(male/female):");genl.pack()
                                       gene = Entry(adding);gene.pack()
                                       dobl = Label(adding,text="ENTER DATE OF BIRTH: ");dobl.pack()
                                       dobe = Entry(adding);dobe.pack()
                                       addressl = Label(adding,text="ENTER RESIDENTIAL ADDRESS:");addressl.pack()
                                       addresse = Entry(adding);addresse.pack()
                                       desigl = Label(adding,text="ENTER THE DESIGNATION AT THE PRISON: ");desigl.pack()
                                       desige = Entry(adding);desige.pack()
                                       hiredatel = Label(adding,text="ENTER THE DATE OF JOINING THE PRISON: ");hiredatel.pack()
                                       hiredatee = Entry(adding);hiredatee.pack()
                                       salaryl = Label(adding,text="ENTER THE SALARY AMOUNT: ");salaryl.pack()
                                       salarye= Entry(adding);salarye.pack()
                                       econtactl = Label(adding,text="ENTER NAME OF EMERGENCY CONTACT: ");econtactl.pack()
                                       econtacte=Entry(adding);econtacte.pack()
                                       erell = Label(adding,text="ENTER RELATION OF EMERGENCY CONTACT WITH GUARD: ");erell.pack()
                                       erele= Entry(adding);erele.pack()
                                       enuml = Label(adding,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT: ");enuml.pack()
                                       enume= Entry(adding);enume.pack()
                                       def addbe():
                                          df = hira.read_csv("grd_rec.csv")
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'name'] = namee.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'gen'] = gene.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'dob'] = dobe.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'address'] = addresse.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'desig'] = desige.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'hired date'] = hiredatee.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'salary'] = salarye.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'econtact'] = econtacte.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'erel'] = erele.get()
                                          df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'enum'] = enume.get()
                                          df.to_csv("grd_rec.csv", index=False)
                                          added = Label(adding,text="YOUR RECORD IS ADDED... ");added.pack()
                                          adding.after(3000,lambda:[adding.pack_forget(),adding.place_forget()])
                                          y.after(3000,lambda:y.place(x=700,y=350)) 
                                       cont = Button(adding,text="Done Adding",cursor='plus',command=addbe);cont.pack()
                                       back=Button(adding,text="Go back",cursor='plus',command=lambda:mainmenu(adding,staffad));back.pack()
                                    y.place_forget()
                                    addsta = Frame(window);addsta.pack()
                                    df = hira.read_csv("grd_rec.csv")
                                    with open('grd_ids.txt') as openfileobject:
                                       count = 0
                                       flag = 0
                                       for line in openfileobject:
                                          temp = df.loc[count, 'name']
                                          #print(temp)
                                          if temp == '0':
                                             flag = 1  
                                             lines = line
                                             lines = lines.strip('\n')
                                             tell = Label(addsta,text=f"THE EXISTING ID {lines} IS FREE TO USE.");tell.pack()
                                          count += 1
                                          line = line.strip('\n')
                                          #print(line)
                                       if flag == 1:
                                          tello = Label(addsta,text=f"WOULD YOU LIKE TO USE ANY OF THESE IDS(y/n)?");tello.pack()
                                          telloe = Entry(addsta);telloe.pack()
                                          def neeche(x):  
                                             if x.get() == 'y' or x.get() == 'Y':
                                                idl = Label(addsta,text="WHICH ID WOULD YOU LIKE TO USE?");idl.pack()
                                                ide = Entry(addsta);ide.pack()
                                                continu = Button(addsta,text="CONTINUE",cursor='plus',command=lambda:add_get(ide));continu.pack()
                                                back=Button(addsta,text="Go back",cursor='plus',command=lambda:mainmenu(addsta,staffad));back.pack()
                                             elif x.get()=='n' or x.get()=='N':
                                                   addsta.pack_forget();addsta.place_forget()
                                                   adding = Frame(window);adding.pack()
                                                   id = str(line[0]+line[1]+chr(ord(line[2])+1))
                                                   joid = Label(adding,text=f"USING ID {id}");joid.pack()
                                                   namel = Label(adding,text="ENTER THE FULL NAME:");namel.pack()
                                                   namee = Entry(adding);namee.pack()
                                                   genl = Label(adding,text="ENTER THE GENDER(male/female):");genl.pack()
                                                   gene = Entry(adding);gene.pack()
                                                   dobl = Label(adding,text="ENTER DATE OF BIRTH: ");dobl.pack()
                                                   dobe = Entry(adding);dobe.pack()
                                                   addressl = Label(adding,text="ENTER RESIDENTIAL ADDRESS:");addressl.pack()
                                                   addresse = Entry(adding);addresse.pack()
                                                   desigl = Label(adding,text="ENTER THE DESIGNATION AT THE PRISON: ");desigl.pack()
                                                   desige = Entry(adding);desige.pack()
                                                   hiredatel = Label(adding,text="ENTER THE DATE OF JOINING THE PRISON: ");hiredatel.pack()
                                                   hiredatee = Entry(adding);hiredatee.pack()
                                                   salaryl = Label(adding,text="ENTER THE SALARY AMOUNT: ");salaryl.pack()
                                                   salarye= Entry(adding);salarye.pack()
                                                   econtactl = Label(adding,text="ENTER NAME OF EMERGENCY CONTACT: ");econtactl.pack()
                                                   econtacte=Entry(adding);econtacte.pack()
                                                   erell = Label(adding,text="ENTER RELATION OF EMERGENCY CONTACT WITH GUARD: ");erell.pack()
                                                   erele= Entry(adding);erele.pack()
                                                   enuml = Label(adding,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT: ");enuml.pack()
                                                   enume= Entry(adding);enume.pack()
                  
                                                   def addb():
                                                      with open('grd_rec.csv', mode='a') as file:
                                                         writerr = csv.writer(
                                                            file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                                         writerr.writerow(
                                                            [id, namee.get(), gene.get(), dobe.get(), addresse.get(), desige.get(), hiredatee.get(), salarye.get(), econtacte.get(), erele.get(), enume.get()])
                                                      db = open("grd_ids.txt", "a")
                                                      db.write(id+"\n")
                                                      adding.pack_forget();adding.place_forget()
                                                      added = Label(window,text="YOUR RECORD IS ADDED... ",font=("broadway",33));added.pack()
                                                      added.after(1500,lambda:added.destroy())
                                                      y.after(3000,lambda:y.place(x=700,y=350))  
                                                   cont = Button(adding,text="Done Adding",cursor='plus',command=addb);cont.pack()
                                                   back=Button(adding,text="Go back",cursor='plus',command=lambda:mainmenu(adding,staffad));back.pack() 
                                          contin = Button(addsta,text="CONTINUE",command=lambda:neeche(telloe));contin.pack() 
                                       else:
                                          addsta.pack_forget();addsta.place_forget()
                                          adding = Frame(window);adding.pack()
                                          id = str(line[0]+line[1]+chr(ord(line[2])+1))
                                          joid = Label(adding,text=f"USING ID {id}");joid.pack()
                                          namel = Label(adding,text="ENTER THE FULL NAME:");namel.pack()
                                          namee = Entry(adding);namee.pack()
                                          genl = Label(adding,text="ENTER THE GENDER(male/female):");genl.pack()
                                          gene = Entry(adding);gene.pack()
                                          dobl = Label(adding,text="ENTER DATE OF BIRTH: ");dobl.pack()
                                          dobe = Entry(adding);dobe.pack()
                                          addressl = Label(adding,text="ENTER RESIDENTIAL ADDRESS:");addressl.pack()
                                          addresse = Entry(adding);addresse.pack()
                                          desigl = Label(adding,text="ENTER THE DESIGNATION AT THE PRISON: ");desigl.pack()
                                          desige = Entry(adding);desige.pack()
                                          hiredatel = Label(adding,text="ENTER THE DATE OF JOINING THE PRISON: ");hiredatel.pack()
                                          hiredatee = Entry(adding);hiredatee.pack()
                                          salaryl = Label(adding,text="ENTER THE SALARY AMOUNT: ");salaryl.pack()
                                          salarye= Entry(adding);salarye.pack()
                                          econtactl = Label(adding,text="ENTER NAME OF EMERGENCY CONTACT: ");econtactl.pack()
                                          econtacte=Entry(adding);econtacte.pack()
                                          erell = Label(adding,text="ENTER RELATION OF EMERGENCY CONTACT WITH GUARD: ");erell.pack()
                                          erele= Entry(adding);erele.pack()
                                          enuml = Label(adding,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT: ");enuml.pack()
                                          enume= Entry(adding);enume.pack()

                                          def addb():
                                             with open('grd_rec.csv', mode='a') as file:
                                                writerr = csv.writer(
                                                   file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                                writerr.writerow(
                                                   [id,namee.get(), gene.get(), dobe.get(), addresse.get(), desige.get(), hiredatee.get(), salarye.get(), econtacte.get(), erele.get(), enume.get()])
                                             db = open("grd_ids.txt", "a")
                                             db.write(id+"\n")
                                             adding.pack_forget();adding.place_forget()
                                             added = Label(window,text="YOUR RECORD IS ADDED... ",font=("broadway",33));added.pack()
                                             added.after(1500,lambda:added.pack_forget())
                                             y.after(3000,lambda:y.place(x=700,y=350))
                                          cont = Button(adding,text="Done Adding",cursor='plus',command=addb);cont.pack()
                                          back=Button(adding,text="Go back",cursor='plus',command=lambda:mainmenu(adding,staffad));back.pack()
                                 add = Button(staffad,text="ADD RECORD",cursor='plus',command=lambda:addst(staffad));add.pack()
                                 def searchst():
                                    staffad.place_forget();staffad.pack_forget()
                                    searst= Frame(window);searst.pack()
                                    sit = Label(searst,text="HERE IS THE SEARCHING MENU");sit.pack()
                                    def show():
                                       file = open('grd_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                          if row == []:
                                             continue
                                          if row[0] == "id":
                                             pass
                                          elif row[1] == "0":
                                             pass
                                          
                                          else:
                                             pid = Label(searst,text=f"GUARD'S ID IS: {row[0]}");pid.pack()
                                             pna = Label(searst,text=f"NAME: {row[1]}");pna.pack()
                                             pde = Label(searst,text=f"DESIGNATION: {row[5]}");pde.pack()
                                       choice = Label(searst,text="WHICH RECORD WOULD YOU LIKE TO SEARCH?");choice.pack()
                                       idel = Label(searst,text="ENTER GUARD ID:");idel.pack();ide=Entry(searst);ide.pack()
                                       def dekho(ach):
                                          ids = ach.get()
                                          if len(ids) < 3:
                                             messagebox.showerror("ERROR","Please enter complete ID.")
                                          else:
                                             file = open('grd_rec.csv', mode='r')
                                             reader = csv.reader(file)
                                             flag = 0
                                             for row in reader:
                                              #skipping empty rows
                                                if row==[]:
                                                     continue
                                                if ids in row:
                                                   searst.pack_forget();searst.place_forget()
                                                   neb=Frame(window);neb.pack()
                                                   dek = Label(neb,text="HERE IS THE COMPLETE RECORD OF GUARD.");dek.pack()
                                                   flag += 1
                                                   joidh = Label(neb,text=f"SHOWING RECORD AGAINST ID {row[0]}");joidh.pack()
                                                   nameh = Label(neb,text=f"NAME: {row[1]}");nameh.pack()
                                                   genderh =Label(neb,text=f"GENDER: {row[2]}");genderh.pack()
                                                   bipl = Label(neb,text=f"DATE OF BIRTH: {row[3]}");bipl.pack()
                                                   ader=Label(neb,text=f"ADDRESS: {row[4]}");ader.pack()
                                                   desi =Label(neb,text=f"DESGINATION: {row[5]}");desi.pack()
                                                   jobh = Label(neb,text=f"JOB JOINING DATE: {row[6]}");jobh.pack()
                                                   salh=Label(neb,text=f"GUARD'S SALARY IS: {row[7]}");salh.pack()
                                                   ecoe =Label(neb,text=f"EMERGENCY CONTACT: {row[8]}");ecoe.pack()
                                                   relh = Label(neb,text=f"RELATION WITH EMERGENCY CONTACT: {row[9]}");relh.pack()
                                                   pnum =Label(neb,text=f"PHONE NUMBER OF EMERGENCY CONTACT: {row[10]}");pnum.pack()
                                                   back = Button(neb,text="GO BACK",command=lambda:mainmenu(neb,searst));back.pack()
                                             if flag == 0:
                                                
                                                messagebox.showerror("ERROR","NO RECORD MATCHING TO THIS ID EXISTS.")

                                       aage = Button(searst,text="SEARCH",cursor='plus',command=lambda:dekho(ide));aage.pack()
                                    press = Button(searst,text="PRESS TO VIEW THE LIST OF GUARDS IDS.",command=show);press.pack()
                                    back = Button(searst,text="GO BACK",command=lambda:mainmenu(searst,staffad));back.pack() 
                                 search = Button(staffad,text="SEARCH RECORD",cursor='plus',command=searchst);search.pack()
                                 def editt():
                                    staffad.pack_forget();staffad.place_forget()
                                    stafed=Frame(window);stafed.pack()
                                    aaiye = Label(stafed,text="WELCOME TO THE EDITING MENU");aaiye.pack()
                                    def don():
                                       file = open('grd_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                           if row == []:
                                                  continue
                                           # print(row)
                                           if row[0] == "id":
                                                  pass
                                           elif row[1] == "0":
                                                pass
                                           else:
                                                diko=Label(stafed,text=f"GUARD'S ID IS:  {row[0]}\nNAME: {row[1]}\nDESIGNATION: {row[5]}");diko.pack()
                                       lel=Label(stafed,text="WHICH RECORD WOULD YOU LIKE TO EDIT(Enter ID)?");lel.pack()
                                       le = Entry(stafed);le.pack()
                                       
                                                
                                       def okies(anti):
                                                   id=anti.get()
                                                   if len(id)<3:
                                                      messagebox.showerror("INVALID ID","Please enter complete ID.")
                                                   else:
                                                      file = open('grd_rec.csv', mode='r')
                                                      reader = csv.reader(file)
                                                      flag = 0
                                                      for row in reader:
                                              #skipping empty rows
                                                         if row==[]:
                                                           continue
                                                         if id in row:
                                                            flag += 1
                                                            stafed.pack_forget();stafed.place_forget()
                                                            rer = Frame(window);rer.pack()
                                                            optiom = Frame(window);optiom.pack()
                                                            rerw=Label(rer,text="YOUR OLD RECORD WAS AS: ");rerw.pack()
                                                            dek = Label(rer,text="HERE IS THE COMPLETE RECORD OF STAFF.");dek.pack()
                                                            joidh = Label(rer,text=f"SHOWING RECORD AGAINST ID {row[0]}");joidh.pack()
                                                            nameh = Label(rer,text=f"NAME: {row[1]}");nameh.pack()
                                                            genderh =Label(rer,text=f"GENDER: {row[2]}");genderh.pack()
                                                            bipl = Label(rer,text=f"DATE OF BIRTH: {row[3]}");bipl.pack()
                                                            ader=Label(rer,text=f"ADDRESS: {row[4]}");ader.pack()
                                                            desi =Label(rer,text=f"DESGINATION: {row[5]}");desi.pack()
                                                            jobh = Label(rer,text=f"JOB JOINING DATE: {row[6]}");jobh.pack()
                                                            salh=Label(rer,text=f"GUARD'S SALARY IS: {row[7]}");salh.pack()
                                                            ecoe =Label(rer,text=f"EMERGENCY CONTACT: {row[8]}");ecoe.pack()
                                                            relh = Label(rer,text=f"RELATION WITH EMERGENCY CONTACT: {row[9]}");relh.pack()
                                                            pnum =Label(rer,text=f"PHONE NUMBER OF EMERGENCY CONTACT: {row[10]}");pnum.pack()
                                                            opti=Label(rer,text="WHAT WOULD YOU LIKE TO EDIT?");opti.pack()
                                                            def chnna():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("grd_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER NAME:");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  name = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+(int(id[0])*260) +
                                                                     (int(id[1])*26)+ord(id[2])-65, 'name'] = name
                                                                  df.to_csv("grd_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            nam = Button(optiom,text="NAME",cursor='plus',command=chnna);nam.pack()
                                                            def geno():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("grd_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER GENDER(male/female)");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  gen = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+(int(id[0])*260) +
                                                                     (int(id[1])*26)+ord(id[2])-65, 'gen'] = gen
                                                                  df.to_csv("grd_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            gen=Button(optiom,text="GENDER",cursor='plus',command=geno);gen.pack()
                                                            def chdob():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("grd_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER DATE OF BIRTH");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  dob = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'dob'] = dob
                                                                  df.to_csv("grd_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            bod=Button(optiom,text="DATE OF BIRTH",cursor='plus',command=chdob);bod.pack()
                                                            def chadd():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("grd_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER RESIDENTIAL ADDRESS");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  address = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'address'] = address
                                                                  df.to_csv("grd_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            addr=Button(optiom,text="ADDRESS",cursor='plus',command=chadd);addr.pack()
                                                            def chddes():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("grd_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER THE DESIGNATION AT THE PRISON");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  desig = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'desig'] = desig
                                                                  df.to_csv("grd_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            desin=Button(optiom,text="DESIGNATION",cursor='plus',command=chddes);desin.pack()
                                                            def doko():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("grd_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER THE DATE OF JOINING THE PRISON");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  hiredate = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'hired date'] = hiredate
                                                                  df.to_csv("grd_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            dojo= Button(optiom,text="DATE OF JOINING",cursor='plus',command=doko);dojo.pack()
                                                            def salm():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("grd_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER THE SALARY AMOUNT");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  salary = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'salary'] = salary
                                                                  df.to_csv("grd_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            saala= Button(optiom,text="SALARY",cursor='plus',command=salm);saala.pack()
                                                            def emcom():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("grd_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER NAME OF EMERGENCY CONTACT");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  econtact = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'econtact'] = econtact
                                                                  df.to_csv("grd_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            emoh=Button(optiom,text="EMERGENCY CONTACT",cursor='plus',command=emcom);emoh.pack()
                                                            def chrelo():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("grd_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER RELATION OF EMERGENCY CONTACT WITH GUARD");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  erel = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'erel'] = erel
                                                                  df.to_csv("grd_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            relo=Button(optiom,text="RELATION WITH EMERGENCY CONTACT",cursor='plus',command=chrelo);relo.pack()
                                                            def chcon():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("grd_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  enum = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) + ord(id[2])-65, 'enum'] = enum
                                                                  df.to_csv("grd_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            conta=Button(optiom,text="CONTACT NO. OF EMERGENCY CONTACT",cursor='plus',command=chcon);conta.pack()
                                                            def aawa():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("grd_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo1 = Label(cnan,text="ENTER GUARD NAME");nameo1.pack()
                                                               nam1 = Entry(cnan);nam1.pack()

                                                               nameo2 = Label(cnan,text="ENTER GENDER (Male/Female)");nameo2.pack()
                                                               nam2 = Entry(cnan);nam2.pack()

                                                               nameo3 = Label(cnan,text="ENTER DATE OF BIRTH");nameo3.pack()
                                                               nam3 = Entry(cnan);nam3.pack()

                                                               nameo4 = Label(cnan,text="ENTER RESIDENTIAL ADDRESS");nameo4.pack()
                                                               nam4 = Entry(cnan);nam4.pack()

                                                               nameo5 = Label(cnan,text="ENTER THE DESIGNATION AT THE PRISON");nameo5.pack()
                                                               nam5 = Entry(cnan);nam5.pack()

                                                               nameo6 = Label(cnan,text="ENTER THE DATE OF JOINING THE PRISON");nameo6.pack()
                                                               nam6 = Entry(cnan);nam6.pack()

                                                               nameo7 = Label(cnan,text="ENTER THE SALARY AMOUNT");nameo7.pack()
                                                               nam7 = Entry(cnan);nam7.pack()

                                                               nameo8 = Label(cnan,text="ENTER NAME OF EMERGENCY CONTACT");nameo8.pack()
                                                               nam8 = Entry(cnan);nam8.pack()

                                                               nameo9 = Label(cnan,text="ENTER RELATION OF EMERGENCY CONTACT WITH GUARD");nameo9.pack()
                                                               nam9 = Entry(cnan);nam9.pack()

                                                               nameo10 = Label(cnan,text="ENTER PHOME NUMBER OF EMERGENCY CONTACT");nameo10.pack()
                                                               nam10 = Entry(cnan);nam10.pack()
                                                               def chjo(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
                                                                  name=a1.get();gen=a2.get();dob=a3.get();address=a4.get();desig=a5.get();hiredate=a6.get();salary=a7.get();econtact=a8.get();erel=a9.get();enum=a10.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) + ord(id[2])-65, 'name'] = name
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'gen'] = gen
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'dob'] = dob
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) + ord(id[2])-65, 'address'] = address
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'desig'] = desig
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'hired date'] = hiredate
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'salary'] = salary
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2]) -65, 'econtact'] = econtact
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'erel'] = erel
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'enum'] = enum
                                                                  df.to_csv("grd_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:chjo(nam1,nam2,nam3,nam4,nam5,nam6,nam7,nam8,nam9,nam10));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:mainmenu(cnan,optiom));peo.pack()
                                                            wrec = Button(optiom,text="WHOLE RECORD",cursor='plus',command=aawa);wrec.pack()
                                                            Back=Button(optiom,text="GO BACK TO MAIN MENU",cursor='plus',command=lambda:mainmenui(optiom,rer,stafed));Back.pack()

                                                      if flag == 0:
                                                         messagebox.showerror("ERROR","NO RECORD MATCHING TO THIS ID EXISTS.")              
                                       dal = Button(stafed,text="GET DATA",cursor='plus',command=lambda:okies(le));dal.pack()
                                    dabaiye = Button(stafed,text="PRESS TO VIEW THE LIST OF GUARD IDS",cursor='plus',command=don);dabaiye.pack()                  
                                    
                                    back=Button(stafed,text="EXIT",cursor='plus',command=lambda:mainmenu(stafed,staffad));back.pack()


                                    
                                    
                                 edit = Button(staffad,text="EDIT RECORD",cursor='plus',command=editt);edit.pack()
                                 def viewst():
                                    staffad.place_forget();staffad.pack_forget()
                                    viewpanel=Frame(window);viewpanel.pack()
                                    wlo=Label(viewpanel,text="WELCOME TO THE VIEWING MENU");wlo.pack()
                                    def krobhai():
                                       kro.pack_forget()
                                       file = open('grd_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                          if row[0] == "id":
                                             pass
                                          elif row==[]:
                                           continue  
                                          elif row[1]=='0':
                                             continue
                                          else:
                                            recor = Label(viewpanel,text=f"SHOWING RECORD AGAINST ID {row[0]}\nNAME {row[1]}\nGENDER: {row[2]}\nDATE OF BIRTH: {row[3]}\nADDRESS: {row[4]}\nDESGINATION: {row[5]}\nJOB JOINING DATE: {row[6]}\nSTAFF'S SALARY IS: {row[7]}\nEMERGENCY CONTACT: {row[8]}\nRELATION WITH EMERGENCY CONTACT: {row[9]}\nPHONE NUMBER OF EMERGENCY CONTACT: {row[10]}\n\n");recor.pack()
                                    

                                    kro = Button(viewpanel,text="PRESS TO VIEW ALL THE GUARDS RECORDS.",cursor='plus',command=krobhai);kro.pack()
                                    back=Button(viewpanel,text="PRESS TO EXIT THE VIEWING MENU.",cursor='plus',command=lambda:mainmenu(viewpanel,staffad));back.pack()                           
                                 view= Button(staffad,text="VIEW RECORD",cursor='plus',command=viewst);view.pack()
                                 def deleteit():
                                    staffad.pack_forget();staffad.place_forget()
                                    delmen = Frame(window);delmen.pack()
                                    oks = Label(delmen,text="HERE IS THE DELETING MENU");oks.pack()
                                    def printo():
                                       file = open('grd_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                       # skipping empty rows causing errors
                                              if row == []:
                                                     continue
                                              # print(row)
                                              if row[0] == "id":
                                                     pass
                                              elif row[1] == "0":
                                                     pass
                                              else:
                                                     stfi=Label(delmen,text=f"GUARD'S ID IS: {row[0]}\nNAME: {row[1]}\nDESIGNATION: {row[5]}") ;stfi.pack() 
                                       joi = Label(delmen,text="ENTER THE GUARD'S ID YOU WANT TO DELETE:");joi.pack()
                                       joidd = Entry(delmen);joidd.pack() 
                                       def dodo(ids):
                                          id = ids.get()
                                          if len(id) < 3:
                                             messagebox.showerror("ERROR","Please enter complete ID.")
                                          else:
                                             file = open('grd_rec.csv', mode='r')
                                             reader = csv.reader(file)
                                             flag = 0
                                             for row in reader:
                                              #skipping empty rows
                                                if row==[]:
                                                     continue
                                                if id in row:
                                                   delmen.pack_forget();delmen.place_forget()
                                                   deko = Frame(window);deko.pack()
                                                   dikhao = Label(deko,text="SHOWING THE WHOLE RECORD OF GUARD.");dikhao.pack()
                                                   dek = Label(deko,text="HERE IS THE COMPLETE RECORD OF GUARD.");dek.pack()
                                                   flag += 1
                                                   joidh = Label(deko,text=f"SHOWING RECORD AGAINST ID {row[0]}");joidh.pack()
                                                   nameh = Label(deko,text=f"NAME: {row[1]}");nameh.pack()
                                                   genderh =Label(deko,text=f"GENDER: {row[2]}");genderh.pack()
                                                   bipl = Label(deko,text=f"DATE OF BIRTH: {row[3]}");bipl.pack()
                                                   ader=Label(deko,text=f"ADDRESS: {row[4]}");ader.pack()
                                                   desi =Label(deko,text=f"DESGINATION: {row[5]}");desi.pack()
                                                   jobh = Label(deko,text=f"JOB JOINING DATE: {row[6]}");jobh.pack()
                                                   salh=Label(deko,text=f"GUARD'S SALARY IS: {row[7]}");salh.pack()
                                                   ecoe =Label(deko,text=f"EMERGENCY CONTACT: {row[8]}");ecoe.pack()
                                                   relh = Label(deko,text=f"RELATION WITH EMERGENCY CONTACT: {row[9]}");relh.pack()
                                                   pnum =Label(deko,text=f"PHONE NUMBER OF EMERGENCY CONTACT: {row[10]}");pnum.pack()
                                                   quwe = Label(deko,text="ARE YOU SURE YOU WANT TO DELETE THE RECORD?");quwe.pack()
                                                   def dhaade():
                                                      df = hira.read_csv("grd_rec.csv")
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) + ord(id[2])-65, 'name'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'gen'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'dob'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) + ord(id[2])-65, 'address'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'desig'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'hired date'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'salary'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2]) -65, 'econtact'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'erel'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, 'enum'] = '0'
                                                      df.to_csv("grd_rec.csv", index=False)
                                                      messagebox.showinfo("SUCCESS","ID deleted successfully")
                                                      deko.pack_forget();deko.place_forget()
                                                      delmen.pack()
                                                   yay = Button(deko,text="YES",cursor='plus',command=dhaade);yay.pack()
                                                   back = Button(deko,text="NO",command=lambda:mainmenu(deko,delmen));back.pack()
                                             if flag == 0:
                                                
                                                messagebox.showerror("ERROR","NO RECORD MATCHING TO THIS ID EXISTS.")

                                       con = Button(delmen,text="VIEW",cursor='plus',command=lambda:dodo(joidd));con.pack()
                                       back=Button(delmen,text="EXIT",cursor='plus',command=lambda:mainmenu(delmen,staffad));back.pack()

                                    prin = Button(delmen,text="PRESS TO VIEW THE LIST OF GUARD IDS.",cursor='plus',command=printo);prin.pack()
                                                                   
                                 delete = Button(staffad,text="DELETE RECORD",cursor='plus',command=deleteit);delete.pack()
                                 back=Button(staffad,text="EXIT",cursor='plus',command=lambda:mainmenu(staffad,admin_panel));back.pack()
                              guards = Button(admin_panel,text="GUARDS",cursor='plus',command=guardi);guards.pack()
                              signou = Button(admin_panel,text="SIGNOUT",cursor='plus',command=lambda:signout(admin_panel,windowframe));signou.pack()
                              
                           else:
                              messagebox.showerror("ERROR","Wrong password")

                        except:
                           messagebox.showerror("ERROR","Incorrect passwords or username")
                           
                     else:
                        messagebox.showerror("ERROR","Username doesn't exist")
                        
                  except:
                     messagebox.showerror("ERROR","Password or username doesn't exist")

         else:
               messagebox.showerror("ERROR","Please attempt login again")
      Login = Button(newframe1,text="Login",cursor='plus',command=lambda: gainAccess(username,passwi));Login.pack()
      back = Button(newframe1,text='EXIT',cursor='plus',command=lambda:mainmenu(newframe1,windowframe));back.pack()
def clicked_staff():
      windowframe.place_forget()
      window.title("Welcome Staff.")
      newframe1 = Frame(window);newframe1.place(x=700,y=350)
      option = Label(newframe1,text='\n PRISON STAFF \n\n\nWhat would you like to do?');option.pack()

      def Signup():
         newframe1.place_forget()
         newlogin = Frame(window);newlogin.place(x=700,y=350)
         usern = Label(newlogin,text="Username");usern.pack()
         username=Entry(newlogin);username.pack()
         passw = Label(newlogin,text="Password");passw.pack()
         passwi=Entry(newlogin,show="*");passwi.pack()
         passww = Label(newlogin,text="Confirm Password");passww.pack()
         passwii=Entry(newlogin,show="*");passwii.pack()
         def register(useren, pass1en, pass2en):
            Username = useren.get()
            Password1 = pass1en.get()
            Password2 = pass2en.get()
            if  not len(Password1)<=8:
               pass
            else: 
               messagebox.showerror("ERROR","Password too short. Enter a different one. ")
            db = open("cred_staff.txt", "r")
            d = []
            for i in db:
               a,b = i.split(",")
               b = b.strip()
               c = a,b
               d.append(a)
            if not len(Password1)<=8:
               db = open("cred_staff.txt", "r")
               if not Username ==None:
                  if len(Username) <1:
                     ("Please provide a username")

                  elif Username in d:
                     messagebox.showerror("ERROR","Username exists")
		
                  else:
                     if Password1 == Password2:
                        Password1 = Password1.encode('utf-8')
                        Password1 = bcrypt.hashpw(Password1, bcrypt.gensalt())      
                        db = open("cred_staff.txt", "a")
                        db.write(Username+", "+str(Password1)+"\n")
                        messagebox.showinfo("User created successfully!","Please login to proceed:")

                     else:
                        messagebox.showerror("ERROR","Passwords do not match")



         enter = Button(newlogin,text = 'Register',cursor='plus',command=lambda:register(username,passwi,passwii));enter.pack()
         back = Button(newlogin,text='EXIT',cursor='plus',command=lambda:mainmenu(newlogin,newframe1));back.pack()

      signup = Button(newframe1,text="Signup",cursor='plus',command=Signup)
      signup.pack()
      
      def login():
         newframe1.place_forget()
         newlogin = Frame(window);newlogin.place(x=700,y=350)
         usern = Label(newlogin,text="Username");usern.pack()
         username=Entry(newlogin);username.pack()
         passw = Label(newlogin,text="Password");passw.pack()
         passwi=Entry(newlogin,show="*");passwi.pack()
         def gainAccess(usern, passwo):
            Username = usern.get()
            Password=passwo.get()
            if not len(Username or Password) < 1:
               if True:
                  db = open("cred_staff.txt", "r")
                  d = []
                  f = []
                  for i in db:
                     a,b = i.split(",")
                     b = b.strip()
                     c = a,b
                     d.append(a)
                     f.append(b)
                     data = dict(zip(d, f))

                  try:
                     if Username in data:
                        hashed = data[Username].strip('b')
                        hashed = hashed.replace("'", "")
                        hashed = hashed.encode('utf-8')

                        try:
                           if bcrypt.checkpw(Password.encode(), hashed):
                              newlogin.place_forget();newlogin.place_forget()
                              messagebox.showinfo("Login Successful",f"Welcome {Username}")
                              
                              admin_panel = Frame(window);admin_panel.after(1000,lambda:admin_panel.place(x=700,y=350))
                              def medpan():
                                 
                                 admin_panel.place_forget()
                                 staffad = Frame(window);staffad.place(x=700,y=350)
                                 ok = Label(staffad,text="WELCOME TO THE PRISONER MEDICAL RECORD\n\n\nMAIN MENU\n\n");ok.pack()
                                 def addst(y):
                                    y.place_forget()
                                    addsta = Frame(window);addsta.pack()
                                    file = open('pri_rec.csv', mode='r')
                                    reader = csv.reader(file)
                                    for row in reader:
                                          if row == []:
                                              continue
                                          elif row[0] == "id":
                                              continue
                                          elif row[1] == "0":
                                              continue
                                          elif row[18] !="0" and row[18] !='':
                                              continue
                                          else:
                                             stfi=Label(addsta,text=f"PRISONER'S ID IS: {row[0]}\nNAME: {row[1]}") ;stfi.pack() 
                                    joi = Label(addsta,text="ENTER THE PRISONER'S ID YOU WANT TO ADD:");joi.pack()
                                    joidd = Entry(addsta);joidd.pack() 
                                    def dalso(n):
                                                id =n.get()
                                                addsta.pack_forget();addsta.place_forget()
                                                adding = Frame(window);adding.pack()
                                                joid = Label(adding,text=f"USING ID {id}");joid.pack()
                                                namel = Label(adding,text="MARK OF IDENTIFICATION");namel.pack()
                                                namee = Entry(adding);namee.pack()
                                                genl = Label(adding,text="BLOOD GROUP:");genl.pack()
                                                gene = Entry(adding);gene.pack()
                                                dobl = Label(adding,text="ANY REGULAR MEDICINES");dobl.pack()
                                                dobe = Entry(adding);dobe.pack()
                                                addressl = Label(adding,text="DIABILTIES");addressl.pack()
                                                addresse = Entry(adding);addresse.pack()
                                                desigl = Label(adding,text="ALERGIES");desigl.pack()
                                                desige = Entry(adding);desige.pack()
                                                hiredatel = Label(adding,text="COVID VACCINATION(yes/no/partial)");hiredatel.pack()
                                                hiredatee = Entry(adding);hiredatee.pack()

                                                def addb():
                                                   df=hira.read_csv('pri_rec.csv')
                                                   df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'markofid'] = namee.get()
                                                   df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'bloodgrp'] = gene.get()
                                                   df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'med'] = dobe.get()
                                                   df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'disb'] = addresse.get()
                                                   df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'alrgs'] = desige.get()
                                                   df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'covid'] = hiredatee.get()
                                                   df.to_csv("pri_rec.csv", index=False)
                                                   adding.pack_forget();adding.place_forget()
                                                   added = Label(window,text="YOUR RECORD IS ADDED... ",font=("broadway",33));added.pack()
                                                   added.after(1500,lambda:added.pack_forget())
                                                   y.after(3000,lambda:y.place(x=700,y=350))
                                                cont = Button(adding,text="Done Adding",cursor='plus',command=addb);cont.pack()
                                    conti = Button(addsta,text="COTINUE",cursor='plus',command=lambda:dalso(joidd));conti.pack()
                                    back=Button(addsta,text="Go back",cursor='plus',command=lambda:mainmenu(addsta,staffad));back.pack()
                                 add = Button(staffad,text="ADD RECORD",cursor='plus',command=lambda:addst(staffad));add.pack()
                                 def searchst():
                                    staffad.place_forget();staffad.pack_forget()
                                    searst= Frame(window);searst.pack()
                                    sit = Label(searst,text="HERE IS THE SEARCHING MENU");sit.pack()
                                    def show():
                                       file = open('pri_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                          if row == []:
                                             continue
                                          if row[0] == "id":
                                             pass
                                          elif row[1] == "0":
                                             continue
                                          else:
                                             pid = Label(searst,text=f"PRISONER'S ID IS: {row[0]}");pid.pack()
                                             pna = Label(searst,text=f"NAME: {row[1]}");pna.pack()
                                             pde = Label(searst,text=f"CRIME: {row[8]}");pde.pack()
                                       choice = Label(searst,text="WHICH MEDICAL RECORD WOULD YOU LIKE TO SEARCH?");choice.pack()
                                       idel = Label(searst,text="ENTER PRISONER ID:");idel.pack();ide=Entry(searst);ide.pack()
                                       def dekho(ach):
                                          ids = ach.get()
                                          if len(ids) < 3:
                                             messagebox.showerror("ERROR","Please enter complete ID.")
                                          else:
                                             file = open('pri_rec.csv', mode='r')
                                             reader = csv.reader(file)
                                             flag = 0
                                             for row in reader:
                                              #skipping empty rows
                                                if row==[]:
                                                     continue
                                                if ids in row and row[1]!='0':
                                                   searst.pack_forget();searst.place_forget()
                                                   neb=Frame(window);neb.pack()
                                                   dek = Label(neb,text="HERE IS THE MEDICAL RECORD OF PRISONER.");dek.pack()
                                                   flag += 1
                                                   joidh = Label(neb,text=f"SHOWING RECORD AGAINST ID {row[0]}");joidh.pack()
                                                   nameh = Label(neb,text=f"NAME: {row[1]}\tAGE: {row[3]}\tWEIGHT: {row[4]}");nameh.pack()
                                                   desi =Label(neb,text=f"HEIGHT: {row[5]}\tMARK OF IDENTIFICATION: {row[18]}\tMEDICINE ON REGULAR BASIS: {row[19]}");desi.pack()
                                                   relh = Label(neb,text=f"BLOOD GROUP: {row[20]}\tANY DISABILITY: {row[21]}");relh.pack()
                                                   pnum =Label(neb,text=f"ANY ALLERGIES: {row[22]}\tCOVID-19 VACCINATION(yes/no): {row[23]}");pnum.pack()
                                                   back = Button(neb,text="GO BACK",command=lambda:mainmenu(neb,searst));back.pack()
                                             if flag == 0:
                                                
                                                messagebox.showerror("ERROR","NO RECORD MATCHING TO THIS ID EXISTS.")

                                       aage = Button(searst,text="SEARCH",cursor='plus',command=lambda:dekho(ide));aage.pack()
                                    press = Button(searst,text="PRESS TO VIEW THE LIST OF PRISONER IDS.",command=show);press.pack()
                                    back = Button(searst,text="GO BACK",command=lambda:mainmenu(searst,staffad));back.pack() 
                                 search = Button(staffad,text="SEARCH RECORD",cursor='plus',command=searchst);search.pack()
                                 def editt():
                                    staffad.pack_forget();staffad.place_forget()
                                    stafed=Frame(window);stafed.pack()
                                    aaiye = Label(stafed,text="WELCOME TO THE EDITING MENU");aaiye.pack()
                                    def don():
                                       file = open('pri_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                           if row == []:
                                                  continue
                                           # print(row)
                                           if row[0] == "id":
                                                  pass
                                           elif row[1] == "0":
                                                continue
                                           else:
                                                diko=Label(stafed,text=f"PRISONER'S ID IS:  {row[0]}\nNAME: {row[1]}\nCRIME: {row[8]}");diko.pack()
                                       lel=Label(stafed,text="WHICH RECORD WOULD YOU LIKE TO EDIT(Enter ID)?");lel.pack()
                                       le = Entry(stafed);le.pack()
                                       
                                                
                                       def okies(anti):
                                                   id=anti.get()
                                                   if len(id)<3:
                                                      messagebox.showerror("INVALID ID","Please enter complete ID.")
                                                   else:
                                                      file = open('pri_rec.csv', mode='r')
                                                      reader = csv.reader(file)
                                                      flag = 0
                                                      for row in reader:
                                              #skipping empty rows
                                                         if row==[]:
                                                           continue
                                                         elif id in row and row[1]=='0':
                                                            flag+=1
                                                            messagebox.showinfo("DELETED ID","NO RECORD EXISTS")
                                                         if id in row and row[1]!='0':
                                                            flag += 1
                                                            stafed.pack_forget();stafed.place_forget()
                                                            rer = Frame(window);rer.pack()
                                                            optiom = Frame(window);optiom.pack()
                                                            dek = Label(rer,text="HERE IS THE MEDICAL RECORD OF PRISONER.");dek.pack()
                                                   
                                                            joidh = Label(rer,text=f"SHOWING RECORD AGAINST ID {row[0]}");joidh.pack()
                                                            nameh = Label(rer,text=f"NAME: {row[1]}\tAGE: {row[3]}\tWEIGHT: {row[4]}");nameh.pack()
                                                            desi =Label(rer,text=f"HEIGHT: {row[5]}\tMARK OF IDENTIFICATION: {row[18]}\tMEDICINE ON REGULAR BASIS: {row[19]}");desi.pack()
                                                            relh = Label(rer,text=f"BLOOD GROUP: {row[20]}\tANY DISABILITY: {row[21]}");relh.pack()
                                                            pnum =Label(rer,text=f"ANY ALLERGIES: {row[22]}\tCOVID-19 VACCINATION(yes/no): {row[23]}");pnum.pack()
                                                            back = Button(rer,text="GO BACK",command=lambda:mainmenu(rer,stafed));back.pack()
                                                            def chnna():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER MARK OF IDENTIFICATION:");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  name = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+(int(id[0])*260) +
                                                                     (int(id[1])*26)+ord(id[2])-65, 'markofid'] = name
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            nam = Button(optiom,text="MARK OF IDENTIFICATION",cursor='plus',command=chnna);nam.pack()
                                                            def geno():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER BLOOD GROUP");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  gen = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+(int(id[0])*260) +
                                                                     (int(id[1])*26)+ord(id[2])-65, 'bloodgrp'] = gen
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            gen=Button(optiom,text="BLOOD GROUP",cursor='plus',command=geno);gen.pack()
                                                            def chdob():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER MEDICINE");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  dob = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'med'] = dob
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            bod=Button(optiom,text="MEDICINE",cursor='plus',command=chdob);bod.pack()
                                                            def chadd():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER DISABILITY");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  address = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'disb'] = address
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            addr=Button(optiom,text="DISABILITY",cursor='plus',command=chadd);addr.pack()
                                                            def chddes():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER ALLERGIES");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  desig = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                     ord(id[2])-65, 'alrgs'] = desig
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            desin=Button(optiom,text="ALLERGIES",cursor='plus',command=chddes);desin.pack()
                                                            def doko():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               df = hira.read_csv("pri_rec.csv")
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo = Label(cnan,text="ENTER STATUS OF VACCINATION");nameo.pack()
                                                               nam = Entry(cnan);nam.pack()
                                                               def ooof(cin):
                                                                  hiredate = cin.get()
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'covid'] = hiredate
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:ooof(nam));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justforthat(optiom,cnan,rer));peo.pack()
                                                            dojo= Button(optiom,text="COVID VACCINATION",cursor='plus',command=doko);dojo.pack()
                                                            def aawa():
                                                               optiom.pack_forget();optiom.place_forget()
                                                               rer.pack_forget();rer.place_forget()
                                                               cnan = Frame(window);cnan.pack()
                                                               phe = Label(cnan,text="ENTER NEW DATA");phe.pack()
                                                               nameo1 = Label(cnan,text="ENTER MARK OF IDENTIFICATION");nameo1.pack()
                                                               nam1 = Entry(cnan);nam1.pack()

                                                               nameo2 = Label(cnan,text="ENTER BLOOD GROUP");nameo2.pack()
                                                               nam2 = Entry(cnan);nam2.pack()

                                                               nameo3 = Label(cnan,text="ENTER ANY REGULAR MEDICINES(IF ANY)");nameo3.pack()
                                                               nam3 = Entry(cnan);nam3.pack()

                                                               nameo4 = Label(cnan,text="ENTER DISABILITIES");nameo4.pack()
                                                               nam4 = Entry(cnan);nam4.pack()

                                                               nameo5 = Label(cnan,text="ENTER ALLERGIES");nameo5.pack()
                                                               nam5 = Entry(cnan);nam5.pack()

                                                               nameo6 = Label(cnan,text="ENTER COVID VACCINATION(yes/no/partial)");nameo6.pack()
                                                               nam6 = Entry(cnan);nam6.pack()

                                                               def chjo(a1,a2,a3,a4,a5,a6):
                                                                  name=a1.get();gen=a2.get();age=a3.get();wei=a4.get();hei=a5.get();hc=a6.get()
                                                                  df = hira.read_csv("pri_rec.csv")

                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'markofid'] = name
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'bloodgrp'] = gen
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'med'] = age
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'disb'] = wei
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26) +
                                                                         ord(id[2])-65, 'alrgs'] = hei
                                                                  df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'covid'] = hc
                                                                  
                                                                  df.to_csv("pri_rec.csv", index=False)
                                                                  messagebox.showinfo("SUCCESS","CHANGE MADE")
                                                                  cnan.place_forget();cnan.pack_forget();rer.pack_forget();rer.place_forget();staffad.pack()
                                                               ooo = Button(cnan,text="MAKE CHANGE",cursor='plus',command=lambda:chjo(nam1,nam2,nam3,nam4,nam5,nam6));ooo.pack()
                                                               peo = Button(cnan,text="GO BACK",command=lambda:justthisonce(rer,optiom,cnan));peo.pack()
                                                            wrec = Button(optiom,text="WHOLE RECORD",cursor='plus',command=aawa);wrec.pack()
                                                            Back=Button(optiom,text="GO BACK TO MAIN MENU",cursor='plus',command=lambda:mainmenui(optiom,rer,stafed));Back.pack()

                                                      if flag == 0:
                                                         messagebox.showerror("ERROR","NO RECORD MATCHING TO THIS ID EXISTS.")              
                                       dal = Button(stafed,text="GET DATA",cursor='plus',command=lambda:okies(le));dal.pack()
                                    dabaiye = Button(stafed,text="PRESS TO VIEW THE LIST OF PRISONER IDS",cursor='plus',command=don);dabaiye.pack()                  
                                    
                                    back=Button(stafed,text="EXIT",cursor='plus',command=lambda:mainmenu(stafed,staffad));back.pack()

                                 edit = Button(staffad,text="EDIT RECORD",cursor='plus',command=editt);edit.pack()
                                 def viewst():
                                    staffad.place_forget();staffad.pack_forget()
                                    viewpanel=Frame(window);viewpanel.pack()
                                    wlo=Label(viewpanel,text="WELCOME TO THE VIEWING MENU");wlo.pack()
                                    def krobhai():
                                       kro.pack_forget()
                                       file = open('pri_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                          if row[0] == "id":
                                             pass
                                          
                                          elif row[1]=='0':
                                             continue
                                          else:
                                           recor = Label(viewpanel,text=f"SHOWING RECORD AGAINST ID {row[0]}\nNAME: {row[1]}\tAGE: {row[3]}\tWEIGHT: {row[4]}\nHEIGHT: {row[5]}\tMARK OF IDENTIFICATION: {row[18]}\tMEDICINE ON REGULAR BASIS: {row[19]}\tBLOOD GROUP: {row[20]}\nANY DISABILITY: {row[21]}\tANY ALLERGIES: {row[22]}\tCOVID-19 VACCINATION(yes/no): {row[23]}");recor.pack()
                                    

                                    kro = Button(viewpanel,text="PRESS TO VIEW ALL THE PRISONER RECORDS.",cursor='plus',command=krobhai);kro.pack()
                                    back=Button(viewpanel,text="PRESS TO EXIT THE VIEWING MENU.",cursor='plus',command=lambda:mainmenu(viewpanel,staffad));back.pack()                           
                                 view= Button(staffad,text="VIEW RECORD",cursor='plus',command=viewst);view.pack()
                                 def deleteit():
                                    staffad.pack_forget();staffad.place_forget()
                                    delmen = Frame(window);delmen.pack()
                                    oks = Label(delmen,text="HERE IS THE DELETING MENU");oks.pack()
                                    def printo():
                                       file = open('pri_rec.csv', mode='r')
                                       reader = csv.reader(file)
                                       for row in reader:
                                       # skipping empty rows causing errors
                                              if row == []:
                                                     continue
                                              # print(row)
                                              if row[0] == "id":
                                                     pass
                                              elif row[1] == "0":
                                                     pass
                                              else:
                                                     stfi=Label(delmen,text=f"PRISONER'S ID IS: {row[0]}\nNAME: {row[1]}\nCRIME: {row[8]}") ;stfi.pack() 
                                       joi = Label(delmen,text="ENTER THE PRISONER'S ID YOU WANT TO DELETE:");joi.pack()
                                       joidd = Entry(delmen);joidd.pack() 
                                       def dodo(ids):
                                          id = ids.get()
                                          if len(id) < 3:
                                             messagebox.showerror("ERROR","Please enter complete ID.")
                                          else:
                                             file = open('pri_rec.csv', mode='r')
                                             reader = csv.reader(file)
                                             flag = 0
                                             for row in reader:
                                              #skipping empty rows
                                                if row==[]:
                                                     continue
                                                
                                                if id in row:
                                                   delmen.pack_forget();delmen.place_forget()
                                                   deko = Frame(window);deko.pack()
                                                   dikhao = Label(deko,text="SHOWING THE WHOLE RECORD OF PRISONER.");dikhao.pack()
                                                   dek = Label(deko,text="HERE IS THE COMPLETE RECORD OF PRISONER.");dek.pack()
                                                   flag += 1
                                                   joidh = Label(deko,text=f"SHOWING RECORD AGAINST ID {row[0]}");joidh.pack()
                                                   nameh = Label(deko,text=f"NAME: {row[1]}\tAGE: {row[3]}\tWEIGHT: {row[4]}");nameh.pack()
                                                   desi =Label(deko,text=f"HEIGHT: {row[5]}\tMARK OF IDENTIFICATION: {row[18]}\tMEDICINE ON REGULAR BASIS: {row[19]}");desi.pack()
                                                   relh = Label(deko,text=f"BLOOD GROUP: {row[20]}\tANY DISABILITY: {row[21]}");relh.pack()
                                                   pnum =Label(deko,text=f"ANY ALLERGIES: {row[22]}\tCOVID-19 VACCINATION(yes/no): {row[23]}");pnum.pack()
                                                   quwe = Label(deko,text="ARE YOU SURE YOU WANT TO DELETE THE RECORD?");quwe.pack()
                                                   def dhaade():
                                                      df = hira.read_csv("pri_rec.csv")
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'markofid'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'bloodgrp'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'med'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'disb'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'alrgs'] = '0'
                                                      df.loc[(int(id[0])*260)+(int(id[1])*26)+ord(id[2])-65, 'covid'] = '0'
                                                      df.to_csv("pri_rec.csv", index=False)
                                                      messagebox.showinfo("SUCCESS","ID deleted successfully")
                                                      deko.pack_forget();deko.place_forget()
                                                      delmen.pack()
                                                   yay = Button(deko,text="YES",cursor='plus',command=dhaade);yay.pack()
                                                   back = Button(deko,text="NO",command=lambda:mainmenu(deko,delmen));back.pack()
                                             if flag == 0:
                                                messagebox.showerror("ERROR","NO RECORD MATCHING TO THIS ID EXISTS.")

                                       con = Button(delmen,text="VIEW",cursor='plus',command=lambda:dodo(joidd));con.pack()
                                       back=Button(delmen,text="EXIT",cursor='plus',command=lambda:mainmenu(delmen,staffad));back.pack()

                                    prin = Button(delmen,text="PRESS TO VIEW THE LIST OF PRISONER IDS.",cursor='plus',command=printo);prin.pack()
                                                                   
                                 delete = Button(staffad,text="DELETE RECORD",cursor='plus',command=deleteit);delete.pack()
                                 back=Button(staffad,text="EXIT",cursor='plus',command=lambda:mainmenu(staffad,admin_panel));back.pack()
                              medrec = Button(admin_panel,text="MEDICAL RECORD",cursor='plus',command=medpan);medrec.pack()
                              def start():
                                 admin_panel.place_forget()
                                 stfr=Frame(window);stfr.pack()
                                 
                                 def attpan():  
                                    stfr.place_forget();stfr.pack_forget()
                                    frameat = Frame(window);frameat.pack()
                                    dayl=Label(frameat,text='Enter the date of attendence:');dayl.pack()
                                    da = Entry(frameat);da.pack()
                                 
                                    with open('pri_rec.csv', mode='r') as file:
                                       reader = csv.reader(file)
                                       rows = list(reader)
                                    checkboxes = [];attendance = []
                                    for row in rows:
                                       if row[1] != '0' and row[0] != 'id':
                                          l = tk.IntVar()
                                          checkbox = Checkbutton(frameat, text=f"{row[0]}  {row[1]}", variable=l);checkbox.pack()
                                          checkboxes.append((checkbox, l))
                                    def update_attendance(x):
                                       attendance = []
                                       for checkbox, var in checkboxes:
                                          v = var.get()
                                          if v ==1:
                                             attendance.append('present')
                                          else:
                                             attendance.append('absent')
                                       day = x.get()
                                       with open('pri_att.csv', 'r') as file:
                                          reader = csv.reader(file)
                                          header = next(reader)
                                          header.append(f'{day}')

                                          data = []
                                          for row in reader:
                                                row.append('')
                                                data.append(row)
                                       with open('pri_att.csv', 'w') as file:
                                          writer = csv.writer(file,lineterminator='\n')
                                          writer.writerow(header)
                                          writer.writerows(data)
                                       myvar=day
                                       df=hira.read_csv("pri_att.csv")
                                       col_list=df.ID.values.tolist() 
                                       i=0
                                       for id in col_list:
                                          df.loc[(int(id[0])*260)+(int(id[1])*26) +ord(id[2])-65, myvar] = str(attendance[i])
                                          i+=1
                                       df.to_csv("pri_att.csv",index=False)
                                       messagebox.showinfo("SUCCESS","ATTENDANCE ADDED")
                                       frameat.pack_forget();frameat.place_forget()
                                       admin_panel.pack()
                                    but = Button(frameat, text="continue", command=lambda:update_attendance(da));but.pack()
                                    bac=Button(frameat,text="Go Back",command=lambda:mainmenu(frameat,stfr));bac.pack()
                                 add =Button(stfr,text="ADD ATTENDANCE",cursor='plus',command=attpan);add.pack()
                                 def viewit():
                                    stfr.place_forget();stfr.pack_forget()
                                    viewpanel=Frame(window);viewpanel.pack()
                                    wlo=Label(viewpanel,text="WELCOME TO THE VIEWING MENU");wlo.pack()
                                    def krobhai():
                                       kro.pack_forget();kro.place_forget()
                                       '''file = open('pri_att.csv',mode='r')
                                       reader = csv.reader(file)

                                       for row in reader:                                       
                                          entries=[]
                                          for entry in row:
                                            entries.append(entry)
                                          break
                                       for row in reader:
                                          i=0
                                          for att in row:
                                             if row[0]=='ID':
                                                continue
                                             else:'''
                                       df=hira.read_csv("pri_att.csv")
                                       #print(df)
                                       f = Label(viewpanel,text=f"{df}");f.pack()
                                                #i+=1
                                    kro = Button(viewpanel,text="PRESS TO VIEW ATTENDANCE OF ALL THE PRISONER RECORDS.",cursor='plus',command=krobhai);kro.pack()
                                    back=Button(viewpanel,text="PRESS TO EXIT THE VIEWING MENU.",cursor='plus',command=lambda:mainmenu(viewpanel,stfr));back.pack()                           
                                         
                                 view =Button(stfr,text="VIEW ATTENDANCE",cursor='plus',command=viewit);view.pack()
                                 bac=Button(stfr,text="Go Back",command=lambda:mainmenu(stfr,admin_panel));bac.pack()
                              att = Button(admin_panel,text="ATTENDANCE",cursor='plus',command=start);att.pack()
                              signou = Button(admin_panel,text="SIGNOUT",cursor='plus',command=lambda:signout(admin_panel,windowframe));signou.pack()
                           else:
                              messagebox.showerror("ERROR","Wrong password")

                        except:
                           messagebox.showerror("ERROR","Incorrect passwords or username")
                           
                     else:
                        messagebox.showerror("ERROR","Username doesn't exist")
                        
                  except:
                     messagebox.showerror("ERROR","Password or username doesn't exist")

            else:
               messagebox.showerror("ERROR","Please attempt login again")
         enter = Button(newlogin,text = 'Continue',command=lambda: gainAccess(username,passwi));enter.pack()
         back = Button(newlogin,text='EXIT',cursor='plus',command=lambda:mainmenu(newlogin,newframe1));back.pack()
      Login = Button(newframe1,text="Login",cursor='plus',command=login);Login.pack()
      back = Button(newframe1,text='EXIT',cursor='plus',command=lambda:mainmenu(newframe1,windowframe));back.pack()

window = Tk()
window.resizable(False, False)
window.title("Prison Management");window.state('zoomed')
windowframe=Frame(window)
ico =Image.open('ICON.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)
welfr = Frame(window);welfr.place(x=450,y=175)
welcome=Label(welfr,text="\n\nNUST Central Jail" ,font=("Broadway",50));welcome.pack();
welfr.after(3000,lambda: welfr.destroy())
admin = Button(windowframe,text='CONTINUE AS ADMIN',cursor='plus',command=clicked_admin);admin.pack()
staff = Button(windowframe,text='CONTINUE AS STAFF',cursor='plus',command=clicked_staff);staff.pack()
close = Button(windowframe,text='EXIT',cursor='plus',command=lambda:window.destroy());close.pack()
windowframe.after(3000,lambda: windowframe.place(x=700,y=350))
window.mainloop()