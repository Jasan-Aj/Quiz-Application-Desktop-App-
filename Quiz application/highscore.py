import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3

def high_score(tab,path,notebook,question_page,question_func,home,database,user_id):

    main_frame = ctk.CTkFrame(tab,fg_color= "#0A082D")
    main_frame.pack(fill="both",expand = True)
    main_frame.columnconfigure(0,weight=1)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=1)

    body = ctk.CTkScrollableFrame(main_frame,fg_color="#0A082D")
    body.grid(row=1,column=0,sticky="nswe")
    body.columnconfigure(0,weight=1)
    body.columnconfigure(1,weight=1)
    body.columnconfigure(2,weight=1)
    body.columnconfigure(3,weight=1)

    image_path1 = path('images/logo.png')
    tab.logo = ctk.CTkImage(light_image=Image.open(image_path1),size=(150,60))

    title_frame = ctk.CTkFrame(body,fg_color="#0A082D")
    title_frame.grid(row=1,column=1,columnspan=2,sticky="we")
    title_frame.columnconfigure(0,weight=1)
    title_frame.columnconfigure(1,weight=1)
    title_frame.columnconfigure(2,weight=1)
    title_frame.columnconfigure(3,weight=1)
    title_frame.columnconfigure(4,weight=1)

    
    

    def show_result():

        subject = tk.StringVar()
    

        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("select subject from selections where user_id=?",(user_id.get(),))
        res = cursor.fetchone()
        subject.set(res[0])
        connection.close()

        ctk.CTkLabel(title_frame,text="",image=tab.logo,font=("calibri",30)).grid(row=0,column=1,pady=6,sticky="e")
        ctk.CTkLabel(title_frame,text=subject.get().upper(),wraplength=170,font=("impact",30),
                     width=300,height=80,fg_color="#0A082D",text_color="white").grid(row=0,column=3,sticky="w")

        def close():
            
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("delete from selections where user_id=?",(user_id.get(),))
            cursor.execute("delete from score where user_id=?",(user_id.get(),))
            connection.commit()
            connection.close()
            notebook.select(home)

        def play_again():
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("delete from score where user_id=?",(user_id.get(),))
            connection.commit()
            connection.close()
            question_func()
            notebook.select(question_page)
            

        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("select score, count from score where user_id=?",(user_id.get(),))
        items = cursor.fetchall()
        connection.close()
        
        container_frame = ctk.CTkFrame(body,fg_color="white")
        container_frame.grid(row=2,column=1,pady=10,columnspan=2)
        
        content_frame = ctk.CTkFrame(container_frame,fg_color="white")
        content_frame.grid(row=0,column=0,pady=25,padx=100)

        color = "green"
        result_frame = ctk.CTkFrame(content_frame,fg_color = color,corner_radius=20)
        result_frame.grid(row=0,column=0,pady=30)

        ctk.CTkLabel(result_frame,text = "Congradulations!\nNew High Score",font=("roboto",30,"bold"),text_color="white").grid(row=0,column=0,pady=20,padx=15)
        ctk.CTkLabel(result_frame,text = f"{items[0][0]}",font=("roboto",40,"bold"),text_color="white").grid(row=1,column=0,pady=20)
        ctk.CTkLabel(result_frame,text = "*",font=("roboto",30,"bold"),text_color="white").grid(row=2,column=0,pady=10)

        user_frame = ctk.CTkFrame(content_frame,fg_color="#AFDDE5",corner_radius=20,)
        user_frame.grid(row=1,column=0,pady=15)

        temp_user_frame = ctk.CTkFrame(user_frame,fg_color="#AFDDE5",corner_radius=20,)
        temp_user_frame.grid(row=0,column=0,padx=50,pady=5)

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute("select user_name from user_names where user_id=?",(user_id.get(),) )
        username = cursor.fetchone()
        connection.close()
        
        ctk.CTkLabel(temp_user_frame,text = "Username: ",font=("roboto",20),text_color = "black").grid(row=0,column=0,pady=4,padx=5)
        ctk.CTkLabel(temp_user_frame,text = username,text_color = "black",font=("roboto",20)).grid(row=0,column=1,pady=4,padx=5)

        score_frame = ctk.CTkFrame(content_frame,fg_color="blue",width=330,height=50,corner_radius=15)
        score_frame.grid(row=2,column=0,pady=20)
        temp_frame=ctk.CTkFrame(score_frame,fg_color="blue")
        temp_frame.grid(row=0,column=0,padx=50,pady=3)
        ctk.CTkLabel(temp_frame,text="Your Score",font=("calibri",20,"bold"),text_color="white").grid(row=0,column=0,padx=10,pady=7)
        ctk.CTkLabel(temp_frame,text=f"{items[0][0]}/{items[0][1]}",font=("calibri",20,"bold"),height=40,corner_radius=20,text_color="white").grid(row=0,column=1,padx=8)

        button_frame = ctk.CTkFrame(content_frame,fg_color="white")
        button_frame.grid(row=3,column=0,pady=25)
        ctk.CTkButton(button_frame,text="Close",fg_color="white",font=("calibri",20,"bold"),width=120,height=45,command=close,
                      corner_radius=25,border_color=color,border_width=2,text_color=color).grid(row=0,column=0,padx=10)
        
        ctk.CTkButton(button_frame,text="Play Again",fg_color=color,font=("calibri",20,"bold"),width=80,height=45,command=play_again,
                      corner_radius=25,border_color=color,border_width=2).grid(row=0,column=1,padx=5)

    return show_result


