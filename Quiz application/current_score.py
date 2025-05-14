import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3


def current_high(tab,path,notebook,qstn_func,question_page,database,user_id,select_sub):
    main_frame = ctk.CTkFrame(tab,fg_color= "#0A082D")
    main_frame.pack(fill="both",expand = True)
    main_frame.columnconfigure(0,weight=1)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=1)

    image_path1 = path('images/logo.png')
    tab.logo = ctk.CTkImage(light_image=Image.open(image_path1),size=(150,60))

    body = ctk.CTkScrollableFrame(main_frame,fg_color="#0A082D")
    body.grid(row=1,column=0,sticky="nswe")
    body.columnconfigure(0,weight=1)
    body.columnconfigure(1,weight=1)
    body.columnconfigure(2,weight=1)
    body.columnconfigure(3,weight=1)

    title_frame = ctk.CTkFrame(body,fg_color="#0A082D")
    title_frame.grid(row=1,column=1,columnspan=2,sticky="we")
    title_frame.columnconfigure(0,weight=1)
    title_frame.columnconfigure(1,weight=1)
    title_frame.columnconfigure(2,weight=1)
    title_frame.columnconfigure(3,weight=1)
    title_frame.columnconfigure(4,weight=1)
    

    def show_result():

        subject = tk.StringVar()
    
        def start_quiz():
            qstn_func()
            notebook.select(question_page)

        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("select subject from selections where user_id=?",(user_id.get(),))
        res = cursor.fetchone()
        subject.set(res[0])
        connection.close()

        ctk.CTkLabel(title_frame,text="",image=tab.logo,font=("calibri",20,"bold")).grid(row=0,column=1,pady=6,sticky="e")
        ctk.CTkLabel(title_frame,text=subject.get().upper(),wraplength=170,font=("impact",30,),
                     width=270,height=80,fg_color="#0A082D",text_color="white").grid(row=0,column=3,sticky="w")
        
        container_frame = ctk.CTkFrame(body,fg_color="white")
        container_frame.grid(row=2,column=1,pady=10,columnspan=2)
        
        content_frame = ctk.CTkFrame(container_frame,fg_color="white")
        content_frame.grid(row=0,column=0,pady=25,padx=115)

        high_score = tk.IntVar()
        sunject_highscore = tk.IntVar()

        if subject.get()=="python":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("SELECT MAX(score) FROM python_score")
            result2 = cursor.fetchone()
            
            cursor.execute("SELECT MAX(score) FROM python_score where user_id = ?",(user_id.get(),))
            result = cursor.fetchone()
      
            if result[0] == None:
               high_score.set(0)
            else:
                high_score.set(result[0])

            if result2[0] == None:
               sunject_highscore.set(0)
            else:
                sunject_highscore.set(result2[0])

        elif subject.get()=="java":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("SELECT MAX(score) FROM java_score")
            result2 = cursor.fetchone()
            cursor.execute("SELECT MAX(score) FROM java_score where user_id = ?",(user_id.get(),))
            result = cursor.fetchone()
      
            if result[0] == None:
               high_score.set(0)
            else:
                high_score.set(result[0])

            if result2[0] == None:
               sunject_highscore.set(0)
            else:
                sunject_highscore.set(result2[0])

        elif subject.get()=="Internet Tech":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("SELECT MAX(score) FROM internet_tech_score")
            result2 = cursor.fetchone()
            cursor.execute("SELECT MAX(score) FROM internet_tech_score where user_id = ?",(user_id.get(),))
            result = cursor.fetchone()
      
            if result[0] == None:
               high_score.set(0)
            else:
                high_score.set(result[0])

            if result2[0] == None:
               sunject_highscore.set(0)
            else:
                sunject_highscore.set(result2[0])

        elif subject.get()=="Accounting & Finance":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("SELECT MAX(score) FROM accounting_score")
            result2 = cursor.fetchone()
            cursor.execute("SELECT MAX(score) FROM accounting_score where user_id = ?",(user_id.get(),))
            result = cursor.fetchone()
      
            if result[0] == None:
               high_score.set(0)
            else:
                high_score.set(result[0])

            if result2[0] == None:
               sunject_highscore.set(0)
            else:
                sunject_highscore.set(result2[0])

        elif subject.get()=="Information System":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("SELECT MAX(score) FROM information_system_score")
            result2 = cursor.fetchone()
            cursor.execute("SELECT MAX(score) FROM information_system_score where user_id = ?",(user_id.get(),))
            result = cursor.fetchone()
      
            if result[0] == None:
               high_score.set(0)
            else:
                high_score.set(result[0])

            if result2[0] == None:
               sunject_highscore.set(0)
            else:
                sunject_highscore.set(result2[0])

        def back_func():
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("delete from selections where user_id = ?",(user_id.get(),))
            connection.commit()
            connection.close()
            notebook.select(select_sub)

        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        
        cursor.execute("select user_name from user_names where user_id=?",(user_id.get(),) )
        user_name = cursor.fetchone()
        connection.close()
        
        color = "green"
        result_frame = ctk.CTkFrame(content_frame,fg_color = color,corner_radius=20)
        result_frame.grid(row=0,column=0,pady=30)

        ctk.CTkLabel(result_frame,text = "Current",font=("roboto",25,"bold"),text_color="white").grid(row=0,column=0,pady=10,padx=40)
        ctk.CTkLabel(result_frame,text = "High Score",font=("roboto",30,"bold"),text_color="white").grid(row=1,column=0,padx=45)
        ctk.CTkLabel(result_frame,text = sunject_highscore.get(),font=("roboto",40,"bold"),text_color="white").grid(row=2,column=0,pady=20)
        ctk.CTkLabel(result_frame,text = "*",font=("roboto",30,"bold"),text_color="white").grid(row=3,column=0,pady=10)

        user_frame = ctk.CTkFrame(content_frame,fg_color="#AFDDE5",corner_radius=20,)
        user_frame.grid(row=1,column=0,pady=15)

        temp_user_frame = ctk.CTkFrame(user_frame,fg_color="#AFDDE5",corner_radius=20,)
        temp_user_frame.grid(row=0,column=0,padx=40,pady=5)
        
        ctk.CTkLabel(temp_user_frame,text = "Username: ",font=("roboto",20),text_color = "black").grid(row=0,column=0,pady=4,padx=5)
        ctk.CTkLabel(temp_user_frame,text = user_name[0],text_color = "black",font=("roboto",20)).grid(row=0,column=1,pady=4,padx=5)

        score_frame = ctk.CTkFrame(content_frame,fg_color="blue",width=330,height=50,corner_radius=15)
        score_frame.grid(row=2,column=0,pady=20)
        
        score_temp_frame = ctk.CTkFrame(score_frame,fg_color="blue",width=330,height=50,corner_radius=15)
        score_temp_frame.grid(row=0,column=0,padx=16,pady=2)
        
        ctk.CTkLabel(score_temp_frame,text="Your High Score",font=("calibri",21,"bold"),text_color="white").grid(row=0,column=0,padx=10)
        ctk.CTkLabel(score_temp_frame,text=high_score.get(),font=("calibri",23,"bold"),height=40,corner_radius=20,text_color="white").grid(row=0,column=1,padx=8)

        button_frame = ctk.CTkFrame(content_frame,fg_color="white")
        button_frame.grid(row=3,column=0,pady=25)
        ctk.CTkButton(button_frame,text="<---",fg_color="white",font=("calibri",20,"bold"),width=70,height=45,
                      corner_radius=25,border_color=color,border_width=2,text_color=color,command= back_func).grid(row=0,column=0,padx=15)
        
        ctk.CTkButton(button_frame,text="Start",fg_color=color,font=("calibri",20,"bold"),width=100,height=45,
                      corner_radius=25,border_color=color,border_width=2,command=start_quiz).grid(row=0,column=1,padx=15)

    return show_result


