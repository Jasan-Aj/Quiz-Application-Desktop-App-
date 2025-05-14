import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import random
from functools import partial
import sqlite3

def admin_func(tab,notebook,path,manage_qstn,manage_qstn_func,add_question,manage_users,
               manage_users_func,add_study_materilas,manage_study,manage_study_func,login):

    main_frame = ctk.CTkFrame(tab,fg_color= "#0A082D")
    main_frame.pack(fill="both",expand = True)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=1)
    main_frame.columnconfigure(0,weight=1)

    image_path1 = path('images/exit.png')
    tab.logout = ctk.CTkImage(light_image=Image.open(image_path1),size=(36,36))

    image_path2 = path('images/man.png')
    tab.users = ctk.CTkImage(light_image=Image.open(image_path2),size=(110,110))

    image_path3 = path('images/question-mark.png')
    tab.add_qstn = ctk.CTkImage(light_image=Image.open(image_path3),size=(110,110))

    image_path4 = path('images/delete.png')
    tab.remove_qstn = ctk.CTkImage(light_image=Image.open(image_path4),size=(110,110))

    image_path5 = path('images/study.png')
    tab.add_materials = ctk.CTkImage(light_image=Image.open(image_path5),size=(110,110))

    image_path6 = path('images/data-analysis.png')
    tab.rmv_materials = ctk.CTkImage(light_image=Image.open(image_path6),size=(110,110))

    image_path7 = path('images/bg.jpg')
    tab.backgraound = ctk.CTkImage(light_image=Image.open(image_path7),size=(1290,410))

    nav = ctk.CTkFrame(main_frame,fg_color="#0A082D",corner_radius=0)
    nav.grid(row=0,column=0,sticky="nsew")

    nav.columnconfigure(0,weight=1)
    nav.columnconfigure(1,weight=1)
    nav.columnconfigure(2,weight=1)
    
    nav.rowconfigure(0,weight=1)

    ctk.CTkLabel(nav,text="ADMIN PANEL",font=("impact",37),text_color="white").grid(row=0,column=1,pady=10,sticky="e",padx=300)
    ctk.CTkButton(nav,text="LogOut  ",command=lambda:notebook.select(login),fg_color="#0A082D",
                  font=("calibri",16),text_color="white",compound="top",image=tab.logout).grid(row=0,column=2,pady=5,sticky="e",padx=20)

    body=ctk.CTkFrame(main_frame,fg_color="white",corner_radius=0)
    body.grid(row=1,column=0,sticky="nswe")
    body.columnconfigure(0,weight=1)
    body.columnconfigure(1,weight=1)
    body.columnconfigure(2,weight=1)
    body.columnconfigure(3,weight=1)
    body.columnconfigure(4,weight=1)
    body.rowconfigure(0,weight=1)
    body.rowconfigure(1,weight=1)

    def switch_manage_qstn():
        manage_qstn_func()
        notebook.select(manage_qstn)

    def switch_manage_users():
        manage_users_func()
        notebook.select(manage_users)

    def switch_manage_study():
        manage_study_func()
        notebook.select(manage_study)

    ctk.CTkLabel(body,text="",image=tab.backgraound).grid(row=0,column=0,columnspan=5)
        

    ctk.CTkButton(body,text="ADD NEW QUESTIONS",width=250,height=180,corner_radius=10,image=tab.add_qstn,compound="top",
                  font=("impact",22),command=lambda:notebook.select(add_question),fg_color="#0A053D",text_color="white").grid(row=1,column=0)

    ctk.CTkButton(body,text="MANAGE QUESTIONS",width=250,height=180,corner_radius=10,compound="top",image=tab.remove_qstn,
                  font=("impact",22),command=switch_manage_qstn,fg_color="#0A053D").grid(row=1,column=1)

    ctk.CTkButton(body,text="MANAGE USERS",width=250,height=180,corner_radius=10,command=switch_manage_users,image=tab.users,
                  font=("impact",22),compound="top",fg_color="#0A053D").grid(row=1,column=2)

    ctk.CTkButton(body,text="ADD STUDY\nMATERIALS",width=250,height=90,corner_radius=10,compound="top",image=tab.add_materials,
                  font=("impact",22),command=lambda:notebook.select(add_study_materilas),fg_color="#0A053D").grid(row=1,column=3)

    ctk.CTkButton(body,text="MANAGE\nMATERIALS",width=250,height=90,corner_radius=10,compound="top",image=tab.rmv_materials,
                  font=("impact",22),command=switch_manage_study,fg_color="#0A053D").grid(row=1,column=4)


