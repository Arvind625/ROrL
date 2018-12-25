from tkinter import *
import tkinter
from tkinter import messagebox
import sqlite3 
win = Tk()
win.geometry("500x1000")
win.title("Login/SignUp")
win.configure(background='pink')


def insertData(values):
  status = 0

  try : 
    conn = sqlite3.connect( 'registration')
    conn.execute("create table if not exists Logindata(name varchar(80) not null,username varchar(80) not null unique,password not null)")
    conn.commit()
    conn.execute("insert into Logindata values(?,?,?)",values)
    conn.commit()
  except IntegrityError:
    return 0
  finally:
    status = conn.total_changes
    conn.close()
    return status

def searchData(values):
  conn = sqlite3.connect( 'registration')
  crsr = conn.cursor()
  crsr.execute("select * from Logindata where username = ? and password = ?",values)
  return crsr.fetchall()
  
def register():
  win2 = Tk()
  win2.geometry("500x500")
  win2.title("Registration")
  win2.configure(background="pink")
  Label(win2,text = "Welcom to Registration Page").grid(row = 0,column=1)
  Label(win2,text = "Name : ").grid(row =2)
  Label(win2,text = "User Name : ").grid(row = 4)
  Label(win2,text = "Password : ").grid(row = 6)

  e1 = Entry(win2)
  e2 = Entry(win2)
  e3 = Entry(win2,show="*")

  e1.grid(row=2,column = 1)
  e2.grid(row=4,column = 1)
  e3.grid(row = 6,column = 1)
 
  def temp1():
    values = (e1.get(),e2.get(),e3.get())
    status = insertData(values)
    if status > 0:
      tkinter.messagebox.showinfo("Done"," Sucessfully Resgistered ! ")
      win2.destroy()
    else:
      tkinter.messagebox.showwarning("Not Registered "," Not Regestered Due to : 1.Username Already Exist \n 2.Weak Password ")
 
  b1 = Button(win2,text="Register",command = temp1)
  b1.grid(row = 8 ,column = 1)
  
Label(win,text = "Login or SignUp",fg="red",bg="white").grid(row=0,column=1)
Label(win,text = "username : ",fg="red",bg="white").grid(row = 2)
Label(win,text = "password : ",fg="red",bg="white").grid(row = 4)
e1 = Entry(win)
e2 = Entry(win,show = "*")
e1.grid(row = 2,column = 1)
e2.grid(row = 4,column = 1)

def temp():
  if not e1.get()  or not  e2.get():
    tkinter.messagebox.showwarning("Not Login","One of the Credential is Blank")
  else:  
    values = (e1.get(),e2.get())
    usr = searchData(values)
    if not usr:
      tkinter.messagebox.showwarning("Not Login","Invalid Credentials")
    else:
      win3 = Tk()
      win3.geometry("500x500")
      win.destroy()
      win3.title("Welcome")
      win3.configure(background='pink')
      Label(win3,text = "Welcome : "+usr[0][0],fg="red",bg="white").grid(row = 3,column = 3,padx=150,pady=150)

b2 = Button(win,text = "Login",fg="red",bg="white",command = temp)
b2.grid(row = 6,column = 1)
b3 = Button(win,text ="New User! Sign Up ",command=register,fg="red",bg="white")

b3.grid(row = 7,column = 1, pady = 5)

win.mainloop()