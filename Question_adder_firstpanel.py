        
####### the following function is popup window to ask the user to input the name of the question########        
    def Question_adder_firstpanel(self):
        self.SmallBox = Toplevel(self.master)
        self.SmallBox.title('Question panel')
        self.SmallBox.transient(self.master)
        self.SmallBox.config(bg='slategray1')
        self.SmallBox.resizable(width=False,height=False)
        y=((self.SmallBox.winfo_screenheight())/2)-220
        x=((self.SmallBox.winfo_screenwidth())/2)-210
        self.SmallBox.geometry(("350x210+"+str(int(x))+"+"+str(int(y))))
        f1=Frame(self.SmallBox,bg='slategray1')
        f1.pack(pady=20)
        self.f2=Frame(self.SmallBox,bg='slategray1')
        self.f2.pack(pady=20)
        Label(f1,text='Enter the name of the row in which\n you put in the User Question tap ',
              font=('Calibri (Body)',15,'bold'),bg='slategray1',fg='DeepSkyBlue4').grid(column=0,row=0,pady=10)
        
        #self.question_entry = Entry(self.f2,font=('Calibri (Body)',15),insertwidth=0,bd=6,bg='white')
        #self.question_entry.grid(column=0,row=0,padx=20)
        
        go_icon = PhotoImage(file='icon\\go.png')
        
        b=Button(self.f2,image=go_icon,relief=FLAT,bg='slategray1',command=self.open_addquestion)
        b.grid(column=1,row=0)
        b.image=go_icon
        
        
        ######################################################
