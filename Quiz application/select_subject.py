import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3


def select_sub(tab,notebook,slect_level,path,home,database,user_id):
    main_frame = ctk.CTkFrame(tab,fg_color= "#0A082D")
    main_frame.pack(fill="both",expand = True)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=1)

    main_frame.columnconfigure(0,weight=1)

    image_path4 = path('images/python.png')
    tab.python = ctk.CTkImage(light_image=Image.open(image_path4),size=(70,70))

    image_path5 = path('images/java.png')
    tab.java = ctk.CTkImage(light_image=Image.open(image_path5),size=(70,70))

    image_path6 = path('images/web-link.png')
    tab.internet = ctk.CTkImage(light_image=Image.open(image_path6),size=(70,70))

    image_path7 = path('images/business.png')
    tab.business = ctk.CTkImage(light_image=Image.open(image_path7),size=(70,70))

    image_path8 = path('images/informative.png')
    tab.information = ctk.CTkImage(light_image=Image.open(image_path8),size=(70,70))

    image_path1 = path('images/back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path1),size=(32,32))

    ctk.CTkButton(main_frame,text="",image=tab.back,height=43,fg_color="aqua",
                  width=40,corner_radius=25,command= lambda:notebook.select(home)).grid(row=0,column=0,pady=15,sticky="w",padx=25)
    
    sub_frame = ctk.CTkFrame(main_frame,fg_color= "#0A082D")
    sub_frame.grid(row=1,column=0)

    def select_python():
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("delete from score")
        cursor.execute("delete from selections")
        cursor.execute("insert into selections (user_id, subject, level) values(?,?,?)",(user_id.get(),"python","easy"))
        connection.commit()
        connection.close()
        notebook.select(slect_level)

    def select_java():
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("delete from score")
        cursor.execute("delete from selections")
        cursor.execute("insert into selections (user_id, subject, level) values(?,?,?)",(user_id.get(),"java","easy"))
        connection.commit()
        connection.close()
        notebook.select(slect_level)

    def select_internet():
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("delete from score")
        cursor.execute("delete from selections")
        cursor.execute("insert into selections (user_id, subject, level) values(?,?,?)",(user_id.get(),"Internet Tech","easy"))
        connection.commit()
        connection.close()
        notebook.select(slect_level)

    def select_accounts():
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("delete from score")
        cursor.execute("delete from selections")
        cursor.execute("insert into selections (user_id, subject, level) values(?,?,?)",(user_id.get(),"Accounting & Finance","easy"))
        connection.commit()
        connection.close()
        notebook.select(slect_level)

    def select_information():
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("delete from score")
        cursor.execute("delete from selections")
        cursor.execute("insert into selections (user_id, subject, level) values(?,?,?)",(user_id.get(),"Information System","easy"))
        connection.commit()
        connection.close()
        notebook.select(slect_level)

    ctk.CTkLabel(sub_frame,text="SELECT YOUR SUBJECT",font=("impact",30),text_color="white").grid(column=0,row=0,pady=10,sticky="w",padx=10)


    ctk.CTkButton(sub_frame,text = "  PYTHON     ",command = select_python,image = tab.python,compound="right",
                  font=("calibri",20,"bold"),fg_color="#2E3756",border_color="#2E3756",corner_radius=5,
                        border_width=1,width=400,height=60).grid(row=1,column=0,pady=10,padx=10)

    ctk.CTkButton(sub_frame,text = "  JAVA     ",command = select_java,image = tab.java,compound="right",
                  font=("calibri",20,"bold"),fg_color="#2E3756",border_color="#2E3756",corner_radius=5,
                        border_width=1,width=400,height=60).grid(row=2,column=0,pady=10)

    ctk.CTkButton(sub_frame,text = "INTERNET TECH    ",command = select_internet,
                  font=("calibri",20,"bold"),image = tab.internet,compound="right",fg_color="#2E3756",border_color="#2E3756",corner_radius=5,
                        border_width=1,width=400,height=60).grid(row=3,column=0,pady=10)

    ctk.CTkButton(sub_frame,text = "BUSINESS      ",command = select_accounts,
                  font=("calibri",20,"bold"),fg_color="#2E3756",border_color="#2E3756",corner_radius=5,
                        border_width=1,width=400,height=60,image = tab.business,compound="right").grid(row=4,column=0,pady=10)

    ctk.CTkButton(sub_frame,text = "INFORMATION SYSTEM    ",command = select_information,
                  font=("calibri",20,"bold"),fg_color="#2E3756",border_color="#2E3756",corner_radius=5,
                        border_width=1,width=400,height=60,image = tab.information,compound="right").grid(row=5,column=0,pady=10)












