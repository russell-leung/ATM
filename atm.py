from tkinter import *
import sqlite3

#GUI version (Graphical user interface via tkinter)


#Account creation functions

#Takes the information from the previous registration forms and adds them to an account if the account is avaliable
def register_account3(username, password, password_check, first_name, last_name, age):
  
  #Takes the informaion the user enters and makes it into a variable
  first_name_info = first_name.get().capitalize()
  last_name_info = last_name.get().capitalize()
  age_info = int(age.get()) 
  username_info = username.get()
  password_info = password.get()
  password_check_info = password_check.get()

  #Checks to see if username is already in database, if not it will allow user to proceed, if it is there it will halt the registartion process
  valid_account = data.execute("SELECT username FROM bank WHERE username=?", (username_info,)).fetchone()

  if valid_account != None:
    registration_success = Label(screen1_2, text = "Your registration\n was unsuccessful,\n your chosen username\n is already in use!", width = 20, height = 10, fg = "red").place(x = 290, y = 60)

    user_username.delete(0, END)
    user_password.delete(0, END)
    user_password_check.delete(0, END)

    return

  if password_info == password_check_info:

    #If password isn't 4 digits it will fail
    if len(str(password_info)) != 4:
      registration_success = Label(screen1_2, text = "Your registration\n was unsuccessful,\n your chosen password\n is not 4 digits!", width = 20, height = 10, fg = "red").place(x = 290, y = 60)

      user_username.delete(0, END)
      user_password.delete(0, END)
      user_password_check.delete(0, END)

      return

    #Inserts user data into database and tells the user it was completed successfully
    data.execute("INSERT INTO bank (username, password, money, first_name, last_name, age) VALUES (?, ?, ?, ?, ?, ?)", (username_info, password_info, 0, first_name_info, last_name_info, age_info))

    data_base.commit()

    registration_success = Label(screen1_2, text = f"Your registration was\n successfully created!\nUsername: {username_info}\nPassword: {password_info}", width = 20, height = 10, fg = "green").place(x = 290, y = 60)

    user_username.delete(0, END)
    user_password.delete(0, END)
    user_password_check.delete(0, END)

    return
    
  #Won't register account if the two passwords the user eneters aren't the same
  if password_info != password_check_info:
    registration_success = Label(screen1_2, text = "Your registration was\n unsuccessful, your passwords\n did not match!", width = 20, height = 10, fg = "red").place(x = 290, y = 60)

    user_username.delete(0, END)
    user_password.delete(0, END)
    user_password_check.delete(0, END)

    return

#2nd page of registration prompt user to make a username and password and register
def register_account2(first_name, last_name, age):
  
  global user_username 
  global user_password 
  global user_password_check
  global screen1_2

  #Screen 1.2, screen 1 is register, this is the second page of registration
  screen1_2 = Toplevel(screen1_1)
  screen1_2.geometry("500x500")
  screen1_2.title("Russell's bank")
  title = Label(screen1_2, text="Account Creation", bg = "grey", width = "500", height = "3").pack()


  #Username creation:
  username = StringVar()
  username_text = Label(screen1_2, text = "Create your desired username:")
  user_username = Entry(screen1_2, textvariable = username, width = "30")
  
  username_text.place(x = 15, y = 70)
  user_username.place(x = 15, y = 100)

  #Password creation:
  password = StringVar()
  password_text = Label(screen1_2, text = "Create your 4 digit password:")
  user_password = Entry(screen1_2, textvariable = password, width = "30")
  
  password_text.place(x = 15, y = 135)
  user_password.place(x = 15, y = 165)

  #Password verify:
  password_check = StringVar()
  password_check_text = Label(screen1_2, text = "Enter your 4 digit password again:")
  user_password_check = Entry(screen1_2, textvariable = password_check, width = "30")
  
  password_check_text.place(x = 15, y = 200)
  user_password_check.place(x = 15, y = 230)

  #Button to register account, calls register_account3
  Button(screen1_2, text = "Press to Register your Account", width = "30", height = "2", command = lambda: register_account3(username, password, password_check, first_name, last_name, age)).place(x = 15, y = 265)

  #Button to go back to main screen
  Button(screen1_2, text = "Press to Return to the Home Screen", width = "30", height = "2", command =  lambda: [screen1_1.destroy(), screen1_2.destroy()]).place(x = 15, y = 330)


