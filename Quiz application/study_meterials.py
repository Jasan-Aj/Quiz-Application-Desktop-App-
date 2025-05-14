import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import random
from functools import partial
import sqlite3
from tkinter import messagebox
import webbrowser


def study_meterials_page(tab,notebook,path,database,home):

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

    image_path4 = path('images/back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path4),size=(32,32))

    ctk.CTkLabel(nav,text="STUDY MATERIALS",font=("impact",35),text_color="white").grid(row=0,column=1,pady=10)
    ctk.CTkButton(nav,text="",image=tab.back,height=43,fg_color="aqua",command=lambda:notebook.select(home),
                  width=40,corner_radius=25).grid(row=0,column=0,sticky="w",padx=15)
    
    body=ctk.CTkFrame(main_frame,fg_color="aqua")
    body.grid(row=1,column=0,sticky="nswe")
    body.columnconfigure(0,weight=1)
    body.rowconfigure(0,weight=1)


    form = ctk.CTkFrame(body,fg_color="white")
    form.grid(row=0,column=0,sticky="nswe")
    form.columnconfigure(0,weight=1)
    form.columnconfigure(1,weight=1)
    form.rowconfigure(1,weight=0)
    form.rowconfigure(2,weight=2)

    def run(event):
        
        meterial_container = ctk.CTkScrollableFrame(form,fg_color="white")
        meterial_container.grid(row=2,column=0,sticky="nswe",columnspan=2,pady=15)
        meterial_container.columnconfigure(0,weight=1)
        meterial_container.rowconfigure(0,weight=2)
        meterial_container.rowconfigure(1,weight=2)

        yt_frame = ctk.CTkFrame(meterial_container,fg_color="white")
        yt_frame.grid(row=0,column=0,sticky="nswe",pady=20)

        yt_lst = []    
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("select id from study_meterials where link_type = 'Youtube Links' AND subject = ? ",(sub_type.get(),))
        res = cursor.fetchall()
        for i in res:
            yt_lst.append(i[0])
        connection.close()

        usefull_links_lst = []    
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("select id from study_meterials where link_type = 'Usefull Links' AND subject = ? ",(sub_type.get(),))
        res = cursor.fetchall()
        for i in res:
            usefull_links_lst.append(i[0])
        connection.close()
      

        ctk.CTkLabel(yt_frame,text="Youtube Links",font=("impact",30),text_color="#0A082D").pack()

        if yt_lst==[]:
            temp_frame = ctk.CTkFrame(yt_frame,corner_radius=5,fg_color="white",border_width=2,border_color="#2A3650")
            temp_frame.pack(pady=20)
            ctk.CTkLabel(temp_frame,text = "NO MATERIALS ADDED YET!",text_color="#2A3650",
                         font=("calibri",30)).pack(pady=5,padx=5)
        else:

            for i in yt_lst:

                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("select caption,link from study_meterials where id=? ",(i,))
                result = cursor.fetchall()
                
                content_frame = ctk.CTkFrame(yt_frame,fg_color="#2A3650")
                content_frame.pack(pady=15)
                content_frame.columnconfigure(0,weight=1)
                content_frame.columnconfigure(1,weight=1)

                ctk.CTkLabel(content_frame,text=result[0][0],text_color="white",font=("calibri",25)).grid(row=0,column=0,padx=20,pady=5)
                link = ctk.CTkLabel(content_frame,text=result[0][1],text_color="white",font=("calibri",25,"underline"),cursor="hand2")
                link.grid(row=0,column=1,padx=15)

                link.bind("<Button-1>",lambda x:webbrowser.open_new(result[0][1]))        

        meterial_frame = ctk.CTkFrame(meterial_container,fg_color="white")
        meterial_frame.grid(row=1,column=0,sticky="nswe",pady=5)

        ctk.CTkLabel(meterial_frame,text="Usefull Links",font=("impact",30),text_color="#0A082D").pack()

        if usefull_links_lst==[]:
            temp_frame = ctk.CTkFrame(meterial_frame,corner_radius=5,fg_color="white",border_width=2,border_color="#2A3650")
            temp_frame.pack(pady=20)
            ctk.CTkLabel(temp_frame,text = "NO MATERIALS ADDED YET!",text_color="#2A3650",
                         font=("calibri",30)).pack(pady=5,padx=5)
        else:
            for i in usefull_links_lst:

                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("select caption,link from study_meterials where id=? ",(i,))
                result = cursor.fetchall()
                
                content_frame = ctk.CTkFrame(meterial_frame,fg_color="#2A3650")
                content_frame.pack(pady=15)
                content_frame.columnconfigure(0,weight=1)
                content_frame.columnconfigure(1,weight=1)

                ctk.CTkLabel(content_frame,text=result[0][0],text_color="white",font=("calibri",25)).grid(row=0,column=0,padx=20,pady=5)
                link = ctk.CTkLabel(content_frame,text=result[0][1],text_color="white",font=("calibri",25,"underline"),cursor="hand2")
                link.grid(row=0,column=1,padx=15)

                link.bind("<Button-1>",lambda x:webbrowser.open_new(result[0][1]))  

    sub_type=tk.StringVar(value="Python")

    slect_container = ctk.CTkFrame(form,fg_color="white")
    slect_container.grid(row=1,column=0,sticky="nswe",columnspan=2,pady=25)
    slect_container.columnconfigure(0,weight=1)
    slect_container.columnconfigure(1,weight=1)
    
    ctk.CTkLabel(slect_container,text="Select Subject: ",text_color="black",font=("calibri",19)).grid(row=1,column=0,padx=15,sticky="e")
    select_sub = ctk.CTkComboBox(slect_container,height=35,variable=sub_type,border_color="#0A082D",button_color="#DB0A41",fg_color="white",
                                 dropdown_font=("calibri",17,"bold"),dropdown_text_color="white",dropdown_fg_color="black",corner_radius=50,width=280,
                                 text_color="black",font=("calibri",19),command=run)
    select_sub.configure(values=["Python","Java","Internet Tech","Accounting & Finance","Information System"])
    select_sub.grid(row=1,column=1,padx=15,sticky="w")

    return run
