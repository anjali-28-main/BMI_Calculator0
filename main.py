from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

root=Tk()
root.title('BMI CALCULATOR')
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")

def BMI():
    h=float(Height.get())
    w=float(Weight.get())
    m=h/100
    bmi=round(float(w/m**2),1)
    print(bmi)
    label1.config(text=bmi)

    if bmi<=18.5:
        label2.config(text="Underwight")
        label3.config(text="you hae lower weight than normal body")

    elif bmi>=18.5 and bmi<=25:
        label2.config(text="Normal")
        label3.config(text="you hare healthy")

    elif bmi>=25 and bmi<=30:
        label2.config(text="Overwight")
        label3.config(text="you hae slightly greater weight than normal body")

    else:
        label2.config(text="Obese!")
        label3.config(text="health at risk")
        
    
image1=PhotoImage(file="C://Users//sweety//Desktop//BMI_Calculator//images//final.png")
root.iconphoto(False,image1)

top=PhotoImage(file="C://Users//sweety//Desktop//BMI_Calculator//images//bmi2.png")
top_label=Label(root,image=top,background="#f0f1f5")
top_label.place(x=70,y=-10)

Label(root,width=72,height=18,bg="lightblue").pack(side=BOTTOM)

box=PhotoImage(file="C://Users//sweety//Desktop//BMI_Calculator//images//box1.png")
Label(root,image=box).place(x=40,y=150)
Label(root,image=box).place(x=260,y=150)

scale=PhotoImage(file="C://Users//sweety//Desktop//BMI_Calculator//images//manscale.png")
Label(root,image=scale,bg="lightblue").place(x=20,y=310,height=270,width=150)

############SLIDER1#################
current_value=tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())

#command tp change style
style=ttk.Style()
style.configure("TScale",background="white")
slider=ttk.Scale(root,from_=0,to=220,orient="horizontal",style="TScale",command=slider_changed,variable=current_value)
slider.place(x=75,y=250)
####################################
##############SLIDER2###############
current_value2=tk.DoubleVar()
def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

#command tp change style
style2=ttk.Style()
style2.configure("TScale",background="white")
slider2=ttk.Scale(root,from_=0,to=200,orient="horizontal",style="TScale",command=slider_changed2,variable=current_value2)
slider2.place(x=290,y=250)

#####################################

Height=StringVar()
Weight=StringVar()
height=Entry(root,textvariable=Height,width=3,font="arial 50",fg="#000",bg="#fff",bd=0,justify=CENTER)
height.place(x=66,y=165)
Height.set(get_current_value())

weight=Entry(root,textvariable=Weight,width=3,font="arial 50",bg="#fff",fg="#000",bd=0,justify=CENTER)
weight.place(x=286,y=165)
Weight.set(get_current_value2())

Button(root,text="View Report",width=15,height=2,font="arial 10 bold",bg="#1f6e68",fg="white",command=BMI).place(x=290,y=340)
label1=Label(root,font="arial 60 bold",bg="lightblue",fg="#fff")
label1.place(x=200,y=305)

label2=Label(root,font="arial 20 bold",bg="lightblue",fg="#3b3a3a")
label2.place(x=280,y=430)

label3=Label(root,font="arial 10 bold",bg="lightblue")
label3.place(x=200,y=500)

root.mainloop()
