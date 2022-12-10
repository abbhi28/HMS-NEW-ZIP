import mysql.connector
import time
from datetime import datetime
from datetime import date
from time import strftime
import qrcode
from PIL import Image
import os
from tkinter import *
from tkinter import messagebox


global conn,cursor
conn = mysql.connector.connect(
  host='127.0.0.1',
  database='HMS',
  user='root',
  password='pass123')
cursor = conn.cursor()

def numOfDays(date1,date2):
    return (date2-date1).days


def Doctor(Doc_ID):
    cursor.execute("select Doctor_name from Doctors where ID='{}'".format(Doc_ID))
    name = cursor.fetchall()
    name= name[0]
    name= name[0]
    def Back():
            Doctor(Doc_ID)
    def exmpatient(): 
        def search():
            ID = entry3.get()
            cursor.execute("select Patient_ID from patients where Patient_ID='{}'".format(ID))
            cursor.fetchall()
            rows = cursor.rowcount
            if rows!=1:
                print("Patient Not Found")
                exmpatient()
            else:
                cursor.execute("select Patient_Name,Patient_Age from patients where Patient_ID='{}'".format(ID))
                Ans = cursor.fetchall()
                Ans =(Ans[0])
                cursor.execute("select Weight,Height,Blood_Pressure,Blood_Sugar from VITALS where Patient_ID='{}'".format(ID))
                vital=cursor.fetchall()
                print(vital)
                vital = vital[0]
                canvas.create_text(#name
                    203.0, 302.0,
                    text = Ans[0],
                    fill = "#000000",
                    font = ("None", int(18.0)))
                canvas.create_text(#age
                    194.0, 330.0,
                    text = Ans[1],
                    fill = "#000000",
                    font = ("None", int(18.0)))
                canvas.create_text(#Height
                    520.0, 302.0,
                    text = vital[1],
                    fill = "#000000",
                    font = ("None", int(18.0)))
                canvas.create_text(#weight
                    520.0, 330.0,
                    text = vital[0],
                    fill = "#000000",
                    font = ("None", int(18.0)))
                canvas.create_text(#BP
                    772.0, 302.0,
                    text = vital[2],
                    fill = "#000000",
                    font = ("None", int(18.0)))  
                canvas.create_text(#BS
                    785.0, 330.0,
                    text = vital[3],
                    fill = "#000000",
                    font = ("None", int(18.0)))                      
        def Submit():
            ID = entry3.get()
            prescription = entry1.get("1.0",'end-1c')
            cursor.execute("update Patient_pres set prescription='{}' where Patient_ID ='{}'".format(prescription,ID))
            conn.commit()
            a = entry2.get()
            a = a.split()#tests table not added
            test_name = []
            test_price = []
            for i in a:
                cursor.execute("select Test,price from test where sno='{}'".format(i))
                dic = cursor.fetchall()
                dic = dic[0]
                test_name.append(dic[0])
                test_price.append(dic[1])
            cursor.execute("select test_Chrg from Bill where Patient_ID='{}'".format(ID))
            price = cursor.fetchall()
            print(price)
            price=price[0]  
            price=price[0]
            print(price)
            for i in test_price:
                price +=i
            print(test_name)
            str =""
            for i in test_name:
                str = str+"--"+i
            cursor.execute("update Bill set test_name='{}',test_Chrg='{}' where Patient_ID ='{}'".format(str,price,ID))
            conn.commit()
            rep = entry0.get("1.0",'end-1c')
            cursor.execute("update Patient_pres set Final_report='{}' where Patient_ID ='{}'".format(rep,ID))
            conn.commit()
            time.sleep(0.5)
            Doctor()    

        canvas = Canvas(
            window,
            bg = "#ffffff",
            height = 825,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"newbg.png")
        background = canvas.create_image(
            720.0, 376.0,
            image=background_img)

        canvas.create_text(
            1294.0, 75.0,
            text = "Dr "+name+"\n    Doctor",
            fill = "#ffffff",
            font = ("None", int(16.0)))

        entry0_img = PhotoImage(file = f"BigBox1.png")
        entry0_bg = canvas.create_image(
            748.0, 576.0,
            image = entry0_img)

        entry0 = Text(window,width=284,height=384,#report
            bd = 0,
            bg = "#ffffff",
            font = ("None", int(16.0)),
            wrap='word')

        entry0.place(
            x = 556, y = 434,
            width = 384,
            height = 282)

        entry1_img = PhotoImage(file = f"BigBox2.png")
        entry1_bg = canvas.create_image(
            297.0, 580.0,
            image = entry1_img)

        entry1 = Text(window,width=284,height=384,#preciption
            bd = 0,
            bg = "#ffffff",
            font = ("None", int(16.0)),
            highlightthickness = 0)

        entry1.place(
            x = 105, y = 438,
            width = 384,
            height = 282)

        entry2_img = PhotoImage(file = f"tb3.png")
        entry2_bg = canvas.create_image(
            1191.0, 725.5,
            image = entry2_img)

        entry2 = Entry(#tests
            bd = 0,
            bg = "#ffffff",
            font = ("None", int(16.0)),
            highlightthickness = 0)

        entry2.place(
            x = 996, y = 706,
            width = 390,
            height = 37)

        entry3_img = PhotoImage(file = f"tb4.png")
        entry3_bg = canvas.create_image(
            393.5, 191.0,
            image = entry3_img)

        entry3 = Entry(#patientID
            bd = 0,
            bg = "#ffffff",
            font = ("None", int(16.0)),
            highlightthickness = 0)

        entry3.place(
            x = 230, y = 170,
            width = 327,
            height = 40)

        img0 = PhotoImage(file = f"submit.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = Submit,
            relief = "flat")

        b0.place(
            x = 587, y = 752,
            width = 266,
            height = 59)
        img1 = PhotoImage(file = f"search.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = search,
            relief = "flat")

        b1.place(
            x = 588, y = 170,
            width = 119,
            height = 44)
        img4 = PhotoImage(file = f"Back.png")
        b4 = Button(
            image = img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = Back,
            relief = "flat")
        b4.place(
            x = 13, y = 172,
            width = 36,
            height = 36)        

        window.resizable(False, False)
        window.mainloop()
    def appo():
        now_date =datetime.now().strftime('%Y-%m-%d')
        print(now_date)
        cursor.execute("select * from appointment where Doctor='{}' and App_date='{}'".format(name,now_date))
        app = cursor.fetchall()    
        print(app)
        Patient_ID=[]
        Patient_Name=[]
        Slot=[]
        Date=[]
        for i in app:
            print(i)
            Patient_ID.append(i[0])
            Patient_Name.append(i[1])
            Slot.append(i[3])
            Date.append(i[4])
        canvas = Canvas(
                window,
                bg = "#ffffff",
                height = 825,
                width = 1440,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"apg.png")
        background = canvas.create_image(
                720.0, 396.0,
                image=background_img)

        canvas.create_text(
            1294.0, 75.0,
            text = "Dr "+name+"\n    Doctor",
            fill = "#ffffff",
            font = ("None", int(16.0)))

        img0 = PhotoImage(file = f"Back.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = Back,
            relief = "flat")

        b0.place(
            x = 13, y = 199,
            width = 36,
            height = 36)
        xcomp = 133
        ycomp = 275
        z = 0
        for i in Patient_ID:
            canvas.create_text(
            xcomp, ycomp,
            text = Patient_ID[z],
            fill = "#000000",
            font = ("None", int(18.0)))
            canvas.create_text(
            xcomp+100, ycomp,
            text = Patient_Name[z],
            fill = "#000000",
            font = ("None", int(18.0)))
            canvas.create_text(
            xcomp+630, ycomp,
            text = Date[z],
            fill = "#000000",
            font = ("None", int(18.0)))
            canvas.create_text(
            xcomp+915, ycomp,
            text = Slot[z],
            fill = "#000000",
            font = ("None", int(18.0)))
            canvas.create_text(
            xcomp+1125, ycomp,
            text = "30 Mins",
            fill = "#000000",
            font = ("None", int(18.0)))
            ycomp+=40
            z+=1
            

        window.resizable(False, False)
        window.mainloop()
        
    def lgot():
        login()
    def clnnurse(): 
        messagebox.showinfo('Notification','Nurse has been called \nwill arrive shortly')
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 825,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    img0 = PhotoImage(file = f"app.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = appo,
        relief = "flat")

    b0.place(
        x = 280, y = 244,
        width = 100,
        height = 144)

    img1 = PhotoImage(file = f"exmpat.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = exmpatient,
        relief = "flat")

    b1.place(
        x = 534, y = 244,
        width = 114,
        height = 131)

    img2 = PhotoImage(file = f"CallNurse.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = clnnurse,
        relief = "flat")

    b2.place(
        x = 800, y = 242,
        width = 100,
        height = 135)

    img3 = PhotoImage(file = f"Logout.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = lgot,
        relief = "flat")

    b3.place(
        x = 1060, y = 244,
        width = 100,
        height = 133)

    background_img = PhotoImage(file = f"docbg.png")
    background = canvas.create_image(
        720.0, 399.0,
        image=background_img)

    canvas.create_text(
        405.5, 67.5,
        text = "        Welcome Dr "+name+",",
        fill = "#ffffff",
        font = ("None", int(50.0)))
    
    canvas.create_text(
            1045.0, 735.0,
            text = "No Emergency Calls",
            fill = "#000000",
            font = ("None", int(12.0)))    

    canvas.create_text(
        1294.0, 70.0,
        text = "Dr "+name+"\n   Doctor",
        fill = "#ffffff",
        font = ("None", int(16.0)))


    window.resizable(False, False)
    window.mainloop()    


