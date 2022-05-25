from tkinter import *
from tkcalendar import *
from datetime import datetime
# from PIL import Image,ImageTk
import tkinter.messagebox as tmsg
import sqlite3 as sql
from tkinter import ttk 

# print(datetime.now())

connector = sql.connect("Hospital_New_Try.db")
cur = connector.cursor()

try:
    cur.execute(""" CREATE TABLE D_In(
                                Doctor_Id varchar, 
                                Time_In varchar,
                                Date_In varchar

                )""")
    cur.execute(""" CREATE TABLE D_Out(
                                Doctor_Id varchar, 
                                Time_Out varchar,
                                Date_Out varchar

                )""")
    cur.execute(""" CREATE TABLE Patient(
                                Name Varchar,
                                Email varchar,
                                Phone_no int Unique,
                                Gender varchar,
                                Blood_g varchar,
                                Password varchar
                                
                )""")
    cur.execute(""" CREATE TABLE Doctor(
                                Name Varchar NOT NULL,
                                Email varchar,
                                Phone_no int NOT NULL,
                                Gender varchar NOT NULL,
                                Blood_g varchar ,
                                Specialization varchar NOT NULL,
                                Id varchar Unique NOT NULL, 
                                Password varchar NOT NULL,
                                Available varchar
                                
                )""")
    cur.execute("""CREATE TABLE Booking(
                                Patient_mobile int,
                                Book_time varchar,
                                Book_date varchar,
                                Doctor_name varchar,
                                Specialization varchar
               )""")
    cur.execute("""CREATE TABLE Admin_login(
                                ID varchar Unique,
                                Password varchar

                )""")
    cur.execute('INSERT into Admin_login values ("Deepak@1","Tewatia@1")')
    connector.commit()
except Exception as e:
    print()
else:
    print('Successfully Done!')