#First page of registration asks user for their name and age
def register_account1():

  global user_first_name
  global user_last_name
  global user_age
  global screen1_1

  #Screen 1.1, registration page 1
  screen1_1 = Toplevel(screen)
  screen1_1.geometry("500x500")
  screen1_1.title("Russell's bank")
  title = Label(screen1_1, text="Account Creation", bg = "grey", width = "500", height = "3").pack()


  #Firstname:
  first_name = StringVar()
  first_name_text = Label(screen1_1, text = "Enter your first name:")
  user_first_name = Entry(screen1_1, textvariable = first_name, width = "30")
  
  first_name_text.place(x = 110, y = 70)
  user_first_name.place(x = 110, y = 100)

  #Last name:
  last_name = StringVar()
  last_name_text = Label(screen1_1, text = "Enter your last name:")
  user_last_name = Entry(screen1_1, textvariable = last_name, width = "30")
  
  last_name_text.place(x = 110, y = 135)
  user_last_name.place(x = 110, y = 165)

  #Age:
  age = StringVar()
  age_text = Label(screen1_1, text = "Enter your age:")
  user_age = Entry(screen1_1, textvariable = age, width = "30")
  
  age_text.place(x = 110, y = 200)
  user_age.place(x = 110, y = 230)

  #Will take user to second page of registration
  Button(screen1_1, text = "Press to Continue", width = "30", height = "2", command = lambda: register_account2(first_name, last_name, age)).place(x = 110, y = 265)

  #Button to go back to main screen
  Button(screen1_1, text = "Press to Return to the Home Screen", width = "30", height = "2", command = screen1_1.destroy).place(x = 110, y = 330)

#User login functions

#Checks the user's balance
def check_balance(username_info, password_info):

  user_money = data.execute("SELECT money FROM bank WHERE username=? AND password=?", (username_info, password_info)).fetchone()

  Label(screen2_1, text = f"Your balance is: ${user_money[0]}", width = 50, height = 2, fg = "red").place(x = 35, y = 345)


#Deposit functions

#Adds the user's deposit to their preexisting balance and adds that new number to the database
def deposit_account(deposit, deposit_check, username_info):

  deposit1 = float(deposit.get())
  deposit_check1 = float(deposit_check.get())

  #Makes sure that the depost is valid and the check is the same
  if deposit1 == deposit_check1:

    original_value = data.execute("SELECT money FROM bank WHERE username =?", (username_info,)).fetchone()

    new_value = round(original_value[0] + deposit1, 2)

    #Updates the database
    data.execute(("UPDATE bank SET money =? WHERE username=?"), (new_value, username_info))

    data_base.commit()

    Label(screen2_1, text = f"Your new balance is: ${new_value}", width = 50, height = 2, fg = "red").place(x = 40, y = 345)

  if deposit1 != deposit_check1:
    Label(screen2_1, text = "Your deposits did not match, no transaction was made.", width = 50, height = 2, fg = "red").place(x = 40, y = 345)


#Prompts user for their deposit amount
def deposit_funds(username_info):
  
  #Screen 2 is login, screen 2.2 is the deposit page
  screen2_2 = Toplevel(screen2_1)
  screen2_2.geometry("500x500")
  screen2_2.title("Russell's bank")

  title = Label(screen2_2, text="Deposit Amount", bg = "grey", width = "500", height = "3")
  title.pack()

  #Deposit:
  deposit = StringVar()
  deposit_text = Label(screen2_2, text = "Enter your  deposit amount:")
  user_deposit = Entry(screen2_2, textvariable = deposit, width = "30")
  
  deposit_text.place(x = 110, y = 70)
  user_deposit.place(x = 110, y = 100)

  #Deposit check:
  deposit_check = StringVar()
  deposit_check_text = Label(screen2_2, text = "Confirm your deposit again:")
  user_deposit_check = Entry(screen2_2, textvariable = deposit_check, width = "30")
  
  deposit_check_text.place(x = 110, y = 135)
  user_deposit_check.place(x = 110, y = 165)

  #Calls the deposit_account function
  Button(screen2_2, text = "Press to Deposit", width = "30", height = "2", command = lambda: [deposit_account(deposit, deposit_check, username_info), screen2_2.destroy()]).place(x = 110, y = 200)

  #Goes back a page
  Button(screen2_2, text = "Press to go Back", width = "30", height = "2", command = screen2_2.destroy).place(x = 110, y = 265)

