class Customer():
    Listdetails=[]
    def __init__(self):
        self.name=None
        self.lastName=None
        self.emailAddress=None
        self.phone=None
        self.address=None
        self.state=None
    def AddCustomers(self):
        Customer.Listdetails.append(self)
        return True
    def SearchCustomer(self,phone):
        for e in Customer.Listdetails:
            if(phone==e.phone):

                self.name=e.name
                self.lastName=e.lastName
                self.emailAddress=e.emailAddress
                self.phone=e.phone
                self.address=e.address
                self.state=e.state
                return True
    def UpdateCustomer(self,phone):
        for e in Customer.Listdetails:
            if(phone==e.phone):
                e.name=self.name
                e.lastName=self.lastName
                e.emailAddress=self.emailAddress
                e.phone=self.phone
                e.address=self.address
                e.state=self.state
                return True





import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
import time
root=tkinter.Tk()
root.title("Customer Management System")
root.minsize("1354","768")
root.maxsize("1354","768")
root.configure(bg="#252528",cursor="left_ptr")

#
######## for Events ########

def on_enter(event):
    Button1['bd']=2
def on_leave(event):
    Button1['bd']=1

######## End of Events  ########

######## Find Details  #########
def FindDetails():
    listTop=tkinter.Toplevel()
    listTop.title("Find Details")
    listTop.maxsize("700","600")
    listTop.minsize(700,600)
    listTop.state("normal")
    scrollbar=tkinter.Scrollbar(listTop)
    scrollbar.pack(side="right",fill="y")

    listCst=tkinter.Listbox(listTop,fg="white",bg="gray",font=2,height=30,width=50,yscrollcommand = scrollbar.set)
    data=[]
    state=[]
    address=[]
    blank=[]

    a=0
    b=1
    c=2
    d=3
    for e in Customer.Listdetails:
        data.append(e.name +", "+ str(e.lastName)+", "+str(e.emailAddress)+", "+str(e.phone))
        state.append(e.state)
        address.append(e.address)
        blank.append("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    data=set(data)
    state=set(state)
    address=set(address)
    blank=set(blank)
    for e in data:
        listCst.insert(a+1,e)
    for e in state:
        listCst.insert(b+1,e)
    for e in address:
        listCst.insert(c+1,e)
    for e in blank:
        listCst.insert(d+1,e)

    listCst.place(x=130,y=20)
    scrollbar.config( command = listCst.yview )


    # top.geometry("600x550")
    listTop.config(bg="#252528")
    listTop.mainloop()




#########  End of Find-Details ########


######## List of Customer ########
def ListofCustomer():
    listTop=tkinter.Toplevel()
    listTop.title("List Of Customer ")
    listTop.maxsize("700","600")
    listTop.minsize(700,600)
    listTop.state("normal")
    scrollbar=tkinter.Scrollbar(listTop)
    scrollbar.pack(side="right",fill="y")

    listCst=tkinter.Listbox(listTop,fg="white",bg="gray",font=2,height=30,width=50,yscrollcommand = scrollbar.set)
    data=[]
    a=0
    for e in Customer.Listdetails:
        data.append(e.name +" "+ str(e.lastName))
    data=set(data)
    for e in data:
        listCst.insert(a+1,e)
    listCst.place(x=130,y=20)
    scrollbar.config( command = listCst.yview )


    # top.geometry("600x550")
    listTop.config(bg="#252528")
    listTop.mainloop()



#########End of List-of-Customer ##########




########  Update Customer ##########
def Update_Customer():
    update_Customer=tkinter.Toplevel()
    update_Customer.title("Update Customer ")
    update_Customer.maxsize("500","300")
    update_Customer.minsize(500,300)
    update_Customer.state("normal")
    # top.geometry("600x550")
    update_Customer.config(bg="#252528")

    updt_Customer_lbl=tkinter.Label(update_Customer,text="Phone no ",fg="white",bg="#252528",font=2)
    updt_Customer_lbl.place(x=70,y=90)


    update_Phone=tkinter.IntVar()
    updt_Customer_no=tkinter.Entry(update_Customer,bg="white",bd=3,width=35,textvariable=update_Phone)
    updt_Customer_no.place(x=170,y=90)

    def Update():
        update_top=tkinter.Toplevel()
        update_top.title("Result")
        update_top.maxsize("600","550")
        update_top.minsize(600,550)
        update_top.state("normal")
        # top.geometry("600x550")
        update_top.config(bg="#252528")




        NameLabel=tkinter.Label(update_top,text="First Name ",fg="white",bg="#252528",font=2)
        NameLabel.place(x=120,y=100)

        var_updt_Name=tkinter.StringVar()
        NameEntry=tkinter.Entry(update_top,bd=3,bg="white",width=35,textvariable=var_updt_Name)
        NameEntry.place(x=250,y=100)

        LastLabel=tkinter.Label(update_top,text="Last Name ",fg="white",bg="#252528",font=2)
        LastLabel.place(x=120,y=150)

        var_updt_Last=tkinter.StringVar()
        LastEntry=tkinter.Entry(update_top,bd=3,bg="white",width=35,textvariable=var_updt_Last)
        LastEntry.place(x=250,y=150)

        EmailLabel=tkinter.Label(update_top,text="Email Address ",fg="white",bg="#252528",font=2)
        EmailLabel.place(x=120,y=200)

        var_updt_Email=tkinter.StringVar()
        EmailEntry=tkinter.Entry(update_top,bg="white",bd=3,width=35,textvariable=var_updt_Email)
        EmailEntry.place(x=250,y=200)

        PhoneLabel=tkinter.Label(update_top,text="Phone",fg="white",bg="#252528",font=2)
        PhoneLabel.place(x=120,y=250)

        var_updt_Phone=tkinter.IntVar()
        PhoneEntry=tkinter.Entry(update_top,bg="white",bd=3,width=35,textvariable=var_updt_Phone)
        PhoneEntry.place(x=250,y=250)

        Addresslabel=tkinter.Label(update_top,text="Address",fg="white",bg="#252528",font=2)
        Addresslabel.place(x=120,y=300)

        var_updt_Address=tkinter.StringVar()
        AddressEntry=tkinter.Entry(update_top,bg="white",bd=3,width=35,textvariable=var_updt_Address)
        AddressEntry.place(x=250,y=300)

        stateLabel=tkinter.Label(update_top,text="State",fg="white",bg="#252528",font=2)
        stateLabel.place(x=120,y=350)

        var_updt_State=tkinter.StringVar()
        stateEntry=tkinter.Entry(update_top,bg="white",bd=3,width=35,textvariable=var_updt_State)
        stateEntry.place(x=250,y=350)

        # varName.set(ob2.name)
        # varLast.set(ob2.lastName)
        # varEmail.set(ob2.emailAddress)
        # varPhone.set(ob2.phone)
        # varAddress.set(ob2.address)
        # varState.set(ob2.state)
        def Finaly_Update():
            phonse_no=update_Phone.get()
            for e in Customer.Listdetails:
                if(e.phone==phonse_no):

                    update_ob=Customer()
                    update_ob.name=var_updt_Name.get()
                    update_ob.lastName=var_updt_Last.get()
                    update_ob.phone=var_updt_Phone.get()
                    update_ob.emailAddress=var_updt_Email.get()
                    update_ob.address=var_updt_Address.get()
                    update_ob.state=var_updt_State.get()
                    update_ob.UpdateCustomer(phonse_no)




        def Add():
            Submitbutton.bind("<Button-1>",lambda event:update_top.destroy())
            update_top.destroy()

        Submit_updt_button=tkinter.Button(update_top,text="Update",width=10,height=2,relief="ridge",bd=1,bg="blue",command=Finaly_Update)
        Submit_updt_button.bind("<Enter>",lambda event:Submit_updt_button.config(bd=2))
        Submit_updt_button.bind("<Leave>",lambda event:Submit_updt_button.config(bd=1))
        Submit_updt_button.bind("<Button-1>",lambda event: messagebox.showinfo("Update","Customer Update Successfully"))
        Submit_updt_button.place(x=280,y=400)


        Submitbutton=tkinter.Button(update_top,text="Exit",width=10,height=2,relief="ridge",bd=1,bg="blue",command=Add)
        Submitbutton.bind("<Enter>",lambda event:Submitbutton.config(bd=2))
        Submitbutton.bind("<Leave>",lambda event:Submitbutton.config(bd=1))
        Submitbutton.place(x=280,y=450)


        update_top.mainloop()
# else:
        # messagebox.showerror("Not Found","Customer Not Found")


    updateBtn=tkinter.Button(update_Customer,text="Update",width=10,height=2,relief="ridge",bd=1,bg="blue",command=Update)
    updateBtn.bind("<Enter>",lambda event:updateBtn.config(bd=2))
    updateBtn.bind("<Leave>",lambda event:updateBtn.config(bd=1))
    updateBtn.place(x=220,y=160)

    def Susss():
        updt_exit_Btn.bind("<Button-1>",lambda event:update_Customer.destroy())
        update_Customer.destroy()

    updt_exit_Btn=tkinter.Button(update_Customer,text="Exit",width=10,height=2,relief="ridge",bd=1,bg="blue",command=Susss)
    updt_exit_Btn.bind("<Enter>",lambda event:updt_exit_Btn.config(bd=2))
    updt_exit_Btn.bind("<Leave>",lambda event:updt_exit_Btn.config(bd=1))
    updt_exit_Btn.place(x=220,y=210)

    update_Customer.mainloop()


##########  End of update Customer #########




######## Total-Customer ########
def Total_Customer():
    a=0
    total_top=tkinter.Toplevel()
    total_top.title("Total Customers")
    total_top.maxsize("400","300")
    total_top.minsize(400,300)
    total_top.state("normal")
    # top.geometry("600x550")
    total_top.config(bg="#252528")

    for element in Customer.Listdetails:
        a+=1
    vartotal=tkinter.StringVar()
    total_msg=tkinter.Message(total_top,textvariable=vartotal,font=2,fg="white",bg="#252528",width=300)
    msg="Total Customers are :-  %d"%a
    vartotal.set(msg)
    total_msg.place(x=100,y=100)


    total_top.mainloop()

########End of Total-Customer ########
########Instructions Section ########

def Instructions():
    instruction_window=tkinter.Toplevel()
    instruction_window.title("Instructions")
    instruction_window.minsize("600","400")
    instruction_window.maxsize("600","400")
    instruction_window.configure(bg="#252528")

    ins_var=tkinter.StringVar()
    ins_msg=tkinter.Message(instruction_window,textvariable=ins_var,font=2,fg="white",bg="#252528",width=500)

    msg=" To manage the Customer \n\n\t1. Choose the first About section and read carefully\n\n\t 2.Choose the options like (Add Customer , Remove \t\t\tCustomer, Search Customer etc) \n \n\t3.To Check Update go to the updates Section \n\n\t 4.To Exit Choose the Exit Button or Section \n\n\n\n \t\t   Thank You  "
    ins_var.set(msg)
    ins_msg.place(x=100,y=100)
    instruction_window.mainloop()

########End of Instruction-Section #######


############  Remove Customer  #############

def Remove_Customer():
    rmv_Customer=tkinter.Toplevel()
    rmv_Customer.title("Remove Customer ")
    rmv_Customer.maxsize("500","300")
    rmv_Customer.minsize(500,300)
    rmv_Customer.state("normal")
    # top.geometry("600x550")
    rmv_Customer.config(bg="#252528")

    rmv_Customer_lbl=tkinter.Label(rmv_Customer,text="Phone no ",fg="white",bg="#252528",font=2)
    rmv_Customer_lbl.place(x=70,y=90)


    rmvsearchPhone=tkinter.IntVar()
    rmv_Customer_no=tkinter.Entry(rmv_Customer,bg="white",bd=3,width=35,textvariable=rmvsearchPhone)
    rmv_Customer_no.place(x=170,y=90)

    def Remove():
        length=0
        a=rmvsearchPhone.get()
        for e in Customer.Listdetails:
            length+=1
        if(length==0):
            messagebox.showerror("Error","No Customer Found")
        else:
            for e in Customer.Listdetails:
                if(e.phone==a):
                    Customer.Listdetails.remove(e)
                    ob=Customer()
                    c=ob.SearchCustomer(a)
                    if(c==True):
                        messagebox.showinfo("Removed","Customer Removed Successfully")


    removeBtn=tkinter.Button(rmv_Customer,text="Remove",width=10,height=2,relief="ridge",bd=1,bg="blue",command=Remove)
    removeBtn.bind("<Enter>",lambda event:removeBtn.config(bd=2))
    removeBtn.bind("<Leave>",lambda event:removeBtn.config(bd=1))
    removeBtn.place(x=220,y=160)

    def Suss():
        rmv_exit_Btn.bind("<Button-1>",lambda event:rmv_Customer.destroy())
        rmv_Customer.destroy()

    rmv_exit_Btn=tkinter.Button(rmv_Customer,text="Exit",width=10,height=2,relief="ridge",bd=1,bg="blue",command=Suss)
    rmv_exit_Btn.bind("<Enter>",lambda event:rmv_exit_Btn.config(bd=2))
    rmv_exit_Btn.bind("<Leave>",lambda event:rmv_exit_Btn.config(bd=1))
    rmv_exit_Btn.place(x=220,y=210)

    rmv_Customer.mainloop()


############ Remove Customer -End #############

######## Updates - Section #######
def Update():
    messgae_window=tkinter.Toplevel()
    messgae_window.title("Updates")
    messgae_window.maxsize("400","300")
    messgae_window.minsize(400,300)
    messgae_window.state("normal")
    # top.geometry("600x550")
    messgae_window.config(bg="#252528")

    updtmsg_var=tkinter.StringVar()
    update_msg=tkinter.Message(messgae_window,textvariable=updtmsg_var,font=2,fg="white",bg="#252528",width=200)

    updtmsg_var.set("Check For Updates ")

    def Check_For_Update():
        time.sleep(2)
        updtmsg_var.set("No updates availabe....")



    checkbtn=tkinter.Button(messgae_window,text="Check",width=10,height=2,relief="ridge",bd=1,bg="blue",command=Check_For_Update,activebackground="blue")
    checkbtn.bind("<Enter>",lambda event:checkbtn.config(bd=2))
    checkbtn.bind("<Leave>",lambda event:checkbtn.config(bd=1))
    checkbtn.place(x=165,y=170)
    update_msg.place(x=130,y=80)
    # while 10:
    #     updtmsg_var.set("Checking for Updates.")
    #     update_msg.place(x=100,y=100)
    #     time.sleep(0.5)
    #     updtmsg_var.set("Checking for Updates..")
    #     update_msg.place(x=100,y=100)
    #     time.sleep(0.5)

    messgae_window.mainloop()

######## End of update-Section ########

########About - Section ########
def About():
    about=tkinter.Toplevel()
    about.title("About")
    about.maxsize("450","400")
    about.minsize(450,400)
    about.state("normal")
    # top.geometry("600x550")
    about.config(bg="#252528")

    var=tkinter.StringVar()
    aboutmessage=tkinter.Message(about,textvariable=var,fg="white",bg="#252528",font=2,width=400)
    msg="Developed By :-  \n\n\t Gaurav Kumar & Bishal Shrestha \n\n\n Reference :- \n\n\t https://stackoverflow.com \n\n For any suggestion or feedback , mail us at\n\n\t Gaurav.gk3676@gmail.com \n\n\t Bishal2367@gmail.com"
    var.set(msg)
    aboutmessage.place(x=60,y=50)


    var1=tkinter.StringVar()
    copyrights=tkinter.Message(about,textvariable=var1,fg="gray",bg="#252528",width=100)
    var1.set("© BSkullll inc.")
    copyrights.place(x=270,y=340)

    about.mainloop()
############## End of About-Section ##############


##############  Top-Level-For-Add-Customers  #########

def AddCustomer():
    top=tkinter.Toplevel()
    top.title("Add Customer")
    top.maxsize("600","550")
    top.minsize(600,550)
    top.state("normal")
    # top.geometry("600x550")
    top.config(bg="#252528")

    NameLabel=tkinter.Label(top,text="First Name ",fg="white",bg="#252528",font=2)
    NameLabel.place(x=120,y=100)

    varName=tkinter.StringVar()
    NameEntry=tkinter.Entry(top,bd=3,bg="white",width=35,textvariable=varName)
    NameEntry.place(x=250,y=100)

    LastLabel=tkinter.Label(top,text="Last Name ",fg="white",bg="#252528",font=2)
    LastLabel.place(x=120,y=150)

    varLast=tkinter.StringVar()
    LastEntry=tkinter.Entry(top,bd=3,bg="white",width=35,textvariable=varLast)
    LastEntry.place(x=250,y=150)

    EmailLabel=tkinter.Label(top,text="Email Address ",fg="white",bg="#252528",font=2)
    EmailLabel.place(x=120,y=200)

    varEmail=tkinter.StringVar()
    EmailEntry=tkinter.Entry(top,bg="white",bd=3,width=35,textvariable=varEmail)
    EmailEntry.place(x=250,y=200)

    PhoneLabel=tkinter.Label(top,text="Phone",fg="white",bg="#252528",font=2)
    PhoneLabel.place(x=120,y=250)

    varPhone=tkinter.IntVar()
    PhoneEntry=tkinter.Entry(top,bg="white",bd=3,width=35,textvariable=varPhone)
    PhoneEntry.place(x=250,y=250)

    Addresslabel=tkinter.Label(top,text="Address",fg="white",bg="#252528",font=2)
    Addresslabel.place(x=120,y=300)

    varAddress=tkinter.StringVar()
    AddressEntry=tkinter.Entry(top,bg="white",bd=3,width=35,textvariable=varAddress)
    AddressEntry.place(x=250,y=300)

    stateLabel=tkinter.Label(top,text="State",fg="white",bg="#252528",font=2)
    stateLabel.place(x=120,y=350)

    varState=tkinter.StringVar()
    stateEntry=tkinter.Entry(top,bg="white",bd=3,width=35,textvariable=varState)
    stateEntry.place(x=250,y=350)

    def Add():
        ob1=Customer()
        ob1.name=varName.get()
        ob1.lastName=varLast.get()
        ob1.emailAddress=varEmail.get()
        ob1.phone=varPhone.get()
        ob1.address=varAddress.get()
        ob1.state=varState.get()
        ob1.AddCustomers()
        if(ob1.AddCustomers()==True):
            messagebox.showinfo("Info","Customer Added Successfully")

        else:
            messagebox.showerror("Info","Customer Not Added")
        Submitbutton.bind("<Button-1>",lambda event:top.destroy())
        top.destroy()



    Submitbutton=tkinter.Button(top,text="Submit",width=10,height=2,relief="ridge",bd=1,bg="blue",command=Add)
    Submitbutton.bind("<Enter>",lambda event:Submitbutton.config(bd=2))
    Submitbutton.bind("<Leave>",lambda event:Submitbutton.config(bd=1))
    Submitbutton.place(x=280,y=430)


    top.mainloop()


##############  End of Top-Level  for-Add-Customer ########

#############   Basic Information ###########
def Basic_Information():
        about=tkinter.Toplevel()
        about.title("Basic Information")
        about.maxsize("400","300")
        about.minsize(400,300)
        about.state("normal")
        # top.geometry("600x550")
        about.config(bg="#252528")

        var=tkinter.StringVar()
        aboutmessage=tkinter.Message(about,textvariable=var,fg="white",bg="#252528",font=2,width=300)
        msg="Customer management System is the combination of solutions, workflow and processes that go into managing the customer"+". So basically it manages the Customers. "
        var.set(msg)
        aboutmessage.place(x=60,y=50)


        var1=tkinter.StringVar()
        copyrights=tkinter.Message(about,textvariable=var1,fg="gray",bg="#252528",width=100)
        var1.set("© BSkullll inc.")
        copyrights.place(x=240,y=240)

        about.mainloop()

############# End of basic Information #######

################    Start of Top Level for Search Customer  #######################

def Search():
    topSearch=tkinter.Toplevel()
    topSearch.title("Search")
    topSearch.minsize(500,300)
    topSearch.maxsize(500,300)
    topSearch.config(bg="#252528")

    searchLabel=tkinter.Label(topSearch,text="Phone no ",fg="white",bg="#252528",font=2)
    searchLabel.place(x=70,y=90)

    def Search_Customer():
        ob2=Customer()
        phn=varsearchPhone.get()
        ob2.SearchCustomer(phn)
        #######Gui ##########
        if(ob2.SearchCustomer(phn)==True):
            messagebox.showinfo("Found","Customer Found")
            topa=tkinter.Toplevel()
            topa.title("Result")
            topa.maxsize("600","550")
            topa.minsize(600,550)
            topa.state("normal")
            # top.geometry("600x550")
            topa.config(bg="#252528")

            NameLabel=tkinter.Label(topa,text="First Name ",fg="white",bg="#252528",font=2)
            NameLabel.place(x=120,y=100)

            varName=tkinter.StringVar()
            NameEntry=tkinter.Entry(topa,bd=3,bg="white",width=35,textvariable=varName)
            NameEntry.place(x=250,y=100)

            LastLabel=tkinter.Label(topa,text="Last Name ",fg="white",bg="#252528",font=2)
            LastLabel.place(x=120,y=150)

            varLast=tkinter.StringVar()
            LastEntry=tkinter.Entry(topa,bd=3,bg="white",width=35,textvariable=varLast)
            LastEntry.place(x=250,y=150)

            EmailLabel=tkinter.Label(topa,text="Email Address ",fg="white",bg="#252528",font=2)
            EmailLabel.place(x=120,y=200)

            varEmail=tkinter.StringVar()
            EmailEntry=tkinter.Entry(topa,bg="white",bd=3,width=35,textvariable=varEmail)
            EmailEntry.place(x=250,y=200)

            PhoneLabel=tkinter.Label(topa,text="Phone",fg="white",bg="#252528",font=2)
            PhoneLabel.place(x=120,y=250)

            varPhone=tkinter.IntVar()
            PhoneEntry=tkinter.Entry(topa,bg="white",bd=3,width=35,textvariable=varPhone)
            PhoneEntry.place(x=250,y=250)

            Addresslabel=tkinter.Label(topa,text="Address",fg="white",bg="#252528",font=2)
            Addresslabel.place(x=120,y=300)

            varAddress=tkinter.StringVar()
            AddressEntry=tkinter.Entry(topa,bg="white",bd=3,width=35,textvariable=varAddress)
            AddressEntry.place(x=250,y=300)

            stateLabel=tkinter.Label(topa,text="State",fg="white",bg="#252528",font=2)
            stateLabel.place(x=120,y=350)

            varState=tkinter.StringVar()
            stateEntry=tkinter.Entry(topa,bg="white",bd=3,width=35,textvariable=varState)
            stateEntry.place(x=250,y=350)

            varName.set(ob2.name)
            varLast.set(ob2.lastName)
            varEmail.set(ob2.emailAddress)
            varPhone.set(ob2.phone)
            varAddress.set(ob2.address)
            varState.set(ob2.state)

            def Add():
                Submitbutton.bind("<Button-1>",lambda event:topa.destroy())
                topa.destroy()

            Submitbutton=tkinter.Button(topa,text="Exit",width=10,height=2,relief="ridge",bd=1,bg="blue",command=Add)
            Submitbutton.bind("<Enter>",lambda event:Submitbutton.config(bd=2))
            Submitbutton.bind("<Leave>",lambda event:Submitbutton.config(bd=1))
            Submitbutton.place(x=280,y=430)


            topa.mainloop()
        else:
            messagebox.showerror("Not Found","Customer Not Found")


#######GUi End######


    varsearchPhone=tkinter.IntVar()
    searchEntry=tkinter.Entry(topSearch,bg="white",bd=3,width=35,textvariable=varsearchPhone)
    searchEntry.place(x=170,y=90)

    searchBtn=tkinter.Button(topSearch,text="Search",width=10,height=2,relief="ridge",bd=1,bg="blue",command=Search_Customer)
    searchBtn.bind("<Enter>",lambda event:searchBtn.config(bd=2))
    searchBtn.bind("<Leave>",lambda event:searchBtn.config(bd=1))
    searchBtn.place(x=220,y=160)

    def Sus():
        searchexitBtn.bind("<Button-1>",lambda event:topSearch.destroy())
        topSearch.destroy()

    searchexitBtn=tkinter.Button(topSearch,text="Exit",width=10,height=2,relief="ridge",bd=1,bg="blue",command=Sus)
    searchexitBtn.bind("<Enter>",lambda event:searchexitBtn.config(bd=2))
    searchexitBtn.bind("<Leave>",lambda event:searchexitBtn.config(bd=1))
    searchexitBtn.place(x=220,y=210)


    topSearch.mainloop
    # searchBtn.bind("<Button-1>",lambda event: topSearch.destroy())
################        End of Top Level for Search Customers       #########
#### For Exit #####
def Exit():
    exit()
##################

Addimg=Image.open(r"Pics\Add Customer.png")
AddCustomerimg=ImageTk.PhotoImage(Addimg)
Button1=tkinter.Button(root,image=AddCustomerimg,bg="black",width=217,height=140,bd=1,relief="ridge",cursor="hand2",command=AddCustomer)
# Button1.bind("<Enter>", lambda event: Button1.configure(bd=2))
# Button1.bind("<Leave>", lambda event: Button1.configure(bd=1))
Button1.bind("<Enter>",on_enter)
Button1.bind("<Leave>",on_leave)
Button1.place(x=200,y=135)

Searchimg=Image.open(r'Pics\Search Customer.png')
SearchCustomerimg=ImageTk.PhotoImage(Searchimg)
Button2=tkinter.Button(root,image=SearchCustomerimg,bg="black",width=217,height=140,bd=1,relief="ridge",cursor="hand2",command=Search)
Button2.bind("<Enter>", lambda event: Button2.config(bd=2))
Button2.bind("<Leave>", lambda event: Button2.config(bd=1))
Button2.place(x=428,y=135)

listimg=Image.open(r'Pics\List of  Customer.png')
listofCustomerimg=ImageTk.PhotoImage(listimg)
Button4=tkinter.Button(root,image=listofCustomerimg,bg="black",width=217,height=140,bd=1,relief="ridge",cursor="hand2",command=ListofCustomer)
Button4.bind("<Enter>",lambda event: Button4.config(bd=2))
Button4.bind("<Leave>",lambda event:Button4.config(bd=1))
Button4.place(x=656,y=135)

removeimg=Image.open(r'Pics\Remove Customer.png')
removeCustomerimg=ImageTk.PhotoImage(removeimg)
Button3=tkinter.Button(root,image=removeCustomerimg,bg="black",width=217,height=140,bd=1,relief="ridge",cursor="hand2",command=Remove_Customer)
Button3.bind("<Enter>",lambda event: Button3.config(bd=2))
Button3.bind("<Leave>",lambda event:Button3.config(bd=1))
Button3.place(x=884,y=135)


findimg=Image.open(r'Pics\Find Details.png')
finddetailsimg=ImageTk.PhotoImage(findimg)
Button5=tkinter.Button(root,image=finddetailsimg,bg="black",width=217,height=140,bd=1,relief="ridge",cursor="hand2",command=FindDetails)
Button5.bind("<Enter>",lambda event:Button5.config(bd=2))
Button5.bind("<Leave>",lambda event:Button5.config(bd=1))
Button5.place(x=200,y=288)

updatecustomerimg=Image.open(r'Pics\Update Customer.png')
updatecustomerimg=ImageTk.PhotoImage(updatecustomerimg)
Button6=tkinter.Button(root,image=updatecustomerimg,bg="black",width=217,height=140,bd=1,relief="ridge",cursor="hand2",command=Update_Customer)
Button6.bind("<Enter>",lambda event:Button6.config(bd=2))
Button6.bind("<Leave>",lambda event:Button6.config(bd=1))
Button6.place(x=428,y=288)

Totalimg=Image.open(r'Pics\Total Customers.png')
TotalCustomerimg=ImageTk.PhotoImage(Totalimg)
Button7=tkinter.Button(root,image=TotalCustomerimg,bg="black",width=217,height=140,bd=1,relief="ridge",cursor="hand2",command=Total_Customer)
Button7.bind("<Enter>",lambda event:Button7.config(bd=2))
Button7.bind("<Leave>",lambda event:Button7.config(bd=1))
Button7.place(x=656,y=288)

Basicimg=Image.open(r"Pics\Basic Information.png")
BasicInformationimg=ImageTk.PhotoImage(Basicimg)
Button8=tkinter.Button(root,image=BasicInformationimg,bg="black",width=217,height=140,bd=1,relief="ridge",cursor="hand2",command=Basic_Information)
Button8.bind("<Enter>",lambda event:Button8.config(bd=2))
Button8.bind("<Leave>",lambda event:Button8.config(bd=1))
Button8.place(x=884,y=288)

instructionimg=Image.open(r'Pics\Instructions.png')
instructionimg=ImageTk.PhotoImage(instructionimg)
Button9=tkinter.Button(root,image=instructionimg,bg="black",width=217,height=140,bd=1,relief="ridge",cursor="hand2",command=Instructions)
Button9.bind("<Enter>",lambda event:Button9.config(bd=2))
Button9.bind("<Leave>",lambda event:Button9.config(bd=1))
Button9.place(x=200,y=441)

updatesimg=Image.open(r'Pics\Updates.png')
updatesimg=ImageTk.PhotoImage(updatesimg)
Button10=tkinter.Button(root,image=updatesimg,bg="black",width=217,height=140,bd=1,relief="ridge",cursor="hand2",command=Update)
Button10.bind("<Enter>",lambda event:Button10.config(bd=2))
Button10.bind("<Leave>",lambda event:Button10.config(bd=1))
Button10.place(x=428,y=441)

aboutimg=Image.open(r'Pics\About.png')
aboutimg=ImageTk.PhotoImage(aboutimg)
Button11=tkinter.Button(root,image=aboutimg,bg="black",width=217,height=140,bd=1,relief="ridge",cursor="hand2",command=About)
Button11.bind("<Enter>",lambda event:Button11.config(bd=2))
Button11.bind("<Leave>",lambda event:Button11.config(bd=1))
Button11.place(x=656,y=441)

exitimg=Image.open(r'Pics\Exit.png')
exitimg=ImageTk.PhotoImage(exitimg)
Button12=tkinter.Button(root,image=exitimg,bg="black",width=217,height=140,bd=1,relief="ridge",cursor="hand2",command=Exit)
Button12.bind("<Enter>",lambda event:Button12.config(bd=2))
Button12.bind("<Leave>",lambda event:Button12.config(bd=1))
Button12.place(x=884,y=441)

############################__________Menu__________#######################

menubar=tkinter.Menu(root,relief="raised")
filemenu=tkinter.Menu(menubar,tearoff=0,relief="raised")
filemenu.add_command(label="Add Customer",command=AddCustomer)
filemenu.add_command(label="Search Customer",command=Search)
filemenu.add_command(label="Remove Customer",command=Remove_Customer)
filemenu.add_separator()
filemenu.add_command(label="Update Customer",command=Update_Customer)
menubar.add_cascade(label="Choose",menu=filemenu)

showmenu=tkinter.Menu(menubar,tearoff=0)
showmenu.add_command(label="List of Customers",command=ListofCustomer)
showmenu.add_command(label="Total Customers",command=Total_Customer)
showmenu.add_command(label="Find Details",command=FindDetails)
showmenu.add_separator()
showmenu.add_command(label="Basic Information",command=Basic_Information)
menubar.add_cascade(label="View",menu=showmenu)

optionmenu=tkinter.Menu(menubar,tearoff=0)
optionmenu.add_command(label="Instructions",command=Instructions)
optionmenu.add_command(label="Updates",command=Update)
optionmenu.add_command(label="About",command=About)
optionmenu.add_separator()
optionmenu.add_command(label="Exit",command=exit)
menubar.add_cascade(label="Options",menu=optionmenu)

helpmenu=tkinter.Menu(menubar,tearoff=0)
helpmenu.add_separator()
helpmenu.add_command(label="Help",command=Instructions)
menubar.add_cascade(label="Help",menu=helpmenu)



############################___________End of Menu _______###################


root.config(menu=menubar)
root.mainloop()
