from tkinter import *
root = Tk()
root.geometry("455x500")
root.title("Calculator by Rathi")
root.wm_iconbitmap("1.ico")

value = StringVar()
value.set("")   #Here we add a blank value to the "value" variable
screen = Entry(root, textvariable=value, font="lucida 20 italic")
screen.pack(fill=X, ipadx=12, padx=10, pady=12)   #"ipadx or ipady gives internal padding or spacing"


#def Number9():
    #print("9")
    

#def Number8():
    #print("8")

#def Number7():
    #print("7")


    #or

def click(event):   #Jab bhi hum button ko bind karte h tab define karte samay command mein "event" likhna compulsory h
    global value
    text_variable = event.widget.cget("text")         #"event.widget" hume vo button de dega jispe click hua h   #".cget("text")" hume button widget se text nikal ke de dega
    #print(text_variable)
    #value.set(value.get() + text_variable)
    #screen.update()
    
    if text_variable == "=":
        if value.get().isdigit():
            make_it = int(value.get())   #Here we typecast it into integer value and then print it
            #value.set(make_it)
            #screen.update()
            #print(screen.get())

        else:
            try:
                make_it = eval(screen.get())     #"eval" means evaluate. Hence it evaluates the result

            except Exception as e:
                print(e)
                make_it = "Error!"
                
        value.set(make_it)   #Hum "value.set()" ki jagah "print()" nhi likh sakte kyuki print func terminal m print karega naki gui main
        screen.update()

    elif text_variable == "c":
        value.set("")
        screen.update()

    elif text_variable == "2/0":
        value.set("Not Defined!")
        screen.update()

    else:
        value.set(value.get() + text_variable)
        screen.update()

f1 = Frame(root, bg="grey")
f1.pack()
b1 = Button(f1, text="9", font="lucida 19 italic")
b1.pack(side=LEFT, ipady=10, fill=X)
b1.bind("<Button-1>", click)

b2 = Button(f1, text="8", font="lucida 19 italic")
b2.pack(side=LEFT, ipady=10)
b2.bind("<Button-1>", click)

b3 = Button(f1, text="7", font="lucida 19 italic")
b3.pack(side=LEFT, ipady=10)
b3.bind("<Button-1>", click)

f1 = Frame(root, bg="grey")
f1.pack()
b4 = Button(f1, text="6", font="lucida 19 italic")
b4.pack(side=LEFT, ipady=10)
b4.bind("<Button-1>", click)

b5 = Button(f1, text="5", font="lucida 19 italic")
b5.pack(side=LEFT, ipady=10)
b5.bind("<Button-1>", click)

b6 = Button(f1, text="4", font="lucida 19 italic")
b6.pack(side=LEFT, ipady=10)
b6.bind("<Button-1>", click)

f1 = Frame(root, bg="grey")
f1.pack()
b7 = Button(f1, text="3", font="lucida 19 italic")
b7.pack(side=LEFT, ipady=10)
b7.bind("<Button-1>", click)

b8 = Button(f1, text="2", font="lucida 19 italic")
b8.pack(side=LEFT, ipady=10)
b8.bind("<Button-1>", click)

b9 = Button(f1, text="1", font="lucida 19 italic")
b9.pack(side=LEFT, ipady=10)
b9.bind("<Button-1>", click)

f1 = Frame(root, bg="grey")
f1.pack()
b10 = Button(f1, text="0", font="lucida 19 italic")
b10.pack(side=LEFT, ipady=10)
b10.bind("<Button-1>", click)

b11 = Button(f1, text="=", font="lucida 19 italic")
b11.pack(side=LEFT, ipady=10)
b11.bind("<Button-1>", click)

b12 = Button(f1, text="c", font="lucida 19 italic")
b12.pack(side=LEFT, ipady=10)
b12.bind("<Button-1>", click)

f1 = Frame(root, bg="grey")
f1.pack()
b13 = Button(f1, text="+", font="lucida 19 italic")
b13.pack(side=LEFT, ipady=10)
b13.bind("<Button-1>", click)

b14 = Button(f1, text="-", font="lucida 19 italic")
b14.pack(side=LEFT, ipadx=5, ipady=10)
b14.bind("<Button-1>", click)

b15 = Button(f1, text="*", font="lucida 19 italic")
b15.pack(side=LEFT, ipady=10)
b15.bind("<Button-1>", click)

f1 = Frame(root, bg="grey")
f1.pack()
b16 = Button(f1, text="/", font="lucida 19 italic")
b16.pack(side=LEFT, ipadx=12, ipady=10)
b16.bind("<Button-1>", click)

b17 = Button(f1, text="%", font="lucida 19 italic")
b17.pack(side=LEFT, ipadx=6, ipady=10)
b17.bind("<Button-1>", click)



root.mainloop()