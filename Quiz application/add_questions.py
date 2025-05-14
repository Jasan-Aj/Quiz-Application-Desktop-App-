import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import random
from functools import partial
import sqlite3
from tkinter import messagebox


def add_question_func(tab,notebook,path,database,admin_panel):

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

    ctk.CTkLabel(nav,text="ADD QUESTIONS",font=("impact",35),text_color="white").grid(row=0,column=1,pady=10)

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
        if question.get(0.0,'end')=="" or answer.get()=="" or option1.get()=="" or option2.get()=="" or option3.get()=="" or option4.get()=="":
            messagebox.showwarning(title="WARNING", message="Fill Required Feilds!")

        else:
            insert()

    def insert():
        
        if sub_type.get()=="Python":
            if sub_level.get()=="Easy":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO python_easy (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
                connection.commit()
                connection.close()
                messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
                clear()

            elif sub_level.get()=="Medium":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO python_medium (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
                connection.commit()
                connection.close()
                messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
                clear()

            elif sub_level.get()=="Hard":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO python_hard (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
                connection.commit()
                connection.close()
                messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
                clear()

        elif sub_type.get()=="Java":
            if sub_level.get()=="Easy":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO java_easy (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
                connection.commit()
                connection.close()
                messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
                clear()

            elif sub_level.get()=="Medium":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO java_medium (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
                connection.commit()
                connection.close()
                messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
                clear()

            elif sub_level.get()=="Hard":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO java_hard (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
                connection.commit()
                connection.close()
                messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
                clear()

        elif sub_type.get()=="Internet Tech":
            if sub_level.get()=="Easy":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO internet_tech_easy (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
                connection.commit()
                connection.close()
                messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
                clear()

            elif sub_level.get()=="Medium":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO internet_tech_medium (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
                connection.commit()
                connection.close()
                messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
                clear()

            elif sub_level.get()=="Hard":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO internet_tech_hard (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
                connection.commit()
                connection.close()
                messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
                clear()

        elif sub_type.get()=="Accounting & Finance":
            if sub_level.get()=="Easy":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO accounting_easy (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
                connection.commit()
                connection.close()
                messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
                clear()

            elif sub_level.get()=="Medium":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO accounting_medium (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
                connection.commit()
                connection.close()
                messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
                clear()

            elif sub_level.get()=="Hard":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO accounting_hard (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
                connection.commit()
                connection.close()
                messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
                clear()

        elif sub_type.get()=="Information System":
            if sub_level.get()=="Easy":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO information_easy (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
                connection.commit()
                connection.close()
                messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
                clear()

            elif sub_level.get()=="Medium":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO information_medium (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
                connection.commit()
                connection.close()
                messagebox.showwarning(title="WARNING", message="Sucessfully Added!")
                clear()

            elif sub_level.get()=="Hard":
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO information_hard (quize, answer, option1, option2, option3, option4) VALUES (?, ?, ?, ?, ?, ?)",
                               (question.get(0.0,'end'),answer.get(), option1.get(), option2.get(), option3.get(), option4.get()))
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

    sub_level=tk.StringVar(value="Easy")
    ctk.CTkLabel(form,text="Select Level: ",text_color="black",font=("calibri",18)).grid(row=2,column=0,padx=15,pady=15)
    select_level = ctk.CTkComboBox(form,height=35,variable=sub_level,border_color="#0A082D",button_color="#DB0A41",
                                 dropdown_font=("calibri",17,"bold"),dropdown_text_color="white",dropdown_fg_color="black",
                                   fg_color="white",corner_radius=50,width=200,
                                 text_color="black",font=("calibri",18))
    select_level.configure(values=["Easy","Medium","Hard"])
    select_level.grid(row=2,column=1,padx=15,sticky="w")

    ctk.CTkLabel(form,text="Enter Qestion: ",text_color="black",font=("calibri",18)).grid(row=3,column=0)
    question = ctk.CTkTextbox(form,height=90,width=400,corner_radius=5,text_color="black",fg_color="white",
                       border_color="#0A082D",border_width=2,font=("calibri",18))
    question.grid(row=3,column=1,pady=15,padx=10)

    ctk.CTkLabel(form,text="Enter Answer: ",text_color="black",font=("calibri",18)).grid(row=4,column=0)
    answer=ctk.CTkEntry(form,width=400,height=35,border_color="#0A082D",border_width=2,corner_radius=5,fg_color="white",
                        font=("calibri",18),text_color="black")
    answer.grid(row=4,column=1,pady=10)

    ctk.CTkLabel(form,text="Enter Option 1: ",text_color="black",font=("calibri",18)).grid(row=5,column=0)
    option1=ctk.CTkEntry(form,width=400,height=35,border_color="#0A082D",border_width=2,corner_radius=5,fg_color="white",
                        font=("calibri",18),text_color="black")
    option1.grid(row=5,column=1,pady=10)

    ctk.CTkLabel(form,text="Enter Option 2: ",text_color="black",font=("calibri",18)).grid(row=6,column=0)
    option2=ctk.CTkEntry(form,width=400,height=35,border_color="#0A082D",border_width=2,corner_radius=5,fg_color="white",
                        font=("calibri",18),text_color="black")
    option2.grid(row=6,column=1,pady=10)

    ctk.CTkLabel(form,text="Enter Option 3: ",text_color="black",font=("calibri",18)).grid(row=7,column=0)
    option3=ctk.CTkEntry(form,width=400,height=35,border_color="#0A082D",border_width=2,corner_radius=5,fg_color="white",
                        font=("calibri",18),text_color="black")
    option3.grid(row=7,column=1,pady=10)

    ctk.CTkLabel(form,text="Enter Option 4: ",text_color="black",font=("calibri",18)).grid(row=8,column=0)
    option4=ctk.CTkEntry(form,width=400,height=35,border_color="#0A082D",border_width=2,corner_radius=5,fg_color="white",
                        font=("calibri",18),text_color="black")
    option4.grid(row=8,column=1,pady=10)

    def clear():
        question.delete(0.0,'end')
        answer.delete(0,tk.END)
        option1.delete(0,tk.END)
        option2.delete(0,tk.END)
        option3.delete(0,tk.END)
        option4.delete(0,tk.END)

    button_frame=ctk.CTkFrame(form,fg_color="white")
    button_frame.grid(row=9,column=0,columnspan=2,pady=10)

    ctk.CTkButton(button_frame,text="ADD",fg_color="#0A082D",corner_radius=20,font=("calibri",17,"bold"),
                  text_color="white",height=35,border_color="white",command=validate).grid(row=0,column=0,padx=8)

    ctk.CTkButton(button_frame,text="CLEAR",fg_color="#0A082D",corner_radius=20,font=("calibri",17,"bold"),
                  text_color="white",height=35,border_color="white",command=clear).grid(row=0,column=1,padx=8)

    ctk.CTkButton(button_frame,text="CANCEL",fg_color="#0A082D",corner_radius=20,font=("calibri",17,"bold"),
                  text_color="white",height=35,border_color="white").grid(row=0,column=2,padx=8)