def Nurse(Nur_ID,abc=0,ID=0):
    cursor.execute("select Name from Employee where ID='{}'".format(Nur_ID))
    name = cursor.fetchall()
    name= name[0]
    name= name[0]
    def Search():
        ID = Tb0.get()    
        cursor.execute("select Patient_ID from patients where Patient_ID='{}'".format(ID))
        cursor.fetchall()
        rows = cursor.rowcount
        if rows!=1:
            Nurse(Nur_ID,1,ID)
        else:
            Nurse(Nur_ID,2,ID)

    def Submit():
        ID = Tb0.get()
        weight = Tb1.get()
        height = Tb2.get()
        BP = Tb3.get()
        sugar = Tb4.get()
        now_date =datetime.now().strftime('%Y-%m-%d')
        now_date=str(now_date)
        now_time =datetime.now().strftime('%H:%M:%S')
        now_time=str(now_time)
        cursor.execute("update VITALS set Weight='{}',Height='{}',Blood_Pressure='{}',Blood_Sugar='{}',Date_Of_Update='{}',Time_Of_Update='{}' where Patient_ID='{}';".format(weight,height,BP,sugar,now_date,now_time,ID))
        conn.commit()
        messagebox.showinfo('Done','Record Has Been Submitted...')
        time.sleep(5)
        Nurse(Nur_ID)
    def callDoc():
        messagebox.showinfo('Message','Doctor Has Been Called')
    def exmpt():
        messagebox.showerror('Error','Already Examining...')                     
    def Logout():
        login() 
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 825,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Nursebg.png")
    background = canvas.create_image(
        720.0, 381.5,
        image=background_img)
    Tb0_img = PhotoImage(file = f"nurtb.png")
    Tb0_bg = canvas.create_image(
        600.0, 315.0,
        image = Tb0_img)
    Tb0 = Entry(
        bd = 0,
        bg = "#ffffff",
        font = ("None", int(18.0)),
        highlightthickness = 0)
            
    Tb0.place(
        x = 460.0, y =298.0,
        width = 280,
        height =32)
    Tb1_img = PhotoImage(file = f"nurtb.png")
    Tb1_bg = canvas.create_image(
        600.0, 476.0,
        image = Tb1_img)
    Tb1 = Entry(
        bd = 0,
        bg = "#ffffff",
        font = ("None", int(18.0)),
        highlightthickness = 0)
            
    Tb1.place(
        x = 460.0, y =460.0,
        width = 280,
        height =32) 
    canvas.create_rectangle(300,460,440,500,fill='#ffffff',outline='white')   
    Tb2_img = PhotoImage(file = f"nurtb.png")
    canvas.create_text(
        361.0, 475.0,
        text = "Weight : ",
        fill = "#000000",
        font = ("None", int(20.0)))
    Tb2_bg = canvas.create_image(
        600.0, 559.0,
        image = Tb2_img)       
    Tb2 = Entry(
        bd = 0,
        bg = "#ffffff",
        font = ("None", int(18.0)),
        highlightthickness = 0)
            
    Tb2.place(
        x = 460.0, y =543.0,
        width = 280,
        height =32)   
    Tb3_img = PhotoImage(file = f"nurtb.png")
    Tb3_bg = canvas.create_image(
        600.0, 626.0,
        image = Tb3_img)       
    Tb3 = Entry(
        bd = 0,
        bg = "#ffffff",
        font = ("None", int(18.0)),
        highlightthickness = 0)
            
    Tb3.place(
        x = 460.0, y =610.0,
        width = 280,
        height =32)       
    Tb4_img = PhotoImage(file = f"nurtb.png")
    Tb4_bg = canvas.create_image(
        600.0, 702.0,
        image = Tb4_img)       
    Tb4 = Entry(
        bd = 0,
        bg = "#ffffff",
        font = ("None", int(18.0)),
        highlightthickness = 0)
            
    Tb4.place(
        x = 460.0, y =686.0,
        width = 280,
        height =32)   

    entry1 = Text(window,width=284,height=384,
            bd = 0,
            bg = "#ffffff",
            font = ("None", int(16.0)),
            highlightthickness = 0)
    entry1.place(
                x = 1050, y = 295,
                width = 340,
                height = 450)        

    img0 = PhotoImage(file = f"NurSearch.png")           
    b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = Search,
            relief = "flat")

    b0.place(
        x = 780, y = 292.0,
        width = 154,
        height = 43)
    img3 = PhotoImage(file = f"exmpat.png")
    b1 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = exmpt,
        relief = "flat")

    b1.place(
        x = 65, y = 244,
        width = 114,
        height = 131)    
    img4 = PhotoImage(file = f"calldoc.png")
    b2 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = callDoc,
        relief = "flat")

    b2.place(
        x = 65, y = 420,
        width = 114,
        height = 131)       
    img5 = PhotoImage(file = f"Logout2.png")    
    b3 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = Logout,
        relief = "flat")

    b3.place(
        x = 65, y = 590,
        width = 114,
        height = 131)       
    img6 = PhotoImage(file = f"NurSubmit.png")
    b4 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = Submit,
        relief = "flat")

    b4.place(
        x = 780, y = 682,
        width = 154,
        height = 43)    
    canvas.create_text(
        405.5, 67.5,
        text = "Welcome "+name+",",
        fill = "#ffffff",
        font = ("None", int(42.0)))
    if abc ==1:
            canvas.create_text(
            600.0, 370.0,
            text = "Patient ID : "+ID+" Not Found",
            fill = "#000000",
            font = ("None", int(16.0)))
            Tb0.insert('0',ID)
    elif abc ==2:
        cursor.execute("select Patient_Name,Patient_Age from patients where Patient_ID='{}'".format(ID))
        pname=cursor.fetchall()
        Tb0.insert('0',ID)
        pname = pname[0]
        age = str(pname[1])
        canvas.create_text(
            600.0, 370.0,
            text = "Patient ID : "+ID+" \nName : "+pname[0]+"   Age :"+age,
            fill = "#000000",
            font = ("None", int(16.0)))            

    canvas.create_text(
        1294.0, 70.0,
        text = "   "+name+"\n   Nurse",
        fill = "#ffffff",
        font = ("None", int(16.0)))     
    window.resizable(False, False)
    window.mainloop()

