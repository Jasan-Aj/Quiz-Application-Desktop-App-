import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import random
from functools import partial
import sqlite3
from tkinter import messagebox


def manage_users(tab,notebook,path,database,admin_panel):

    main_frame = ctk.CTkFrame(tab,fg_color="white")
    main_frame.pack(fill="both",expand = True)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=1)
    main_frame.columnconfigure(0,weight=1)

    nav = ctk.CTkFrame(main_frame,fg_color="#0A082D",corner_radius=0)
    nav.grid(row=0,column=0,sticky="nsew")

    nav.columnconfigure(0,weight=1)
    nav.columnconfigure(1,weight=1)
    nav.columnconfigure(2,weight=1)
    nav.rowconfigure(2,weight=1)

    def remove(user_id):

        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("delete from user_names where user_id = ?",(user_id,))
        cursor.execute("delete from user_logins where user_id = ?",(user_id,))
        cursor.execute("delete from python_score where user_id = ?",(user_id,))
        cursor.execute("delete from java_score where user_id = ?",(user_id,))
        cursor.execute("delete from internet_tech_score where user_id = ?",(user_id,))
        cursor.execute("delete from information_system_score where user_id = ?",(user_id,))
        cursor.execute("delete from accounting_score where user_id = ?",(user_id,))
        connection.commit()
        connection.close()
        run()

    image_path4 = path('images/back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path4),size=(32,32))

    ctk.CTkLabel(nav,text="MANAGE USERS",font=("impact",35),text_color="white").grid(row=0,column=1,pady=10)
    ctk.CTkButton(nav,text="",image=tab.back,height=43,fg_color="aqua",command=lambda:notebook.select(admin_panel),
                  width=40,corner_radius=25).grid(row=0,column=0,sticky="w",padx=15)
    
    def run():

        body=ctk.CTkScrollableFrame(main_frame,fg_color="#EAEAEA")
        body.grid(row=1,column=0,sticky="nswe")
        body.columnconfigure(0,weight=1)

        user_frames = ctk.CTkFrame(body,fg_color="#2A3650",corner_radius=10)
        user_frames.pack(fill="both",pady=15)
        user_frames.columnconfigure(0,weight=1)
        user_frames.columnconfigure(1,weight=2)
        user_frames.columnconfigure(2,weight=1)
            
        ctk.CTkLabel(user_frames,text="User Id",height=45,fg_color="#2A3650",
                        text_color="white",font=("roboto",19,"bold"),corner_radius=15).grid(row=0,column=0,sticky="w",padx=50,pady=3)
        ctk.CTkLabel(user_frames,text="Username",height=45,fg_color="#2A3650",
                        text_color="white",font=("roboto",19,"bold"),corner_radius=15).grid(row=0,column=1,sticky="w",padx=300)
        ctk.CTkLabel(user_frames,text="",height=45,fg_color="#2A3650",
                        text_color="white",font=("roboto",19,"bold"),corner_radius=15).grid(row=0,column=2,sticky="w")

        lst = []
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("select user_id from user_names")
        res = cursor.fetchall()
       
    
        for i in res:
            lst.append(i[0])
        connection.close()

        for i in lst:
            user_frames = ctk.CTkFrame(body,fg_color="white",corner_radius=10)
            user_frames.pack(fill="both",pady=20)
            user_frames.columnconfigure(0,weight=1)
            user_frames.columnconfigure(1,weight=5)
            user_frames.columnconfigure(2,weight=1)

            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select user_name from user_names where user_id = ?",(i,))
            result = cursor.fetchone()
            connection.close()
            
                        
            ctk.CTkLabel(user_frames,text=i,
                            text_color="black",font=("roboto",20,"bold"),fg_color="white").grid(row=0,column=0,sticky="w",padx=90)
            ctk.CTkLabel(user_frames,text=result,text_color="black",
                            font=("roboto",20,"bold"),wraplength=750,fg_color="white").grid(row=0,column=1,sticky="we",pady=12)
            ctk.CTkButton(user_frames,text="Remove",fg_color="#DB0A41",height=35,command=partial(remove,i),
                            text_color="white",font=("roboto",18,"bold")).grid(row=0,column=2,sticky="e",padx=90)
    return run
