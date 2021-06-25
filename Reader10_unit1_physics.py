"""this the main code which read question from text file"""

from tkinter import *
import Pmw
from tkinter import ttk
from tkinter import messagebox
import time

class Question_reader:
    
    def __init__(self,master,question_file,answer_file,AnswerIndex):
        self.win = Toplevel(master)
        self.win.title('Exam Book')
        self.win.config(bg='powder blue')
        y=((self.win.winfo_screenheight())/2)-350
        x=((self.win.winfo_screenwidth())/2)-360
        self.win.geometry(("680x650+"+str(int(x))+"+"+str(int(y))))
        self.tops=Frame(self.win,height=50,relief=GROOVE,bg='white')#33CCCC
        self.tops.pack(anchor=NE,padx=20)

        self.me = 'wubshet'
        self.submit_btn = Button(self.tops,text='submit',bg='DeepSkyBlue4',fg='white',padx=10,font=('Calibri (Body)',12,'bold'),
                               command=self.evaluator,relief=FLAT)
        self.submit_btn.grid(column=4,row=1,padx=5)
        self.submit_btn.bind('<Enter>',self.submit_btn_enter)
        self.submit_btn.bind('<Leave>',self.submit_btn_leave)
        
        self.output_sign = []
        self.each_question_var = []
        self.all_choice = []
        self.mark_counter = []
        
        self.answer_index = AnswerIndex
        #########place of answer index###############################################
        #pmw frame_______________
        
        sf = Pmw.ScrolledFrame(self.win,borderframe = 0,usehullsize=0,hull_width=400, hull_height=220)
        sf.pack(padx=5, pady=3, fill=BOTH, expand=True)
        scroll_frame = sf.interior() 
 
        scroll_frame.configure(background = 'white')
        ###########################################################################
        ###################################################################################
        
        #_____read the question file and the answer file_________
        file = open(question_file,'r')
        self.each_question = file.read().split('===')
        self.file = open(answer_file)
        self.correct_answer=self.file.read().split('\n')
        #__________________________________________
        
        #loop over each question
        Label(scroll_frame,text = '     # choose the best answer from the given alternative.\n',
              bg = 'white',font = ('Cambria(Headings)',13,'italic','bold')).pack(anchor = NW,padx = 20)
        for num_of_question in range(len(self.each_question)):
            question_choice_list = self.each_question[num_of_question].split('\n')
            question_label = Label(scroll_frame,text = question_choice_list[1],bg = 'white',font = ('calibri',13))
            question_label.pack(anchor = NW,padx = 10)
            var = 'var'+str(num_of_question)
            var = StringVar()
            #loop over each choice in each question
            for num_of_choice in range(2,6):
                radio = Radiobutton(scroll_frame,text=question_choice_list[num_of_choice],
                                    variable = var,value = question_choice_list[num_of_choice],
                                    bg='white',fg = 'black',font = ('calibri',13))
                radio.pack(anchor=NW,padx =30)
                self.all_choice.append(question_choice_list[num_of_choice])
            self.each_question_var.append(var)
            Label(scroll_frame,text='\n',bg='white').pack()
        
        self.makeTimeButton()

        ###################################################################################
        ####################inserting image#############
        
        p1 = PhotoImage(file='grade10\\physics\\airplane.png')
        l = Label(scroll_frame, image=p1)
        l.place(x=200, y=640)
        l.image = p1
        #__________________________
        p2 = PhotoImage(file='grade10\\physics\\Capture1.png')
        l = Label(scroll_frame, image=p2)
        l.place(x=85, y=1630)
        l.image = p2
        # __________________________
        p2 = PhotoImage(file='grade10\\physics\\Capture2.png')
        l = Label(scroll_frame, image=p2)
        l.place(x=85, y=1670)
        l.image = p2
        
    def evaluator(self):
        self.Stop()
        self.icon_right = PhotoImage(file='icon\icon_right.png')
        self.icon_wrong = PhotoImage(file='icon\icon_wrong.png')
        i = 0
        self.output_sign.clear()
        self.mark_counter.clear()
        for number_of_var in range(len(self.each_question_var)):
            your_choice = self.each_question_var[number_of_var].get()
            if your_choice == self.all_choice[self.answer_index[i]]:
                self.output_sign.append(self.icon_right)
                self.mark_counter.append(number_of_var)
            else:
                self.output_sign.append(self.icon_wrong)   
            i = i+1
        self.show_result()
        self.win.destroy()

        
    def show_result(self):
        
        
        self.result_win = Toplevel(self.win)
        self.result_win.resizable(height=False,width=False)
        y=((self.result_win.winfo_screenheight())/2)-250
        x=((self.result_win.winfo_screenwidth())/2)-250
        self.result_win.geometry(("318x500+"+str(int(x+150))+"+"+str(int(y))))
        self.result_win.title('Result')
        
        self.result_win.transient(self.win)
        f1 = Frame(self.result_win,height=35,relief=GROOVE)
        f1.pack(side=TOP,fill=X)
        sf = Pmw.ScrolledFrame(self.result_win,borderframe = 0,usehullsize=0,hull_width=400, hull_height=100)
        sf.pack(fill=BOTH, expand=True)
        scroll_frame = sf.interior() 
        f2 = Frame(scroll_frame,relief=GROOVE,width=100)
        f2.pack(side=LEFT,padx=20,fill=BOTH,expand=True)
        
        f3 = Frame(scroll_frame,relief=GROOVE,width=100)
        f3.pack(side=RIGHT,padx=20,fill=BOTH,expand=True)
        
        f4=Frame(scroll_frame,width=1,relief=RAISED,bg='grey')
        f4.pack(side=RIGHT,fill=BOTH,expand=True)
        
        
        if len(self.mark_counter)<=len(self.each_question)/2:
            f1.configure(bg='red')
        elif len(self.mark_counter)<len(self.each_question)*3/4:
            f1.configure(bg='yellow')
        if len(self.mark_counter)>=len(self.each_question)*3/4:
            f1.configure(bg='green')    
        
        y=((self.result_win.winfo_screenheight())/2)-150
        x=((self.result_win.winfo_screenwidth())/2)-200
        
        Label(f2,text='Your answer',font=('chiller',17)).grid(column = 0,row = 0)
        for q in range(len(self.output_sign)):
            Label(f2,text = '%d.'%(q+1),font=('areal',20)).grid(column = 0,row = q+1)
            lbl = Label(f2,image = self.output_sign[q],font=('areal',20))
            lbl.grid(column = 1,row = q+1)
        bottom_f=Frame(self.result_win)
        bottom_f.pack()
        self.okBtn=Button(bottom_f,text='ok',width=15,bg='DeepSkyBlue4',fg='white',font=('Calibri (Body)',12,'bold'),relief=FLAT,command = self.result_win_destroy)
        self.okBtn.grid(column=1,row=0)
        self.okBtn.bind('<Enter>',self.okBtn_enter)
        self.okBtn.bind('<Leave>',self.okBtn_leave)

        mark=len(self.mark_counter)
        all_q=len(self.output_sign)
        
        Label(bottom_f,text='Result: %d/%d'%(mark,all_q),font=('Courier New',15,'bold')).grid(column=0,row=0,padx=13)
        
        #____writing the coorect answer_________
        Label(f3,text='Correct answer',font=('chiller',17)).grid(column=0,row=0)
        
        
        for i in range(len(self.correct_answer)):
            Label(f3,text='%d.  %s'%(i+1,self.correct_answer[i]),font=('areal',17)).grid(column = 0,row = i+1)
            
            
            
        
        self.result_win.mainloop()
    def result_win_destroy(self):
        self.Reset()
        self.result_win.destroy()
    #================events for color change=======================
    def submit_btn_enter(self,event):
        self.submit_btn.config(bg='DeepSkyBlue3')
    def submit_btn_leave(self,event):
        self.submit_btn.config(bg='DeepSkyBlue4')   
    def okBtn_enter(self,event):
        self.okBtn.config(bg='DeepSkyBlue3')
    def okBtn_leave(self,event):
        self.okBtn.config(bg='DeepSkyBlue4')
    def start_enter(self,event):
        self.start.config(bg='DeepSkyBlue3')
    def start_leave(self,event):
        self.start.config(bg='DeepSkyBlue4')
    def stop_enter(self,event):
        self.stop.config(bg='DeepSkyBlue3')
    def stop_leave(self,event):
        self.stop.config(bg='DeepSkyBlue4')
    def reset_enter(self,event):
        self.reset.config(bg='DeepSkyBlue3')
    def reset_leave(self,event):
        self.reset.config(bg='DeepSkyBlue4') 
    #_____________________________________________    
                   