def Mess(Mess_ID):
    ID = int(input("Enter Patient ID"))
    print("Mess Portal")
    print("1.Menu")
    print("2.Orders")
    a = int(input("Select an option :"))
    if a ==1:
        print("*"*60)
        print("Menu")
        print("*"*60)
        i = 1
        print("S.no","  Food","  Price")
        cursor.execute("select Sno from mess ")
        cursor.fetchall()
        a = cursor.rowcount
        for i in range(1,a+1):
            cursor.execute("select Food,Price from mess where Sno='{}'".format(i))
            menu = cursor.fetchall()
            menu = menu[0]
            print(i,"    ",menu[0],"   ",menu[1])
        a = input("Select Your Options")
        a = a.split()
        cursor.execute("select Food_Chrg from Bill where Patient_ID='{}'".format(ID))
        FC = cursor.fetchall()
        FC = FC[0]
        FC = FC[0]
        sum = FC
        for i in a:
            cursor.execute("select Price from mess where Sno ='{}'".format(i))
            Price = cursor.fetchall()
            Price = Price[0]
            Price = Price[0]
            sum = sum + Price
            print(sum)
        cursor.execute("update Bill set Food_Chrg='{}' where Patient_ID='{}'".format(sum,ID))
               
    elif a==2:
        print("*"*60)
        print("Orders")
        print("*"*60)


