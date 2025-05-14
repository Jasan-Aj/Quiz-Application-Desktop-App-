import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import random
from functools import partial
import sqlite3
from tkinter import messagebox


def add_meterials_page(tab,notebook,path,database,admin_panel):

    main_frame = ctk.CTkFrame(tab,fg_color="white")
    main_frame.pack(fill="both",expand = True)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=1)
    main_frame.columnconfigure(0,weight=1)

    image_path4 = path('images/back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path4),size=(32,32))

    nav = ctk.CTkFrame(main_frame,fg_color="#0A082D",corner_radius=0)
    nav.grid(row=0,column=0,sticky="nsew")

    nav.columnconfigure(0,weight=1)
    nav.columnconfigure(1,weight=1)
    nav.columnconfigure(2,weight=1)
    nav.rowconfigure(2,weight=1)

    ctk.CTkLabel(nav,text="ADD STUDY MATERIALS",font=("impact",35),text_color="white").grid(row=0,column=1,pady=10)

    ctk.CTkButton(nav,text="",image=tab.back,height=43,fg_color="aqua",command=lambda:notebook.select(admin_panel),
                  width=40,corner_radius=25).grid(row=0,column=0,sticky="w",padx=15)
    
    body=ctk.CTkFrame(main_frame,fg_color="#EAEAEA")
    body.grid(row=1,column=0,sticky="nswe")
    body.columnconfigure(0,weight=1)
    body.rowconfigure(0,weight=1)

    container = ctk.CTkFrame(body,fg_color="white")
    container.grid(row=0,column=0)

    form = ctk.CTkFrame(container,fg_color="white")
    form.grid(row=0,column=0,pady=15,padx=20)
    form.columnconfigure(0,weight=1)
    form.columnconfigure(1,weight=1)

    def validate():
        if caption.get()=="" or link.get()=="":
            messagebox.showwarning(title="WARNING", message="Fill Required Feilds!")

        else:
            insert()

    def insert():
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("insert into study_meterials (subject,caption,link_type,link) values(?,?,?,?)",(sub_type.get(),caption.get(),link_type.get(),link.get()))
        connection.commit()
        connection.close()
        messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
        clear()

    sub_type=tk.StringVar(value="Python")
    ctk.CTkLabel(form,text="Select Subject: ",text_color="black",font=("calibri",18)).grid(row=1,column=0,padx=15)
    select_sub = ctk.CTkComboBox(form,height=35,variable=sub_type,border_color="#0A082D",button_color="#DB0A41",
                                dropdown_font=("calibri",17,"bold"),dropdown_text_color="white",dropdown_fg_color="black",
                                 fg_color="white",corner_radius=50,width=280,
                                 text_color="black",font=("calibri",18))
    
    select_sub.configure(values=["Python","Java","Internet Tech","Accounting & Finance","Information System"])
    select_sub.grid(row=1,column=1,padx=15,sticky="w")

    link_type=tk.StringVar(value="Youtube Links")
    ctk.CTkLabel(form,text="Select Material: ",text_color="black",font=("calibri",18)).grid(row=2,column=0,padx=15)
    select_type = ctk.CTkComboBox(form,height=35,variable=link_type,border_color="#0A082D",button_color="#DB0A41",
                                 dropdown_font=("calibri",17,"bold"),dropdown_text_color="white",dropdown_fg_color="black"
                                  ,fg_color="white",corner_radius=50,width=200,
                                 text_color="black",font=("calibri",18))
    select_type.configure(values=["Youtube Links","Usefull Links"])
    select_type.grid(row=2,column=1,padx=15,sticky="w",pady=15)

    ctk.CTkLabel(form,text="Enter Caption: ",text_color="black",font=("calibri",18)).grid(row=3,column=0)
    caption = ctk.CTkEntry(form,width=400,height=35,corner_radius=5,text_color="black",fg_color="white",
                       border_color="#0A082D",border_width=2,font=("calibri",18))
    caption.grid(row=3,column=1,pady=15,padx=10)

    ctk.CTkLabel(form,text="Enter Link: ",text_color="black",font=("calibri",18)).grid(row=4,column=0)
    link=ctk.CTkEntry(form,width=400,height=35,border_color="#0A082D",border_width=2,corner_radius=5,fg_color="white",
                        font=("calibri",18),text_color="black")
    link.grid(row=4,column=1,pady=10)


    def clear():
        link.delete(0,tk.END)
        caption.delete(0,tk.END)

    button_frame=ctk.CTkFrame(form,fg_color="white")
    button_frame.grid(row=9,column=0,columnspan=2,pady=10)

    ctk.CTkButton(button_frame,text="ADD",fg_color="#0A082D",corner_radius=20,font=("calibri",17,"bold"),
                  text_color="white",height=35,border_color="white",command=validate).grid(row=0,column=0,padx=8)

    ctk.CTkButton(button_frame,text="CLEAR",fg_color="#0A082D",corner_radius=20,font=("calibri",17,"bold"),
                  text_color="white",height=35,border_color="white",command=clear).grid(row=0,column=1,padx=8)

    ctk.CTkButton(button_frame,text="CANCEL",fg_color="#0A082D",corner_radius=20,font=("calibri",17,"bold"),
                  text_color="white",height=35,border_color="white").grid(row=0,column=2,padx=8)

    






