from tkinter import *
from random import choice

wind=Tk()
wind.title("Random Password Generator")
wind.configure(bg="skyblue")
wind.geometry("400x300")

def password(n):

    text2.delete("1.0",END)

    captial_letter=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    small_letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers=["0","1","2","3","4","5","6","7","8","9"]
    special_characters=['~', '`', '!', ' ', '@', '#', '$', '%', '^', '&', '*','"', '(', ')', '_', '-', '+', '=', '{', '[','}', ']', '|', '\\', ':', ';', "'", '<', 
                        ',','>', '.', '?', '/']

    n=int(n)

    if(n<8):
        result="Plz enter password length greater than or equal to 8."
    elif(n>40):
        result="Please enter password length less than or equal to 40."
    else:
        l=[]
        result=""

        l.append(choice(captial_letter))
        l.append(choice(small_letter))
        l.append(choice(numbers))
        l.append(choice(special_characters))

        while(len(l)>0):
            i=choice(l)
            result+=i
            l.remove(i)

        l=captial_letter+small_letter+numbers+special_characters

        for i in range(n-4):
            result+=choice(l)

    text2.insert("1.0",result)

def reset():
    text1.delete("1.0",END)
    text2.delete("1.0",END)

label1=Label(master=wind,text="Enter the length of the password:",bg="skyblue",font=("Times", "12", "bold italic"))
label1.place(x=15,y=10)

text1=Text(master=wind,height=1,width=45,bd=4,font=("Times", "12", "bold italic"),relief="raised")
text1.place(x=15,y=48)

button1=Button(master=wind,text="Get Password",font=("Times", "10", "bold italic"),relief="raised",bg="lightgreen",command=lambda:password(text1.get("1.0",END)))
button1.place(x=155,y=100)

label2=Label(master=wind,text="Your Password:",bg="skyblue",font=("Times", "12", "bold italic"))
label2.place(x=15,y=140)

text2=Text(master=wind,height=1,width=45,bd=4,font=("Times", "12", "bold italic"),relief="raised")
text2.place(x=15,y=185)

button1=Button(master=wind,text="  RESET  ",font=("Times", "10", "bold italic"),bg="orange",relief="raised",command=lambda:reset())
button1.place(x=170,y=240)

reset()

wind.mainloop()