def Pharmacists(Pha_ID):
    print("\n\n\n")
    print("*"*60)
    print("Pharmacists Portal")
    print("*"*60)   
    print("1.Inventory")
    print("2.Patient Prescription")
    print("3.Bill")
    print("4.Expired Med")
    print("5.LOGOUT")
    a = int(input("Select an option :"))
    if a ==1:
        print("1.Check availability")
        print("2.Add stock")
        s = int(input("Select an Option:"))
        if s ==1 :
            print("\n\n\n")
            print("*"*60)
            print("Availability")
            print("*"*60)
            cursor.execute("select S_no from Inventory")
            Sno = cursor.fetchall()
            r = 0
            z = 0
            for i in Sno:
                S = Sno[r]
                S = S[0]
                cursor.execute("Select Medicine_Name,Stock,Exp_date from Inventory where S_No='{}'".format(S))
                Med_output = cursor.fetchall()
                for i in Med_output:
                    Name_Med = Med_output[0]
                    print(Name_Med[0],Name_Med[1],Name_Med[2],sep="     ")
                    z+=1
                r+=1
            time.sleep(5)    
            Pharmacists()
        elif s == 2:
            med_name=str(input("Enter Medicine name with Dosage :"))
            cursor.execute("select Stock from Inventory where Medicine_Name='{}'".format(med_name))
            cursor.fetchall()
            rows = cursor.rowcount
            if rows==0:
                cursor.execute("select S_no from Inventory")
                Sno = cursor.fetchall()
                a = []
                if Sno == a:
                    Sno = 1
                else:
                    Sno = Sno[-1]
                    Sno = Sno[0]
                    Sno = Sno+1    
                print("Medicine not in inventory...Adding medicine")
                med_quantity=int(input("Enter Quantity :")) 
                med_price=int(input("Enter Price(per unit) :"))   
                date_components = input('Enter Expiry date formatted as YYYY-MM-DD: ').split('-')
                year, month, day = [int(item) for item in date_components]
                d = date(year,month,day)
                cursor.execute("insert into Inventory(S_no,Medicine_Name,Exp_date,Price,stock) values('{}','{}','{}','{}','{}')".format(Sno,med_name,d,med_price,med_quantity))            
                conn.commit()
                print("Record submitted")     
                time.sleep(5)
                Pharmacists()
            else:
                print("Adding stock to medicine")
                med_quantity=int(input("Enter Quantity :"))
                cursor.execute("select Stock from Inventory where Medicine_Name='{}'".format(med_name))
                stock = cursor.fetchall()
                stock=stock[0]
                stock=stock[0]
                stock =stock+med_quantity
                date_components = input('Enter Expiry date formatted as YYYY-MM-DD: ').split('-')
                year, month, day = [int(item) for item in date_components]
                d = date(year,month,day)
                cursor.execute("update Inventory set Stock='{}',Exp_date = '{}' where Medicine_Name ='{}' ".format(stock,d,med_name))
                conn.commit()
                print("Record submitted")     
                time.sleep(5)
                Pharmacists()

    elif a==2:
        pid=int(input("Enter Patients ID:"))
        cursor.execute("select prescription from Patient_pres where Patient_ID='{}'".format(pid))
        pres = cursor.fetchall()
        pres = pres[0]
        print(pres[0])
    elif a==3:
        print("Generate Bill")
        med_name="Default"
        while med_name!="":
            med_name=str(input("Enter Medicine Name with Dosage :"))
            med_quant=int(input("Enter quantity :"))
    elif a==4:
        print("Expired med")
    elif a==5:
        login()        


def Bill(Bil_ID):
    print("Bill Generator")
    a = int(input("Enter Patients ID: "))
    def clearbill():
        cursor.execute("update Bill set consulting =0,test_Chrg=0,Pharma_Chrg=0,Food_chrg=0,Room_Chrg=0,Entry_date='0000-00-00',Exit_date='0000-00-00' where Patient_ID='{}'".format(a))
        conn.commit()
        print("Payment successfull......")
        time.sleep(5)
        Bill()
    cursor.execute("select consulting,test_Chrg,Pharma_Chrg,Food_Chrg,Room_Chrg from Bill where Patient_ID='{}' ".format(a))
    out = cursor.fetchall()
    out = out[0]
    Bill_amt = 0
    for i in out:
        Bill_amt +=i
    print("Bill Generated")
    print("Payment Options :")
    print("1.Cash\n2.Debit/Credit card\n3.UPI")
    op=int(input("Select an option "))
    if op == 1:
        print(Bill_amt,"Rs is to be paid")
        r = int(input("Amount Given :"))
        print("Amount to be returned is",r-Bill_amt)
        print("Transaction Complete")
        cursor.execute("Insert into transactions(Patient_ID, Bill_amt, Payment_method) values('{}','{}','{}')".format(a,Bill_amt,"CASH"))
        conn.commit()
        clearbill()
    elif op==2:
        print("Paying Via Card")
        print(Bill_amt,"Rs is to be paid")
        pay_id=int(input("Enter Payment ID"))
        cursor.execute("Insert into transactions(Patient_ID, Bill_amt,Payment_ID, Payment_method) values('{}','{}','{}','{}')".format(a,Bill_amt,pay_id,"CARD"))
        conn.commit()
        clearbill()
    elif op ==3:
        print("UPI QR CODE")
        qr = "Paying rupee",Bill_amt,"via UPI"
        ans = qrcode.make(qr)
        location="Downloads\qr.jpg"
        ans.save(location,'JPEG',scale = 8)
        filename = location
        img = Image.open(filename)
        img.show()
        pay_id=int(input("Enter Payment ID"))
        cursor.execute("Insert into transactions(Patient_ID, Bill_amt,Payment_ID, Payment_method) values('{}','{}','{}','{}')".format(a,Bill_amt,pay_id,"UPI"))
        conn.commit()        
        clearbill()
        os.remove(location)
        

