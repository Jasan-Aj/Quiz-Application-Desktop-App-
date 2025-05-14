import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import random
from functools import partial
import sqlite3

window = tk.Tk()
window.geometry("500x500")
def run():
    main_frame = ctk.CTkFrame(window,fg_color="white")
    main_frame.pack(fill="both",expand = True)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=0)
    main_frame.rowconfigure(2,weight=1)
    main_frame.columnconfigure(0,weight=1)

    nav = ctk.CTkFrame(main_frame,fg_color="#0A082D",corner_radius=0)
    nav.grid(row=0,column=0,sticky="nsew")

    nav.columnconfigure(0,weight=1)
    nav.columnconfigure(1,weight=1)
    nav.columnconfigure(2,weight=1)
    nav.rowconfigure(2,weight=1)

    ctk.CTkLabel(nav,text="ADD QUESTIONS",font=("impact",35)).grid(row=0,column=1,pady=10)
    
    body=ctk.CTkScrollableFrame(main_frame,fg_color="aqua")
    body.grid(row=2,column=0,sticky="nswe")
    body.columnconfigure(0,weight=1)
    body.rowconfigure(0,weight=2)

    
    row=0
    column=5

    user_frame = ctk.CTkFrame(body,fg_color="white")
    user_frame.grid(row=0,column=0,pady=20)

    ctk.CTkLabel(user_frame,text = "user id",font= ("calibri",22),text_color="black").grid(row=0,column=0,padx=40)
    ctk.CTkLabel(user_frame,text = "User name",font= ("calibri",22),text_color="black").grid(row=0,column=1,padx=40)
    ctk.CTkLabel(user_frame,text = "",font= ("calibri",22),text_color="black").grid(row=0,column=2,padx=40)

    
    ctk.CTkLabel(user_frame,text="1",fg_color="#0A082D",font= ("calibri",20),text_color="white").grid(row=1,column=0,padx=20,pady=15,sticky="ew")   
    ctk.CTkLabel(user_frame,text="Username",fg_color="#0A082D",font= ("calibri",20),text_color="white").grid(row=1,column=1,padx=20,sticky="ew")
    ctk.CTkButton(user_frame,text="Remove",fg_color="#0A082D",font= ("calibri",20),text_color="white").grid(row=1,column=2,padx=20,sticky="ew")
  
run()
window.mainloop()
