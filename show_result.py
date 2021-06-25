"""this the main code which read question from text file"""

from tkinter import *
import Pmw
from tkinter import ttk
from tkinter import messagebox
import time


class Question_reader:

    def __init__(self, master, question_file):
        self.win = Toplevel(master)
        self.win.title('Exam Book')
        self.win.config(bg='powder blue')
        y = ((self.win.winfo_screenheight()) / 2) - 350
        x = ((self.win.winfo_screenwidth()) / 2) - 360
        self.win.geometry(("680x650+" + str(int(x)) + "+" + str(int(y))))
        self.tops = Frame(self.win, height=50, relief=GROOVE, bg='white')  # 33CCCC
        self.tops.pack(anchor=NE, padx=20)


        #self.submit_btn.grid(column=4, row=1, padx=5)
        #self.submit_btn.bind('<Enter>', self.submit_btn_enter)
        #self.submit_btn.bind('<Leave>', self.submit_btn_leave)

        self.output_sign = []
        self.each_question_var = []
        self.all_choice = []

        #########place of answer index###############################################
        # pmw frame_______________

        sf = Pmw.ScrolledFrame(self.win, borderframe=0, usehullsize=0, hull_width=400, hull_height=220)
        sf.pack(padx=5, pady=3, fill=BOTH, expand=True)
        scroll_frame = sf.interior()

        scroll_frame.configure(background='white')

        # _____read the question file and the answer file_________
        file = open(question_file, 'r')
        self.each_question = file.read().split('===')
        #
        # self.file = open(answer_file)
        #self.correct_answer = self.file.read().split('\n')
        # __________________________________________

        # loop over each question
        Label(scroll_frame, text='     # choose the best answer from the given alternative.\n',
              bg='white', font=('Cambria(Headings)', 13, 'italic', 'bold')).pack(anchor=NW, padx=20)
        for num_of_question in range(len(self.each_question)):
            question_choice_list = self.each_question[num_of_question].split('\n')
            question_label = Label(scroll_frame, text=question_choice_list[1], bg='white', font=('calibri', 13))
            question_label.pack(anchor=NW, padx=10)
            var = 'var' + str(num_of_question)
            var = StringVar()
            # loop over each choice in each question
            for num_of_choice in range(2, 6):
                radio = Radiobutton(scroll_frame, text=question_choice_list[num_of_choice],
                                    variable=var, value=question_choice_list[num_of_choice],
                                    bg='white', fg='black', font=('calibri', 13))
                radio.pack(anchor=NW, padx=30)
                self.all_choice.append(question_choice_list[num_of_choice])
            self.each_question_var.append(var)
            Label(scroll_frame, text='\n', bg='white').pack()