#Withdraw functions
#Same as deposi functions but they take user's withdraw out of their original balance

def withdraw_account(withdraw, withdraw_check, username_info):

  withdraw1 = float(withdraw.get())
  withdraw_check1 = float(withdraw_check.get())

  if withdraw1 == withdraw_check1:

    original_value = data.execute("SELECT money FROM bank WHERE username =?", (username_info,)).fetchone()

    new_value = round(original_value[0] - withdraw1, 2)

    data.execute(("UPDATE bank SET money =? WHERE username=?"), (new_value, username_info))

    data_base.commit()

    Label(screen2_1, text = f"Your new balance is: ${new_value}", width = 50, height = 2, fg = "red").place(x = 40, y = 345)

  if withdraw1 != withdraw_check1:
    Label(screen2_1, text = "Your withdraws did not match, no transaction was made.", width = 50, height = 2, fg = "red").place(x = 40, y = 345)

def withdraw_funds(username_info):

  #Screen 2.3 is the deposit page
  screen2_3 = Toplevel(screen2_1)
  screen2_3.geometry("500x500")
  screen2_3.title("Russell's bank")

  title = Label(screen2_3, text="Withdraw Amount", bg = "grey", width = "500", height = "3")
  title.pack()

  withdraw = StringVar()
  withdraw_text = Label(screen2_3, text = "Enter your  withdraw amount:")
  user_withdraw = Entry(screen2_3, textvariable = withdraw, width = "30")
  
  withdraw_text.place(x = 110, y = 70)
  user_withdraw.place(x = 110, y = 100)

  withdraw_check = StringVar()
  withdraw_check_text = Label(screen2_3, text = "Confirm your deposit again:")
  user_withdraw_check = Entry(screen2_3, textvariable = withdraw_check, width = "30")
  
  withdraw_check_text.place(x = 110, y = 135)
  user_withdraw_check.place(x = 110, y = 165)


  Button(screen2_3, text = "Press to Withdraw", width = "30", height = "2", command = lambda: [withdraw_account(withdraw, withdraw_check, username_info), screen2_3.destroy()]).place(x = 110, y = 200)

  Button(screen2_3, text = "Press to go Back", width = "30", height = "2", command = screen2_3.destroy).place(x = 110, y = 265)

#Admin account

#Checks the database for bank accounts and displays them to the admin
def admin_user_data():

  #Admin screen 1 is the page where the admin can check the bak data
  admin_screen1 = Toplevel(admin_screen)
  admin_screen1.geometry("500x500")
  admin_screen.title("Russell's bank")

  title = Label(admin_screen1, text="Admin Actions", bg = "grey", width = "500", height = "3")
  title.pack()

  data.execute("SELECT * FROM bank")
  user_data = list(data.fetchall())

  #These for loops dislpay the user data on admi screen 1
  x = 7
  for word in ("Username", "Password", "Balance", "Firstname", "Lastname"):
    Label(admin_screen1, text = word, width = "10", height = "2", fg = "Blue").place(x = x, y = 70)
    x += 100

  y = 110
  for user in user_data:
    x = 7
    for i in user:
      Label(admin_screen1, text = i, width = "10", height = "2").place(x = x, y = y)
      x += 100
    y += 25


  Button(admin_screen1, text = "Press to go Back", width = "30", height = "2", command = admin_screen1.destroy).place(x = 110, y = y + 25)

#Takes admin input from previous page and updates the users accounts
def admin_change_funds(username, balance):

  username_info = username.get()
  balance_info = float(balance.get())

  data.execute("SELECT money FROM bank WHERE username =?", (username_info,))
  change_info = data.fetchone()


  if change_info == None:
    Label(admin_screen, text="The username of password was incorrect", fg = "red").place(x = 160, y =  315)

  if change_info != None:

    #Makes the change in the database and saves it
    data.execute("UPDATE bank SET money =? WHERE username =?", (balance_info, username_info))

    data_base.commit()

    Label(admin_screen, text="Your change was successful", fg = "green").place(x = 160, y =  315)

