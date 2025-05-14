import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3

def start_quizes(tab,path,notebook,start_page,start_func,database,user_id):

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

    image_path2 = path('images/trophy.png')
    tab.trophy = ctk.CTkImage(light_image=Image.open(image_path2),size=(170,170))


    ctk.CTkLabel(body,text="",image=tab.logo,font=("calibri",20,"bold")).grid(row=1,column=1,padx=55,pady=6)

    def select_start():
        notebook.select(start_page)
        start_func()

    def show_result():
        container_frame = ctk.CTkFrame(body,fg_color="white")
        container_frame.grid(row=2,column=1,pady=10,columnspan=2)
        
        content_frame = ctk.CTkFrame(container_frame,fg_color="white")
        content_frame.grid(row=0,column=0,pady=25,padx=100)

        color = "green"
        result_frame = ctk.CTkFrame(content_frame,fg_color = color,corner_radius=50)
        result_frame.grid(row=0,column=0,pady=10)

        ctk.CTkLabel(result_frame,text = "",image=tab.trophy,font=("roboto",30,"bold")).grid(row=0,column=0,pady=30,padx=30)

        ctk.CTkLabel(content_frame,text="Attemp the Quize and Be the Top 1",font=("calibri",19),text_color="black").grid(row=1,column=0,pady=15)

        user_frame = ctk.CTkFrame(content_frame,fg_color="white",corner_radius=20,border_width=3,border_color="#AFDDE5")
        user_frame.grid(row=2,column=0,pady=15)

        temp_user_frame = ctk.CTkFrame(user_frame,fg_color="white",corner_radius=20)
        temp_user_frame.grid(row=0,column=0,padx=50,pady=5)

        subject = tk.StringVar()
        table = tk.StringVar()

        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("select subject from selections where user_id=?",(user_id.get(),))
        res = cursor.fetchone()
        subject.set(res[0])
        connection.close()

        if subject.get() == "python":
            table.set("python_score")

        elif subject.get() == "java":
            table.set("java_score")

        elif subject.get() == "Internet Tech":
            table.set("internet_tech_score")

        elif subject.get() == "Information System":
            table.set("information_system_score")

        elif subject.get() == "Accounting & Finance":
            table.set("accounting_score")
    
        lst = []

        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        
        cursor.execute("select user_name from user_names where user_id=?",(user_id.get(),) )
        username = cursor.fetchone()

        
        
        cursor.execute(f"SELECT user_id FROM {table.get()} ORDER BY score DESC")
        scores=cursor.fetchall()

        connection.close()

        rank=0
        for i in scores:
            lst.append(i[0])

        userid = int(user_id.get())

        if userid in lst :
    
            for i in lst:
                rank+=1
                if i == userid:
                    break
        else:
            rank="Null"

        ctk.CTkLabel(temp_user_frame,text = "Username: ",font=("roboto",20),text_color = "black").grid(row=0,column=0,pady=4,padx=5)
        ctk.CTkLabel(temp_user_frame,text = username[0],text_color = "black",font=("roboto",20)).grid(row=0,column=1,pady=4,padx=5)

        score_frame = ctk.CTkFrame(content_frame,fg_color="blue",width=330,height=53,corner_radius=15)
        score_frame.grid(row=3,column=0,pady=20)

        score_temp_frame = ctk.CTkFrame(score_frame,fg_color="blue",width=330,height=50,corner_radius=15)
        score_temp_frame.grid(row=0,column=0,padx=32,pady=2)
        
        ctk.CTkLabel(score_temp_frame,text="Your Standing",font=("calibri",20,"bold"),text_color="white").grid(row=0,column=0,padx=10)
        ctk.CTkLabel(score_temp_frame,text=rank,font=("calibri",23,"bold"),height=40,corner_radius=20,text_color="white").grid(row=0,column=1,padx=8)

        button_frame = ctk.CTkFrame(content_frame,fg_color="white")
        button_frame.grid(row=4,column=0,pady=25)
        ctk.CTkButton(button_frame,text="Next",fg_color="blue",font=("calibri",20,"bold"),width=100,height=50,
                      corner_radius=25,text_color="white",command=select_start).grid(row=0,column=0,padx=15,columnspan=2)
        
        
    return show_result


