from tkinter import*
from tkinter import messagebox
class Adder:
    def __init__(self,where):
        self.Qpanel = Toplevel(where)
        self.Qpanel.transient(where)
        self.Qpanel.title('Question panel')
        self.Qpanel.config(bg='slategray1')
        self.Qpanel.resizable(height=False,width=False)
        y=((self.Qpanel.winfo_screenheight())/2)-300
        x=((self.Qpanel.winfo_screenwidth())/2)-360
        self.Qpanel.geometry(("630x365+"+str(int(x))+"+"+str(int(y))))
        
        #--------------------------------
        f1 = Frame(self.Qpanel,bg='slategray1')
        f1.pack(side=TOP)
        f2 = Frame(self.Qpanel,width=680,padx=30,bg='slategray1')
        f2.pack(side=LEFT)
        Label(f1,text='Question panel',bg='slategray1',font=('Calibri (Body)',24,'bold'),
              fg='DeepSkyBlue4').grid()
        Label(f2,text='Question: ',font=('Calibri (Body)',15,'bold'),bg='slategray1').grid(column=0,row=0,padx=10)
        
        
        Label(f2,text='Choices',font=('Calibri (Body)',15,'bold'),bg='slategray1').grid(column=0,row=1,padx= 0,pady=0)

        Label(f2,text='A:',font=('arial',18,),bg='slategray1').grid(column=0,row=2,padx= 0,pady=3)
        Label(f2,text='B:',font=('arial',18,),bg='slategray1').grid(column=0,row=3,padx= 0,pady=3)
        Label(f2,text='C:',font=('arial',18,),bg='slategray1').grid(column=0,row=4,padx= 0,pady=3)
        Label(f2,text='D:',font=('arial',18,),bg='slategray1').grid(column=0,row=5,padx= 0,pady=3)

        self.var_a = StringVar()
        self.var_b = StringVar()
        self.var_c = StringVar()
        self.var_d = StringVar()
        self.var_q = StringVar()
        
        self.question_entry = Entry(f2,width = 35,font=('arial',17,),insertwidth=0,bd=3,
                                    textvariable=self.var_q,bg='white',justify='left',relief=FLAT).grid(column=1,row=0,pady=20)
        self.choose_entry = Entry(f2,width = 38,font=('arial',16,),insertwidth=0,bd=3,textvariable=self.var_a,
                               bg='white',justify='left',relief=FLAT).grid(column=1,row=2)
        self.choose_entry = Entry(f2,width = 38,font=('arial',16,),insertwidth=0,bd=3,textvariable=self.var_b,
                               bg='white',justify='left',relief=FLAT).grid(column=1,row=3)
        self.choose_entry = Entry(f2,width = 38,font=('arial',16,),insertwidth=0,bd=3,textvariable=self.var_c,
                               bg='white',justify='left',relief=FLAT).grid(column=1,row=4)
        self.choose_entry = Entry(f2,width = 38,font=('arial',16,),insertwidth=0,bd=3,textvariable=self.var_d,
                               bg='white',justify='left',relief=FLAT).grid(column=1,row=5)
        f3 = Frame(f2,width=200,bg='slategray1')
        f3.grid(column=1,row=7,pady=20)
        self.BtnSave = Button(f3,text='Save',font=('arial',13,'bold'),bd=4,
                              bg='DeepSkyBlue4',fg='white',relief=FLAT,command=self.Save_theQuestion)
        self.BtnSave.grid(column=0,row=0,padx=10)
        self.BtnClear = Button(f3,text='Clear',font=('arial',13,'bold'),bd=4,
                              bg='DeepSkyBlue4',fg='white',relief=FLAT,command=self.clear)
        self.BtnClear.grid(column=1,row=0,padx=10)
        self.BtnExit = Button(f3,text='Exit',font=('arial',13,'bold'),bd=4,
                              bg='DeepSkyBlue4',fg='white',relief=FLAT,command=self.Qpanel.destroy,padx=10)
        self.BtnExit.grid(column=2,row=0,padx=10)
        #======binding hover color======
        self.BtnSave.bind('<Enter>',self.btnsave_enter)
        self.BtnSave.bind('<Leave>',self.btnsave_leave)
        
        self.BtnClear.bind('<Enter>',self.btnclear_enter)
        self.BtnClear.bind('<Leave>',self.btnclear_leave)
        
        self.BtnExit.bind('<Enter>',self.btnexit_enter)
        self.BtnExit.bind('<Leave>',self.btnexit_leave)
        #=====function hover color======
    def btnsave_enter(self,e):
        self.BtnSave.config(bg='DeepSkyBlue3')
    def btnsave_leave(self,e):
        self.BtnSave.config(bg='DeepSkyBlue4')
    def btnclear_enter(self,e):
        self.BtnClear.config(bg='DeepSkyBlue3')
    def btnclear_leave(self,e):
        self.BtnClear.config(bg='DeepSkyBlue4')
    def btnexit_enter(self,e):
        self.BtnExit.config(bg='DeepSkyBlue3')
    def btnexit_leave(self,e):
        self.BtnExit.config(bg='DeepSkyBlue4')

    def Save_theQuestion(self):
        self.question=self.var_q.get()
        self.choice_a=self.var_a.get()
        self.choice_b=self.var_b.get()
        self.choice_c=self.var_c.get()
        self.choice_d=self.var_d.get()
        if self.question == '':
            messagebox.showerror('error','the question is not inserted!')
        elif self.choice_a == '' or self.choice_b == '' or self.choice_c == '' or self.choice_d == '':
            ask = messagebox.showerror('error','all choices are not inserted!')
        else:
            file = open('user_question.txt','r')
            read_previuosfile = file.read()
            if len(read_previuosfile) > 0:
                file = open('user_question.txt','a')
                file.write('\n'+'===')
                file.write('\n'+self.question)
                file.write('\n'+'    '+'A.'+self.choice_a)
                file.write('\n'+'    '+'B.'+self.choice_b)
                file.write('\n'+'    '+'C.'+self.choice_c)
                file.write('\n'+'    '+'D.'+self.choice_d)
                file.close()
                messagebox.showinfo('add question','succefully saved')
            elif len(read_previuosfile) == 0:
                file = open('user_question.txt','w')
                file.write('\n'+self.question)
                file.write('\n'+'    '+'A.'+self.choice_a)
                file.write('\n'+'    '+'B.'+self.choice_b)
                file.write('\n'+'    '+'C.'+self.choice_c)
                file.write('\n'+'    '+'D.'+self.choice_d)
                messagebox.showinfo('add question','succefully saved')
    def clear(self):
        self.var_q.set('')
        self.var_a.set('')
        self.var_b.set('')
        self.var_c.set('')
        self.var_d.set('')     

