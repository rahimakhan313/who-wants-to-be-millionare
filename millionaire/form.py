from tkinter import *
import main_menu

class form:
    def __init__(self):

        window=Tk()
        window.geometry("1300x700" )

        canvas=Canvas(window , width=1300 , height=700 ,bg="black")
        canvas.pack()

        bg=PhotoImage(file="C:\\Users\\USER\\Desktop\\millionaire\\form.png")
        canvas.create_image(0 , 0, anchor= NW, image= bg)

        frame=Frame(window , bg="black").place(x=1200  ,y =700)

        label=Label(frame, text="  Login Account ", fg="black" , bg="#7D7524", font="Verdana 18 bold").place(x= 950 ,y = 170)
        f_name=Label(frame, text=" First Name ", fg="black" , bg="#7D7524", font=" time 12 ").place(x= 870 ,y = 250)
        l_name=Label(frame, text=" Last Name ", fg="black" , bg="#7D7524", font="time 12 ").place(x= 870 ,y = 300)
        btn=Radiobutton(frame , text="   Male ",  bg="#7D7524", fg="black", font="time 12" , value=1).place(x=890 ,y = 350)
        btn=Radiobutton(frame , text="   Female ", bg="#7D7524", fg="black" , font="time 12" ,value=2).place(x=1020 ,y = 350)
        country=Label(frame, text="  Country ", fg="black" , bg="#7D7524", font="time 12").place(x= 870 ,y = 400)
        city=Label(frame, text=" City  ", fg="black" , bg="#7D7524", font="time 12 ").place(x= 870 ,y = 450)
        email=Label(frame, text="  Email Address ", fg="black" , bg="#7D7524", font="time 12 ").place(x= 870 ,y = 500)
        password=Label(frame, text=" Password  ", fg="black" , bg="#7D7524", font="time 12 ").place(x= 870 ,y = 550)

        f_n=Entry(frame, bg="#7D7524", fg="black", font="time 12").place(x=1000, y=250)
        l_n=Entry(frame, bg="#7D7524", fg="black", font="time 12").place(x=1000, y=300)
        country=Entry(frame, bg="#7D7524", fg="black", font="time 12").place(x=1000, y=400)
        city=Entry(frame, bg="#7D7524", fg="black", font="time 12").place(x=1000, y=450)
        em=Entry(frame, bg="#7D7524", fg="black", font="time 12").place(x=1000, y=500)
        p=Entry(frame, bg="#7D7524", fg="black", font="time 12" , show="*").place(x=1000, y=550)
        btn=Button(frame , text="   Signup    ", bg="#ed2a51", font="time 16", command=main_menu.menu).place(x=1000 ,y = 600)

        window.mainloop()

