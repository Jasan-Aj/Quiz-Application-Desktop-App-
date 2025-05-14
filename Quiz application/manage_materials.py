import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import random
from functools import partial
import sqlite3
from tkinter import messagebox


def manage_study(tab,notebook,path,database,admin_panel):

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

    ctk.CTkLabel(nav,text="MANAGE STUDY MATERIALS",font=("impact",35),text_color="white").grid(row=0,column=1,pady=10)
    ctk.CTkButton(nav,text="",image=tab.back,height=43,fg_color="aqua",command=lambda:notebook.select(admin_panel),
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

    slect_container = ctk.CTkFrame(form,fg_color="white")
    slect_container.grid(row=1,column=0,sticky="nswe",columnspan=2,pady=25)
    slect_container.columnconfigure(0,weight=1)
    slect_container.columnconfigure(1,weight=1)

    def remove(material_id):
            
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute(f"delete from study_meterials where id=?",(material_id,))
            connection.commit()
            connection.close()
            run("")

    def run(event):

        lst = []
        if material_type.get()=="Youtube Links":

            connection=sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute(f"select id from study_meterials where link_type='Youtube Links' AND subject=? ",(subject.get(),))
            ids = cursor.fetchall()
            for i in ids:
                lst.append(i[0])
            connection.close()

        else:
            
            connection=sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute(f"select id from study_meterials where link_type='Usefull Links' AND subject=? ",(subject.get(),))
            ids = cursor.fetchall()
            for i in ids:
                lst.append(i[0])
            connection.close()

        quize_container = ctk.CTkScrollableFrame(form,fg_color="#EAEAEA")
        quize_container.grid(row=2,column=0,columnspan=2,sticky="nswe")

        quize_frames = ctk.CTkFrame(quize_container,fg_color="#2A3650",corner_radius=10)
        quize_frames.pack(fill="both")
        quize_frames.columnconfigure(0,weight=1)
        quize_frames.columnconfigure(1,weight=2)
        quize_frames.columnconfigure(2,weight=1)
        
        ctk.CTkLabel(quize_frames,text="Material Id",height=40,fg_color="#2A3650",
                     text_color="white",font=("roboto",19,"bold"),corner_radius=15).grid(row=0,column=0,sticky="w",padx=50)
        ctk.CTkLabel(quize_frames,text="Caption",height=40,fg_color="#2A3650",
                     text_color="white",font=("roboto",19,"bold"),corner_radius=15).grid(row=0,column=1,sticky="w",padx=245)
        ctk.CTkLabel(quize_frames,text="",height=40,fg_color="#2A3650",
                     text_color="white",font=("roboto",19,"bold"),corner_radius=15).grid(row=0,column=2,sticky="w")
        
        def show_materials():

            if lst==[]:
                quize_frames = ctk.CTkFrame(quize_container,border_color="#2A3650",fg_color="white",border_width=2,corner_radius=10)
                quize_frames.pack(pady=20)
                quize_frames.columnconfigure(0,weight=1)

                ctk.CTkLabel(quize_frames,text="NO ANY MATERIALS ADDED YET!",font=("calibri",25),text_color="#2A3650").grid(row=0,column=0,pady=15,padx=10)


            else:
                for material_id in lst:

                    connection = sqlite3.connect(database)
                    cursor = connection.cursor()
                    cursor.execute(f"select caption from study_meterials where id=?",(material_id,))
                    material = cursor.fetchone()
                    connection.close()
        
                    quize_frames = ctk.CTkFrame(quize_container,fg_color="white",corner_radius=10)
                    quize_frames.pack(fill="both",pady=20)
                    quize_frames.columnconfigure(0,weight=1)
                    quize_frames.columnconfigure(1,weight=5)
                    quize_frames.columnconfigure(2,weight=1)
                    
                    ctk.CTkLabel(quize_frames,text=material_id,
                                 text_color="black",font=("roboto",20,"bold"),fg_color="white").grid(row=0,column=0,sticky="w",padx=90)
                    ctk.CTkLabel(quize_frames,text=material[0],text_color="black",
                                 font=("roboto",20,"bold"),wraplength=750,fg_color="white").grid(row=0,column=1,sticky="we",pady=12)
                    ctk.CTkButton(quize_frames,text="Remove",fg_color="#DB0A41",height=35,command=partial(remove,material_id),
                                 text_color="white",font=("roboto",18,"bold")).grid(row=0,column=2,sticky="e",padx=90)
        show_materials()

    material_type=tk.StringVar(value="Youtube Links")
    ctk.CTkLabel(slect_container,text="Select Material Type: ",text_color="black",font=("calibri",19)).grid(row=1,column=0,padx=15,sticky="e")
    select_material = ctk.CTkComboBox(slect_container,height=35,variable=material_type,border_color="#0A082D",button_color="#DB0A41",fg_color="white",
                                 dropdown_font=("calibri",17,"bold"),dropdown_text_color="white",dropdown_fg_color="black",corner_radius=50,width=200,
                                 text_color="black",font=("calibri",19),command=run)
    select_material.configure(values=["Youtube Links","Usefull Links"])
    select_material.grid(row=1,column=1,padx=15,sticky="w",pady=10)

    subject=tk.StringVar(value="Python")
    ctk.CTkLabel(slect_container,text="Select Subject: ",text_color="black",font=("calibri",19)).grid(row=2,column=0,padx=15,sticky="e")
    select_sub = ctk.CTkComboBox(slect_container,height=35,variable=subject,border_color="#0A082D",button_color="#DB0A41",fg_color="white",
                                 dropdown_font=("calibri",17,"bold"),dropdown_text_color="white",dropdown_fg_color="black",corner_radius=50,width=280,
                                 text_color="black",font=("calibri",19),command=run)
    select_sub.configure(values=["Python","Java","Internet Tech","Accounting & Finance","Information System"])
    select_sub.grid(row=2,column=1,padx=15,sticky="w")

    

    return run



    