#Prompts admin to enter the account their changing and their new balance
def admin_change():

  #Admin screen 2 is the change funds screen
  admin_screen2 = Toplevel(admin_screen)
  admin_screen2.geometry("500x500")
  admin_screen2.title("Russell's bank")

  title = Label(admin_screen2, text="Admin Actions", bg = "grey", width = "500", height = "3")
  title.pack()

  #Account username:
  username = StringVar()
  username_text = Label(admin_screen2, text = "Enter the username of the account:")
  user_username = Entry(admin_screen2, textvariable = username, width = "30")
  
  username_text.place(x = 110, y = 70)
  user_username.place(x = 110, y = 100)

  #Their new balance: 
  balance = StringVar()
  balance_text = Label(admin_screen2, text = "Enter their new balance:")
  user_balance = Entry(admin_screen2, textvariable = balance, width = "30")

  balance_text.place(x = 110, y = 135)
  user_balance.place(x = 110, y = 165)


  Button(admin_screen2, text = "Change Funds", width = "30", height = "2", command = lambda: [admin_change_funds(username, balance), admin_screen2.destroy()]).place(x = 110, y = 230)

  Button(admin_screen2, text = "Press to go Back", width = "30", height = "2", command = admin_screen2.destroy).place(x = 110, y = 295)

#Screen with all the potential admin actions
def admin():

  global admin_screen

  #Main admin screen, has the potential actions on it
  admin_screen = Toplevel(screen2)

  admin_screen.geometry("500x500")
  admin_screen.title("Russell's bank")
  
  title = Label(admin_screen, text="Admin Actions", bg = "grey", width = "500", height = "3")
  title.pack()

  #Button to view all the bank's data
  Button(admin_screen, text = "Press to View User Data", width = "30", height = "2", command = admin_user_data).place(x = 110, y = 100)

  #Button to change a user's data
  Button(admin_screen, text = "Press to Change User Balance", width = "30", height = "2", command = admin_change).place(x = 110, y = 165)

  #Button to go back
  Button(admin_screen, text = "Press to go Back", width = "30", height = "2", command = admin_screen.destroy).place(x = 110, y = 230)

  #Button to log out, closes all admin windows
  Button(admin_screen, text = "Press to go Log Out", width = "30", height = "2", command =  lambda: [screen2.destroy(), admin_screen.destroy()]).place(x = 110, y = 295)

#Sees if entered info was a valid account, if so, it opens the new login screen with all te actions, if not it checks for the admin account before stopping
def login(username, password):

  global screen2_1

  username_info = username.get()
  password_info = password.get()

  user_info = data.execute("SELECT username, password FROM bank WHERE username=? AND password=?", (username_info, password_info)).fetchone()

  if user_info == None:

    #If the user enter the admin account info, it calls the admin function
    if username_info == "ADMIN" and password_info == "0000":
      admin()
      return

    Label(screen2, text = "Your login was unsuccessful!\nYour username or password is incorrect!", width = 50, height = 5, fg = "red").place(x = 35, y = 315)

    return

  #If the account if valid:
  if user_info != None:

    #Screen 2.1 is the login options
    screen2_1 = Toplevel(screen2)
    screen2_1.geometry("500x500")
    screen2_1.title("Russell's bank")
  
    title = Label(screen2_1, text="User Actions", bg = "grey", width = "500", height = "3")
    title.pack()

    user_name = data.execute("SELECT first_name, last_name FROM bank WHERE username=? AND password=?", (username_info, password_info)).fetchone()

    #Button to check balance
    Button(screen2_1, text = "Press to Check your Balance", width = "30", height = "2",  command = lambda: [check_balance(username_info, password_info)]).place(x = 110, y = 100)

    #Button to deposit money
    Button(screen2_1, text = "Press to Deposit into your Account", width = "30", height = "2", command = lambda: [deposit_funds(username_info)]).place(x = 110, y = 165)
    
    #Button to withdraw money
    Button(screen2_1, text = "Press to Withdraw from your Account", width = "30", height = "2", command = lambda: [withdraw_funds(username_info)]).place(x = 110, y = 230)

    #Button to close ATM (close the window)
    Button(screen2_1, text = "Press to Logout of your Account", width = "30", height = "2", command =  lambda: [screen2.destroy(), screen2_1.destroy()]).place(x = 110, y = 295)

    Label(screen2_1, text = f"User: {user_name[0]} {user_name[1]}", width = 25, height = 1).place(x = 7, y = 60)