def appointment():
    print("*"*60)
    print("Booking Appointment")
    print("*"*60)
    a = int(input("Is patient Registered...if yes press 1"))
    if a == 1:
       ID = int(input("Enter Patient ID"))
    else:
        Name=str(input("Enter Name of Patient"))
        print("Please Register Patient Before Visiting Doctor....")
        ID = 1
    date_components = input('Enter date of appointment formatted as YYYY-MM-DD: ').split('-')
    year, month, day = [int(item) for item in date_components]
    d = date(year,month,day)
    time.sleep(2) 
    print("Sno  Specialist")   
    print("1.   General")
    print("2.   ENT")
    print("3.   Cardiologist")
    print("4.   Gynocologist")
    print("5.   Dentist")
    print("6.   Neurologists")
    print("7.   PhysioTheraphist")
    print("8.   Pediatricians")
    print("9.   Dermatologists")
    print("10.  Hematologists")
    print("11.  Physiatrists")
    print("12.  Pulmonologists")

    Type =int(input("Enter Specialist Type :"))
    if Type == 1:
        cursor.execute("select Sno,Doctor_Name from Doctors where Specialist='General'")
        Doc = cursor.fetchall()
    elif Type == 2:
        cursor.execute("select Sno,Doctor_Name from Doctors where Specialist='ENT'")
        Doc = cursor.fetchall()
    elif Type == 3:
        cursor.execute("select Sno,Doctor_Name from Doctors where Specialist='Cardiologist'")
        Doc = cursor.fetchall()
    elif Type == 4:
        cursor.execute("select Sno,Doctor_Name from Doctors where Specialist='Gynocologist'")
        Doc = cursor.fetchall()
    elif Type == 5:
        cursor.execute("select Sno,Doctor_Name from Doctors where Specialist='Dentist'")
        Doc = cursor.fetchall()
    elif Type == 6:
        cursor.execute("select Sno,Doctor_Name from Doctors where Specialist='Neurologists'")
        Doc = cursor.fetchall()
    elif Type == 7:
        cursor.execute("select Sno,Doctor_Name from Doctors where Specialist='Physiotheraphist'")
        Doc = cursor.fetchall()
    elif Type == 8:
        cursor.execute("select Sno,Doctor_Name from Doctors where Specialist='Pediatricians'")
        Doc = cursor.fetchall()
    elif Type == 9:
        cursor.execute("select Sno,Doctor_Name from Doctors where Specialist='Dermatologists'")
        Doc = cursor.fetchall()
    elif Type == 10:
        cursor.execute("select Sno,Doctor_Name from Doctors where Specialist='Hematologists'")
        Doc = cursor.fetchall()
    elif Type == 11:
        cursor.execute("select Sno,Doctor_Name from Doctors where Specialist='Physiatrists'")
        Doc = cursor.fetchall()
    elif Type == 12:
        cursor.execute("select Sno,Doctor_Name from Doctors where Specialist='Pulmonologists'")
        Doc = cursor.fetchall()                        
    else :
         print("No Doc")
    rows = cursor.rowcount
    for i in Doc:
            N = Doc[z]
            print(N[0],"   ",N[1])       #([(1,ABC),(2,DEF)])
            z = z+1
    if rows ==0:
        print("No Doctors Available")     
    else:
        z = 0
        for i in Doc:
            N = Doc[z]
            print(N[0],"   ",N[1])
            z = z+1     
        Doctor = int(input("select Doctor :"))
        cursor.execute("select Doctor_name from Doctors where Sno='{}'".format(Doctor))
        Doctor=cursor.fetchall()
        Doctor = Doctor[0]
        Doctor = Doctor[0]
        print("Sno.","  Time Slots")
        Bookd_Slot=[]
        Full_Slot=['9:30','10:00','10:30','11:00','11:30','12:00','2:00','2:30','3:00','3:30','4:00','4:30','5:00','5:30','6:00','6:30','7:00','7:30','8:00','8:30','9:00']
            #should add date element
        cursor.execute("select Time_slot from appointment where Doctor='{}' and App_date='{}'".format(Doctor,d))
        slots = cursor.fetchall()
        for i in slots:
            i = i[0]
            Bookd_Slot.append(i)
        for i in Bookd_Slot[:]:
            if i in Full_Slot:
                Full_Slot.remove(i)
        Avail_Slot=Full_Slot
        Sd = 1
        for i in Avail_Slot:
            if Sd <=9:
                print("",Sd,"     ",i)
            else:
                print("",Sd,"    ",i)    
            Sd+=1
        sel = int(input("Select Slot :"))
        sel = Avail_Slot[sel-1]
        state = ("You Have selected Slot",sel,"for Doctor",Doctor,"press 1 to confirm")
        confirm = int(input(state))
        if confirm ==1:
            cursor.execute("insert into appointment(Patient_ID,Patient_Name,Doctor,Time_slot,App_date)values('{}','{}','{}','{}','{}')".format(ID,Name,Doctor,sel,d))
            conn.commit()
            print("Booking Successfull.......")
            time.sleep(2)
            Rec()
        else:
            print("Try Again")
            appointment() 


