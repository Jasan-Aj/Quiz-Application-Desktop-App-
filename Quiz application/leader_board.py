import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3
import warnings

def laeder_board_func(tab,notebook,path,database,home,user_id):

    main_frame = ctk.CTkFrame(tab,fg_color= "#0A082D")
    main_frame.pack(fill="both",expand = True)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=1)

    main_frame.columnconfigure(0,weight=1)
    main_frame.columnconfigure(1,weight=1)
    main_frame.columnconfigure(2,weight=1)

    def back_func():
        connection= sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("delete from leaderboard_selection")
        connection.commit()
        connection.close()
        notebook.select(home)

    image_path4 = path('images/back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path4),size=(32,32))

    ctk.CTkButton(main_frame,text="",image=tab.back,height=43,fg_color="aqua",command = back_func,
                  width=40,corner_radius=25).grid(row=0,column=0,pady=15,sticky="w",padx=25,columnspan=2)

    image_path1 = path('images/leader.jpg')
    tab.leaderboard = ctk.CTkImage(light_image=Image.open(image_path1),size=(200,200))

    image_path2 = path('images/avatar.jpg')
    tab.default = ctk.CTkImage(light_image=Image.open(image_path2),size=(60,60))

    ctk.CTkLabel(main_frame,text="LEADER BOARD",font=("impact",35)).grid(row=0,column=1,pady=10)

    body = ctk.CTkFrame(main_frame,fg_color="white",corner_radius=0)
    body.grid(row=1,column=1,sticky="nswe")
    body.rowconfigure(0,weight=0)
    body.rowconfigure(1,weight=1)
    body.columnconfigure(0,weight=1)

    ctk.CTkLabel(body,text="",image=tab.leaderboard).grid(row=0,column=0)

    def run_leaderboard():

        subject = tk.StringVar()
        table = tk.StringVar()

        connection= sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("select subject from leaderboard_selection where user_id=?",(user_id.get(),))
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
        
        container=ctk.CTkScrollableFrame(body,corner_radius=25,fg_color="white")
        container.grid(row=1,column=0,sticky="nswe")
        container.columnconfigure(0,weight=1)

        warnings.filterwarnings("ignore", category=UserWarning, module="customtkinter")
        connection= sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute(f"SELECT user_id,score FROM {table.get()} ORDER BY score DESC")
        scores=cursor.fetchall()
        connection.close()

        ctk.CTkLabel(main_frame,text=f"{subject.get().upper()} LEADER BOARD",font=("impact",35),text_color="white").grid(row=0,column=1,pady=10,sticky="we")

        if scores == []:
            ctk.CTkLabel(container,text="No Users Parcticipated Yet!",fg_color="white",
                         font=("calibri",35,"bold"),text_color="black").grid(row=0,column=0,pady=20)


        else:
            
            rank = 1
            ranks_list = ["1st","2nd","3rd"]
            row = 0
            column = 0
            for score in scores:

                if rank == 1:
                    text = "black"
                    bg = "#6BC2C7"
                    rank_prefix = "st"

                elif rank == 2:
                    text = "black"
                    bg = "#74D5DA"
                    rank_prefix = "nd"

                elif rank == 3:
                    text = "black"
                    bg = "#A6E3E9"
                    rank_prefix = "rd"

                else:
                    text = "black"
                    bg = "#CBF1F5"
                    rank_prefix = "th"
        
                connection= sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("SELECT image from user_names WHERE user_id = ?", (score[0],))
                binary_data = cursor.fetchone()
        
                                
                if binary_data[0] == None:
                    img = tab.default
                
                else:
                    binary_data = binary_data[0]
                    with open('retrieved_image.jpg', 'wb') as file:
                        file.write(binary_data)
                    img = Image.open('retrieved_image.jpg')
                    img = img.resize((75, 75), Image.LANCZOS)
                    img = ImageTk.PhotoImage(img)

                
                cursor.execute("SELECT user_name from user_names WHERE user_id = ?", (score[0],))
                user_name = cursor.fetchone()

                cursor.execute(f"SELECT score from {table.get()} WHERE user_id = ?", (score[0],))
                retrived_score = cursor.fetchone()
                
                connection.close()

                participents_frame = ctk.CTkFrame(container,fg_color=bg,corner_radius=5)
                participents_frame.grid(row=row,column=column,sticky="ew",pady=3)

                participents_frame.columnconfigure(0,weight=1)
                participents_frame.columnconfigure(1,weight=1)
                participents_frame.columnconfigure(2,weight=3)

                ctk.CTkLabel(participents_frame,text=f"{rank}{rank_prefix}",fg_color=bg,font=("calibri",32,"bold"),text_color=text).grid(row=1,column=0,rowspan=2,sticky="w",padx=25)
                ctk.CTkLabel(participents_frame,text="",image=img,fg_color=bg,font=("calibri",17),text_color=text,corner_radius=20).grid(row=1,column=1,rowspan=2,pady=5,sticky="w",padx=20)
                ctk.CTkLabel(participents_frame,text=user_name,fg_color=bg,font=("calibri",25,"bold"),text_color=text).grid(row=1,column=2,sticky="w",padx=10)
                ctk.CTkLabel(participents_frame,text=f"score: {retrived_score[0]}",fg_color=bg,font=("calibri",23),text_color=text).grid(row=2,column=2,sticky="w",padx=10)

                row += 1
                rank+=1

    return run_leaderboard







