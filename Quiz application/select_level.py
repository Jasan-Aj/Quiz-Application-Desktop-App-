import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3


def select_level(tab,notebook,path,select_sub,start_quiz,start_quize_func,database,user_id):
    main_frame = ctk.CTkFrame(tab,fg_color= "#0A082D")
    main_frame.pack(fill="both",expand = True)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=0)

    image_path1 = path('images/happy-face (1).png')
    tab.easy = ctk.CTkImage(light_image=Image.open(image_path1),size=(80,80))

    image_path2 = path('images/smile (1).png')
    tab.medium = ctk.CTkImage(light_image=Image.open(image_path2),size=(85,85))

    image_path3 = path('images/explosion.png')
    tab.hard = ctk.CTkImage(light_image=Image.open(image_path3),size=(87,87))

    image_path4 = path('images/back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path4),size=(32,32))

    def back_func():
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("delete from selections where user_id = ?",(user_id.get(),))
        connection.commit()
        connection.close()
        notebook.select(select_sub)

    main_frame.columnconfigure(0,weight=1)

    ctk.CTkButton(main_frame,text="",image=tab.back,height=43,fg_color="aqua",command = back_func,
                  width=40,corner_radius=25).grid(row=0,column=0,pady=15,sticky="w",padx=25)

    sub_frame = ctk.CTkFrame(main_frame,fg_color= "#0A082D")
    sub_frame.grid(row=1,column=0,pady=90)
    
    def set_level_easy():
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("update selections set level = 'easy' where user_id = ?",(user_id.get(),))
        connection.commit()
        connection.close()
        start_quize_func()
        notebook.select(start_quiz)

    def set_level_medium():
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("update selections set level = 'medium' where user_id = ?",(user_id.get(),))
        connection.commit()
        connection.close()
        start_quize_func()
        notebook.select(start_quiz)

    def set_level_hard():
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("update selections set level = 'hard' where user_id = ?",(user_id.get(),))
        connection.commit()
        connection.close()
        start_quize_func()
        notebook.select(start_quiz)

    ctk.CTkLabel(sub_frame,text="SELECT YOUR DIFFUCULTY LEVEL",font=("impact",30),text_color="white").grid(column=0,row=0,pady=20,sticky="w",padx=10)

    ctk.CTkButton(sub_frame,text = "    EASY    ",command=set_level_easy,image=tab.easy,compound="right",
                  font=("calibri",20,"bold"),fg_color="#2E3756",border_color="#2E3756",corner_radius=5,
                        border_width=1,width=400,height=60).grid(row=1,column=0,pady=15,padx=10)

    ctk.CTkButton(sub_frame,text = "MEADIUM  ",command=set_level_medium,image=tab.medium,compound="right",
                  font=("calibri",20,"bold"),fg_color="#2E3756",border_color="#2E3756",corner_radius=5,
                        border_width=1,width=400,height=60).grid(row=2,column=0,pady=15)

    ctk.CTkButton(sub_frame,text = "   HARD    ",command=set_level_hard,image=tab.hard,compound="right",
                  font=("calibri",20,"bold"),fg_color="#2E3756",border_color="#2E3756",corner_radius=5,
                        border_width=1,width=400,height=60).grid(row=3,column=0,pady=15)







