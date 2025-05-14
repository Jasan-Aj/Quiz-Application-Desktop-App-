import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

time_lap = 10        
poster1_x1 = 0.06
poster1_x = 1


def entry_page(tab,notebook,login_page,signup_page,path):
    main_frame = ctk.CTkFrame(tab,fg_color= "#0A082D",corner_radius=0)
    main_frame.pack(fill="both",expand = True)

    sub_frame = ctk.CTkFrame(main_frame,fg_color= "#0A082D")
    sub_frame.pack(fill="y",expand = True)

    sub_frame.rowconfigure(0,weight=0)
    sub_frame.rowconfigure(1,weight=1)
    sub_frame.rowconfigure(2,weight=1)

    image_path1 = path('images/app1.png')
    tab.img1 = ctk.CTkImage(light_image=Image.open(image_path1),size=(530,360))

    image_path2 = path('images/pic1.png')
    tab.img2 = ctk.CTkImage(light_image=Image.open(image_path2),size=(545,365))

    image_path3 = path('images/pic2.png')
    tab.img3 = ctk.CTkImage(light_image=Image.open(image_path3),size=(545,365))

    image_path3 = path('images/pic3.png')
    tab.img4 = ctk.CTkImage(light_image=Image.open(image_path3),size=(545,365))


    def move_poster_1():
        global poster1_x
        poster1_x-=0.005
        poster1.place(relx = poster1_x,rely=0)
        if poster1_x>0.06:
           posters_frame.after(2,move_poster_1)
           
        else:
            time_pass()
            poster1_x=1

    def time_pass():
        global time_lap
        time_lap-=0.5
        if time_lap>0:
            posters_frame.after(200,time_pass)

        else:
            move_2()
            time_lap=10
        
    def move_2():
        global poster1_x1
        poster1_x1-=0.005
        poster1.place(relx = poster1_x1,rely=0.00)
        if poster1_x1>-1:
             posters_frame.after(2,move_2)

        else:
            move_poster_2()
            poster1_x1 = 0.06

    ###############################################################

    def move_poster_2():
        global poster1_x
        poster1_x-=0.005
        poster2.place(relx = poster1_x,rely=0.0)
        if poster1_x>0.06:
           posters_frame.after(2,move_poster_2)

        else:
            time_pass2()
            poster1_x=1
            
    def time_pass2():
        global time_lap
        time_lap-=0.5
        if time_lap>0:
            posters_frame.after(200,time_pass2)

        else:
            move_after_one()
            time_lap=10

    def move_after_one():
        global poster1_x1
        poster1_x1-=0.005
        poster2.place(relx = poster1_x1,rely=0.00)
        if poster1_x1>-1:
             posters_frame.after(2,move_after_one)

        else:
            move_poster_3()
            poster1_x1 = 0.06

    ###############################################################

    def move_poster_3():
        global poster1_x
        poster1_x-=0.005
        poster3.place(relx = poster1_x,rely=0.0)
        if poster1_x>0.06:
           posters_frame.after(2,move_poster_3)

        else:
            time_pass3()
            poster1_x=1
            
    def time_pass3():
        global time_lap
        time_lap-=0.5
        if time_lap>0:
            posters_frame.after(200,time_pass3)

        else:
            move_after_three()
            time_lap=10

    def move_after_three():
        global poster1_x1
        poster1_x1-=0.005
        poster3.place(relx = poster1_x1,rely=0.0)
        if poster1_x1>-1:
             posters_frame.after(2,move_after_three)

        else:
            move_poster_4()
            poster1_x1 = 0.06

    ###############################################################

    def move_poster_4():
        global poster1_x
        poster1_x-=0.005
        poster4.place(relx = poster1_x,rely=0.00)
        if poster1_x>0.06:
           posters_frame.after(2,move_poster_4)

        else:
            time_pass4()
            poster1_x=1
            
    def time_pass4():
        global time_lap
        time_lap-=0.5
        if time_lap>0:
            posters_frame.after(200,time_pass4)

        else:
            move_after_four()
            time_lap=10

    def move_after_four():
        global poster1_x1
        poster1_x1-=0.005
        poster4.place(relx = poster1_x1,rely=0.00)
        if poster1_x1>-1:
             posters_frame.after(2,move_after_four)

        else:
            move_poster_1()
            poster1_x1 = 0.06

    
    posters_frame = ctk.CTkFrame(sub_frame,width=600,height=405,fg_color="#0A082D")
    posters_frame.grid(row=1,column=0,columnspan=2)

    poster1= ctk.CTkFrame(posters_frame,fg_color = "#0A082D",width=550,height=430)
    poster1.place(relx = poster1_x,rely=0)

    ctk.CTkLabel(poster1,text="",image=tab.img1).place(rely=0,relx=0)
    ctk.CTkLabel(poster1,text="ATTEMPT THE QUIZE FROM ANYWHERE",text_color="white",font=("impact",36)).place(rely=0.84,relx=0.038)
    
    poster2= ctk.CTkFrame(posters_frame,fg_color = "#0A082D",width=550,height=430)
    poster2.place(relx = poster1_x,rely=0.0)

    ctk.CTkLabel(poster2,text="",image=tab.img2).place(rely=0,relx=0)
    ctk.CTkLabel(poster2,text="ACCESS STUDY MATERIALS",text_color="white",font=("impact",36)).place(rely=0.84,relx=0.155)

    poster3= ctk.CTkFrame(posters_frame,fg_color = "#0A082D",width=550,height=430)
    poster3.place(relx = poster1_x,rely=0.0)

    ctk.CTkLabel(poster3,text="",image=tab.img3).place(rely=0,relx=0)
    ctk.CTkLabel(poster3,text="ACHIEVE YOUR GOALS",text_color="white",font=("impact",36)).place(rely=0.84,relx=0.225)

    poster4= ctk.CTkFrame(posters_frame,fg_color = "#0A082D",width=550,height=430)
    poster4.place(relx = poster1_x,rely=0.00)

    ctk.CTkLabel(poster4,text="",image=tab.img4).place(rely=0,relx=0)
    ctk.CTkLabel(poster4,text="COMPETE WITH OTHERS",text_color="white",font=("impact",36)).place(rely=0.84,relx=0.18)

    btn_frame = ctk.CTkFrame(sub_frame,fg_color="#0A082D")
    btn_frame.grid(row=2,column=0,columnspan=2)

    ctk.CTkLabel(btn_frame,text = "Privacy Policy",text_color="white",font=("calibri",16)).pack()
    ctk.CTkButton(btn_frame,text = "SIGN UP FOR FREE",fg_color="#4355FF",
                  font = ("calibri",20,"bold"),command=lambda:notebook.select(signup_page),
                  width=260,height=50,corner_radius = 8 ).pack(pady=10)
    ctk.CTkButton(btn_frame,text = "OR LOG IN",width=260,font = ("calibri",20,"bold"),
                  command=lambda:notebook.select(login_page),
                  fg_color="#0A082D",border_color="#58637F",border_width = 2,
                  height=50,corner_radius = 8).pack(pady=10)

    if True:
       move_poster_1() 





