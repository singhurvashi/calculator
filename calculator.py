from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                scvalue.set("Error")
                screen.update()
                
        scvalue.set(value)
        screen.update()


        
    elif text== "C":
        
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() +text)
        screen.update()
root =Tk()
root.geometry("280x570")
root.title("URVASHI'S CALCULATOR")
               
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucie 40 bold",bd=30,insertwidth=4,bg="powder blue",justify="right")
screen.pack(fill=X,ipadx=8,pady=5,padx=5)

f1=Frame(root,bg="black")
b=Button(f1,text="9",padx=5, fg="black",pady=5,font="lucida 25 bold",relief=SUNKEN,bg="pink")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="8",padx=5, pady=5,font="lucida 25 bold",bg="pink")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="7",padx=5, pady=5,font="lucida 25 bold",bg="pink")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="+",padx=5, pady=5,font="lucida 25 bold",bg="pink")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

f1.pack()

f1=Frame(root,bg="black")
b=Button(f1,text="6",padx=5, pady=5,font="lucida 25 bold",bg="powder blue")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="5",padx=7, pady=5,font="lucida 25 bold",bg="powder blue")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="4",padx=5, pady=5,font="lucida 25 bold",bg="powder blue")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="-",padx=9, pady=9,font="lucida 25 bold",bg="powder blue")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)

f1.pack()

f1=Frame(root,bg="black")
b=Button(f1,text="3",padx=7, pady=5,font="lucida 25 bold",bg="pink")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="2",padx=7, pady=5,font="lucida 25 bold",bg="pink")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="1",padx=7, pady=5,font="lucida 25 bold",bg="pink")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="*",padx=5, pady=5,font="lucida 25 bold",bg="pink")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f1.pack()



f1=Frame(root,bg="black")
b=Button(f1,text=".",padx=7, pady=5,font="lucida 25 bold",bg="powder blue")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="0",padx=7, pady=5,font="lucida 25 bold",bg="powder blue")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="%",padx=7, pady=5,font="lucida 25 bold",bg="powder blue")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="/",padx=7, pady=5,font="lucida 25 bold",bg="powder blue")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="black")
b=Button(f1,text="00",padx=7, pady=5,font="lucida 25 bold",bg="pink")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="=",padx=7, pady=5,font="lucida 25 bold",bg="pink")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f1,text="C",padx=25, pady=5,font="lucida 25 bold",bg="pink")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
f1.pack()













root.mainloop()