def Rec(Rec_ID):
    print("\n\n\n")
    print("*"*60)
    print("Reception Portal")
    print("*"*60)
    print("1.Book Appointment")
    print("2.Book Room")
    print("3.Register Patient")
    print("4.Clinical Management")
    print("5.Emergency")
    print("6.Ambulance")
    print("7.In-Patient Management")
    print("8.Discharge")
    print("9.LOGOUT")
    #a =int(input("Select a option :"))
    def app():
        appointment()
    def RM():
            print("*"*60)
            ID = int(input("Enter Patient ID: "))
            now_date =datetime.now().strftime('%Y-%m-%d')
            now_date=str(now_date)
            cursor.execute("select Patient_ID from patients where Patient_ID='{}'".format(ID))
            cursor.fetchall()
            rows = cursor.rowcount
            if rows!=1:
                print("Patient Not Found")
                RM()
            else:
                print("1.General NON AC single rooms           Rs.2500")
                print("2.General AC single rooms               Rs.5000")
                print("3.Shared Rooms ")
                a = int(input("Select a room Type "))
                if a==1:
                    cursor.execute("select Room_Number from rooms where Avail = '{}' and price = '{}'".format("EMPTY","2500"))
                    cursor.fetchall()
                    rows = cursor.rowcount
                    print("The Number of Rooms Available",rows)
                    if rows==0:
                        print("Rooms unavailable At the moment....Try other rooms....")
                        time.sleep(2)
                            
                    else:
                        cursor.execute("select Room_Number from rooms where Avail = '{}' and price = '{}'".format("EMPTY","2500"))
                        rooms_avail = cursor.fetchall()
                        rooms_avail = (rooms_avail[0])
                        room_select= rooms_avail[0]
                        a = int(input("Press 1 to confirm room Booking"))
                        if a ==1:
                            cursor.execute("update rooms set Usage_ID='{}',Avail='{}',Entry_date='{}' where Room_Number='{}';".format(ID,"FULL",now_date,room_select))
                            conn.commit()
                            print("Room Number",room_select,"Has Been Booked Successfully")  
                            time.sleep(5)             
                        else:
                            print("Booking cancelled")
                            RM()
                elif a==2:
                    cursor.execute("select Room_Number from rooms where Avail = '{}' and price = '{}'".format("EMPTY","5000"))
                    cursor.fetchall()
                    rows = cursor.rowcount
                    print("The Number of Rooms Available",rows)
                    if rows==0:
                        print("Rooms unavailable At the moment....Try other rooms....")
                        time.sleep(2)
                            
                    else:
                        cursor.execute("select Room_Number from rooms where Avail = '{}' and price = '{}'".format("EMPTY","5000"))
                        rooms_avail = cursor.fetchall()
                        rooms_avail = (rooms_avail[0])
                        room_select= rooms_avail[0]
                        a = int(input("Press 1 to confirm room Booking"))
                        if a ==1:
                            cursor.execute("update rooms set Usage_ID='{}',Avail='{}',Entry_date='{}' where Room_Number='{}';".format(ID,"FULL",now_date,room_select))
                            conn.commit()
                            print("Room Number",room_select,"Has Been Booked Successfully")
                            time.sleep(5)               
                        else:
                            print("Booking cancelled")
                            RM()            
                elif a==3:
                    cursor.execute("select Bed_Number from shared where Usage_ID = '{}'".format("0000"))
                    cursor.fetchall()
                    rows = cursor.rowcount
                    print("The Number of Rooms Available",rows)
                    if rows==0:
                        print("Rooms unavailable At the moment....Try other rooms....")
                        time.sleep(2)
                            
                    else:
                        cursor.execute("select Bed_Number from shared where Usage_ID = '{}'".format("0000"))
                        Bed_avail = cursor.fetchall()
                        Bed_avail = (Bed_avail[0])
                        Bed_select= Bed_avail[0]
                        a = int(input("Press 1 to confirm room Booking  "))
                        if a ==1:
                            cursor.execute("update shared set Usage_ID='{}',Entry_date='{}' where Bed_Number='{}';".format(ID,now_date,Bed_select))
                            conn.commit()
                            print("Shared Room Bed Number",Bed_select,"Has Been Booked Successfully")   
                            time.sleep(5)            
                        else:
                            print("Booking cancelled")
                            RM()
      


    def RegPatient():
        print("\n\n\n")
        print("*"*60)
        print("Register Patient")
        print("*"*60)
        cursor.execute("select Patient_ID from patients")
        a = cursor.fetchall()
        a = a[-1]
        a = a[0]
        ID_NEW = a+1
        Name = str(input("Enter Name of Patient:"))
        Age =  str(input("Enter Age Of Patient:"))        
        date_components = input('Enter Date of Birth formatted as YYYY-MM-DD: ').split('-')
        year, month, day = [int(item) for item in date_components]
        DOB = date(year,month,day)
        Address = str(input("Enter Address:"))
        Mobile = int(input("Mobile No.:"))
        Oth_contact = str(input("Other Contact Name :"))
        Contact_no = int(input("Other Contact Number:"))
        cursor.execute("insert into patients(Patient_ID,Patient_Name,Patient_Age,DOB,Address,Mobile,Other_contact_Name,Contact_Number) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(ID_NEW,Name,Age,DOB,Address,Mobile,Oth_contact,Contact_no))
        conn.commit()
        cursor.execute("insert into VITALS(Patient_ID,Patient_Name,Patient_Age,DOB) values('{}','{}','{}','{}')".format(ID_NEW,Name,Age,DOB))
        conn.commit()
        cursor.execute("insert into Bill(Patient_ID,consulting,test_Chrg,Pharma_Chrg,Food_Chrg,Entry_date,Exit_date,Room_Chrg) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(ID_NEW,"0","0","0","0","0000-00-00","0000-00-00","0"))
        conn.commit()
        cursor.execute("insert into Patient_pres(Patient_ID,Patient_Name) values('{}','{}')".format(ID_NEW,Name))
        conn.commit()
        print("Patient Admitted.....successfully")
        time.sleep(5)
    def Clinical():
        print("Clinical Management")
    def Emergency():
        print("Emergency")   
    def Ambulance():
        print("Ambulance")
    def Inpatient():
        print("In-Patient Management")
    def discharge():
        print("\n\n\n")
        print("*"*60)
        print("Discharge")
        print("*"*60)
        ID = int(input("Enter Patients ID for Discharge: "))
        con_qns ="Confirm Patient ID:",ID,"Press 1 to continue"
        confirm = int(input(con_qns))
        if confirm == 1:
            print("1.Room Discharge")
            print("2.Shared room Discharge")
            a = int(input("select an option :"))
            if a ==1:
                cursor.execute("select Entry_date from rooms where Usage_ID='{}'".format(ID))
                ans= cursor.fetchall()
                ans = ans[0]
                ans = ans[0]
                now_date =date.today()
                days = (numOfDays(now_date,ans ))
                cursor.execute("select price from rooms where Usage_ID='{}'".format(ID))
                price=cursor.fetchall()
                price = price[0]
                price = price[0] 
                cost = days*price
                cursor.execute("update Bill set Entry_date='{}',Exit_date='{}',Room_Chrg='{}'where Patient_ID='{}'".format(ans,now_date,cost,ID))
                conn.commit()
                cursor.execute("select Room_Number from rooms where Usage_ID='{}'".format(ID))
                roomno=cursor.fetchall()
                roomno=roomno[0]
                roomno=roomno[0]
                cursor.execute("update rooms set Entry_date='{}',Avail ='{}',Usage_ID='{}'where Room_Number='{}'".format("0000-00-00","EMPTY","0000",roomno))
                conn.commit()
                print("Patient Discharged.....")
                time.sleep(5)
            if a==2:
                cursor.execute("select Entry_date from shared where Usage_ID='{}'".format(ID))
                ans= cursor.fetchall()
                ans=ans[0]
                ans=ans[0]
                now_date =date.today()
                days = (numOfDays(now_date,ans ))
                cost = days*1000
                cursor.execute("update Bill set Entry_date='{}',Exit_date='{}',Room_Chrg='{}'where Patient_ID='{}'".format(ans,now_date,cost,ID))
                conn.commit()
                cursor.execute("select Bed_Number from shared where Usage_ID='{}'".format(ID))
                bedno=cursor.fetchall()
                bedno=bedno[0]
                bedno=bedno[0]
                cursor.execute("update shared set Entry_date='{}',Usage_ID='{}'where Bed_Number='{}'".format("0000-00-00","0000",bedno))
                conn.commit()
                print("Patient Discharged.....")
                time.sleep(5)

            
    def Logout():
        login()    
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 825,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"recbg.png")
    background = canvas.create_image(
        720.0, 72.5,
        image=background_img)

    img0 = PhotoImage(file = f"Bookapn.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = app,
        relief = "flat")

    b0.place(
        x = 178, y = 336,
        width = 100,
        height = 144)

    img1 = PhotoImage(file = f"Bookroom.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = RM,
        relief = "flat")

    b1.place(
        x = 424, y = 336,
        width = 100,
        height = 127)

    img2 = PhotoImage(file = f"regpa.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = RegPatient,
        relief = "flat")

    b2.place(
        x = 665, y = 336,
        width = 110,
        height = 127)

    img3 = PhotoImage(file = f"clima.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = Clinical,
        relief = "flat")

    b3.place(
        x = 916, y = 336,
        width = 100,
        height = 144)

    img4 = PhotoImage(file = f"emg.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = Emergency,
        relief = "flat")

    b4.place(
        x = 1162, y = 336,
        width = 100,
        height = 127)

    img5 = PhotoImage(file = f"amb.png")
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = Ambulance,
        relief = "flat")

    b5.place(
        x = 298, y = 534,
        width = 100,
        height = 127)

    img6 = PhotoImage(file = f"inpa.png")
    b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = Inpatient,
        relief = "flat")

    b6.place(
        x = 544, y = 534,
        width = 100,
        height = 144)

    img7 = PhotoImage(file = f"dis.png")
    b7 = Button(
        image = img7,
        borderwidth = 0,
        highlightthickness = 0,
        command = discharge,
        relief = "flat")

    b7.place(
        x = 790, y = 531,
        width = 100,
        height = 127)

    img8 = PhotoImage(file = f"Logout.png")
    b8 = Button(
        image = img8,
        borderwidth = 0,
        highlightthickness = 0,
        command = Logout,
        relief = "flat")

    b8.place(
        x = 1036, y = 534,
        width = 100,
        height = 127)
    
    date=datetime.now()
    format_date=f"{date:%a, %b %d %Y}"
    label=Label(window,bg="white", text=format_date, font=("Calibri", 25))
    label.place(x= 600.0,y= 240.5)
    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000, time)
 
    lbl = Label(window, font=('calibri', 45, 'bold'),
                background='White',
                foreground='Black')
    lbl.place(x=560,y=170)            
    time()


    window.resizable(False, False)
    window.mainloop()  