class Center:
    def Make_Center(self,app_width,app_height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        w = int(( screen_width / 2) - (app_width/2))
        h = int(( screen_height / 2 - 30) - (app_height/2))
        return [w,h]

class Photo:
    def Root_Icon(self,root):
        root.title('Hospital')
        image = Image.open(r"C:\Users\DELL\Desktop\Python\Projects\Awakinn Project\Hospital\hospital.ico")
        # image = image.resize((20, 20), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        root.iconphoto(False,photo)

class Go_back:
    def go_back(self,cmd):
        Menubar = Menu(root)
        Menubar.add_command(label='Go back',command=cmd)
        root.config(menu=Menubar)

    def go_backandmain(self,cmd):
        menu = Menu(root)
        menu.add_command(label='Go back',command=cmd)
        menu.add_command(label='Log Out',command=lambda : Main_menu.Menu_0(self))
        root.config(menu=menu)

class Button_display:
    def b_main_menu(self,root,textlist,commandlist,w):
        for i in range(len(textlist)):
            Button(root,text=textlist[i],command=commandlist[i],font='lucida 25 bold',height=1,relief=GROOVE,border=10,width=w).pack()


    def b_Close_grid(self,root,row1):
        Button(root,text='Close',command=quit,fg='White',bg='red',font='lucida 20 bold',relief=GROOVE,border=10,width=6).grid(row=row1,column=0)

    def b_Work_grid(self,root,row2,work,call):
        Button(root,text=work,command=call,font='lucida 20 bold',fg='White',bg='blue',relief=GROOVE,border=10,width=10).grid(row=row2,column=1)

    def b_Exit(self,root,w):
        Button(root,text='Exit',command=quit,fg='White',bg='red',font='lucida 20 bold',relief=GROOVE,border=10,width=w).pack()

    def b_Close_sub(self,root,des,w):
        Button(root,text='Close',command=quit,fg='White',bg='red',font='lucida 25 bold',relief=GROOVE,border=10,width=w).pack()



class Disp_text:
    def label_fortxt(self,root,textlist):
        for i in range(len(textlist)):
            Label(root,text=f'{textlist[i]}:',font='lucida 20 bold',padx=3,pady=3).grid(row=i,column=0)

    def Main_text(self,root,txt):
        Label(root,text=txt,font='lucida 30 bold',bg='grey',justify='center').pack()


class Admin(Button_display,Disp_text,Photo,Go_back,Center):
    def Admin_main(self):
        global root
        root.destroy()
        root = Tk()
        w,h = self.Make_Center(400,170)
        root.geometry(f'400x170+{w}+{h}')
        root.minsize(400,170)
        root.maxsize(400,170)

        root.title('Admin Login')

        self.go_back(lambda : Main_menu.Menu_0(self))

        txt = ['ID','Password']

        self.label_fortxt(root,txt)

        global Id_1,Pass_1

        Id_1 = StringVar(root)
        Pass_1 = StringVar(root)

        Id = Entry(root,textvariable=Id_1,font='lucida 16')
        Id.grid(row=0,column=1)
        pas = Entry(root,textvariable=Pass_1,font='lucida 16',show='*')
        pas.grid(row=1,column=1)

        self.b_Work_grid(root,2,'Login',self.Admin_login)
        self.b_Close_grid(root,2)

    def Admin_login(self):
        Id = Id_1.get()
        pas = Pass_1.get()

        cur.execute('SELECT * from Admin_login where ID=(?) and Password=(?)',(Id,pas))
        x = cur.fetchall()
        if x!= []:
            self.A_function()
        else:
            tmsg.showinfo('Not found','Either you have entered wrong Id or Password or you are not allowed to use this login')

    def A_add_doctor_call(self):
        name = name_101.get()
        email = email_101.get()
        mobile = mobile_101.get()
        spc = spc_101.get()
        Id = id_101.get()
        pas = pas_101.get()
        if  name=='' or spc=='' or Id=='' or pas =='' :
            tmsg.showinfo('Not filled','All important details are not filled')
        elif len(str(mobile)) != 10:
            tmsg.showinfo('No','Number is not of 10 digit')
        else:
            try:
                self.A_add_doctor()
                cur.execute('INSERT Into Doctor values(?,?,?,?,?,?,?,?,"No")',(name,email,mobile,gender_101.get(),blood_g_101.get(),spc,Id,pas,))
                connector.commit()
                tmsg.showinfo('Done','Successfully Added!')
            except Exception as e:
                tmsg.showinfo('Issue',f'Some Issue as given below\n {e}')

    def A_add_doctor(self):
        global root
        root.destroy()
        root = Tk()
        w,h = self.Make_Center(470,430)
        root.geometry(f'470x430+{w}+{h}')
        root.minsize(470,430)
        root.maxsize(470,430)

        root.title('Doctor Details')
        txtD = ['Cardiologist','NeuroSurgeon','ENT Specialist','Orthopaedics','Ophthalmologist']

        txt = ['Name*','Email','Mobile*','Gender*','Blood Group','Specialization*','Id*','Password*']
        self.label_fortxt(root,txt)
        self.go_backandmain(self.A_function)

        global name_101,email_101,mobile_101,gender_101,blood_g_101,spc_101,id_101,pas_101

        name_101 = StringVar(root)
        email_101 = StringVar(root)
        mobile_101 = IntVar(root)
        gender_101 = StringVar(root)
        blood_g_101 = StringVar(root)
        spc_101 = StringVar(root)
        id_101 = StringVar(root)
        pas_101 = StringVar(root)

        name = Entry(root,textvariable=name_101,font='lucida 16')
        name.grid(row=0,column=1)
        email = Entry(root,textvariable=email_101,font='lucida 16')
        email.grid(row=1,column=1)
        mobile = Entry(root,textvariable=mobile_101,font='lucida 16')
        mobile.grid(row=2,column=1)
        gender = ttk.Combobox(root,textvariable=gender_101,font='lucida 14')
        gender['values'] = ['Male','Female','Others']
        gender.grid(row=3,column=1)
        gender.current(0)
        blood = ttk.Combobox(root,textvariable=blood_g_101,font='lucida 14')
        blood['values'] = ['A+','B+','O+','AB+','A-','B-','O-','AB-']
        blood.grid(row=4,column=1)
        blood.current(0)
        Specialization = ttk.Combobox(root,textvariable=spc_101,font='lucida 14')
        Specialization['values'] = txtD
        Specialization.grid(row=5,column=1)
        Specialization.current(0)
        Id = Entry(root,textvariable=id_101,font='lucida 16')
        Id.grid(row=6,column=1)
        pas = Entry(root,textvariable=pas_101,font='lucida 16',show='*')
        pas.grid(row=7,column=1)

        self.b_Close_grid(root,8)
        self.b_Work_grid(root,8,'Add',self.A_add_doctor_call)

    def A_remove_doctor_call(self):
        D_Id = D_Id_102.get()
        cur.execute('SELECT * from Doctor where Id = (?)',(D_Id,))
        data = cur.fetchall()
        if data != []:
            self.A_remove_doctor()
            cur.execute('DELETE From Doctor where Id=(?)',(D_Id,))
            connector.commit()
            tmsg.showinfo('Done','Successfully Done')
        else:
            tmsg.showinfo('No Doctor',f'There is no Doctor as such having Id {D_Id}')


    def A_remove_doctor(self):
        global root
        root.destroy()
        root = Tk()
        w,h = self.Make_Center(400,150)
        root.geometry(f'400x150+{w}+{h}')
        root.title('Remove Doctor')
        self.label_fortxt(root,['Doctor Id'])
        self.go_backandmain(self.A_function)
        global D_Id_102
        D_Id_102 = StringVar(root)

        Id = Entry(root,textvariable=D_Id_102,font='lucida 16')
        Id.grid(row=0,column=1)

        self.b_Close_grid(root,1)
        self.b_Work_grid(root,1,'Delete',self.A_remove_doctor_call)

    def A_doctor_list(self):
        cur.execute('SELECT Name,Email,Phone_no,Specialization,Id From Doctor')
        data = cur.fetchall()
        if data != []: 
            global root
            root.destroy()           
            root = Tk()
            w,h = self.Make_Center(920,600)
            root.geometry(f'920x600+{w}+{h}')
            root.title('Doctor list')
            self.go_backandmain(self.A_function)
            data.insert(0,('Name','Email','Phone_no','Specialization','Id'))
            Trow = len(data)
            Tcolumn = len(data[0])
            for i in range(Trow):
                for j in range(Tcolumn):
                    e = Entry(root,width=15,font='lucida 16 bold')
                    e.grid(row=i,column=j)
                    e.insert(END,data[i][j])
        else:
            tmsg.showinfo('No Doctor','There is no Doctor in your Data')


    def A_patient_list(self):
        cur.execute('SELECT Name,Email,Phone_no,Gender,Blood_g From Patient')
        data = cur.fetchall()
        if data != []: 
            global root
            root.destroy()          
            root = Tk()
            w,h = self.Make_Center(920,600)
            root.geometry(f'920x600+{w}+{h}')
            self.go_backandmain(self.A_function)
            root.title('Patient list')
            data.insert(0,('Name','Email','Phone_no','Gender','Blood_g'))
            Trow = len(data)
            Tcolumn = len(data[0])
            for i in range(Trow):
                for j in range(Tcolumn):
                    e = Entry(root,width=15,font='lucida 16 bold')
                    e.grid(row=i,column=j)
                    e.insert(END,data[i][j])

        else:
            tmsg.showinfo('No Patient','There is no Patient in your Data')

    def A_change_patient_detail(self):
        pass
    def A_change_doctor_detail(self):
        pass

    def A_function(self):
        global root
        root.destroy()
        root = Tk()
        w,h = self.Make_Center(500,550)
        root.geometry(f'500x550+{w}+{h}')
        root.minsize(500,550)        
        root.maxsize(500,550)        

        root.title('Admin Function')
        # self.go_back(self.Doctor_main)
        self.go_backandmain(self.Doctor_main)

        txt = ['Add Doctor','Remove Doctor','Doctor List','Patient List']#,'Change Patient Details','Change Doctor Details']
        cmd = [self.A_add_doctor,self.A_remove_doctor,self.A_doctor_list,self.A_patient_list,]

        f0 = Frame(root,bg='grey')
        self.Main_text(f0,'Welcome To Admin!')
        f0.pack(fill=X)

        f1 = Frame(root)
        self.b_main_menu(f1,txt,cmd,18)
        self.b_Close_sub(f1,root,13)
        f1.pack(fill=BOTH,pady=30)



class Patient(Button_display,Disp_text,Photo,Go_back,Center):

    def Patient_profile_call(self):
        global root
        root.destroy()
        cur.execute("SELECT * From Patient where Phone_no = (?)",(P_Id,))
        Data = cur.fetchall()
        root = Tk()
        w,h = self.Make_Center(900,330)
        root.geometry(f'900x330+{w}+{h}')
        root.title('Your Details')
        self.go_backandmain(self.P_function)
        
        b = ('Name' , 'Email' , 'Phone_no' , 'Gender' , 'Blood Group ', )
        Data.insert(0,b)
        Trow = len(Data[0])
        Tcolumn = 2

        for i in range(Tcolumn):
            for j in range(Trow):
                e = Entry(root,width=30,font='lucida 20 bold')
                e.grid(row=j,column=i)
                e.insert(END,Data[i][j])

    def Patient_profile(self,root):
        cur.execute("SELECT Name From Patient where Phone_no = (?)",(P_Id,))
        Data = cur.fetchone()

        mymenu = Menu(root)
        mymenu.add_command(label=f'{Data[0]}',command=self.Patient_profile_call)
        mymenu.add_command(label='Go back',command=self.patient_main)
        mymenu.add_command(label='Log Out',command=lambda : Main_menu.Menu_0(self))

        root.config(menu=mymenu)


    def patient_main(self):
        global root
        root.destroy()
        root = Tk()
        w,h = self.Make_Center(370,350)
        root.geometry(f'370x350+{w}+{h}')
        root.minsize(370,350)
        root.maxsize(370,350)

        root.title('Patient')
        self.go_back(lambda : Main_menu.Menu_0(self))

        text = ['Login','Register']
        cmd = [self.P_login,self.P_register]

        f_21 = Frame(root,bg='grey')
        self.Main_text(f_21,'Patient Block')
        f_21.pack(fill=X)

        f_22 = Frame(root)
        self.b_main_menu(f_22,text,cmd,12)
        self.b_Close_sub(f_22,root,8)
        f_22.pack(fill=BOTH,pady=30)

    def P_booking_call(self,event):
        global root
        time = event.widget.cget('text')       
        x = tmsg.askquestion('Sure?','Do you want to take Appointment?')
        if x == 'yes':
            try:
                cur.execute('INSERT INTO Booking values (?,?,?,?,?)',(P_Id,time,P_B_date,P_B_doctor_name,P_B_spc,))
                connector.commit()
            except Exception as e:             
                tmsg.showinfo('Issue',f'There is some Issue as given below\n{e}')
            else:
                tmsg.showinfo('Booked',f'Your Appointment is booked for {P_B_date} at {time} ')
                self.P_function()
        else:           
            tmsg.showinfo('Not Booked','Your Appointment is not booked ')

    def P_taking_time(self,date,spc):
        global P_B_doctor_name,root
        # root.destroy()
        doctor_name = d_name.get()
        # print(P_B_doctors,doctor_name)
        if (doctor_name,) not in P_B_doctors:
            tmsg.showinfo('NO','Please Select doctors from given list')
        else:
            P_B_doctor_name = doctor_name
            cur.execute('''SELECT Book_time From Booking where Book_date=(?) and Doctor_name= (?) and Specialization = (?) ''',(P_B_date,doctor_name,spc,))
            data = cur.fetchall()
            Time_list = ['10:00-10:30','10:35-11:00','11:05-11:30','11:35-12:00',
                         '14:00-14:30','14:35-15:00','15:05-15:30','15:35-16:00',
                         '16:05-16:30','16:35-17:00'
                        ]
            if data != []:
                for i in range(len(data)):
                    if data[i][0] in Time_list:
                        Time_list.remove(data[i][0])
            root.destroy()
            root = Tk()
            root.title('Select your time')


            f = Frame(root,bg='grey')
            for i in range(len(Time_list)):
                if (i)%4 == 0 and i > 1:
                    f = Frame(root,bg='grey')
                b = Button(f,text=f'{Time_list[i]}',padx=10,pady=5,font='lucida 16 bold',relief=GROOVE,border=10)
                b.pack(side='left')
                b.bind('<Button-1>',self.P_booking_call)
                if (i)%4 == 0 and i > 1:
                    f.pack(pady=20)
                if i == 3:
                    f.pack(pady=20)
            self.go_backandmain(self.P_Booking)
            
        # button = Button(root,text='Book',command=lambda : self.P_booking_call(P_Id,doctor_name,spc,date),border=10,relief=GROOVE,width=10,bg='blue',fg='white').pack(pady=20)

        

    def P_Pas_Calender_date(self):
        global P_B_date,P_B_spc,P_B_doctors
        dt = datetime.now()
        date = cal.get_date()
        spc = d_spc.get()
        # P_B_date = date
        P_B_spc = spc
        txt = ['Cardiologist',
                'NeuroSurgeon',
                'ENT Specialist',
                'Orthopaedics',
                'Ophthalmologist'
                ]

        if date == '':
            tmsg.showinfo('Choose?','Please choose date first')
        elif spc not in txt:
            tmsg.showinfo('No','Please choose from list')
        else:
            date = str(date).split('/')
            date = list(map(int,date))
            st = '20%02d-%02d-%02d'%(date[2],date[0],date[1])
            P_B_date = st
            if st >= str(dt.date()):
                cur.execute('SELECT Name From Doctor where Specialization=(?)',(spc,))
                P_B_doctors = cur.fetchall()
                if P_B_doctors != []:
                    my_button.destroy()
                    l = Label(root,text='Choose Doctor from list',font='lucida 16 bold').pack(pady=5)
                    global d_name
                    d_name = StringVar(root)
                    doctor_name = ttk.Combobox(root,textvariable=d_name,font='lucida 14')
                    doctor_name['values'] = P_B_doctors 
                    doctor_name.pack(pady=5)
                    doctor_name.current(0)
                    new_button = Button(root,text='Look for time',font='lucida 16',command=lambda : self.P_taking_time(date,spc),relief=GROOVE,border=10,fg='white',bg='blue').pack(pady=10)
                else:
                    tmsg.showinfo('NO Doctor','No Doctors in Hospital')
            else:
                tmsg.showinfo('OOPS','You are trying to take Appointment of previous date that\'s not possible ')


    def P_Booking(self):
        dt = datetime.now()
        global root
        root.destroy()
        root = Tk()
        root.title('Choose Date and more options')
        # root.geometry(f'300x400+{w}+{h}')

        self.go_backandmain(self.P_function)

        txt = ['Cardiologist','NeuroSurgeon','ENT Specialist','Orthopaedics','Ophthalmologist']

        global cal,d_spc
        cal  = Calendar(root,selectmode='day',year=dt.year,month=dt.month)
        cal.pack(pady=20)
        l = Label(root,text='Choose options from list',font='lucida 16 bold').pack()

        d_spc = StringVar(root)

        doctor = ttk.Combobox(root,font='lucida 14 ',textvariable=d_spc)
        doctor['values'] = txt
        doctor.pack(pady=10)
        doctor.current(0)
        global my_button
        my_button = Button(root,text='procced',bg='blue',fg='white',command=self.P_Pas_Calender_date,font='lucida 14 bold',relief=GROOVE,border=10,width=8)
        my_button.pack(padx=20)
        # my_button2 = Button(root,command=quit,text='Close',bg='red',fg='white',font='lucida 14 bold',relief=GROOVE,border=10,width=8).pack()


    def P_Doctor_check_call(self,spc):
        dt = datetime.now()
        cur.execute('SELECT Name,Id from Doctor as dd inner join D_In as di ON dd.Id=di.Doctor_Id where Specialization=(?)  and Date_In = (?) and Available=("Yes")',(spc,str(dt.date())))
        Data = cur.fetchall()
        x = len(Data)*80 + 100
        global root
        if Data != []:
            global root 
            root.destroy()            
            root = Tk()
            w,h = self.Make_Center(500,x)
            root.geometry(f'500x{x}+{w}+{h}')
            root.title(f'{spc}')
            self.go_backandmain(self.P_Doctor_check)

            txt = []
            cmd = []
            for i in Data:
                txt.append(f'Dr.{i[0]}')
                # cmd.append(lambda: self.P_booking(i[1],P_Id))
            cmd = len(txt)*['1']
            f0 = Frame(root,bg='grey')
            self.Main_text(f0,'Available Doctors for now')
            f0.pack(fill=X)
            f1 = Frame(root)
            self.b_main_menu(f1,txt,cmd,18)
            f1.pack(fill=BOTH,pady=20)
        else:    
            tmsg.showinfo('No','Sorry! For now no Doctor is Available')

    def P_Doctor_check(self):
        global root
        root.destroy()
        root = Tk()
        w,h = self.Make_Center(500,600)
        root.geometry(f'500x600+{w}+{h}')
        root.minsize(500,600)
        root.minsize(500,600)

        root.title('You can choose ')
        self.go_backandmain(self.P_function)

        txt = ['Cardiologist','NeuroSurgeon','ENT Specialist','Orthopaedics','Ophthalmologist']
        cmd = [lambda: self.P_Doctor_check_call('Cardiologist'),
               lambda: self.P_Doctor_check_call('NeuroSurgeon'),
               lambda: self.P_Doctor_check_call('ENT Specialist'),
               lambda: self.P_Doctor_check_call('Orthopaedics'),
               lambda: self.P_Doctor_check_call('Ophthalmologist')
               ]

        f0 = Frame(root,bg='grey')
        self.Main_text(f0,'Choose from options')
        f0.pack(fill=X)

        f1 = Frame(root)
        self.b_main_menu(f1,txt,cmd,20)
        self.b_Close_sub(f1,root,15)
        f1.pack(fill=BOTH,pady=20)

    # def P_Options(self):


    def P_function(self):
        global root
        root.destroy()
        root = Tk()
        # root.geometry(f'500x600+{w}+{h}')
        # root.minsize(500,600)
        # root.minsize(500,600)

        root.title('You can choose ')
        self.Patient_profile(root)

        txt = ['Check Doctors','Appointments']
        cmd = [self.P_Doctor_check,self.P_Booking]
        f0 = Frame(root,bg='grey')
        self.Main_text(f0,'Choose from options')
        f0.pack(fill=X)

        f1 = Frame(root)
        self.b_main_menu(f1,txt,cmd,20)
        self.b_Close_sub(f1,root,15)
        f1.pack(fill=BOTH,pady=20)

    def P_login_call(self):
        global P_Id
        P_Id = Id_21.get()
        Pas = pas_21.get()
        cur.execute('SELECT * from Patient where Phone_no=(?) and Password = (?)',(P_Id,Pas,))
        Data = cur.fetchone()
        if Data == None:
            tmsg.showinfo('Not Found','Either you have not Register\nor While entering you did mistake!')
        else:
            self.P_function()

    def P_login(self):
        global root
        root.destroy()
        root = Tk()
        w,h = self.Make_Center(480,180)
        root.geometry(f'480x180+{w}+{h}')
        root.minsize(480,180)
        root.maxsize(480,180)

        root.title('Patient Login')
        self.go_backandmain(self.patient_main)
        text = ['Your Mobile','Your Password']
        self.label_fortxt(root,text)

        global Id_21,pas_21

        Id_21 = StringVar(root)
        pas_21 = StringVar(root)

        ID = Entry(root,textvariable=Id_21,font='lucida 16')
        ID.grid(row=0,column=1)
        Pass = Entry(root,textvariable=pas_21,font='lucida 16',show='*')
        Pass.grid(row=1,column=1)

        self.b_Work_grid(root,2,'Login',self.P_login_call)
        self.b_Close_grid(root,2)
    

    def P_register_call(self):
        
        name = name_22.get()
        email = email_22.get()
        mobile = p_no_22.get()
        gender = gender_22.get()
        blood  = blood_22.get()
        pas = Pass_22.get()
        if name=='' or mobile == 0 or gender == '' or pas == '' :
            tmsg.showinfo('Not filled','You have not filled Important fields!')
        elif len(str(mobile)) != 10:
            tmsg.showinfo('Not valid','You have entered the length of mobile number not equal to 10')
        else:
            self.P_register()
            try:
                cur.execute('INSERT into Patient values (?,?,?,?,?,?)',(name,email,mobile,gender,blood,pas,))
                connector.commit()
            except Exception as e:
                tmsg.showinfo('Issue',f'Your Details are not filled,\n{e}')
            else:
                tmsg.showinfo('Done','Please remember your phone number and Password for login purpose!')


    def P_register(self):
        global root
        root.destroy()
        root = Tk()
        w,h = self.Make_Center(500,330)
        root.geometry(f'500x330+{w}+{h}')
        root.minsize(500,330)
        root.maxsize(500,330)
        self.go_backandmain(self.patient_main)
        root.title('Register')

        txt = ['Name*','E mail','Phone Number*','Gender*','Blood Group','Password*']
        self.label_fortxt(root,txt)

        global name_22,email_22,p_no_22,gender_22,blood_22,Pass_22

        name_22 = StringVar(root)
        email_22 = StringVar(root)
        p_no_22 = IntVar(root)
        gender_22 = StringVar(root)
        blood_22 = StringVar(root)
        Pass_22 = StringVar(root)

        name = Entry(root,textvariable=name_22,font='lucida 16')
        name.grid(row=0,column=1)
        email = Entry(root,textvariable=email_22,font='lucida 16')
        email.grid(row=1,column=1)
        phone = Entry(root,textvariable=p_no_22,font='lucida 16')
        phone.grid(row=2,column=1)
        gender = ttk.Combobox(root,textvariable=gender_22,font='lucida 14')
        gender['values'] = ['Male','Female','Others']
        gender.grid(row=3,column=1)
        gender.current(0)
        blood = ttk.Combobox(root,textvariable=blood_22,font='lucida 14')
        blood['values'] = ['A+','B+','O+','AB+','A-','B-','O-','AB-']
        blood.grid(row=4,column=1)
        blood.current(0)
        Pass = Entry(root,textvariable=Pass_22,font='lucida 16')
        Pass.grid(row=5,column=1)

        self.b_Work_grid(root,6,'Create',self.P_register_call)
        self.b_Close_grid(root,6)


class Doctor(Button_display,Disp_text,Photo,Go_back,Center):

    def D_Change_Password_call(self):
        old = o_pas_311.get()
        new = n_pas_311.get()
        r_new = r_pas_311.get()
        cur.execute('SELECT * From Doctor where Id=(?) and Password=(?)',(D_Id_3,old,))
        data = cur.fetchall()
        if data != [] and (new==r_new):
            cur.execute('UPDATE Doctor set Password=(?) where Id=(?)',(new,D_Id_3,))
            connector.commit()
            tmsg.showinfo('Done','Successfully Updated')
        elif data != [] and new!=r_new:
            tmsg.showinfo('Issue',"Your Re-entered Password don't matches")
        else:
            tmsg.showinfo('Issue','Your old Password is wrong check it again')

    def D_Change_Password(self):
        global root
        root.destroy()
        root = Tk()
        w,h = self.Make_Center(450,200)
        root.geometry(f'450x200+{w}+{h}')

        txt = ['Old Password','New Password','Re-enter New']
        self.go_backandmain(self.Doctor_profile_call)
        self.label_fortxt(root,txt)

        global o_pas_311 , n_pas_311, r_pas_311
        o_pas_311 = StringVar(root)
        n_pas_311 = StringVar(root)
        r_pas_311 = StringVar(root)

        Menubar = Menu(root)
        Menubar.add_command(label='Go Main Function',command=self.D_function)
        root.config(menu=Menubar)
        Old = Entry(root,textvariable=o_pas_311,font='lucida 16',show='*')
        Old.grid(row=0,column=1)
        New = Entry(root,textvariable=n_pas_311,font='lucida 16',show='*')
        New.grid(row=1,column=1)
        Re_new = Entry(root,textvariable=r_pas_311,font='lucida 16',show='*')
        Re_new.grid(row=2,column=1)

        self.b_Close_grid(root,3)
        self.b_Work_grid(root,3,'Update',self.D_Change_Password_call)

    def Doctor_profile_call(self):
        global root
        root.destroy()
        cur.execute("SELECT Name,Email,Phone_no,Gender,Blood_g,Specialization,Id,Available From Doctor where Id = (?)",(D_Id_3,))
        Data = cur.fetchall()
        root = Tk()
        w,h = self.Make_Center(900,330)
        root.geometry(f'900x330+{w}+{h}')
        root.title('Your Details')
        Menubar = Menu(root)
        Menubar.add_command(label='Go back',command=self.D_function)
        Menubar.add_command(label='Log Out',command=lambda : Main_menu.Menu_0(self))
        Menubar.add_command(label='Change Password',command=self.D_Change_Password)
        root.config(menu=Menubar)
        b = ('Name' , 'Email' , 'Phone_no' , 'Gender' , 'Blood Group ', 'Specialization' ,  'Id' , 'Available' )
        Data.insert(0,b)
        Trow = len(Data[0])
        Tcolumn = 2

        for i in range(Tcolumn):
            for j in range(Trow):
                e = Entry(root,width=30,font='lucida 20 bold')
                e.grid(row=j,column=i)
                e.insert(END,Data[i][j])

    def Doctor_profile(self,root):
        cur.execute("SELECT Name From Doctor where Id = (?)",(D_Id_3,))
        Data = cur.fetchone()

        mymenu = Menu(root)
        mymenu.add_command(label=f'{Data[0]}',command=self.Doctor_profile_call)
        mymenu.add_command(label='Log Out',command=lambda : Main_menu.Menu_0(self))

        root.config(menu=mymenu)


    def Doctor_main(self):
        global root
        root.destroy()
        root = Tk()
        w,h = self.Make_Center(400,180)
        root.geometry(f'400x180+{w}+{h}') 
        root.title('Doctor Login')
        self.go_back(lambda : Main_menu.Menu_0(self))

        txt = ['Doctor ID','Password']
        self.label_fortxt(root,txt)

        global Id_3,Pas_3

        Id_3 = StringVar(root)
        Pas_3 = StringVar(root)

        Id = Entry(root,textvariable=Id_3,font='lucida 16')
        Id.grid(row=0,column=1)
        Pas = Entry(root,textvariable=Pas_3,font='lucida 16',show='*')
        Pas.grid(row=1,column=1)

        self.b_Work_grid(root,2,'Login',self.D_login)
        self.b_Close_grid(root,2)

    def D_login(self):
        global D_Id_3
        D_Id_3 = Id_3.get()
        pas = Pas_3.get()

        cur.execute('SELECT * From Doctor where ID = (?) and Password = (?)',(D_Id_3,pas,))
        Data = cur.fetchall()
        if Data == []:
            
            
            tmsg.showinfo('Error','Either You are not allowed to use this or\nYou entered something wrong')
        else:
            self.D_function()


    def Virtual_In(self):
        dt = datetime.now()
        cur.execute('SELECT * from D_In where Doctor_Id=(?) and Date_In=(?)',(D_Id_3,str(dt.date())))
        data = cur.fetchall()
        if data == []:
            q = tmsg.askquestion('?','Are you sure you want to make yourself In ?')
            if q == 'yes':            
                cur.execute("INSERT Into D_In values (?,?,?)",(D_Id_3,str(dt.time()),str(dt.date()),))
                connector.commit()
                self.D_function()
        else:
            
            
            tmsg.showinfo('No','You can only use In option 1 time a day!')

    def Virtual_out(self):
        dt = datetime.now()
        cur.execute('SELECT Date_In,Time_In from D_In where Date_In=(?) and Doctor_Id=(?)',(str(dt.date()),D_Id_3,))
        x = cur.fetchall()
        cur.execute('SELECT Date_Out,Time_Out from D_Out where Date_Out=(?) and Doctor_Id=(?)',(str(dt.date()),D_Id_3,))
        y = cur.fetchall()
        if x[0][1] < str(dt.time()) and x[0][0] < str(dt.date()) :
            if x != [] and y == []:
                    q = tmsg.askquestion('?','Are you sure you want to make yourself out?\nbeacuse you can use in only one time.. in a day')
                    if q == 'yes':
                        cur.execute('INSERT INTO D_Out values (?,?,?)',(D_Id_3,str(dt.time()),str(dt.date()),))
                        connector.commit()
                        self.D_function()
            else:
                
                
                tmsg.showinfo("Can't",'You are previously not In!')
        else:
            tmsg.showinfo('No','there is some issue with your current date and time!')
            

    def Available(self):
        cur.execute('SELECT Available from Doctor where Id = (?)',(D_Id_3,))
        x = cur.fetchone()
        if x[0] == 'Yes':
            
            
            tmsg.showinfo('Done','You are already Available!')
        else:
            y = tmsg.askquestion('Available?','Do you want to make yourself Available?')
            if y == 'yes':                
                cur.execute('UPDATE Doctor set Available="Yes" where Id = (?)',(D_Id_3,))
                connector.commit()
                self.D_function()
    
    def NotAvailable(self):
        x = tmsg.askquestion('?','Do you want to make yourself not Available?')
        if x == 'yes':            
            cur.execute('UPDATE Doctor set Available="No" where Id = (?)',(D_Id_3,))
            connector.commit()
            self.D_function()


    def Patient_list(self):
        Date = datetime.now()
        cur.execute('SELECT Name,Specialization From Doctor where Id=(?)',(D_Id_3,))
        doctor = cur.fetchall()
        cur.execute('SELECT Patient_mobile,Book_time from Booking where Doctor_name = (?) and Book_date = (?) and Specialization=(?)',(doctor[0][0],str(Date.date()),doctor[0][1],))
        Data = cur.fetchall()
        x = [('Name','Gender','Blood Group','Mobile','Booked Time')]
        r = ()
        for i in range(len(Data)):
            cur.execute('SELECT Name,Gender,Blood_g from Patient where Phone_no=(?)',(Data[i][0],))
            r = cur.fetchone()
            k = r +Data[i]
            x.append(k)


        if Data != []:
            Trow = len(x)
            Tcolumn = len(x[0])
            global root
            root.destroy()
            root = Tk()
            w,h = self.Make_Center(900,600)
            root.geometry(f'900x600+{w}+{h}')
            # root.minsize(1150,600)
            # root.maxsize(1150,600)
            self.go_backandmain(self.D_function)

            root.title('Patient Requests')
            Trow = len(x)
            Tcolumn = len(x[0])
            for i in range(Trow):
                for j in range(Tcolumn):
                    e = Entry(root,width=15,font='lucida 16')
                    e.grid(row=i,column=j)
                    e.insert(END,x[i][j])

        else:
            
            
            tmsg.showinfo('Empty','There is no request!')
            self.D_function()

    def D_status(self,f1):
        dt = datetime.now()
        cur.execute('SELECT * from D_In where Date_In=(?) and Doctor_Id=(?)',(str(dt.date()),D_Id_3,))
        x = cur.fetchall()
        cur.execute('SELECT * from D_Out where Date_Out=(?) and Doctor_Id=(?)',(str(dt.date()),D_Id_3,))
        y = cur.fetchall()
        cur.execute('SELECT Available From Doctor where Id=(?)',(D_Id_3,))
        z = cur.fetchall()
        if x != [] and y !=[] and z[0][0] == 'No':
            status = StringVar()
            status.set('Out.....  Not Available...')
            sbar = Label(f1,textvariable=status,border=5,anchor=W,fg='red',font='lucida 12 bold')
            sbar.pack(side=RIGHT,pady=10)
        elif x != [] and y !=[] and z[0][0] == 'Yes':
            status = StringVar()
            status.set('Out.....  Available...')
            sbar = Label(f1,textvariable=status,border=5,anchor=W,fg='red',font='lucida 12 bold')
            sbar.pack(side=RIGHT,pady=10)

        elif x != [] and y == [] and z[0][0] == 'Yes':
            status = StringVar()
            status.set('In.....  Available...')
            sbar = Label(f1,textvariable=status,border=5,anchor=W,fg='green',font='lucida 12 bold')
            sbar.pack(side=RIGHT,pady=10)
        elif x != [] and y == [] and z[0][0] == 'No':
            status = StringVar()
            status.set('In.....  Not Available...')
            sbar = Label(f1,textvariable=status,border=5,anchor=W,fg='red',font='lucida 12 bold')
            sbar.pack(side=RIGHT,pady=10)
        elif x ==[] and y == [] and z[0][0] == 'Yes':
            status = StringVar()
            status.set('Available...')
            sbar = Label(f1,textvariable=status,border=5,anchor=W,fg='green',font='lucida 12 bold')
            sbar.pack(side=RIGHT,pady=10)
        elif x ==[] and y == [] and z[0][0] == 'No':
            status = StringVar()
            status.set(' Not Available...')
            sbar = Label(f1,textvariable=status,border=5,anchor=W,fg='red',font='lucida 12 bold')
            sbar.pack(side=RIGHT,pady=10)



    def D_function(self):
        global root
        root.destroy()
        root = Tk()
        w,h = self.Make_Center(500,630)
        root.geometry(f'500x630+{w}+{h}')
        root.minsize(500,630)
        root.maxsize(500,630)

        root.title('Doctor Function')

        txt = ['In','Out','Available','Not Available','Patient list']
        cmd = [self.Virtual_In,self.Virtual_out,self.Available,self.NotAvailable,self.Patient_list]

        self.Doctor_profile(root)

        f0 = Frame(root,bg='grey')
        self.Main_text(f0,'Doctor Function!')
        f0.pack(fill=X)

        f = Frame(root)
        self.D_status(f)
        f.pack(fill=X)

        f1 = Frame(root)
        self.b_main_menu(f1,txt,cmd,18)
        self.b_Close_sub(f1,root,13)
        f1.pack(fill=BOTH,pady=10)

class Main_menu(Patient,Admin,Doctor):

    def Menu_0(self):
        global root,loop
        if loop != 0:
            root.destroy()
        loop=1
        
        root = Tk()
        w,h = self.Make_Center(480,450)
        root.geometry(f'480x450+{w}+{h}')
        root.minsize(480,450)
        root.maxsize(480,450)
        root.title('Hospital')


        f_0 = Frame(root,bg='grey')
        self.Main_text(f_0,'Welcome to Hospital!')
        f_0.pack(fill=X)
        text = ['Admin Login','Patient','Doctor Login']
        cmd = [self.Admin_main,self.patient_main,self.Doctor_main]

        f_1 = Frame(root)
        self.b_main_menu(f_1,text,cmd,15)
        self.b_Exit(f_1,10)
        f_1.pack(fill=BOTH,pady=30)


if __name__ == '__main__':

    loop = 0
    a = Main_menu()
    a.Menu_0()
    root.mainloop()
    connector.close()