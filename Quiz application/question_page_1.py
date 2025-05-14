import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import random
from functools import partial
import textwrap
import sqlite3
from tkinter import messagebox

def quize_page(tab,notebook,high_score,high_score_func,database,path,home,user_id,
               normel_score,normel_score_func):
    main_frame = ctk.CTkFrame(tab,fg_color= "#0A082D")
    main_frame.pack(fill="both",expand = True)
    main_frame.columnconfigure(0,weight=1)
    main_frame.rowconfigure(0,weight=0)
    main_frame.rowconfigure(1,weight=1)

    image_path1 = path('images/back.png')
    tab.back = ctk.CTkImage(light_image=Image.open(image_path1),size=(32,32))

    def qstn_run():

        body = ctk.CTkScrollableFrame(main_frame,fg_color="#0A082D")
        body.grid(row=1,column=0,sticky="nswe")
        body.columnconfigure(0,weight=1)

        def move_togle():
            global togle_x
            togle_x+=0.005
            togle_frame.place(relx=togle_x,rely=0)
            if togle_x<0:
                main_frame.after(2,move_togle)

        def close_togle():
            global togle_x
            togle_x-=0.005
            togle_frame.place(relx=togle_x,rely=0)
            if togle_x>-0.5:
                main_frame.after(2,close_togle)
                
        sub = tk.StringVar()
        level = tk.StringVar()
        
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("select subject, level from selections where user_id = ?",(user_id.get(),))
        select = cursor.fetchall()
        sub.set(select[0][0])
        level.set(select[0][1])
        connection.close()


        options = {}
        questions={}
        answers = {}

        i=1

        if sub.get() == "python" and level.get() == "easy":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from python_easy")
            items = cursor.fetchall()
            
                
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        elif sub.get() == "python" and level.get() == "medium":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from python_medium")
            items = cursor.fetchall()
            
            
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        elif sub.get() == "python" and level.get() == "hard":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from python_hard")
            items = cursor.fetchall()
            
            
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        elif sub.get() == "java" and level.get() == "easy":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from java_easy")
            items = cursor.fetchall()
                
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        elif sub.get() == "java" and level.get() == "medium":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from java_medium")
            items = cursor.fetchall()
            
            
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        elif sub.get() == "java" and level.get() == "hard":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from java_hard")
            items = cursor.fetchall()
            
            
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        elif sub.get() == "Internet Tech" and level.get() == "easy":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from internet_tech_easy")
            items = cursor.fetchall()
                
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        elif sub.get() == "Internet Tech" and level.get() == "medium":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from internet_tech_medium")
            items = cursor.fetchall()
            
            
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        elif sub.get() == "Internet Tech" and level.get() == "hard":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from internet_tech_hard")
            items = cursor.fetchall()
            
            
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        elif sub.get() == "Accounting & Finance" and level.get() == "easy":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from accounting_easy")
            items = cursor.fetchall()
                
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        elif sub.get() == "Accounting & Finance" and level.get() == "medium":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from accounting_medium")
            items = cursor.fetchall()
            
            
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        elif sub.get() == "Accounting & Finance" and level.get() == "hard":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from accounting_hard")
            items = cursor.fetchall()
            
            
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        elif sub.get() == "Information System" and level.get() == "easy":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from information_easy")
            items = cursor.fetchall()
                
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        elif sub.get() == "Information System" and level.get() == "medium":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from information_medium")
            items = cursor.fetchall()
            
            
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        elif sub.get() == "Information System" and level.get() == "hard":
            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute("select quize ,answer ,option1 ,option2 ,option3 ,option4 from information_hard")
            items = cursor.fetchall()
            
            
            for item in items:
                questions[i]= item[0]
                options[i]=[item[2],item[3],item[4],item[5]]
                answers[i]=item[1]
                i+=1
                  
            connection.close()

        

        togle_x=-1
        togle_frame = ctk.CTkFrame(main_frame,fg_color="blue")
        togle_frame.place(relx=togle_x,rely=0)
        ctk.CTkButton(togle_frame,text="X",command=close_togle,width=20,height=0).grid(row=0,column=1)
        ctk.CTkButton(togle_frame,text="home").grid(row=1,column=0,pady=20)
        

        def select_next(state): 
            global count

            if count==len(questions):
              
                connection = sqlite3.connect(database)
                cursor = connection.cursor()
                cursor.execute("insert into score (user_id, score, count) values(?,?,?)",(user_id.get(),marks,len(questions)))
                connection.commit()
                
                if sub.get()=="python":
                    cursor.execute("SELECT MAX(score) FROM python_score")
                    highest_score = cursor.fetchone()

                    cursor.execute("SELECT MAX(score) FROM python_score where user_id=?",(user_id.get(),))
                    current_user_Hscore = cursor.fetchone()
                    
                    
                    if highest_score[0] == None:
                        highest_score=[0]

                    if current_user_Hscore[0] == None:
                        current_user_Hscore=[0]

                    if marks > highest_score[0]:
                        high_score_func()
                        notebook.select(high_score)

                    else:
                        normel_score_func()
                        notebook.select(normel_score)

                    if marks>current_user_Hscore[0]:
                        cursor.execute("delete from python_score where user_id=?",(user_id.get(),))
                        cursor.execute("insert into python_score (user_id, score) values(?,?)",(user_id.get(),marks))

                elif sub.get()=="java":
                    cursor.execute("SELECT MAX(score) FROM java_score")
                    highest_score = cursor.fetchone()

                    cursor.execute("SELECT MAX(score) FROM java_score where user_id=?",(user_id.get(),))
                    current_user_Hscore = cursor.fetchone()
                    
                    if highest_score[0] == None:
                        highest_score=[0]

                    if current_user_Hscore[0] == None:
                        current_user_Hscore=[0]
                        
                    if marks > highest_score[0]:
                        high_score_func()
                        notebook.select(high_score)

                    else:
                        normel_score_func()
                        notebook.select(normel_score)

                    if marks>current_user_Hscore[0]:
                        cursor.execute("delete from java_score where user_id=?",(user_id.get(),))
                        cursor.execute("insert into java_score (user_id, score) values(?,?)",(user_id.get(),marks))

                elif sub.get()=="Internet Tech":
                    cursor.execute("SELECT MAX(score) FROM internet_tech_score")
                    highest_score = cursor.fetchone()

                    cursor.execute("SELECT MAX(score) FROM internet_tech_score where user_id=?",(user_id.get(),))
                    current_user_Hscore = cursor.fetchone()
                    
                    if highest_score[0] == None:
                        highest_score=[0]

                    if current_user_Hscore[0] == None:
                        current_user_Hscore=[0]
                        
                    if marks > highest_score[0]:
                        high_score_func()
                        notebook.select(high_score)

                    else:
                        normel_score_func()
                        notebook.select(normel_score)

                    if marks>current_user_Hscore[0]:
                        cursor.execute("delete from internet_tech_score where user_id=?",(user_id.get(),))
                        cursor.execute("insert into internet_tech_score (user_id, score) values(?,?)",(user_id.get(),marks))

                elif sub.get()=="Information System":
                    cursor.execute("SELECT MAX(score) FROM information_system_score")
                    highest_score = cursor.fetchone()

                    cursor.execute("SELECT MAX(score) FROM information_system_score where user_id=?",(user_id.get(),))
                    current_user_Hscore = cursor.fetchone()
                    
                    if highest_score[0] == None:
                        highest_score=[0]

                    if current_user_Hscore[0] == None:
                        current_user_Hscore=[0]
                        
                    if marks > highest_score[0]:
                        high_score_func()
                        notebook.select(high_score)

                    else:
                        normel_score_func()
                        notebook.select(normel_score)

                    if marks>current_user_Hscore[0]:
                        cursor.execute("delete from information_system_score where user_id=?",(user_id.get(),))
                        cursor.execute("insert into information_system_score (user_id, score) values(?,?)",(user_id.get(),marks))

                elif sub.get()=="Accounting & Finance":
                    cursor.execute("SELECT MAX(score) FROM accounting_score")
                    highest_score = cursor.fetchone()

                    cursor.execute("SELECT MAX(score) FROM accounting_score where user_id=?",(user_id.get(),))
                    current_user_Hscore = cursor.fetchone()
                    
                    if highest_score[0] == None:
                        highest_score=[0]

                    if current_user_Hscore[0] == None:
                        current_user_Hscore=[0]
                        
                    if marks > highest_score[0]:
                        high_score_func()
                        notebook.select(high_score)

                    else:
                        normel_score_func()
                        notebook.select(normel_score)

                    if marks>current_user_Hscore[0]:
                        cursor.execute("delete from accounting_score where user_id=?",(user_id.get(),))
                        cursor.execute("insert into accounting_score (user_id, score) values(?,?)",(user_id.get(),marks))
                
                connection.commit()
                connection.close()
    

            elif state=="":
                messagebox.showwarning(title="WARNING", message="Pick any answer!")

            else:
                count+=1
                feed_back.configure(text="")
                increase_progress()
                run()

        def increase_progress():
            
            current_value = progress.get()
            increase_value = (10/len(questions))/10
            progress.set(current_value + increase_value)

        def start_count():
            global count
            total_qstns = len(questions)
            qstn_counting.configure(text = f"Question {count}/{total_qstns}")

        def start():
            if len(questions) == 0:
                messagebox.showwarning(title="WARNING", message="No Questions Added Yet!")

            else:  
                increase_progress()
                run()


        progress_frame = ctk.CTkFrame(body,fg_color="#0A082D")
        progress_frame.grid(row=0,column=0,pady=15)

        ctk.CTkButton(body,text="",image=tab.back,height=43,fg_color="aqua",
                  width=40,corner_radius=25,command= lambda:notebook.select(home)).grid(row=0,column=0,pady=15,sticky="w")

        progress = ctk.CTkProgressBar(progress_frame, width=600,fg_color= "#0FA4AF",height=25,progress_color="#964734")
        progress.pack()
        progress.set(0)
     
        global count
        count = 1

        global marks
        marks = 0

        def run():

            state = tk.StringVar(value = None)
            start_count()
            def validate(qstn_nmr,answer):
                global marks
                state.set("clicked")
                
                if answers[qstn_nmr]==answer:
                    feed_back.configure(text="Your Answer Is Correct",text_color="white",font=("roboto",20))
                    marks+=1

                else:
                    feed_back.configure(text=f"Correct Answer Is {answers[qstn_nmr]}",
                                        text_color="white",font=("roboto",20))

                answer_btn1.configure(state = "disabled")
                answer_btn2.configure(state = "disabled")
                answer_btn3.configure(state = "disabled")
                answer_btn4.configure(state = "disabled")

            
                
            content_frame = ctk.CTkFrame(body,fg_color="#0A082D",border_width=2,border_color="#58637f")
            content_frame.grid(row=2,column=0,pady=10)
                
            question_frame = ctk.CTkFrame(content_frame,fg_color ="#0A082D")
            question_frame.grid(row=1,column=0,padx=10,pady=5)
            question = ctk.CTkLabel(question_frame,text = questions[count],wraplength=400,justify="left",text_color="white",
                                    font=("roboto",21,"bold"),height=150,width=500)
            question.pack(padx=20,pady=10)

            answer_frame = ctk.CTkFrame(content_frame,fg_color="#0A082D",corner_radius = 10)
            answer_frame.grid(row=2,column=0,pady=10)

                

            answer_btn1 = ctk.CTkButton(answer_frame,text = options[count][0],fg_color="#0A082D",font=("roboto",18),corner_radius=20,anchor="w",
                            border_color="#58637f",border_width=2,width=400,height=60,text_color="white",command = partial(validate,count,options[count][0]))
            answer_btn1.grid(row=1,column=0,pady=10)

            answer_btn2 = ctk.CTkButton(answer_frame,text = options[count][1],anchor="w",fg_color="#0A082D",font=("roboto",18),corner_radius=20,
                            border_color="#58637f",border_width=2,width=400,height=60,text_color="white",command = partial(validate,count,options[count][1]))
            answer_btn2.grid(row=2,column=0,pady=10)

            answer_btn3 = ctk.CTkButton(answer_frame,text = options[count][2],fg_color="#0A082D",font=("roboto",18),corner_radius=20,anchor="w",
                            border_color="#58637f",border_width=2,width=400,height=60,text_color="white",command = partial(validate,count,options[count][2]))
            answer_btn3.grid(row=3,column=0,pady=10)

            answer_btn4 = ctk.CTkButton(answer_frame,text = options[count][3],fg_color="#0A082D",font=("roboto",18),corner_radius=20,anchor="w",
                            border_color="#58637f",border_width=2,width=400,height=60,text_color="white",command = partial(validate,count,options[count][3]))
            answer_btn4.grid(row=4,column=0,pady=10)
    
            ctk.CTkButton(content_frame,text="Next",command = lambda:select_next(state.get()),corner_radius=25,font=("roboto",19,"bold"),
                          width=105,height=48,fg_color="blue").grid(row=4,column=0,pady=10)

        feed_back = ctk.CTkLabel(body,text="",text_color="black",font=("roboto",15,"bold"))
        feed_back.grid(row=3,column=0)  

        start_btn = ctk.CTkButton(body,text="Start Quize",command = start,width=50,height=50,
                                  font=("roboto",20,"bold"),fg_color="red")
        start_btn.grid(row=2,column=0,pady=160)

        qstn_counting =ctk.CTkLabel(body,text="",text_color="white",font=("roboto",20,"bold"))
        qstn_counting.grid(row=1,column=0,pady=10)
    

    return qstn_run