def Admin(Adm_ID):
    print("Admin Portal")
    print("1.Faculty")
    print("2.Add/Remove Employee")
    print("3.Employee Appointments")
    print("4.Add/Remove Rooms")
    print("5.Room Availability/Usage")              
    def Faculty():
        print("Faculty")
    def ADR():
        print("Employee Details")    
    def appoint():
        print("Employee Appointments")
    def Room():
        print("ADD/Remove Rooms")
    def RAU():
        print("Room Availability/Usage")   
    canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 825,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"admbg.png")
    background = canvas.create_image(
        720.0, 72.5,
        image=background_img)

    img0 = PhotoImage(file = f"app0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = appoint,
        relief = "flat")

    b0.place(
        x = 295, y = 338,
        width = 100,
        height = 127)

    img1 = PhotoImage(file = f"ARR.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = Room,
        relief = "flat")

    b1.place(
        x = 545, y = 338,
        width = 100,
        height = 144)

    img2 = PhotoImage(file = f"FA.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = Faculty,
        relief = "flat")

    b2.place(
        x = 795, y = 338,
        width = 100,
        height = 127)

    img3 = PhotoImage(file = f"RU.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = RAU,
        relief = "flat")

    b3.place(
        x = 545, y = 534,
        width = 100,
        height = 127)

    img4 = PhotoImage(file = f"ARE.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = ADR,
        relief = "flat")

    b4.place(
        x = 795, y = 530,
        width = 100,
        height = 150)

    date=datetime.now()
    format_date=f"{date:%a, %b %d %Y}"
    label=Label(window,bg="white", text=format_date, font=("Calibri", 25))
    label.place(x= 600.0,y= 240.5)
    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000, time)
 
    lbl = Label(window, font=('calibri', 45, 'bold'),
                background='White',
                foreground='Black')
    lbl.place(x=560,y=170)            
    time()

    img5 = PhotoImage(file = f"Logout.png")
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = login,
        relief = "flat")

    b5.place(
        x = 1045, y = 338,
        width = 100,
        height = 144)

    window.resizable(False, False)
    window.mainloop()            