#stopwatch class is the following        
    def makeTimeButton(self):
        self.msec = 50
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = False
        self.timestr = StringVar()
        self.makeWidgets()
        self.start=Button(self.tops,text='Start',command=self.Start,bg='DeepSkyBlue4',fg='white',font=('Calibri (Body)',12,'bold'),relief=FLAT,padx=20)
        self.start.grid(column=1,row=1,padx=5)
        self.stop=Button(self.tops,text='Stop',command=self.Stop,state=DISABLED,bg='DeepSkyBlue4',fg='white',font=('Calibri (Body)',12,'bold'),relief=FLAT,padx=20)
        self.stop.grid(column=2,row=1,padx=5)
        self.reset=Button(self.tops,text='Reset',command=self.Reset,state=DISABLED,bg='DeepSkyBlue4',fg='white',font=('Calibri (Body)',12,'bold'),relief=FLAT,padx=20)
        self.reset.grid(column=3,row=1,padx=5)
        #binding the time button
        self.start.bind('<Enter>',self.start_enter)
        self.start.bind('<Leave>',self.start_leave)
        self.stop.bind('<Enter>',self.stop_enter)
        self.stop.bind('<Leave>',self.stop_leave)
        self.reset.bind('<Enter>',self.reset_enter)
        self.reset.bind('<Leave>',self.reset_leave)
    def makeWidgets(self):
        l = Label(self.tops,textvariable=self.timestr,font=('areal',14,'bold'),bg='white',fg='DeepSkyBlue4')
        self._setTime(self._elapsedtime)
        l.grid(column=4,row=0)
    
    def _update(self):
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.win.after(self.msec, self._update)
        
    def _setTime(self,elap):
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        
        self.timestr.set('%02d:%02d' % (minutes, seconds))
        
    def Start(self):
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = True
            self.stop.config(state=NORMAL)
            self.reset.config(state=NORMAL)
            
    def Stop(self):
        if self._running:
            self.win.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = False
    
    def Reset(self):
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)

    def addimage(self):
        p1=PhotoImage(file='grade10\\physics\\airplane.png')
        l=Label(scroll_frame,image=p1)
        l.place(x=100,y=300)
        l.image=p1
#root = Tk()
#app=Question_reader(root,'grade10\\physics\\unit1_ques.txt','grade10\\physics\\unit1_ans.txt', [2,7,11,14,17,22,26,31,33,39])
#root.mainloop()        
