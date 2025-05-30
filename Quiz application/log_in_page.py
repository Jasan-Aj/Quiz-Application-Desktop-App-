import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

def login(tab,notebook,entry_page,sign_up,database,home,admin,path):
    main_frame = ctk.CTkFrame(tab,fg_color= "#0A082D",corner_radius=0)
    main_frame.pack(fill="both",expand = True)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=1)
    main_frame.columnconfigure(0,weight=1)

    image_path4 = path('images/back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path4),size=(32,32))

    user_id = tk.StringVar(value=None)

    ctk.CTkButton(main_frame,text="",command=lambda:notebook.select(entry_page),image=tab.back,height=43,
                  fg_color="aqua",width=40,corner_radius=25).grid(row=0,column=0,sticky="w",padx=20,pady=20)

    sub_frame = ctk.CTkFrame(main_frame,fg_color= "#0A082D",border_color="#BAD5CC",
                             border_width=2)
    sub_frame.grid(row=1,column=0)

    def validate():
        if email.get()=="" or password.get()=="":
            messagebox.showwarning(title="WARNING", message="Fill All Required Feilds!")

        else:
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select password from user_logins where email=?",(email.get(),))
            res = cursor.fetchone()
            connection.close()

            if email.get()=="admin" and password.get()=="admin123":
                notebook.select(admin)

            elif res == None:
                messagebox.showwarning(title="WARNING", message="Incorrect Email or password!")

            elif res[0] == password.get():
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("select user_id from user_logins where email=?",(email.get(),))
                user_fetch = cursor.fetchone()
                user_id.set(user_fetch[0])
                connection.close()
                notebook.select(home)
                
            else:
                messagebox.showwarning(title="WARNING", message="Incorrect Email or password!")
                
                


    ctk.CTkLabel(sub_frame,text = "LOG IN",font=("calibri",22,"bold"),text_color="white").grid(row=0,column=0,sticky="w",padx=40,pady=10)

    frame1 = ctk.CTkFrame(sub_frame,fg_color="#0A082D")
    frame1.grid(row=1,column=0,columnspan=2,pady=20,padx=5)
    email = ctk.CTkEntry(frame1,width=300,height=35,fg_color = "#2c344d",font=("calibri",18),
                       placeholder_text_color = "white",
                       border_color="#2E3756",border_width = 2,corner_radius=5,text_color="white")
    email.grid(row=1,column=0,padx=20)
    ctk.CTkLabel(frame1,text = "EMAIL",font=("calibri",17,"bold"),text_color="white").grid(row=2,column=0,sticky="w",padx=20)

    frame2 = ctk.CTkFrame(sub_frame,fg_color="#0A082D")
    frame2.grid(row=2,column=0,columnspan=2,pady=20,padx=20)
    password = ctk.CTkEntry(frame2,width=300,height=35,fg_color = "#2c344d",font=("calibri",18),
                       border_color="#2E3756",border_width = 2,corner_radius=5,text_color="white")
    password.grid(row=0,column=0,padx=20)
    ctk.CTkLabel(frame2,text = "PASSWORD",font=("calibri",17,"bold"),text_color="white").grid(row=1,column=0,sticky="w",padx=20)


    ctk.CTkButton(sub_frame,text = "LOGIN",width=260,font = ("calibri",20,"bold"),text_color="#0A082D",
                  fg_color="#BAD5CC",border_color="#58637f",border_width = 2,command=validate,
                  height=50,corner_radius = 8).grid(row=4,column=0,columnspan=2,pady=15)

    ctk.CTkLabel(sub_frame,text = "Don't have an account?",font=("calibri",18),fg_color="#0A082D",text_color="white").grid(row=5,column=0,pady=15,sticky="e")
    ctk.CTkButton(sub_frame,text = "Signup Now",hover_color="#0A082D",command=lambda:notebook.select(sign_up),font=("calibri",18,"bold"),fg_color="#0A082D",text_color="skyblue").grid(row=5,column=1,sticky="w",padx=10)

    return user_id
