# Copyright Rubel Shakh
from tkinter import *
import tkinter 
import time
from tkinter import messagebox
# This software is all about personal use, anyone can use.
# I recommended everyone to use the app, it will help you to remember for taking break between your work.
# Long time nonstop work can cause serious issue on your health
# exe file link is here >>> 
class dearFreelancer:
    def __init__(self, root):
        self.root = root        
        self.root.title("Dear Freelancer - Love Your Health")
        self.root.geometry("400x320+950+100")
        self.root.configure(bg="#ffffff")
        self.userTime = IntVar()
        self.counterFun()
        self.userInputLabel = Label(text='কত সময় পর ব্রেক নিতে চাচ্ছেন?', fg='#3ae374',bg='white', font=('raleway',15,'bold'))
        self.userInputLabel.place(x=50,y=100)
        self.userInput = Entry(textvariable = self.userTime,width=5, bg='#3ae374', fg='white', font=('raleway',20,'bold'))
        self.userInput.place(x=120,y=135)
        self.minute = Label(text = 'মিনিট',width=5, bg='white', fg='#3ae374', font=('raleway',18,'bold'))
        self.minute.place(x=180,y=135)
        self.startButton = Button(text="START",command=lambda: self.counter(), width=50, height=2, bg="#3ae374", fg="white",font=('raleway',10,'bold'))
        self.startButton.place(y=250)
        self.powerdBy = Label(root,text='Powered by Runi Digital', bg='#ffffff', font=('raleway',9)).place(x = 130, y=295)

    def counterFun(self):    
        self.timeCount2 = Label(root,text = "Current Time: {}".format(time.strftime("%H:%M:%S")),fg="#3ae374",bg="white", font=('raleway',20,'bold'))
        self.timeCount2.place(x = 50,y = 0)
        self.root.after(1000, self.counterFun)

    count = 0
    def counter(self):
        if self.userTime.get() > 0:
            self.startedText = Label(text="Started",bg="yellow", fg="red",font=('raleway',15,'bold'))
            self.startedText.place(x=150,y=200)
            global count
            self.count += 1
            self.timeCounts = Label(text = str(self.count),bg="white",fg="white", font=('raleway',20,'bold'))
            self.timeCounts.place(x = 50,y = 30)
            self.root.after(1000, self.counter)
            self.b = self.userTime.get()
            if self.count == self.b*60:
                self.second = Tk()
                self.second.title("Dear Freelancer - Love Your Health (Times UP)")
                self.second.geometry('1200x700+0+100')
                self.timesUp = Label(self.second,text="Times UP!", font=('raleway',35,'bold'), bg='white')
                self.timesUp.place(x=250, y=200)
                self.standUp = Label(self.second,text="1. Stand up and walk for 2 minutes", font=('raleway',30), bg='white')
                self.standUp.place(x=250, y=260)
                self.eyesText = Label(self.second,text="2. Close Your eyes 10 times", font=('raleway',30),bg='white')
                self.eyesText.place(x=250, y=320)
                self.startAgain = Label(self.second,text="3. Start me AGAIN! ", font=('raleway',30),bg='white')
                self.startAgain.place(x=250, y=380)
                self.smileEmoji = Label(self.second,text="  😊", font=('raleway',30),bg='white',fg='green')
                self.smileEmoji.place(x=600 ,y=370)
                self.dearFriend = Label(self.second,text="Dear Friend Love Your Health First", font=('raleway',22,'bold'), bg='white',fg='#3ae374')
                self.dearFriend.place(x=250, y=450)
                self.email = Label(self.second,text="if you find it good for you then you can say thanks here:    igrubel@protonmail.com", font=('raleway',13), bg='white')
                self.email.place(x=250, y=600)
                self.second.attributes('-topmost', True)
                self.second.configure(bg="#ffffff")
                self.root.destroy()
        else:
            messagebox.showwarning(title='Value Error', message='Time should be more than Zero')

if __name__ == "__main__":
    root = Tk()
    application = dearFreelancer(root)
    root.mainloop()


# END OF THE PROGRAM
# All right reserved (Runi Digital and Rubel Shakh)
