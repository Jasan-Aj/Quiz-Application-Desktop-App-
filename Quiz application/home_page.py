import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3


def home(tab,notebook,select_sub,path,user_id,database,login,slect_level,leaderboard_select,
         study_materials,run_study):
    main_frame = ctk.CTkFrame(tab,fg_color= "#0A082D")
    main_frame.pack(fill="both",expand = True)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=3)
    main_frame.rowconfigure(2,weight=0)
    main_frame.columnconfigure(0,weight=1)

    image_path1 = path('images/quiz.png')
    tab.quize = ctk.CTkImage(light_image=Image.open(image_path1),size=(65,65))

    image_path2 = path('images/leaderboard.png')
    tab.leader_board = ctk.CTkImage(light_image=Image.open(image_path2),size=(65,65))

    image_path3 = path('images/stack-of-books.png')
    tab.books = ctk.CTkImage(light_image=Image.open(image_path3),size=(65,65))

    image_path4 = path('images/python.png')
    tab.python = ctk.CTkImage(light_image=Image.open(image_path4),size=(90,90))

    image_path5 = path('images/java.png')
    tab.java = ctk.CTkImage(light_image=Image.open(image_path5),size=(85,85))

    image_path6 = path('images/web-link.png')
    tab.internet = ctk.CTkImage(light_image=Image.open(image_path6),size=(90,90))

    image_path7 = path('images/business.png')
    tab.business = ctk.CTkImage(light_image=Image.open(image_path7),size=(90,90))

    image_path8 = path('images/informative.png')
    tab.information = ctk.CTkImage(light_image=Image.open(image_path8),size=(90,90))

    image_path9 = path('images/exit.png')
    tab.logout = ctk.CTkImage(light_image=Image.open(image_path9),size=(32,32))

    image_path10 = path('images/logo.png')
    tab.logo = ctk.CTkImage(light_image=Image.open(image_path10),size=(150,60))
    
    nav_bar = ctk.CTkFrame(main_frame,fg_color= "#1A082D")
    nav_bar.grid(row=0,column=0,sticky="nswe")
    nav_bar.columnconfigure(0,weight=1)
    nav_bar.columnconfigure(1,weight=1)

    ctk.CTkLabel(nav_bar,text = "",image=tab.logo).grid(row=0,column=0,padx=60,sticky="w")
    ctk.CTkButton(nav_bar,text="Logout",command=lambda:notebook.select(login),fg_color="#1A082D",
                  font=("calibri",17),text_color="white",compound="top",image=tab.logout).grid(row=0,column=1,padx=45,sticky="e",pady=5)

    body = ctk.CTkScrollableFrame(main_frame,fg_color= "#0A082D")
    body.grid(row=1,column=0,sticky = "nswe")
    body.columnconfigure(0,weight=1)

    def validate(page):
        if user_id.get()=="":
            result = messagebox.askokcancel("Confirmation", "Login To Continue!")
            if result:
                notebook.select(login)
            else:
                pass

        else:
            notebook.select(page)

    def sub_validate(subject):
        if user_id.get()=="":
            result = messagebox.askokcancel("Confirmation", "Login To Continue!")
            if result:
                notebook.select(login)
            else:
                pass

        else:
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("delete from score")
            cursor.execute("delete from selections")
            cursor.execute("insert into selections (user_id, subject, level) values(?,?,?)",(user_id.get(),subject,"easy"))
            connection.commit()
            connection.close()
            notebook.select(slect_level)

    def switch_study_materials():
        run_study()
        notebook.select(study_materials)        
            
    get_start_frame = ctk.CTkFrame(body,fg_color= "#0A082D")
    get_start_frame.grid(row=0,column=0,columnspan=3,pady=50)

    ctk.CTkLabel(get_start_frame,text = "Here's How To Get Strated",
                 font=("impact",29),text_color="white").grid(row=0,column=0,pady=10,sticky="w")
    ctk.CTkButton(get_start_frame,text = "             Attempt Quize Now    ",image=tab.quize,compound="right",
                  font=("calibri",22,"bold"),fg_color="#0A082D",border_color="#BAD5CC",corner_radius=8,
                  command=lambda:validate(select_sub),
                        border_width=1,width=400,height=60).grid(row=1,column=0,pady=15)

    ctk.CTkButton(get_start_frame,text = "            Top Performers            ",image=tab.leader_board,compound="right",
                  font=("calibri",22,"bold"),fg_color="#0A082D",border_color="#BAD5CC",corner_radius=8,
                        border_width=1,width=400,height=60,command=lambda:notebook.select(leaderboard_select)).grid(row=2,column=0)

    ctk.CTkButton(get_start_frame,text = "Search Your Study Materials    ",image=tab.books,compound="right",
                  font=("calibri",22,"bold"),fg_color="#0A082D",border_color="#BAD5CC",corner_radius=8,
                        border_width=1,width=400,height=60,command=switch_study_materials).grid(row=3,column=0,pady=15)

    subject_frame = ctk.CTkFrame(body,fg_color = "#0A082D")
    subject_frame.grid(row=1,column=0)

    ctk.CTkLabel(subject_frame,text = "Select By Subject",font=("impact",29),text_color="white").grid(row=1,column=0,columnspan=2,padx=20,pady=20)

    ctk.CTkButton(subject_frame,text = "Python",width = 150,image=tab.python,compound="top",fg_color="white",font=("roboto",20,"bold"),
                  height=150,text_color="black",command=lambda:sub_validate("python")).grid(row=2,column=0,pady=20,padx=25)
    ctk.CTkButton(subject_frame,text = "Java",width = 150,image=tab.java,compound="top",fg_color="white",font=("roboto",20,"bold"),
                  height=150,text_color="black",command=lambda:sub_validate("java")).grid(row=2,column=1,pady=20,padx=25)
    ctk.CTkButton(subject_frame,text = "Internet\nTech",width = 150,image=tab.internet,compound="top",fg_color="white",font=("roboto",20,"bold"),
                  height=150,text_color="black",command=lambda:sub_validate("Internet Tech")).grid(row=2,column=2,pady=20,padx=25)
    ctk.CTkButton(subject_frame,text = "Information\nSystem",width = 150,image=tab.information,compound="top",fg_color="white",font=("roboto",20,"bold"),
                  height=150,text_color="black",command=lambda:sub_validate("Information System")).grid(row=2,column=3,pady=20,padx=25)
    ctk.CTkButton(subject_frame,text = "Business",width = 150,image=tab.business,compound="top",fg_color="white",font=("roboto",20,"bold"),
                  height=150,text_color="black",command=lambda:sub_validate("Accounting & Finance")).grid(row=2,column=4,pady=20,padx=25)

    