def login(abc=0):
    def btn_clicked():
        password = Password.get()
        ID = IDN.get()
        cursor.execute("select ID,Pass from login where ID='{}'and Pass='{}'".format(ID,password))
        cursor.fetchall()
        rows = cursor.rowcount
        if rows!=1:
            print("Invalid credentials.....\nTry Again...")
            login(1)
        else:
            cursor.execute("select Job from login where ID='{}'".format(ID))
            Job = cursor.fetchall()
            for i in Job:
                Job = i[0]
            if Job =="Doctor":
                Doctor(ID)
            elif Job == "Nurse":
                Nurse(ID)
            elif Job == "Pharmacists":
                Pharmacists(ID)
            elif Job == "Resceptionist":
                Rec(ID)
            elif Job == "Mess":
                Mess(ID)
            elif Job == "Bill":
                Bill(ID)
            elif Job =="Admin":
                Admin(ID)
            else:
                messagebox.showinfo('ERROR','JOB not found\nPlease Contact Admin')            
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 825,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    canvas.create_text(
        887.0, 284.5,
        text = "USER ID",
        fill = "#000000",
        font = ("None", int(14.0)))

    canvas.create_text(
        896.0, 398.5,
        text = "Password",
        fill = "#000000",
        font = ("None", int(14.0)))

    canvas.create_text(
        1067.0, 141.5,
        text = "LOGIN",
        fill = "#000000",
        font = ("None", int(30.0)))
    
    ID_img = PhotoImage(file = f"img_textBox0.png")
    ID_bg = canvas.create_image(
        1067.0, 333.0,
        image = ID_img)

    IDN = Entry(
        bd = 0,
        bg = "#ffffff",
        font = ("None", int(18.0)),
        highlightthickness = 0)
        

    IDN.place(
        x = 859.0, y = 299,
        width = 416.0,
        height = 68)   


    Password_img = PhotoImage(file = f"img_textBox1.png")
    Password_bg = canvas.create_image(
        1067.0, 446.5,
        image = Password_img)

    Password = Entry(
        bd = 0,
        bg = "#ffffff",
        font = ("None", int(18.0)),
        highlightthickness = 0)

    Password.place(
        x = 859.0, y = 414,
        width = 416.0,
        height = 67)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 946, y = 528,
        width = 241,
        height = 61)

    if abc ==1:
            img1 = PhotoImage(file = f"img1.png")
            b1 = Button(
                image = img1,
                borderwidth = 0,
                highlightthickness = 0,
                command = btn_clicked,
                relief = "flat")

            b1.place(
                x = 960, y = 498,
                width = 214,
                height = 23)

    img2 = PhotoImage(file = f"img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b2.place(
        x =1008, y = 612,
        width = 119,
        height = 22)

    background_img = PhotoImage(file = f"background.png")
    background = canvas.create_image(
        720.0, 416.0,
        image=background_img)
    

    window.resizable(False, False)
    window.mainloop()

window = Tk()
window.geometry("1440x825")
window.configure(bg = "#ffffff")
login(0)