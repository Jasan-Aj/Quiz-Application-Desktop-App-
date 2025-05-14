import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk, ImageFile
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import sqlite3


def final_details(tab,notebook,database,login,user_id,path,sign_up):
    main_frame = ctk.CTkFrame(tab,fg_color= "#0A082D")
    main_frame.pack(fill="both",expand = True)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=1)
    main_frame.columnconfigure(0,weight=1)

    image_path1 = path('images/avatar.jpg')
    tab.default_avatar = ctk.CTkImage(light_image=Image.open(image_path1),size=(160,80))

    image_path4 = path('images/back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path4),size=(32,32))

    ctk.CTkButton(main_frame,text="",image=tab.back,height=43,command=lambda:notebook.select(sign_up),
                  fg_color="aqua",width=40,corner_radius=25).grid(row=0,column=0,sticky="w",padx=20,pady=20)

    sub_frame = ctk.CTkFrame(main_frame,fg_color= "#0A082D",border_color="#BAD5CC",
                             border_width=2)
    sub_frame.grid(row=1,column=0)

    def validate():
        if " " in username.get():
            messagebox.showwarning(title="WARNING", message="Username Cannot Contain Spaces!")
            
        elif country_var.get()=="" or username.get()=="":
            messagebox.showwarning(title="WARNING", message="Fill All Required Feilds!")

        else:
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select user_name from user_names")
            res = cursor.fetchall()
            connection.close()

            for i in res:
                if i[0] == username.get():
                    messagebox.showwarning(title="WARNING", message="Username Already Taken Use Different One!")

            else:
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                if img[0] == None:
                    cursor.execute("insert into user_names (user_name,user_id,image) values(?,?,?)",(username.get(),user_id.get(),None))
                    connection.commit()
                    connection.close()
                    notebook.select(login)

                else:
                    cursor.execute("insert into user_names (user_name,user_id,image) values(?,?,?)",(username.get(),user_id.get(),img[0]))
                    connection.commit()
                    connection.close()
                    notebook.select(login)
                                    
    def convert_to_binary(file_path):
        with open(file_path, 'rb') as file:
            binary_data = file.read()
        return binary_data

    img = [None]
    def upload():
        file_path = askopenfilename()
        binary_img = convert_to_binary(file_path)
        img[0] = binary_img
                

    ctk.CTkLabel(sub_frame,text = "FINALE DETAILS",font=("calibri",22,"bold"),text_color="white").grid(row=0,column=0,sticky="w",padx=45,pady=10)

    frame1 = ctk.CTkFrame(sub_frame,fg_color="#0A082D")
    frame1.grid(row=1,column=0,columnspan=2,pady=20,padx=25)

    countries = ("Sri Lanka","India","United States", "China", "India","Pakistan","Bangaladesh","Germany", "France", "Japan", "United Kingdom", "Canada", "Australia")
    country_var=ctk.StringVar(value=countries[0])
    country = ctk.CTkComboBox(frame1,width=300,height=35,fg_color = "#2c344d",text_color="white",
                       border_color="#2E3756",border_width = 2,variable = country_var,
                              button_color="#58637f",dropdown_font=("calibri",17,"bold"),dropdown_text_color="white",
                              dropdown_fg_color="black")
    country.configure(values=countries)
    country.grid(row=0,column=0,padx=20)

    ctk.CTkLabel(frame1,text = "SELECT YOUR COUNTRY",font=("calibri",17,"bold"),text_color="white").grid(row=1,column=0,sticky="w",padx=20)

    frame2 = ctk.CTkFrame(sub_frame,fg_color="#0A082D")
    frame2.grid(row=2,column=0,columnspan=2,pady=20,padx=5)
    username = ctk.CTkEntry(frame2,width=300,height=35,fg_color = "#2c344d",font=("calibri",18),
                       border_color="#2E3756",border_width = 2,text_color="white")
    username.grid(row=0,column=0,padx=20)
    ctk.CTkLabel(frame2,text = "USER NAME",font=("calibri",18,"bold"),text_color="white").grid(row=1,column=0,sticky="w",padx=20)

    frame3 = ctk.CTkFrame(sub_frame,fg_color="#0A082D")
    frame3.grid(row=3,column=0,columnspan=2,pady=20,padx=5,sticky="ew")
    ctk.CTkButton(frame3,text="Upload",height=35,width=40,corner_radius=10,
                  font=("calibri",18,"bold"),command=upload).grid(row=0,column=0,sticky="w",padx=43)
    ctk.CTkLabel(frame3,text = "UPLOAD PROFILE",font=("calibri",18,"bold"),text_color="white").grid(row=2,column=0,sticky="w",padx=43)

    ctk.CTkButton(sub_frame,text = "Create Account",width=260,font = ("calibri",20,"bold"),fg_color="#BAD5CC",
                  border_color="#58637f",text_color="#0A082D",border_width = 2,command=validate,
                  height=50,corner_radius = 8).grid(row=4,column=0,columnspan=2,pady=20)

    ctk.CTkLabel(sub_frame,text = "Privacy Policy",text_color="white").grid(row=5,column=0,columnspan=2,pady=15)



