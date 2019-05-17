from tkinter import *
import main_menu

class form:
    def __init__(self):

        window=Tk()
        window.geometry("1300x700" )

        canvas=Canvas(window , width=1300 , height=700 ,bg="black")
        canvas.pack()

        bg=PhotoImage(file="C:\\Users\\USER\\Desktop\\millionaire\\ex_form.png")
        canvas.create_image(0 , 0, anchor= NW, image= bg)

        frame=Frame(window , bg="black").place(x=1200  ,y =700)

        label=Label(frame, text="  Login Account ", fg="black" , bg="#7D7524", font="Verdana 18 bold").place(x= 950 ,y = 200)
       
        email=Label(frame, text="  Email Address ", fg="black" , bg="#7D7524", font="time 12 ").place(x= 900 ,y = 350)
        password=Label(frame, text=" Password  ", fg="black" , bg="#7D7524", font="time 12 ").place(x= 900 ,y = 400)

        em=Entry(frame, bg="#7D7524", fg="black", font="time 12").place(x=1030, y=350)
        p=Entry(frame, bg="#7D7524", fg="black", font="time 12" , show="*").place(x=1030, y=400)
        
        btn=Button(frame , text="   Signup    ", bg="#ed2a51", font="time 16", command=main_menu.menu).place(x=1020 ,y = 500)

        window.mainloop()
