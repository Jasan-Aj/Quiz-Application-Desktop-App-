import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from entry_page import entry_page
from home_page import home
from log_in_page import login
from signup_page import signup
from final_details import final_details
from select_subject import select_sub
from select_level import select_level
from highscore import high_score
from start_quize import start_quizes
from current_score import current_high
from question_page_1 import quize_page
from normel_score import normel_score
from leader_board import laeder_board_func
from add_questions import add_question_func
from admin import admin_func
from leader_board_select import select_sub_leaderbaord
from manage_questions import manage_question
from manage_users import manage_users
from study_meterials import study_meterials_page
from add_meterials import add_meterials_page
from manage_materials import manage_study
from resourcse import resource_path
import os

class Quiz_application:

    def __init__(self,window):

        self.resource_path = resource_path
        images_folder_path = self.resource_path('images')        
        self.database = os.path.join(images_folder_path, 'quize_app.db')
        
        self.window=window
        self.window.title("Quize Application")
        self.window.geometry("1400x750")

        self.notebook=ttk.Notebook(self.window)
        self.notebook.pack(fill="both",expand=True)

        self.entry_page = ctk.CTkFrame(self.window)
        self.home_page = ctk.CTkFrame(self.window)
        self.login_page = ctk.CTkFrame(self.window)
        self.signup_page = ctk.CTkFrame(self.window)
        self.select_subject_page = ctk.CTkFrame(self.window)
        self.final_details_page = ctk.CTkFrame(self.window)
        self.select_level_page = ctk.CTkFrame(self.window)
        self.high_score_page = ctk.CTkFrame(self.window)
        self.start_page = ctk.CTkFrame(self.window)
        self.current_high_page = ctk.CTkFrame(self.window)
        self.quize_page = ctk.CTkFrame(self.window)
        self.normel_score_page = ctk.CTkFrame(self.window)
        self.leader_board_page = ctk.CTkFrame(self.window)
        self.add_question_page = ctk.CTkFrame(self.window)
        self.admin_page = ctk.CTkFrame(self.window)
        self.select_sub_leaderboard = ctk.CTkFrame(self.window)
        self.manage_quiz_tab = ctk.CTkFrame(self.window)
        self.manage_users_tab = ctk.CTkFrame(self.window)
        self.study_meterials_tab = ctk.CTkFrame(self.window)
        self.add_meterials_tab = ctk.CTkFrame(self.window)
        self.manage_meterials_tab = ctk.CTkFrame(self.window)

        style = ttk.Style()
        style.layout("TNotebook.Tab",[])

        self.notebook.add(self.entry_page,text = "Entry")
        self.notebook.add(self.home_page,text = "Home")
        self.notebook.add(self.login_page,text = "Login")
        self.notebook.add(self.signup_page,text = "Signup")
        self.notebook.add(self.select_subject_page,text = "Select sub")
        self.notebook.add(self.final_details_page,text = "final")
        self.notebook.add(self.select_level_page,text = "level")
        self.notebook.add(self.high_score_page,text = "high score")
        self.notebook.add(self.start_page,text = "start page")
        self.notebook.add(self.current_high_page,text = "high page")
        self.notebook.add(self.quize_page,text = "quize page")
        self.notebook.add(self.normel_score_page,text = "normel score")
        self.notebook.add(self.leader_board_page,text = "leaderboard")
        self.notebook.add(self.add_question_page,text = "add question")
        self.notebook.add(self.admin_page,text = "admin")
        self.notebook.add(self.select_sub_leaderboard,text = "select leader")
        self.notebook.add(self.manage_quiz_tab,text = "manage quiz")
        self.notebook.add(self.manage_users_tab,text = "manage users")
        self.notebook.add(self.study_meterials_tab,text = "study page")
        self.notebook.add(self.add_meterials_tab,text = "add page")
        self.notebook.add(self.manage_meterials_tab,text = "manage materias")
        

        def qstn_func():
            qstn_run()

        def current_score_run():
            current_run()

        def start_quize_func():
            start_quize_run()

        def normel_score_run():
            normel_func()

        def manage_qstn_func():
            manage_qstn_run("")

        def manage_users_run():
            manage_users_func()

        def study_func():
            study_run("")

        def manage_study_func():
            manage_study_run("")
            
        entry_page(self.entry_page,self.notebook,self.login_page,self.signup_page,self.resource_path)

        user_id=login(self.login_page,self.notebook,self.entry_page,self.signup_page,self.database,self.home_page,self.admin_page,self.resource_path)

        signup_user_id = signup(self.signup_page,self.notebook,self.entry_page,self.login_page,self.final_details_page,self.database,self.resource_path)

        home(self.home_page,self.notebook,self.select_subject_page,self.resource_path,user_id,self.database,self.login_page,
             self.select_level_page,self.select_sub_leaderboard,self.study_meterials_tab,study_func)

        final_details(self.final_details_page,self.notebook,self.database,self.login_page,signup_user_id,self.resource_path,self.signup_page)

        select_sub(self.select_subject_page,self.notebook,self.select_level_page,self.resource_path,self.home_page,self.database,user_id)

        select_level(self.select_level_page,self.notebook,self.resource_path,self.select_subject_page,self.start_page,start_quize_func,self.database,user_id)

        high_score_func = high_score(self.high_score_page,self.resource_path,self.notebook,self.quize_page,qstn_func,self.home_page,self.database,user_id)

        start_quize_run = start_quizes(self.start_page,self.resource_path,self.notebook,self.current_high_page,current_score_run,self.database,user_id)

        current_run =current_high(self.current_high_page,self.resource_path,self.notebook,qstn_func,self.quize_page,self.database,user_id,self.select_subject_page)

        qstn_run =quize_page(self.quize_page,self.notebook,self.high_score_page,high_score_func,self.database,self.resource_path,self.home_page,user_id,
                             self.normel_score_page,normel_score_run)

        normel_func = normel_score(self.normel_score_page,self.resource_path,self.notebook,self.quize_page,qstn_func,self.home_page,self.database,user_id)

        leaderboard_run = laeder_board_func(self.leader_board_page,self.notebook,self.resource_path,self.database,self.home_page,user_id)

        admin_func(self.admin_page,self.notebook,self.resource_path,self.manage_quiz_tab,manage_qstn_func,self.add_question_page,self.manage_users_tab,manage_users_run,
                   self.add_meterials_tab,self.manage_meterials_tab,manage_study_func,self.login_page)

        add_question_func(self.add_question_page,self.notebook,self.resource_path,self.database,self.admin_page)

        select_sub_leaderbaord(self.select_sub_leaderboard,self.notebook,self.leader_board_page,self.resource_path,self.home_page,self.database,user_id,leaderboard_run)

        manage_qstn_run = manage_question(self.manage_quiz_tab,self.notebook,self.resource_path,self.database,self.admin_page)

        manage_users_func = manage_users(self.manage_users_tab,self.notebook,self.resource_path,self.database,self.admin_page)

        study_run = study_meterials_page(self.study_meterials_tab,self.notebook,self.resource_path,self.database,self.home_page)

        add_meterials_page(self.add_meterials_tab,self.notebook,self.resource_path,self.database,self.admin_page)

        manage_study_run = manage_study(self.manage_meterials_tab,self.notebook,self.resource_path,self.database,self.admin_page)
        
       
if __name__ == "__main__":
    window=ctk.CTk()
    app=Quiz_application(window)
    #app.main()
    app.window.mainloop()


