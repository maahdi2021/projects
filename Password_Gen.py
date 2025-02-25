from tkinter import *
import random
def main():
    
    root = Tk()
    #root.geometry('700x600')

    passwordNum = Label(root, text = "Please enter desired number of Passwords to generate")
    passwrodlength = Label(root, text = "Please enter desired password length")

    passwordNum.grid(column=0, row=0)
    passwrodlength.grid(column=0, row=3)

    spin = Spinbox(root, from_=0, to=20,width=5)
    spin1 = Spinbox(root, from_=0,to=20,width=5)

    spin.grid(column=0,row=1)
    spin1.grid(column=0,row=4)

    chars = "abcdefgijklmnopqrstuvwxyzABCDEFGIJKLMNOPQRSTUVWXYZ1234567890!@#$%&"

    def clicked():
        i = 0
        t.delete("1.0",END)
        while i < int(spin.get()):
            password = ""
            while len(password) < int(spin1.get()):
                password += chars[random.randint(0,len(chars)-1)]
            
            t.insert(INSERT, "Password " + str(i + 1) + " : " + password + "\n")
            i += 1
    btn = Button(root, text = "Generate",command=clicked)

    btn.grid(column=0,row=5)

    t = Text(root,height=15,width=30)
    t.grid(column=0,row=7)
    root.title("Random Password Genarator")



    #main loop

    root.mainloop()

if __name__ == "__main__":
    main()