#Prompts user to enter their username and password
def user_login():

  global screen2

  #Screen 2 is the user login screen
  screen2 = Toplevel(screen)
  screen2.geometry("500x500")
  screen2.title("Russell's bank")
  
  title = Label(screen2, text="User Login", bg = "grey", width = "500", height = "3")
  title.pack()

  #Username login
  username = StringVar()
  username_text = Label(screen2, text = "Enter your username:")
  user_username = Entry(screen2, textvariable = username, width = "30")
  
  username_text.place(x = 110, y = 70)
  user_username.place(x = 110, y = 100)

  #Password login:
  password = StringVar()
  password_text = Label(screen2, text = "Enter your 4 digit password:")
  user_password = Entry(screen2, textvariable = password, width = "30")
  
  password_text.place(x = 110, y = 135)
  user_password.place(x = 110, y = 165)

  Button(screen2, text = "Press to Login", width = "30", height = "2", command = lambda: login(username, password)).place(x = 110, y = 200)

  Button(screen2, text = "Press to Return to the Home Screen", width = "30", height = "2", command = screen2.destroy).place(x = 110, y = 265)

#Delete account function, takes user's entered info from previous page and if its vald it deletes the account
def delete(username, password):
  username_info = username.get()
  password_info = password.get()

  user_info = data.execute("SELECT username, password FROM bank WHERE username=? AND password=?", (username_info, password_info)).fetchone()

  if user_info == None:
    Label(screen3, text = "Your login was unsuccessful!\nYour username or password is incorrect!", width = 50, height = 5, fg = "red").place(x = 40, y = 315)

    return

  if user_info != None:

    #Deletes the account
    deleted_account = data.execute(("SELECT username FROM bank WHERE username =? AND password =?"), (username_info, password_info)).fetchone()

    data.execute("DELETE FROM bank WHERE username =?", (deleted_account[0],))

    data_base.commit()

    Label(screen3, text = "Your account was successful deleted!\nYour login is no longer eligable!", width = 50, height = 5, fg = "green").place(x = 40, y = 315)

#Asks user for their username and password so that they can delete their account
def delete_account():

  global screen3

  #Screen 3 is the delete account screen
  screen3 = Toplevel(screen)
  screen3.geometry("500x500")
  screen3.title("Russell's bank")

  title = Label(screen3, text="Delete Account", bg = "grey", width = "500", height = "3")
  title.pack()
  
  #Username login:
  username = StringVar()
  username_text = Label(screen3, text = "Enter your  username:")
  user_username = Entry(screen3, textvariable = username, width = "30")
  
  username_text.place(x = 110, y = 70)
  user_username.place(x = 110, y = 100)

  #Password login:
  password = StringVar()
  password_text = Label(screen3, text = "Enter your 4 digit password:")
  user_password = Entry(screen3, textvariable = password, width = "30")
  
  password_text.place(x = 110, y = 135)
  user_password.place(x = 110, y = 165)

  #Button to delete account
  Button(screen3, text = "Press to Delete Account", width = "30", height = "2", command =  lambda: [delete(username, password)]).place(x = 110, y = 200)

  Button(screen3, text = "Press to Return to the Home Screen", width = "30", height = "2", command = screen3.destroy).place(x = 110, y = 265)


#MAIN

global screen

#Set up database
data_base = sqlite3.connect("Bank_Data.db")
data = data_base.cursor()
# data.execute("Create TABLE bank(username TEXT, password TEXT, money FLOAT, first_name STRING, last_name STRING, age INTEGER)")

#Main screen
screen = Tk()
screen.geometry("500x500")
screen.title("Russell's bank")
title = Label(text="Russell's bank", bg = "grey", width = "500", height = "3")
title.pack()


#Button to create account, calls account_creation
Button(screen, text = "Press to Create an Account", width = "30", height = "2", command = register_account1).place(x = 110, y = 100)

#Button to login, calls user_login
Button(screen, text = "Press to Login to your Account", width = "30", height = "2", command = user_login).place(x = 110, y = 165)

#Button to delete user's account, calls delete_account
Button(screen, text = "Press to Delete your Account", width = "30", height = "2", command = delete_account).place(x = 110, y = 230)

#Button to close ATM (close the window)
Button(screen, text = "Press to Close the ATM", width = "30", height = "2", command = lambda: [screen.destroy(),data_base.close()]).place(x = 110, y = 295)