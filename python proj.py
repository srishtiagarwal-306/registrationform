from tkinter import *

base = Tk()
background="#06283D"
# Set window color
base.configure(bg='antiquewhite')
scrollbar = Scrollbar(base)
scrollbar.pack(side = RIGHT, fill = BOTH) 
#set window size
base.geometry("1250x700+210+100")  
base.title("Exhibition Registration Form")  
base.config(bg=background)

#top frames
Label(base,text="Email: artexhbition@gmail.com",width=10,height=3,bg="#E3CF57",anchor="e").pack(side=TOP,fill=X)
Label(base,text="EXHIBITION REGISTRATION FORM",width=10,height=2,bg="#FF7256",fg="#fff",font="arial 20 bold").pack(side=TOP,fill=X)

Form = Label(base, text="National Art Exhibition", font=("copperplate",20),fg="dodgerblue3",bg="cyan",anchor="center")
Form.place(x=20, y=10)

#personal details
personal = LabelFrame(base, text="Personal Details",fg="darkgreen",bg="#CDC8B1",font=("AbhayaLibre",20),bd=2,width=900,height=250,relief=GROOVE)
personal.place(x=20, y=150)

Name= Label(base, text="Enter Name:", font=("arial",12))  
Name.place(x=50, y=190)  
en1= Entry(base)  
en1.place(x=170, y=190)  
  
Email= Label(base, text="Enter Email:", font=("arial",12))  
Email.place(x=520, y=190)  
en3= Entry(base)  
en3.place(x=670, y=190)  

#contact_number 
Contact= Label(base, text="Contact No.:", font=("arial",12))  
Contact.place(x=520, y=230) 
en4= Entry(base)  
en4.place(x=670, y=230)  

#dob
DOB= Label(base, text="Date of Birth: ", width=10, font=("arial",12))
DOB.place(x=520, y= 310)
list_of_dates = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'
               ,'20','21','22','23','24','25','26','27','28','29','30','31')
list_of_months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
list_of_year = ('1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003')
cv=StringVar()
dd= OptionMenu(base, cv, *list_of_dates)  
dd.config(width=15)
mm= OptionMenu(base, cv, *list_of_months)  
mm.config(width=15)
yyyy= OptionMenu(base, cv, *list_of_year)  
yyyy.config(width=15)
cv.set("1")
cv.set("January")
cv.set("1985")  
dd.place(x=670, y=310)  
mm.place(x=700, y=310)  
yyyy.place(x=730, y=310)  
ddl = Label(base, text="dd", fg= 'grey').place(x=675, y=310)
mml = Label(base, text="mm",  fg= 'grey').place(x=705, y=310)
yyl = Label(base, text="yyyy",  fg= 'grey').place(x=735, y=310)

#gender
Gender= Label(base, text="Select Gender", font=("arial",12))  
Gender.place(x=50, y=230)  
vars = IntVar()  
Radiobutton(base, text="Male", padx=3,variable=vars, value=1).place(x=170, y=230)  
Radiobutton(base, text="Female", padx=3,variable=vars, value=2).place(x=230,y=230)  
Radiobutton(base, text="Others", padx=3, variable=vars, value=3).place(x=300,y=230)  

list_of_cntry = ("United States", "India", "Nepal", "Germany","Algeria","Canada","Australia","Germany","France","China","United Kingdom",
                 "Italy","Brazil","Japan","Greece","Indonesia","Argentina","Spain","Belgium","Sweden","Finland")

cv = StringVar()  
drplist= OptionMenu(base, cv, *list_of_cntry)  
drplist.config(width=15)  
cv.set("India")  

Nationality= Label(base, text="Nationality", font=("arial",12))  
Nationality.place(x=50,y=310)  
drplist.place(x=170, y=305)  
  
Job= Label(base, text="Job:", font=("arial",12))  
Job.place(x=50, y=360)      
vars = IntVar()  
Radiobutton(base, text="Independent", padx=5,variable=vars, value=1).place(x=170, y=360)  
Radiobutton(base, text="Cooperation", padx=10,variable=vars, value=2).place(x=290,y=360)   
  
#artwork details

artwork = LabelFrame(base, text="Artwork Details",fg="darkgreen",bg="#CDC8B1",font=("AbhayaLibre",20),bd=2,width=900,height=250,relief=GROOVE)
artwork.place(x=20, y=470)


Title= Label(base, text="Title of Artwork:", font=("arial",12))  
Title.place(x=20, y=520) 
en4= Entry(base)  
en4.place(x=170, y=520)  


Sale= Label(base, text="Is the piece for sale:", font=("arial",12))  
Sale.place(x=20, y=600) 
Y_N= ("Yes", "No")  
YN = StringVar()  
drplist1= OptionMenu(base, YN, *Y_N)  
drplist1.config(width=15)  
YN.set("No")
drplist1.place(x= 170, y=595)

Dimensions= Label(base, text="Dimensions:", font=("arial",12))  
Dimensions.place(x=520, y=520) 
en4= Entry(base)  
en4.place(x=670, y=520)  


Workshop= Label(base, text="Workshop:\n/Studio\n Address", font=("arial",12))  
Workshop.place(x=520, y=580) 
en4= Entry(base)  
en4.place(x=670, y=600)  

Button(base, text="Register", width=10).place(x=400,y=660)
base.mainloop()
