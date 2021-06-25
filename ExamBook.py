from tkinter import*
from tkinter import ttk
import shelve
import os
from tkinter import messagebox
import Reader
#importing specific readers
import Reader10_unit1_physics
import Reader10_unit2_physics
import Reader10_unit4_physics
import Reader9_unit1_physics
from Reader import Question_reader
import physics_constant
import show_result

class Home:
    """This class build the main(homepage) graphical part of the application"""
    def __init__(self,master):
        self.master = master
        i=PhotoImage(file='icon.png')
        self.master.iconphoto(self.master,i)
        self.master.title('E  x  a  m   B  o  o  k     2 0 1 0 ')
        self.master.config(bg='slategray1')
        y=((self.master.winfo_screenheight())/2)-380
        x=((self.master.winfo_screenwidth())/2)-690
        self.master.geometry(("1366x768+"+str(int(x))+"+"+str(int(y))))
        
        self.left_frame = Frame(self.master,width = 683,height=700,bg='slategray1')
        self.left_frame.pack(side=RIGHT)
        
        self.right_frame = Frame(self.master,width = 683,height=700,bg='white')
        self.right_frame.pack(side = LEFT)#,padx=3,pady=2)
        
        self.upper_frame=Frame(self.left_frame,width=450,height=350,bg='slategray1')
        self.upper_frame.pack(side=TOP)
        
        self.bottom_frame=Frame(self.left_frame,width=450,height=330,bg='slategray1')
        self.bottom_frame.pack(side=BOTTOM)
        #==============================
        exambook_frame=Frame(self.master,bg='white').pack(side=TOP)
        lbl=Label(self.right_frame,text='E X A M  B O O K  2 0 1 0',font=('Calibri (Body)',24,'bold'),bg='white',fg='DeepSkyBlue4').pack()
        lbl=Label(self.right_frame,text='       Question and answer from grade 7 - 10 based on Ethiopian Curriculum',font=('Calibri (Body)',8),bg='white').pack(pady=7)
        Label(self.bottom_frame,text='    '*27,bg='slategray1').grid(column = 0,row=0)
        self.btn_addquestion=Button(self.bottom_frame,bg='DeepSkyBlue4',fg='white',command=self.Question_adder_firstpanel,
                                    text='Add Question',font=('Calibri (Body)',12,'bold'),relief=FLAT)
        self.btn_addquestion.grid(column = 1,row=0)

        self.btn_addquestion.bind('<Enter>',self.btn_addquestion_enter)
        self.btn_addquestion.bind('<Leave>',self.btn_addquestion_leave)

        def_img = PhotoImage(file = 'icon_bg.png')
        label = Label(self.upper_frame,image = def_img)
        label.grid(padx=10,pady=50,column = 0,row=1)
        label.image=def_img    
        """the following code is used to read images that discribe each grade level and each subject.
        it is only list of image which used on the treeview selection"""
        
        self.img1=PhotoImage(file='')
        self.img2=PhotoImage(file='')
        #=========giving none name for the user defined question and update later below
        self.pass_rowname1 = None
        self.pass_rowname2 = None
        self.pass_rowname3 = None
        self.pass_rowname4 = None
        self.pass_rowname5 = None
        self.pass_rowname6 = None
        self.pass_rowname7 = None
        self.pass_rowname8 = None
        self.pass_rowname9 = None
        self.pass_rowname10 = None
        #=====
        self.pass_rowname11 = None
        self.pass_rowname12 = None
        self.pass_rowname13 = None
        self.pass_rowname14 = None
        self.pass_rowname15 = None
        self.pass_rowname16 = None
        self.pass_rowname17 = None
        self.pass_rowname18 = None
        self.pass_rowname19 = None
        self.pass_rowname20 = None

        self.Qpanel = None
        #the following are methods called from the below functions
        self.create_notebook()
        self.menubar(self.master)
        self.tree()
        self.atstart()
        #===============================
       
    def btn_addquestion_enter(self,event):
        self.btn_addquestion.config(bg='DeepSkyBlue3')
    def btn_addquestion_leave(self,event):
        self.btn_addquestion.config(bg='DeepSkyBlue4')    
    def create_notebook(self):

        style = ttk.Style()
        style.theme_create('MyStyle',
                           settings={'Treeview': {'configure': {'tabmargins': [10, 20, 15, 0]}},
                                     'TNotebook.Tab': {'configure': {'padding': [15, 7]}, }})
        #style.theme_use('MyStyle')
        
        notebook = ttk.Notebook(self.right_frame,width = 680,height = 700)
        notebook.pack(expand=YES, fill=BOTH,pady = 5,padx =5)
        self.frame_in_garde7 = Frame(bg='slategray1')
        self.frame_in_garde8 = Frame(bg='slategray1')
        self.frame_in_garde9 = Frame(bg='slategray1')
        self.frame_in_garde10 = Frame(bg='slategray1')
        self.frame_user_question = Frame(bg='slategray1')

        
        notebook.add(self.frame_in_garde7,text = 'grade 7',padding = 10)
        notebook.add(self.frame_in_garde8,text = 'grade 8',padding = 10)
        notebook.add(self.frame_in_garde9,text = 'grade 9',padding = 10)
        notebook.add(self.frame_in_garde10,text = 'grade 10',padding = 10)
        notebook.add(self.frame_user_question,text = 'User Question',padding = 10)
        Label(self.frame_in_garde7,text='grade 7 Exambook Question',font=('Hobo Std',17),bg='slategray1').pack(pady=10)
        Label(self.frame_in_garde8,text='grade 8 Exambook Question',font=('Hobo Std',17),bg='slategray1').pack(pady=10)
        Label(self.frame_in_garde9,text='grade 9 Exambook Question',font=('Hobo Std',17),bg='slategray1').pack(pady=10)
        Label(self.frame_in_garde10,text='grade 10 Exambook Question',font=('Hobo Std',17),bg='slategray1').pack(pady=10)
        Label(self.frame_user_question,text='User defined questions',font=('Hobo Std',17),bg='slategray1').pack(pady=10)


        
#=========creating treeview starts here================================
    def tree(self):
    #____________###########____________________grade 7 treewiw information__________________#######_________________
        self.tree_grade7 = ttk.Treeview(self.frame_in_garde7,selectmode=BROWSE,columns=("quanta"))
        self.tree_grade7.pack(expand=True,fill=BOTH)
        self.tree_grade7.heading('#0',text='Topics')
        #self.tree_grade7.heading('#1',text='images')
        self.tree_grade7.column(0, anchor=E)
        
        biology_7 = self.tree_grade7.insert("",index=END , text='Biology')
        chemistry_7 = self.tree_grade7.insert("",index=END , text='Chemistry')
        mathematics_7 = self.tree_grade7.insert("",index=END , text='Mathematics')
        physics_7 = self.tree_grade7.insert("",index=END , text='Physics')

     #grade7 biology topics
        g7_bio_unit1 = self.tree_grade7.insert(biology_7,index=END , text='Unit 1 :  Biology and Technology')
        g7_bio_unit2 = self.tree_grade7.insert(biology_7,index=END , text='Unit 2 :  Cell Biology')
        g7_bio_unit3 = self.tree_grade7.insert(biology_7,index=END , text='Unit 3 :  Human Biology and Health')
        g7_bio_unit4 = self.tree_grade7.insert(biology_7,index=END , text='Unit 4 :  Plants')
        g7_bio_unit5 = self.tree_grade7.insert(biology_7,index=END , text='Unit 5 :  Animals')
        g7_bio_unit6 = self.tree_grade7.insert(biology_7,index=END , text='Unit 6 :  Enviroment')

     #grade7 chemistry topics
        g7_chem_unit1 = self.tree_grade7.insert(chemistry_7,index=END , text='Unit 1 :  Chemistry and its important')
        g7_chem_unit2 = self.tree_grade7.insert(chemistry_7,index=END , text='Unit 2 :  Substance')
        g7_chem_unit3 = self.tree_grade7.insert(chemistry_7,index=END , text='Unit 3 :  The language of Chemistry')
        g7_chem_unit4 = self.tree_grade7.insert(chemistry_7,index=END , text='Unit 4 :  The structure of substances')
        g7_chem_unit5 = self.tree_grade7.insert(chemistry_7,index=END , text='Unit 5 :  Periodic Classification of the Element')

     #grade7 mathematics topics
        g7_math_unit1 = self.tree_grade7.insert(mathematics_7,index=END , text='Unit 1 :  Rational numbers')
        g7_math_unit2 = self.tree_grade7.insert(mathematics_7,index=END , text='Unit 2 :  Linear equations and Inequalities')
        g7_math_unit3 = self.tree_grade7.insert(mathematics_7,index=END , text='Unit 3 :  Ratio,Proportion and Percentage')
        g7_math_unit4 = self.tree_grade7.insert(mathematics_7,index=END , text='Unit 4 :  Data handling')
        g7_math_unit5 = self.tree_grade7.insert(mathematics_7,index=END , text='Unit 5 :  Geometric figure and measurment')

     #grade7 physics topics
        g7_phy_unit1 = self.tree_grade7.insert(physics_7,index=END , text='Unit 1 :  Physics and Measurment')
        g7_phy_unit2 = self.tree_grade7.insert(physics_7,index=END , text='Unit 2 :  Motion')
        g7_phy_unit3 = self.tree_grade7.insert(physics_7,index=END , text="Unit 3 :  Force and Newton's laws of motion")
        g7_phy_unit4 = self.tree_grade7.insert(physics_7,index=END , text='Unit 4 :  Work, Energy and Power')
        g7_phy_unit5 = self.tree_grade7.insert(physics_7,index=END , text='Unit 5 :  Simple machine')
        g7_phy_unit6 = self.tree_grade7.insert(physics_7,index=END , text='Unit 6 :  Temprature and Heat')
        g7_phy_unit7 = self.tree_grade7.insert(physics_7,index=END , text='Unit 7 :  Sound')
        g7_phy_unit8 = self.tree_grade7.insert(physics_7,index=END , text='Unit 8 :  Electricity and Magnetism')

        self.tree_grade7.bind("<Double-1>",lambda event:self.grade7_onDoubleClick(self.tree_grade7.item(self.tree_grade7.selection())['text']))
        self.tree_grade7.bind("<<TreeviewSelect>>",lambda event:self.ImageSender7(self.tree_grade7.item(self.tree_grade7.selection())['text']))
        #====call the yellow color when hover on=========
        self.tree_grade7.tag_configure('focus', background='slategray1')
        self.tree_grade7.bind("<Motion>", self.mycallback7)
        self.last_focus = None

    # ____________########____________________grade 8 treewiw information__________________#######_________________
        self.tree_grade8 = ttk.Treeview(self.frame_in_garde8,selectmode=BROWSE,columns=("quanta"))
        self.tree_grade8.pack(expand=True,fill=BOTH)
        self.tree_grade8.heading('#0',text='Topics')
        #self.tree_grade8.heading('#1',text='images')
        self.tree_grade8.column(0, anchor=E)
        biology_8 = self.tree_grade8.insert("",index=END , text='Biology')
        chemistry_8 = self.tree_grade8.insert("",index=END , text='Chemistry')
        mathematics_8 = self.tree_grade8.insert("",index=END , text='Mathematics')
        physics_8 = self.tree_grade8.insert("",index=END , text='Physics')

        #grade8 biology topics

        g8_bio_unit1 = self.tree_grade8.insert(biology_8, index=END, text='Unit 1 :  Biology and Technology')
        g8_bio_unit2 = self.tree_grade8.insert(biology_8, index=END, text='Unit 2 :  Cell Biology')
        g8_bio_unit3 = self.tree_grade8.insert(biology_8, index=END, text='Unit 3 :  Human Biology and Health')
        g8_bio_unit4 = self.tree_grade8.insert(biology_8, index=END, text='Unit 4 :  Plants')
        g8_bio_unit5 = self.tree_grade8.insert(biology_8, index=END, text='Unit 5 :  Animals')
        g8_bio_unit6 = self.tree_grade8.insert(biology_8, index=END, text='Unit 6 :  Enviroment')

        # grade8 chemistry topics

        g8_chem_unit1 = self.tree_grade8.insert(chemistry_8, index=END, text='Unit 1 :  Classification of compounds')
        g8_chem_unit2 = self.tree_grade8.insert(chemistry_8, index=END, text='Unit 2 :  Some important metals')
        g8_chem_unit3 = self.tree_grade8.insert(chemistry_8, index=END, text='Unit 3 :  Some important non-metals')
        g8_chem_unit4 = self.tree_grade8.insert(chemistry_8, index=END, text='Unit 4 :  Enviromental chemistry')
        g8_chem_unit5 = self.tree_grade8.insert(chemistry_8, index=END, text='Unit 5 :  Calculations based on formulas')

        # grade8 mathematics topics
        g8_math_unit1 = self.tree_grade8.insert(mathematics_8, index=END, text='Unit 1 :  Squares, Square roots, cubes and cube roots')
        g8_math_unit2 = self.tree_grade8.insert(mathematics_8, index=END, text='Unit 2 :  Further on working with variable')
        g8_math_unit3 = self.tree_grade8.insert(mathematics_8, index=END, text='Unit 3 :  Linear equation and Inequalities')
        g8_math_unit4 = self.tree_grade8.insert(mathematics_8, index=END, text='Unit 4 :  Similar figures')
        g8_math_unit5 = self.tree_grade8.insert(mathematics_8, index=END, text='Unit 5 :  Circle')
        g8_math_unit6 = self.tree_grade8.insert(mathematics_8, index=END, text='Unit 6 :  Introduction to probability')
        g8_math_unit7 = self.tree_grade8.insert(mathematics_8, index=END, text='Unit 7 :  Geometry and measurment')

        # grade8 physics topics
        g8_phy_unit1 = self.tree_grade8.insert(physics_8, index=END, text='Unit 1 :  Physics and measurment')
        g8_phy_unit2 = self.tree_grade8.insert(physics_8, index=END, text='Unit 2 :  Motion in one dimention')
        g8_phy_unit3 = self.tree_grade8.insert(physics_8, index=END, text='Unit 3 :  pressure')
        g8_phy_unit4 = self.tree_grade8.insert(physics_8, index=END, text='Unit 4 :  Heat energy')
        g8_phy_unit5 = self.tree_grade8.insert(physics_8, index=END, text='Unit 5 :  Electricity and magnetism')
        g8_phy_unit6 = self.tree_grade8.insert(physics_8, index=END, text='Unit 6 :  Light')

        self.tree_grade8.bind("<Double-1>",lambda event:self.grade8_onDoubleClick(self.tree_grade8.item(self.tree_grade8.selection())['text']))
        self.tree_grade8.bind("<<TreeviewSelect>>",lambda event:self.ImageSender8(self.tree_grade8.item(self.tree_grade8.selection())['text']))
        #====call the yellow color when hover on=========
        self.tree_grade8.tag_configure('focus', background='slategray1')
        self.tree_grade8.bind("<Motion>", self.mycallback8)
        self.last_focus = None


        

    #______########______________grade 9 treeview information______________##########________________________

        
        self.tree_grade9 = ttk.Treeview(self.frame_in_garde9,selectmode=BROWSE,columns=("quanta"))
        self.tree_grade9.pack(expand=True,fill=BOTH)
        self.tree_grade9.heading('#0',text='Topics')
        #self.tree_grade9.heading('#1',text='images')
        self.tree_grade9.column(0, anchor=E)
        biology_9 = self.tree_grade9.insert("",index=END , text='Biology')
        chemistry_9 = self.tree_grade9.insert("",index=END , text='Chemistry')
        mathematics_9 = self.tree_grade9.insert("",index=END , text='Mathematics')
        physics_9 = self.tree_grade9.insert("",index=END , text='Physics')

     #grade9 biology topics
        g9_bio_unit1 = self.tree_grade9.insert(biology_9,index=END , text='Unit 1 :  Biology and Technology')
        g9_bio_unit2 = self.tree_grade9.insert(biology_9,index=END , text='Unit 2 :  Cell Biology')
        g9_bio_unit3 = self.tree_grade9.insert(biology_9,index=END , text='Unit 3 :  Human Biology and Health')
        g9_bio_unit4 = self.tree_grade9.insert(biology_9,index=END , text='Unit 4 :  Micro-organisms and disease')
        g9_bio_unit5 = self.tree_grade9.insert(biology_9,index=END , text='Unit 5 :  Classification')
        g9_bio_unit6 = self.tree_grade9.insert(biology_9,index=END , text='Unit 6 :  Enviroment')

     #grade9 chemistry topics
        g9_chem_unit1 = self.tree_grade9.insert(chemistry_9,index=END , text='Unit 1 :  Structure of the Atom')
        g9_chem_unit2 = self.tree_grade9.insert(chemistry_9,index=END , text='Unit 2 :  Periodic Classification of the Elements')
        g9_chem_unit3 = self.tree_grade9.insert(chemistry_9,index=END , text='Unit 3 :  Chemical Bonding and Intermolecular Forces')
        g9_chem_unit4 = self.tree_grade9.insert(chemistry_9,index=END , text='Unit 4 :  Chemical Reaction and Stoichiometery')
        g9_chem_unit5 = self.tree_grade9.insert(chemistry_9,index=END , text='Unit 5 :  Physical States of Matter')
     #grade9 mathematics topics
        g9_math_unit1 = self.tree_grade9.insert(mathematics_9,index=END , text='Unit 1 :  The Number System')
        g9_math_unit2 = self.tree_grade9.insert(mathematics_9,index=END , text='Unit 2 :  Solutions of Equations')
        g9_math_unit3 = self.tree_grade9.insert(mathematics_9,index=END , text='Unit 3 :  Further on Sets')
        g9_math_unit4 = self.tree_grade9.insert(mathematics_9,index=END , text='Unit 4 :  Relations and Functions')
        g9_math_unit5 = self.tree_grade9.insert(mathematics_9,index=END , text='Unit 5 :  Geometry and Measurement')
        g9_math_unit6 = self.tree_grade9.insert(mathematics_9,index=END , text='Unit 6 :  Statistics and Probability')
        g9_math_unit7 = self.tree_grade9.insert(mathematics_9,index=END , text='Unit 7 :  Vectors in Two Dimensions')
     #grade9 physics topics
        g9_phy_unit1 = self.tree_grade9.insert(physics_9,index=END , text='Unit 1 :  Vectors')
        g9_phy_unit1 = self.tree_grade9.insert(physics_9,index=END , text='Unit 2 :  Motion in a straight line')
        g9_phy_unit1 = self.tree_grade9.insert(physics_9,index=END , text="Unit 3 :  Forces and Newton’s laws of motion")
        g9_phy_unit1 = self.tree_grade9.insert(physics_9,index=END , text='Unit 4 :  Work, energy and power')
        g9_phy_unit1 = self.tree_grade9.insert(physics_9,index=END , text='Unit 5 :  Simple machines')
        g9_phy_unit1 = self.tree_grade9.insert(physics_9,index=END , text='Unit 6 :  Fluid statics')
        g9_phy_unit1 = self.tree_grade9.insert(physics_9,index=END , text='Unit 7 :  Temperature and heat')
        g9_phy_unit1 = self.tree_grade9.insert(physics_9,index=END , text='Unit 8 :  Wave motion and sound')

        self.tree_grade9.bind("<Double-1>", lambda event: self.grade9_onDoubleClick(self.tree_grade9.item(self.tree_grade9.selection())['text']))
        self.tree_grade9.bind("<<TreeviewSelect>>",lambda event:self.ImageSender9(self.tree_grade9.item(self.tree_grade9.selection())['text']))
        self.tree_grade9.tag_configure('focus', background='slategray1')
        self.tree_grade9.bind("<Motion>", self.mycallback9)
        self.last_focus = None




    #_______#########______________grade 10 treeview information_____________#########_______________________

        self.tree_grade10 = ttk.Treeview(self.frame_in_garde10, selectmode=BROWSE, columns=("quanta"))
        self.tree_grade10.pack(expand=True, fill=BOTH)
        self.tree_grade10.heading('#0', text='Topics')
        #self.tree_grade10.heading('#1', text='images')
        self.tree_grade10.column(0, anchor=E)

        biology_10 = self.tree_grade10.insert("", index=END, text='Biology')
        chemistry_10 = self.tree_grade10.insert("", index=END, text='Chemistry')
        mathematics_10 = self.tree_grade10.insert("", index=END, text='Mathematics')
        physics_10 = self.tree_grade10.insert("", index=END, text='Physics')

    # grade10 biology topics
        g10_bio_unit1 = self.tree_grade10.insert(biology_10, index=END, text='Unit 1 :  Biotechnology')
        g10_bio_unit2 = self.tree_grade10.insert(biology_10, index=END, text='Unit 2 :  Heredity')
        g10_bio_unit3 = self.tree_grade10.insert(biology_10, index=END, text='Unit 3 :  Human biology and health')
        g10_bio_unit4 = self.tree_grade10.insert(biology_10, index=END, text='Unit 4 :  Food making and growth in plant')
        g10_bio_unit5 = self.tree_grade10.insert(biology_10, index=END, text='Unit 5 :  Conservation of natural resources')

    # grade10 chemistry topics
        g10_chem_unit1 = self.tree_grade10.insert(chemistry_10, index=END, text='Unit 1 :  Introduction to Organic chemistry')
        g10_chem_unit2 = self.tree_grade10.insert(chemistry_10, index=END, text='Unit 2 :  Important Inorganic compounds')
        g10_chem_unit3 = self.tree_grade10.insert(chemistry_10, index=END, text='Unit 3 :  Electrochemistry')
        g10_chem_unit4 = self.tree_grade10.insert(chemistry_10, index=END, text='Unit 4 :  Chemistry in industry and Enviromental pollution')

    # grade10 mathematics topics

        g10_math_unit1 = self.tree_grade10.insert(mathematics_10, index=END, text='Unit 1 :  Polynomial Functions')
        g10_math_unit2 = self.tree_grade10.insert(mathematics_10, index=END, text='Unit 2 :  Exponential and Logarithimic Functions')
        g10_math_unit3 = self.tree_grade10.insert(mathematics_10, index=END, text='Unit 3 :  Solving Inequalities')
        g10_math_unit4 = self.tree_grade10.insert(mathematics_10, index=END, text='Unit 4 :  Coordinate Geometry')
        g10_math_unit5 = self.tree_grade10.insert(mathematics_10, index=END, text='Unit 5 :  Trigonomertic Functions')
        g10_math_unit6 = self.tree_grade10.insert(mathematics_10, index=END, text='Unit 6 :  Plane Geometry')
        g10_math_unit7 = self.tree_grade10.insert(mathematics_10, index=END, text='Unit 7 :  Measurment')

    # grade10 physics topics
        g10_phy_unit1 = self.tree_grade10.insert(physics_10, index=END, text='Unit 1 :  Motion in 2D')
        g10_phy_unit2 = self.tree_grade10.insert(physics_10, index=END, text='Unit 2 :  Electrostatics')
        g10_phy_unit3 = self.tree_grade10.insert(physics_10, index=END, text='Unit 3 :  Current electricity')
        g10_phy_unit4 = self.tree_grade10.insert(physics_10, index=END, text='Unit 4 :  Electromagnetism')
        g10_phy_unit5 = self.tree_grade10.insert(physics_10, index=END, text='Unit 5 :  Introduction to electronics')
        g10_phy_unit6 = self.tree_grade10.insert(physics_10, index=END, text='Unit 6 :  Electromagnegtic waves and geometrical optics')

        self.tree_grade10.bind("<Double-1>", lambda event: self.grade10_onDoubleClick(self.tree_grade10.item(self.tree_grade10.selection())['text']))
        self.tree_grade10.bind("<<TreeviewSelect>>",lambda event: self.ImageSender10(self.tree_grade10.item(self.tree_grade10.selection())['text']))
        self.tree_grade10.tag_configure('focus', background='slategray1')
        self.tree_grade10.bind("<Motion>", self.mycallback10)
        self.last_focus = None

    #________#########______________user defined questions information___________##########_____________________

        self.tree_userQuestion = ttk.Treeview(self.frame_user_question,selectmode=BROWSE,columns=("quanta"))
        self.tree_userQuestion.bind("<Double-1>",lambda event:self.userQuestion_onDoubleClick(self.tree_userQuestion.item(self.tree_userQuestion.selection())['text']))
        self.tree_userQuestion.pack(expand=True,fill=BOTH)

        self.remove_btn = Button(self.tree_userQuestion,text='Remove',command=self.remove_treeview)

        self.remove_btn.pack(side=BOTTOM,anchor=SE)
        self.tree_userQuestion.tag_configure('focus', background='slategray1')
        self.tree_userQuestion.bind("<Motion>", self.mycallbackUser)
        self.last_focus = None

    def remove_treeview(self):
        idd = self.tree_userQuestion.selection()
        for i in idd:

                self.tree_userQuestion.delete(i)
        
        """from the begining of this line up to the comment 'question reader ends here',the following
        function are used for reading the questions and answers
        from text file.each function are for each question in each garde level, in each subject.
        the function 'grade_onDoubleClick',is event function for each grade level."""


    def grade7_onDoubleClick(self,row_text):

        # grade 7 on biology doubleclick
        if row_text == 'Unit 1 :  Biology and Technology':
            self.reader_g7bioUnit1()
        elif row_text == 'Unit 2 :  Cell Biology':
            self.reader_g7bioUnit2()
        elif row_text == 'Unit 3 :  Human Biology and Health':
            self.reader_g7bioUnit3()
        elif row_text == 'Unit 4 :  Plants':
            self.reader_g7bioUnit4()
        elif row_text == 'Unit 5 :  Animals':
            self.reader_g7bioUnit5()
        elif row_text == 'Unit 6 :  Enviroment':
            self.reader_g7bioUnit6()

        # grade 7 on chemistry doubleclick
        elif row_text == 'Unit 1 :  Chemistry and its important':
            self.reader_g7chemUnit1()
        elif row_text == 'Unit 2 :  Substance':
            self.reader_g7chemUnit2()
        elif row_text == 'Unit 3 :  The language of Chemistry':
            self.reader_g7chemUnit3()
        elif row_text == 'Unit 4 :  The structure of substances':
            self.reader_g7chemUnit4()
        elif row_text == 'Unit 5 :  Periodic Classification of the Element':
            self.reader_g7chemUnit5()

        # grade 7 on math doubleclick
        elif row_text == 'Unit 1 :  Rational numbers':
            self.reader_g7mathUnit1()
        elif row_text == 'Unit 2 :  Linear equations and Inequalities':
            self.reader_g7mathUnit2()
        elif row_text == 'Unit 3 :  Ratio,Proportion and Percentage':
            self.reader_g7mathUnit3()
        elif row_text == 'Unit 4 :  Data handling':
            self.reader_g7mathUnit4()
        elif row_text == 'Unit 5 :  Geometric figure and measurment':
            self.reader_g7mathUnit5()

        # grade 7 on physics doubleclick
        elif row_text == 'Unit 1 :  Physics and Measurment':
            self.reader_g7phyUnit1()
        elif row_text == 'Unit 2 :  Motion':
            self.reader_g7phyUnit2()
        elif row_text == "Unit 3 :  Force and Newton's laws of motion":
            self.reader_g7phyUnit3()
        elif row_text == 'Unit 4 :  Work, Energy and Power':
            self.reader_g7phyUnit4()
        elif row_text == 'Unit 5 :  Simple machine':
            self.reader_g7phyUnit5()
        elif row_text == 'Unit 6 :  Temprature and Heat':
            self.reader_g7phyUnit6()
        elif row_text == 'Unit 7 :  Sound':
            self.reader_g7phyUnit7()
        elif row_text == 'Unit 8 :  Electricity and Magnetism':
            self.reader_g7phyUnit8()

    def grade8_onDoubleClick(self, row_text):
        # grade 8 on biology doubleclick
        if row_text == 'Unit 1 :  Biology and Technology':
            self.reader_g8bioUnit1()
        elif row_text == 'Unit 2 :  Cell Biology':
            self.reader_g8bioUnit2()
        elif row_text == 'Unit 3 :  Human Biology and Health':
            self.reader_g8bioUnit3()
        elif row_text == 'Unit 4 :  Plants':
            self.reader_g8bioUnit4()
        elif row_text == 'Unit 5 :  Animals':
            self.reader_g8bioUnit5()
        elif row_text == 'Unit 6 :  Enviroment':
            self.reader_g8bioUnit6()

        # grade 8 on chemistry doubleclick
        elif row_text == 'Unit 1 :  Classification of compounds':
            self.reader_g8chemUnit1()
        elif row_text == 'Unit 2 :  Some important metals':
            self.reader_g8chemUnit2()
        elif row_text == 'Unit 3 :  Some important non-metals':
            self.reader_g8chemUnit3()
        elif row_text == 'Unit 4 :  Enviromental chemistry':
            self.reader_g8chemUnit4()
        elif row_text == 'Unit 5 :  Calculations based on formulas':
            self.reader_g8chemUnit5()

        # grade 8 on math doubleclick
        elif row_text == 'Unit 1 :  Squares, Square roots, cubes and cube roots':
            self.reader_g8mathUnit1()
        elif row_text == 'Unit 2 :  Further on working with variable':
            self.reader_g8mathUnit2()
        elif row_text == 'Unit 3 :  Linear equation and Inequalities':
            self.reader_g8mathUnit3()
        elif row_text == 'Unit 4 :  Similar figures':
            self.reader_g8mathUnit4()
        elif row_text == 'Unit 5 :  Circle':
            self.reader_g8mathUnit5()
        elif row_text == 'Unit 6 :  Introduction to probability':
            self.reader_g8mathUnit6()
        elif row_text == 'Unit 7 :  Geometry and measurment':
            self.reader_g8mathUnit7()

        # grade 8 on physics doubleclick
        elif row_text == 'Unit 1 :  Physics and measurment':
            self.reader_g8phyUnit1()
        elif row_text == 'Unit 2 :  Motion in one dimention':
            self.reader_g8phyUnit2()
        elif row_text == "Unit 3 :  pressure":
            self.reader_g8phyUnit3()
        elif row_text == 'Unit 4 :  Heat energy':
            self.reader_g8phyUnit4()
        elif row_text == 'Unit 5 :  Electricity and magnetism':
            self.reader_g8phyUnit5()
        elif row_text == 'Unit 6 :  Light':
            self.reader_g8phyUnit6()

    def grade9_onDoubleClick(self, row_text):

        # grade 9 on biology doubleclick

        if row_text == 'Unit 1 :  Biology and Technology':
            self.reader_g9bioUnit1()
        elif row_text == 'Unit 2 :  Cell Biology':
            self.reader_g9bioUnit2()
        elif row_text == 'Unit 3 :  Human Biology and Health':
            self.reader_g9bioUnit3()
        elif row_text == 'Unit 4 :  Micro-organisms and disease':
            self.reader_g9bioUnit4()
        elif row_text == 'Unit 5 :  Classification':
            self.reader_g9bioUnit5()
        elif row_text == 'Unit 6 :  Enviroment':
            self.reader_g9bioUnit6()


        # grade 9 on chemistry doubleclick
        elif row_text == 'Unit 1 :  Structure of the Atom':
            self.reader_g9chemUnit1()
        elif row_text == 'Unit 2 :  Periodic Classification of the Elements':
            self.reader_g9chemUnit2()
        elif row_text == 'Unit 3 :  Chemical Bonding and Intermolecular Forces':
            self.reader_g9chemUnit3()
        elif row_text == 'Unit 4 :  Chemical Reaction and Stoichiometery':
            self.reader_g9chemUnit4()
        elif row_text == 'Unit 5 :  Physical States of Matter':
            self.reader_g9chemUnit5()


        # grade 9 on math doubleclick
        elif row_text == 'Unit 1 :  The Number System':
            self.reader_g9mathUnit1()
        elif row_text == 'Unit 2 :  Solutions of Equations':
            self.reader_g9mathUnit2()
        elif row_text == 'Unit 3 :  Further on Sets':
            self.reader_g9mathUnit3()
        elif row_text == 'Unit 4 :  Relations and Functions':
            self.reader_g9mathUnit4()
        elif row_text == 'Unit 5 :  Geometry and Measurement':
            self.reader_g9mathUnit5()
        elif row_text == 'Unit 6 :  Statistics and Probability':
            self.reader_g9mathUnit6()
        elif row_text == 'Unit 7 :  Vectors in Two Dimensions':
            self.reader_g9mathUnit7()


        # grade 9 on physics doubleclick

        elif row_text == 'Unit 1 :  Vectors':
            self.reader_g9phyUnit1()
        elif row_text == 'Unit 2 :  Motion in a straight line':
            self.reader_g9phyUnit2()
        elif row_text == "Unit 3 :  Forces and Newton's laws of motion":
            self.reader_g9phyUnit3()
        elif row_text == 'Unit 4 :  Work, energy and power':
            self.reader_g9phyUnit4()
        elif row_text == 'Unit 5 :  Simple machines':
            self.reader_g9phyUnit5()
        elif row_text == 'Unit 6 :  Fluid statics':
            self.reader_g9phyUnit6()
        elif row_text == 'Unit 7 :  Temperature and heat':
            self.reader_g9phyUnit7()
        elif row_text == 'Unit 8 :  Wave motion and sound':
            self.reader_g9phyUnit8()

    def grade10_onDoubleClick(self, row_text):


        # grade 10 on biology doubleclick
        if row_text == 'Unit 1 :  Biotechnology':
            self.reader_g10bioUnit1()
        elif row_text == 'Unit 2 :  Heredity':
            self.reader_g10bioUnit2()
        elif row_text == 'Unit 3 :  Human biology and health':
            self.reader_g10bioUnit3()
        elif row_text == 'Unit 4 :  Food making and growth in plant':
            self.reader_g10bioUnit4()
        elif row_text == 'Unit 5 :  Conservation of natural resources':
            self.reader_g10bioUnit5()


        # grade 10 on chemistry doublecclick
        elif row_text == 'Unit 1 :  Introduction to Organic chemistry':
            self.reader_g10chemUnit1()
        elif row_text == 'Unit 2 :  Important Inorganic compounds':
            self.reader_g10chemUnit2()
        elif row_text == 'Unit 3 :  Electrochemistry':
            self.reader_g10chemUnit3()
        elif row_text == 'Unit 4 :  Chemistry in industry and Enviromental pollution':
            self.reader_g10chemUnit4()


        # grade 10 on math doubleclick
        elif row_text == 'Unit 1 :  Polynomial Functions':
            self.reader_g10mathUnit1()
        elif row_text == 'Unit 2 :  Exponential and Logarithimic Functions':
            self.reader_g10mathUnit2()
        elif row_text == 'Unit 3 :  Solving Inequalities':
            self.reader_g10mathUnit3()
        elif row_text == 'Unit 4 :  Coordinate Geometry':
            self.reader_g10mathUnit4()
        elif row_text == 'Unit 5 :  Trigonomertic Functions':
            self.reader_g10mathUnit5()
        elif row_text == 'Unit 6 :  Plane Geometry':
            self.reader_g10mathUnit6()
        elif row_text == 'Unit 7 :  Measurment':
            self.reader_g10mathUnit7()


        # grade 10 on physics doubleclick
        elif row_text == 'Unit 1 :  Motion in 2D':
            self.reader_g10phyUnit1()
        elif row_text == 'Unit 2 :  Electrostatics':
            self.reader_g10phyUnit2()
        elif row_text == "Unit 3 :  Current electricity":
            self.reader_g10phyUnit3()
        elif row_text == 'Unit 4 :  Electromagnetism':
            self.reader_g10phyUnit4()
        elif row_text == 'Unit 5 :  Introduction to electronics':
            self.reader_g10phyUnit5()
        elif row_text == 'Unit 6 :  Electromagnegtic waves and geometrical optics':
            self.reader_g10phyUnit6()

    #reading questions starts here for grade 7,8,9,10

#reading grade 7 question======================================
    #reading questions grade 7 biology
    def reader_g7bioUnit1(self):
        Reader.Question_reader(self.master,'grade7\\biology\\unit1_ques.txt','grade7\\biology\\unit1_ans.txt',[2,5,8,13,18,22,24,30,33,37])
    def reader_g7bioUnit2(self):
        Reader.Question_reader(self.master,'grade7\\biology\\unit2_ques.txt','grade7\\biology\\unit2_ans.txt',[2,6,9,14,17,22,27,31,34,36,42,45,49,55,57])
    def reader_g7bioUnit3(self):
        Reader.Question_reader(self.master,'grade7\\biology\\unit3_ques.txt','grade7\\biology\\unit3_ans.txt',[2,6,11,12,16,21,27,30,33,39,42,45,49,54,57])
    def reader_g7bioUnit4(self):
        Reader.Question_reader(self.master,'grade7\\biology\\unit4_ques.txt','grade7\\biology\\unit4_ans.txt',[2,5,10,14,19,20,25,28,33,39])
    def reader_g7bioUnit5(self):
        Reader.Question_reader(self.master,'grade7\\biology\\unit5_ques.txt','grade7\\biology\\unit5_ans.txt',[1,7,8,13,18,22,27,29,33,37])
    def reader_g7bioUnit6(self):
        Reader.Question_reader(self.master,'grade7\\biology\\unit6_ques.txt','grade7\\biology\\unit6_ans.txt',[2,5,9,12,17,22,27,31,34,37])

    #reading questions grade 7 chemistry
    def reader_g7chemUnit1(self):
        Reader.Question_reader(self.master,'grade7\\chemistry\\unit1_ques.txt','grade7\\chemistry\\unit1_ans.txt',[2,7,11,15,18,21,26,30,35,39])
    def reader_g7chemUnit2(self):
        Reader.Question_reader(self.master,'grade7\\chemistry\\unit2_ques.txt','grade7\\chemistry\\unit2_ans.txt',[2,4,8,12,18,21,27,31,34,37,40,46,48,52,59])
    def reader_g7chemUnit3(self):
        Reader.Question_reader(self.master,'grade7\\chemistry\\unit3_ques.txt','grade7\\chemistry\\unit3_ans.txt',[3,5,10,12,18,22,25,28,35,36])
    def reader_g7chemUnit4(self):
        Reader.Question_reader(self.master,'grade7\\chemistry\\unit4_ques.txt','grade7\\chemistry\\unit4_ans.txt',[2,4,8,15,16,22,24,28,35,38])
    def reader_g7chemUnit5(self):
        Reader.Question_reader(self.master,'grade7\\chemistry\\unit5_ques.txt','grade7\\chemistry\\unit5_ans.txt',[2,5,8,13,17,20,24,31,35,38])

    # reading questions grade7 math
    def reader_g7mathUnit1(self):
        Reader.Question_reader(self.master, 'grade7\\mathematics\\unit1_ques.txt', 'grade7\\mathematics\\unit1_ans.txt', [])
    def reader_g7mathUnit2(self):
        Reader.Question_reader(self.master, 'grade7\\mathematics\\unit2_ques.txt', 'grade7\\mathematics\\unit2_ans.txt', [])
    def reader_g7mathUnit3(self):
        Reader.Question_reader(self.master, 'grade7\\mathematics\\unit3_ques.txt', 'grade7\\mathematics\\unit3_ans.txt', [])
    def reader_g7mathUnit4(self):
        Reader.Question_reader(self.master, 'grade7\\mathematics\\unit4_ques.txt', 'grade7\\mathematics\\unit4_ans.txt', [])
    def reader_g7mathUnit5(self):
        Reader.Question_reader(self.master, 'grade7\\mathematics\\unit5_ques.txt', 'grade7\\mathematics\\unit5_ans.txt', [])

    # reading questions grade7 physics
    def reader_g7phyUnit1(self):
        Reader.Question_reader(self.master, 'grade7\\physics\\unit1_ques.txt', 'grade7\\physics\\unit1_ans.txt', [])
    def reader_g7phyUnit2(self):
        Reader.Question_reader(self.master, 'grade7\\physics\\unit2_ques.txt', 'grade7\\physics\\unit2_ans.txt', [])
    def reader_g7phyUnit3(self):
        Reader.Question_reader(self.master, 'grade7\\physics\\unit3_ques.txt', 'grade7\\physics\\unit3_ans.txt', [])
    def reader_g7phyUnit4(self):
        Reader.Question_reader(self.master, 'grade7\\physics\\unit4_ques.txt', 'grade7\\physics\\unit4_ans.txt', [])
    def reader_g7phyUnit5(self):
        Reader.Question_reader(self.master, 'grade7\\physics\\unit5_ques.txt', 'grade7\\physics\\unit5_ans.txt', [])
    def reader_g7phyUnit6(self):
        Reader.Question_reader(self.master, 'grade7\\physics\\unit6_ques.txt', 'grade7\\physics\\unit6_ans.txt', [])
    def reader_g7phyUnit7(self):
        Reader.Question_reader(self.master, 'grade7\\physics\\unit7_ques.txt', 'grade7\\physics\\unit7_ans.txt', [])
    def reader_g7phyUnit8(self):
        Reader.Question_reader(self.master, 'grade7\\physics\\unit8_ques.txt', 'grade7\\physics\\unit8_ans.txt', [])

# reading grade 8 question========================================

    # reading questions grade8 Biology
    def reader_g8bioUnit1(self):
        Reader.Question_reader(self.master,'grade8\\biology\\unit1_ques.txt','grade8\\biology\\unit1_ans.txt',[3,6,8,14,17,21,27,30,35,36])
    def reader_g8bioUnit2(self):
        Reader.Question_reader(self.master,'grade8\\biology\\unit2_ques.txt','grade8\\biology\\unit2_ans.txt',[0,5,11,12,19,22,24,28,34,37,43,47,50,52,57,60,65,70,75,79])
    def reader_g8bioUnit3(self):
        Reader.Question_reader(self.master,'grade8\\biology\\unit3_ques.txt','grade8\\biology\\unit3_ans.txt',[1,6,9,12,19,22,24,30,35,37,40,47,49,54,59,60,65,71,73,79])
    def reader_g8bioUnit4(self):
        Reader.Question_reader(self.master,'grade8\\biology\\unit4_ques.txt','grade8\\biology\\unit4_ans.txt',[2,6,8,15,17,23,26,29,35,36,41,47,49,52,58,63,65,70,74,79])
    def reader_g8bioUnit5(self):
        Reader.Question_reader(self.master,'grade8\\biology\\unit5_ques.txt','grade8\\biology\\unit5_ans.txt',[1,7,8,14,17,22,26,28,34,39,42,46,51,55,58])
    def reader_g8bioUnit6(self):
        Reader.Question_reader(self.master,'grade8\\biology\\unit6_ques.txt','grade8\\biology\\unit6_ans.txt',[1,4,8,13,17,23,26,30,34,39,43,47,78,54,56,63,65,69,74,78])

    # reading questions grade8 chemistry
    def reader_g8chemUnit1(self):
        Reader.Question_reader(self.master,'grade8\\chemistry\\unit1_ques.txt','grade8\\chemistry\\unit1_ans.txt',[])
    def reader_g8chemUnit2(self):
        Reader.Question_reader(self.master,'grade8\\chemistry\\unit2_ques.txt','grade8\\chemistry\\unit2_ans.txt',[])
    def reader_g8chemUnit3(self):
        Reader.Question_reader(self.master,'grade8\\chemistry\\unit3_ques.txt','grade8\\chemistry\\unit3_ans.txt',[])
    def reader_g8chemUnit4(self):
        Reader.Question_reader(self.master,'grade8\\chemistry\\unit4_ques.txt','grade8\\chemistry\\unit4_ans.txt',[])
    def reader_g8chemUnit5(self):
        Reader.Question_reader(self.master,'grade8\\chemistry\\unit5_ques.txt','grade8\\chemistry\\unit5_ans.txt',[])

    # reading questions grade8 mathematics
    def reader_g8mathUnit1(self):
        Reader.Question_reader(self.master, 'grade8\\mathematics\\unit1_ques.txt', 'grade8\\mathematics\\unit1_ans.txt', [])
    def reader_g8mathUnit2(self):
        Reader.Question_reader(self.master, 'grade8\\mathematics\\unit2_ques.txt', 'grade8\\mathematics\\unit2_ans.txt', [])
    def reader_g8mathUnit3(self):
        Reader.Question_reader(self.master, 'grade8\\mathematics\\unit3_ques.txt', 'grade8\\mathematics\\unit3_ans.txt', [])
    def reader_g8mathUnit4(self):
        Reader.Question_reader(self.master, 'grade8\\mathematics\\unit4_ques.txt', 'grade8\\mathematics\\unit4_ans.txt', [])
    def reader_g8mathUnit5(self):
        Reader.Question_reader(self.master, 'grade8\\mathematics\\unit5_ques.txt', 'grade8\\mathematics\\unit5_ans.txt', [])
    def reader_g8mathUnit6(self):
        Reader.Question_reader(self.master, 'grade8\\mathematics\\unit6_ques.txt', 'grade8\\mathematics\\unit6_ans.txt', [])
    def reader_g8mathUnit7(self):
        Reader.Question_reader(self.master, 'grade8\\mathematics\\unit7_ques.txt', 'grade8\\mathematics\\unit7_ans.txt', [])

    # reading questions grade8 physics
    def reader_g8phyUnit1(self):
        Reader.Question_reader(self.master, 'grade8\\physics\\unit1_ques.txt', 'grade8\\physics\\unit1_ans.txt', [])
    def reader_g8phyUnit2(self):
        Reader.Question_reader(self.master, 'grade8\\physics\\unit2_ques.txt', 'grade8\\physics\\unit2_ans.txt', [])
    def reader_g8phyUnit3(self):
        Reader.Question_reader(self.master, 'grade8\\physics\\unit3_ques.txt', 'grade8\\physics\\unit3_ans.txt', [])
    def reader_g8phyUnit4(self):
        Reader.Question_reader(self.master, 'grade8\\physics\\unit4_ques.txt', 'grade8\\physics\\unit4_ans.txt', [])
    def reader_g8phyUnit5(self):
        Reader.Question_reader(self.master, 'grade8\\physics\\unit5_ques.txt', 'grade8\\physics\\unit5_ans.txt', [])
    def reader_g8phyUnit6(self):
        Reader.Question_reader(self.master, 'grade8\\physics\\unit6_ques.txt', 'grade8\\physics\\unit6_ans.txt', [])

# reading grade 9 question===================================
    # reading questions grade9 Biology
    def reader_g9bioUnit1(self):
        Reader.Question_reader(self.master,'grade9\\biology\\unit1_ques.txt','grade9\\biology\\unit1_ans.txt',[])
    def reader_g9bioUnit2(self):
        Reader.Question_reader(self.master,'grade9\\biology\\unit2_ques.txt','grade9\\biology\\unit2_ans.txt',[])
    def reader_g9bioUnit3(self):
        Reader.Question_reader(self.master,'grade9\\biology\\unit3_ques.txt','grade9\\biology\\unit3_ans.txt',[])
    def reader_g9bioUnit4(self):
        Reader.Question_reader(self.master,'grade9\\biology\\unit4_ques.txt','grade9\\biology\\unit4_ans.txt',[])
    def reader_g9bioUnit5(self):
        Reader.Question_reader(self.master,'grade9\\biology\\unit5_ques.txt','grade9\\biology\\unit5_ans.txt',[])
    def reader_g9bioUnit6(self):
        Reader.Question_reader(self.master,'grade9\\biology\\unit6_ques.txt','grade9\\biology\\unit6_ans.txt',[])

    # reading questions grade9 chemistry
    def reader_g9chemUnit1(self):
        Reader.Question_reader(self.master,'grade9\\chemistry\\unit1_ques.txt','grade9\\chemistry\\unit1_ans.txt',[])
    def reader_g9chemUnit2(self):
        Reader.Question_reader(self.master,'grade9\\chemistry\\unit2_ques.txt','grade9\\chemistry\\unit2_ans.txt',[])
    def reader_g9chemUnit3(self):
        Reader.Question_reader(self.master,'grade9\\chemistry\\unit3_ques.txt','grade9\\chemistry\\unit3_ans.txt',[])
    def reader_g9chemUnit4(self):
        Reader.Question_reader(self.master,'grade9\\chemistry\\unit4_ques.txt','grade9\\chemistry\\unit4_ans.txt',[])
    def reader_g9chemUnit5(self):
        Reader.Question_reader(self.master,'grade9\\chemistry\\unit5_ques.txt','grade9\\chemistry\\unit5_ans.txt',[])

    # reading questions grade9 mathematics
    def reader_g9mathUnit1(self):
        Reader.Question_reader(self.master, 'grade9\\mathematics\\unit1_ques.txt', 'grade9\\mathematics\\unit1_ans.txt', [])
    def reader_g9mathUnit2(self):
        Reader.Question_reader(self.master, 'grade9\\mathematics\\unit2_ques.txt', 'grade9\\mathematics\\unit2_ans.txt', [])
    def reader_g9mathUnit3(self):
        Reader.Question_reader(self.master, 'grade9\\mathematics\\unit3_ques.txt', 'grade9\\mathematics\\unit3_ans.txt', [])
    def reader_g9mathUnit4(self):
        Reader.Question_reader(self.master, 'grade9\\mathematics\\unit4_ques.txt', 'grade9\\mathematics\\unit4_ans.txt', [])
    def reader_g9mathUnit5(self):
        Reader.Question_reader(self.master, 'grade9\\mathematics\\unit5_ques.txt', 'grade9\\mathematics\\unit5_ans.txt', [])
    def reader_g9mathUnit6(self):
        Reader.Question_reader(self.master, 'grade9\\mathematics\\unit6_ques.txt', 'grade9\\mathematics\\unit6_ans.txt', [])
    def reader_g9mathUnit7(self):
        Reader.Question_reader(self.master, 'grade9\\mathematics\\unit7_ques.txt', 'grade9\\mathematics\\unit7_ans.txt', [])

    # reading questions grade9 physics
    def reader_g9phyUnit1(self):
        Reader9_unit1_physics.Question_reader(self.master, 'grade9\\physics\\unit1_ques.txt', 'grade9\\physics\\unit1_ans.txt', [1,6,9,15,16,22,24,29,32,37])
    def reader_g9phyUnit2(self):
        Reader.Question_reader(self.master, 'grade9\\physics\\unit2_ques.txt', 'grade9\\physics\\unit2_ans.txt', [3,6,9,13,19,21,24,29,35,36,42,44,51,55,57])
    def reader_g9phyUnit3(self):
        Reader.Question_reader(self.master, 'grade9\\physics\\unit3_ques.txt', 'grade9\\physics\\unit3_ans.txt', [])
    def reader_g9phyUnit4(self):
        Reader.Question_reader(self.master, 'grade9\\physics\\unit4_ques.txt', 'grade9\\physics\\unit4_ans.txt', [])
    def reader_g9phyUnit5(self):
        Reader.Question_reader(self.master, 'grade9\\physics\\unit5_ques.txt', 'grade9\\physics\\unit5_ans.txt', [])
    def reader_g9phyUnit6(self):
        Reader.Question_reader(self.master, 'grade9\\physics\\unit6_ques.txt', 'grade9\\physics\\unit6_ans.txt', [])
    def reader_g9phyUnit7(self):
        Reader.Question_reader(self.master, 'grade9\\physics\\unit7_ques.txt', 'grade9\\physics\\unit7_ans.txt', [])
    def reader_g9phyUnit8(self):
        Reader.Question_reader(self.master, 'grade9\\physics\\unit8_ques.txt', 'grade9\\physics\\unit8_ans.txt', [])


# reading grade 10 question=====================================

    # reading questions grade10 Biology
    def reader_g10bioUnit1(self):
        Reader.Question_reader(self.master,'grade10\\biology\\unit1_ques.txt','grade10\\biology\\unit1_ans.txt',[])
    def reader_g10bioUnit2(self):
        Reader.Question_reader(self.master,'grade10\\biology\\unit2_ques.txt','grade10\\biology\\unit2_ans.txt',[])
    def reader_g10bioUnit3(self):
        Reader.Question_reader(self.master,'grade10\\biology\\unit3_ques.txt','grade10\\biology\\unit3_ans.txt',[])
    def reader_g10bioUnit4(self):
        Reader.Question_reader(self.master,'grade10\\biology\\unit4_ques.txt','grade10\\biology\\unit4_ans.txt',[])
    def reader_g10bioUnit5(self):
        Reader.Question_reader(self.master,'grade10\\biology\\unit5_ques.txt','grade10\\biology\\unit5_ans.txt',[])

    # reading questions grade10 chemistry
    def reader_g10chemUnit1(self):
        Reader.Question_reader(self.master,'grade10\\chemistry\\unit1_ques.txt','grade10\\chemistry\\unit1_ans.txt',[])
    def reader_g10chemUnit2(self):
        Reader.Question_reader(self.master,'grade10\\chemistry\\unit2_ques.txt','grade10\\chemistry\\unit2_ans.txt',[])
    def reader_g10chemUnit3(self):
        Reader.Question_reader(self.master,'grade10\\chemistry\\unit3_ques.txt','grade10\\chemistry\\unit3_ans.txt',[])
    def reader_g10chemUnit4(self):
        Reader.Question_reader(self.master,'grade10\\chemistry\\unit4_ques.txt','grade10\\chemistry\\unit4_ans.txt',[])


    # reading questions grade10 math
    def reader_g10mathUnit1(self):
        Reader.Question_reader(self.master,'grade10\\mathematics\\unit1_ques.txt','grade10\\mathematics\\unit1_ans.txt',[])
    def reader_g10mathUnit2(self):
        Reader.Question_reader(self.master,'grade10\\mathematics\\unit2_ques.txt','grade10\\mathematics\\unit2_ans.txt',[])
    def reader_g10mathUnit3(self):
        Reader.Question_reader(self.master,'grade10\\mathematics\\unit3_ques.txt','grade10\\mathematics\\unit3_ans.txt',[])
    def reader_g10mathUnit4(self):
        Reader.Question_reader(self.master,'grade10\\mathematics\\unit4_ques.txt','grade10\\mathematics\\unit4_ans.txt',[])
    def reader_g10mathUnit5(self):
        Reader.Question_reader(self.master,'grade10\\mathematics\\unit5_ques.txt','grade10\\mathematics\\unit5_ans.txt',[])
    def reader_g10mathUnit6(self):
        Reader.Question_reader(self.master,'grade10\\mathematics\\unit6_ques.txt','grade10\\mathematics\\unit6_ans.txt',[])
    def reader_g10mathUnit7(self):
        Reader.Question_reader(self.master,'grade10\\mathematics\\unit7_ques.txt','grade10\\mathematics\\unit7_ans.txt',[])
    # reading questions grade10 physics

    def reader_g10phyUnit1(self):
        Reader10_unit1_physics.Question_reader(self.master, 'grade10\\physics\\unit1_ques.txt','grade10\\physics\\unit1_ans.txt', [2,7,11,14,17,22,26,31,33,39])
    def reader_g10phyUnit2(self):
        Reader10_unit2_physics.Question_reader(self.master, 'grade10\\physics\\unit2_ques.txt','grade10\\physics\\unit2_ans.txt', [1,5,9,14,17,23,25,31,32,39])
    def reader_g10phyUnit3(self):
        Reader.Question_reader(self.master, 'grade10\\physics\\unit3_ques.txt','grade10\\physics\\unit3_ans.txt', [3,7,8,15,18,23,26,31,35,37,43,47])
    def reader_g10phyUnit4(self):
        Reader10_unit4_physics.Question_reader(self.master, 'grade10\\physics\\unit4_ques.txt','grade10\\physics\\unit4_ans.txt', [0, 7, 11, 12, 19, 20, 27, 30, 32, 36, 42, 47, 50, 55, 59])
    def reader_g10phyUnit5(self):
        Reader.Question_reader(self.master, 'grade10\\physics\\unit5_ques.txt','grade10\\physics\\unit5_ans.txt', [])
    def reader_g10phyUnit6(self):
        Reader.Question_reader(self.master, 'grade10\\physics\\unit6_ques.txt','grade10\\physics\\unit6_ans.txt', [])



    def userQuestion_onDoubleClick(self,row_text):
        if row_text == self.pass_rowname1:
            self.reader_userQuestion1()
        elif row_text == self.pass_rowname2:
            self.reader_userQuestion2()
        elif row_text == self.pass_rowname3:
            self.reader_userQuestion3()
        elif row_text == self.pass_rowname4:
            self.reader_userQuestion4()
        elif row_text == self.pass_rowname5:
            self.reader_userQuestion5()
        elif row_text == self.pass_rowname6:
            self.reader_userQuestion6()
        elif row_text == self.pass_rowname7:
            self.reader_userQuestion7()
        elif row_text == self.pass_rowname8:
            self.reader_userQuestion8()
        elif row_text == self.pass_rowname9:
            self.reader_userQuestion9()
        elif row_text == self.pass_rowname10:
            self.reader_userQuestion10()
        elif row_text == self.pass_rowname11:
            self.reader_userQuestion11()
        elif row_text == self.pass_rowname12:
            self.reader_userQuestion12()
        elif row_text == self.pass_rowname13:
            self.reader_userQuestion13()
        elif row_text == self.pass_rowname14:
            self.reader_userQuestion14()
        elif row_text == self.pass_rowname15:
            self.reader_userQuestion15()
        elif row_text == self.pass_rowname16:
            self.reader_userQuestion16()
        elif row_text == self.pass_rowname17:
            self.reader_userQuestion17()
        elif row_text == self.pass_rowname18:
            self.reader_userQuestion18()
        elif row_text == self.pass_rowname19:
            self.reader_userQuestion19()
        elif row_text == self.pass_rowname20:
            self.reader_userQuestion20()


    #reading question from file for userquestion 
    def reader_userQuestion1(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions1.txt')
    def reader_userQuestion2(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions2.txt')
    def reader_userQuestion3(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions3.txt')
    def reader_userQuestion4(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions4.txt')
    def reader_userQuestion5(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions5.txt')
    def reader_userQuestion6(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions6.txt')
    def reader_userQuestion7(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions7.txt')
    def reader_userQuestion8(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions8.txt')
    def reader_userQuestion9(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions9.txt')
    def reader_userQuestion10(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions10.txt')
    def reader_userQuestion11(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions11.txt')
    def reader_userQuestion12(self):
       show_result.Question_reader(self.master,'UserQuestions\\UserQuestions12.txt')
    def reader_userQuestion13(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions13.txt')
    def reader_userQuestion14(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions14.txt')
    def reader_userQuestion15(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions15.txt')
    def reader_userQuestion16(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions16.txt')
    def reader_userQuestion17(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions17.txt')
    def reader_userQuestion18(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions18.txt')
    def reader_userQuestion19(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions19.txt')
    def reader_userQuestion20(self):
        show_result.Question_reader(self.master,'UserQuestions\\UserQuestions20.txt')
        
       
    """question reader ends here"""


    """the following code is used to read the img for the different topics. it is up to 'image reader ends here'."""

    def ImageReader(self,imgfile_name):
        opened_img = PhotoImage(file=imgfile_name)
        imglbl=Label(self.upper_frame,image=opened_img)
        imglbl.grid(padx=10,pady=10,column = 0,row=1)
        imglbl.image=opened_img

    def ImageSender7(self,row_text):
    #grade 7 images
        #biology grade 7 images

        if row_text == 'Unit 1 :  Biology and Technology':
            self.ImageReader('image\\grade7\\biology\\Unit1.png')
        elif row_text == 'Unit 2 :  Cell Biology':
            self.ImageReader('image\\grade7\\biology\\Unit2.png')
        elif row_text == 'Unit 3 :  Human Biology and Health':
            self.ImageReader('image\\grade7\\biology\\Unit3.png')
        elif row_text == 'Unit 4 :  Plants':
            self.ImageReader('image\\grade7\\biology\\Unit4.png')
        elif row_text == 'Unit 5 :  Animals':
            self.ImageReader('image\\grade7\\biology\\Unit5.png')
        elif row_text == 'Unit 6 :  Enviroment':
            self.ImageReader('image\\grade7\\biology\\Unit6.png')


        #chemistry grade 7 image
        elif row_text == 'Unit 1 :  Chemistry and its important':
            self.ImageReader('image\\grade7\\chemistry\\Unit1.png')
        elif row_text == 'Unit 2 :  Substance':
            self.ImageReader('image\\grade7\\chemistry\\Unit2.png')
        elif row_text == 'Unit 3 :  The language of Chemistry':
            self.ImageReader('image\\grade7\\chemistry\\Unit3.png')
        elif row_text == 'Unit 4 :  The structure of substances':
            self.ImageReader('image\\grade7\\chemistry\\Unit4.png')
        elif row_text == 'Unit 5 :  Periodic Classification of the Element':
            self.ImageReader('image\\grade7\\chemistry\\Unit5.png')

        #math grade7 image
        elif row_text == 'Unit 1 :  Rational numbers':
            self.ImageReader('image\\grade7\\mathematics\\Unit1.png')
        elif row_text == 'Unit 2 :  Linear equations and Inequalities':
            self.ImageReader('image\\grade7\\mathematics\\Unit2.png')
        elif row_text == 'Unit 3 :  Ratio,Proportion and Percentage':
            self.ImageReader('image\\grade7\\mathematics\\Unit3.png')
        elif row_text == 'Unit 4 :  Data handling':
            self.ImageReader('image\\grade7\\mathematics\\Unit4.png')
        elif row_text == 'Unit 5 :  Geometric figure and measurment':
            self.ImageReader('image\\grade7\\mathematics\\Unit5.png')

        # physics grade7 image
        elif row_text == 'Unit 1 :  Physics and Measurment':
            self.ImageReader('image\\grade7\\physics\\Unit1.png')
        elif row_text == 'Unit 2 :  Motion':
            self.ImageReader('image\\grade7\\physics\\Unit2.png')
        elif row_text == "Unit 3 :  Force and Newton's laws of motion":
            self.ImageReader('image\\grade7\\physics\\Unit3.png')
        elif row_text == 'Unit 4 :  Work, Energy and Power':
            self.ImageReader('image\\grade7\\physics\\Unit4.png')
        elif row_text == 'Unit 5 :  Simple machine':
            self.ImageReader('image\\grade7\\physics\\Unit5.png')
        elif row_text == 'Unit 6 :  Temprature and Heat':
            self.ImageReader('image\\grade7\\physics\\Unit6.png')
        elif row_text == 'Unit 7 :  Sound':
            self.ImageReader('image\\grade7\\physics\\Unit7.png')
        elif row_text == 'Unit 8 :  Electricity and Magnetism':
            self.ImageReader('image\\grade7\\physics\\Unit8.png')

    def ImageSender8(self,row_text):
    #grade 8 images
        # grade 8 biology images
        if row_text == 'Unit 1 :  Biology and Technology':
            self.ImageReader('image\\grade8\\biology\\Unit1.png')
        elif row_text == 'Unit 2 :  Cell Biology':
            self.ImageReader('image\\grade8\\biology\\Unit2.png')
        elif row_text == 'Unit 3 :  Human Biology and Health':
            self.ImageReader('image\\grade8\\biology\\Unit3.png')
        elif row_text == 'Unit 4 :  Plants':
            self.ImageReader('image\\grade8\\biology\\Unit4.png')
        elif row_text == 'Unit 5 :  Animals':
            self.ImageReader('image\\grade8\\biology\\Unit5.png')
        elif row_text == 'Unit 6 :  Enviroment':
            self.ImageReader('image\\grade8\\biology\\Unit6.png')

        # grade 8 chemistry image
        elif row_text == 'Unit 1 :  Classification of compounds':
            self.ImageReader('image\\grade8\\biology\\Unit1.png')
        elif row_text == 'Unit 2 :  Some important metals':
            self.ImageReader('image\\grade8\\biology\\Unit2.png')
        elif row_text == 'Unit 3 :  Some important non-metals':
            self.ImageReader('image\\grade8\\biology\\Unit3.png')
        elif row_text == 'Unit 4 :  Enviromental chemistry':
            self.ImageReader('image\\grade8\\biology\\Unit4.png')
        elif row_text == 'Unit 5 :  Calculations based on formulas':
            self.ImageReader('image\\grade8\\biology\\Unit5.png')

            # grade 8 math image
        elif row_text == 'Unit 1 :  Squares, Square roots, cubes and cube roots':
            self.ImageReader('image\\grade8\\mathematics\\Unit1.png')
        elif row_text == 'Unit 2 :  Further on working with variable':
            self.ImageReader('image\\grade8\\mathematics\\Unit1.png')
        elif row_text == 'Unit 3 :  Linear equation and Inequalities':
            self.ImageReader('image\\grade8\\mathematics\\Unit1.png')
        elif row_text == 'Unit 4 :  Similar figures':
            self.ImageReader('image\\grade8\\mathematics\\Unit1.png')
        elif row_text == 'Unit 5 :  Circle':
            self.ImageReader('image\\grade8\\mathematics\\Unit1.png')
        elif row_text == 'Unit 6 :  Introduction to probability':
            self.ImageReader('image\\grade8\\mathematics\\Unit1.png')
        elif row_text == 'Unit 7 :  Geometry and measurment':
            self.ImageReader('image\\grade8\\mathematics\\Unit1.png')

            # grade 8 physics image
        elif row_text == 'Unit 1 :  Physics and measurment':
            self.ImageReader('image\\grade8\\physics\\Unit1.png')
        elif row_text == 'Unit 2 :  Motion in one dimention':
            self.ImageReader('image\\grade8\\physics\\Unit2.png')
        elif row_text == "Unit 3 :  pressure":
            self.ImageReader('image\\grade8\\physics\\Unit3.png')
        elif row_text == 'Unit 4 :  Heat energy':
            self.ImageReader('image\\grade8\\physics\\Unit4.png')
        elif row_text == 'Unit 5 :  Electricity and magnetism':
            self.ImageReader('image\\grade8\\physics\\Unit5.png')
        elif row_text == 'Unit 6 :  Light':
            self.ImageReader('image\\grade8\\physics\\Unit6.png')




    def ImageSender9(self, row_text):
        # grade 9  biology images
        if row_text == 'Unit 1 :  Biology and Technology':
            self.ImageReader('image\\grade9\\biology\\Unit1.png')
        elif row_text == 'Unit 2 :  Cell Biology':
            self.ImageReader('image\\grade9\\biology\\Unit2.png')
        elif row_text == 'Unit 3 :  Human Biology and Health':
            self.ImageReader('image\\grade9\\biology\\Unit3.png')
        elif row_text == 'Unit 4 :  Micro-organisms and disease':
            self.ImageReader('image\\grade9\\biology\\Unit4.png')
        elif row_text == 'Unit 5 :  Classification':
            self.ImageReader('image\\grade9\\biology\\Unit5.png')
        elif row_text == 'Unit 6 :  Enviroment':
            self.ImageReader('image\\grade9\\biology\\Unit6.png')

        # grade 9  chemistry images
        elif row_text == 'Unit 1 :  Structure of the Atom':
            self.ImageReader('image\\grade9\\chemistry\\Unit1.png')
        elif row_text == 'Unit 2 :  Periodic Classification of the Elements':
            self.ImageReader('image\\grade9\\chemistry\\Unit2.png')
        elif row_text == 'Unit 3 :  Chemical Bonding and Intermolecular Forces':
            self.ImageReader('image\\grade9\\chemistry\\Unit3.png')
        elif row_text == 'Unit 4 :  Chemical Reaction and Stoichiometery':
            self.ImageReader('image\\grade9\\chemistry\\Unit4.png')
        elif row_text == 'Unit 5 :  Physical States of Matter':
            self.ImageReader('image\\grade9\\chemistry\\Unit5.png')

        #grade 9 math images
        elif row_text == 'Unit 1 :  The Number System':
            self.ImageReader('image\\grade9\\mathematics\\Unit1.png')
        elif row_text == 'Unit 2 :  Solutions of Equations':
            self.ImageReader('image\\grade9\\mathematics\\Unit2.png')
        elif row_text == 'Unit 3 :  Further on Sets':
            self.ImageReader('image\\grade9\\mathematics\\Unit3.png')
        elif row_text == 'Unit 4 :  Relations and Functions':
            self.ImageReader('image\\grade9\\mathematics\\Unit4.png')
        elif row_text == 'Unit 5 :  Geometry and Measurement':
            self.ImageReader('image\\grade9\\mathematics\\Unit5.png')
        elif row_text == 'Unit 6 :  Statistics and Probability':
            self.ImageReader('image\\grade9\\mathematics\\Unit6.png')
        elif row_text == 'Unit 7 :  Vectors in Two Dimensions':
            self.ImageReader('image\\grade9\\mathematics\\Unit7.png')
        # grade 9 physics images
        elif row_text == 'Unit 1 :  Vectors':
            self.ImageReader('image\\grade9\\physics\\Unit1.png')
        elif row_text == 'Unit 2 :  Motion in a straight line':
            self.ImageReader('image\\grade9\\physics\\Unit2.png')
        elif row_text == "Unit 3 :  Forces and Newton's laws of motion":
            self.ImageReader('image\\grade9\\physics\\Unit3.png')
        elif row_text == 'Unit 4 :  Work, energy and power':
            self.ImageReader('image\\grade9\\physics\\Unit4.png')
        elif row_text == 'Unit 5 :  Simple machines':
            self.ImageReader('image\\grade9\\physics\\Unit5.png')
        elif row_text == 'Unit 6 :  Fluid statics':
            self.ImageReader('image\\grade9\\physics\\Unit6.png')
        elif row_text == 'Unit 7 :  Temperature and heat':
            self.ImageReader('image\\grade9\\physics\\Unit7.png')
        elif row_text == 'Unit 8 :  Wave motion and sound':
            self.ImageReader('image\\grade9\\physics\\Unit8.png')

    def ImageSender10(self, row_text):
        # grade 10 on biology images
        if row_text == 'Unit 1 :  Biotechnology':
            self.ImageReader('image\\grade10\\biology\\Unit1.png')
        elif row_text == 'Unit 2 :  Heredity':
            self.ImageReader('image\\grade10\\biology\\Unit2.png')
        elif row_text == 'Unit 3 :  Human biology and health':
            self.ImageReader('image\\grade10\\biology\\Unit3.png')
        elif row_text == 'Unit 4 :  Food making and growth in plant':
            self.ImageReader('image\\grade10\\biology\\Unit4.png')
        elif row_text == 'Unit 5 :  Conservation of natural resources':
            self.ImageReader('image\\grade10\\biology\\Unit5.png')

            # grade 10 on chemistry images
        elif row_text == 'Unit 1 :  Introduction to Organic chemistry':
            self.ImageReader('image\\grade10\\chemistry\\Unit1.png')
        elif row_text == 'Unit 2 :  Important Inorganic compounds':
            self.ImageReader('image\\grade10\\chemistry\\Unit2.png')
        elif row_text == 'Unit 3 :  Electrochemistry':
            self.ImageReader('image\\grade10\\chemistry\\Unit3.png')
        elif row_text == 'Unit 4 :  Chemistry in industry and Enviromental pollution':
            self.ImageReader('image\\grade10\\chemistry\\Unit4.png')

            # grade 10 on math images
        elif row_text == 'Unit 1 :  Polynomial Functions':
            self.ImageReader('image\\grade10\\mathematics\\Unit1.png')
        elif row_text == 'Unit 2 :  Exponential and Logarithimic Functions':
            self.ImageReader('image\\grade10\\mathematics\\Unit2.png')
        elif row_text == 'Unit 3 :  Solving Inequalities':
            self.ImageReader('image\\grade10\\mathematics\\Unit3.png')
        elif row_text == 'Unit 4 :  Coordinate Geometry':
            self.ImageReader('image\\grade10\\mathematics\\Unit4.png')
        elif row_text == 'Unit 5 :  Trigonomertic Functions':
            self.ImageReader('image\\grade10\\mathematics\\Unit5.png')
        elif row_text == 'Unit 6 :  Plane Geometry':
            self.ImageReader('image\\grade10\\mathematics\\Unit6.png')
        elif row_text == 'Unit 7 :  Measurment':
            self.ImageReader('image\\grade10\\mathematics\\Unit7.png')

            # grade 10 physics images
        elif row_text == 'Unit 1 :  Motion in 2D':
            self.ImageReader('image\\grade10\\physics\\Unit1.png')
        elif row_text == 'Unit 2 :  Electrostatics':
            self.ImageReader('image\\grade10\\physics\\Unit2.png')
        elif row_text == "Unit 3 :  Current electricity":
            self.ImageReader('image\\grade10\\physics\\Unit3.png')
        elif row_text == 'Unit 4 :  Electromagnetism':
            self.ImageReader('image\\grade10\\physics\\Unit4.png')
        elif row_text == 'Unit 5 :  Introduction to electronics':
            self.ImageReader('image\\grade10\\physics\\Unit5.png')
        elif row_text == 'Unit 6 :  Electromagnegtic waves and geometrical optics':
            self.ImageReader('image\\grade10\\physics\\Unit6.png')



    """image reader ends here"""


    #functions for hovering over
    def mycallback7(self, event):
 
        _iid = self.tree_grade7.identify_row(event.y)
 
        if _iid != self.last_focus:
            if self.last_focus:
                self.tree_grade7.item(self.last_focus, tags=[])
            self.tree_grade7.item(_iid, tags=['focus'])
            self.last_focus = _iid
    def mycallback8(self, event):
 
        _iid = self.tree_grade8.identify_row(event.y)
 
        if _iid != self.last_focus:
            if self.last_focus:
                self.tree_grade8.item(self.last_focus, tags=[])
            self.tree_grade8.item(_iid, tags=['focus'])
            self.last_focus = _iid
    def mycallback9(self, event):
 
        _iid = self.tree_grade9.identify_row(event.y)
 
        if _iid != self.last_focus:
            if self.last_focus:
                self.tree_grade9.item(self.last_focus, tags=[])
            self.tree_grade9.item(_iid, tags=['focus'])
            self.last_focus = _iid
    def mycallback10(self, event):
        _iid = self.tree_grade10.identify_row(event.y)
 
        if _iid != self.last_focus:
            if self.last_focus:
                self.tree_grade10.item(self.last_focus, tags=[])
            self.tree_grade10.item(_iid, tags=['focus'])
            self.last_focus = _iid

    def mycallbackUser(self, event):
        _iid = self.tree_userQuestion.identify_row(event.y)

        if _iid != self.last_focus:
            if self.last_focus:
                self.tree_userQuestion.item(self.last_focus, tags=[])
            self.tree_userQuestion.item(_iid, tags=['focus'])
            self.last_focus = _iid










#=====================creating menubar starts here======================================================
    def CallPhysicalConstant(self):
        physics_constant.PhysicalConstant(self.master)

    def menubar(self,where):
        mymenu = Menu(where,tearoff=False)
        mymenu_file = Menu(mymenu,tearoff=False)
        mymenu_tool = Menu(mymenu,tearoff=False)
        mymenu_option = Menu(mymenu,tearoff=False)
        mymenu_puzzle = Menu(mymenu,tearoff=False)
        mymenu_help = Menu(mymenu,tearoff=False)
        mymenu_about = Menu(mymenu,tearoff=False)

        mymenu_option_bgcolor = Menu(mymenu_option)

        mymenu_option_language = Menu(mymenu_option)
        mymenu_option_language = Menu(mymenu_option)
        #============option to change language===============
        mymenu_option_language.add_radiobutton(label = 'English',command = None)
        mymenu_option_language.add_radiobutton(label  ='Amharic',command = None)
        #================inside the main menu============================

        mymenu_option_bgcolor.add_radiobutton(label = '',command = None)

        mymenu_file.add_command(label = "Quite",command = where.destroy)
        mymenu_tool.add_command(label = "calculator",command = None)
        mymenu_tool.add_command(label="Physical constant", command=self.CallPhysicalConstant)
        mymenu_tool.add_command(label = "text_editor",command = None)
        mymenu_option.add_cascade(label = "Background color", menu = mymenu_option_bgcolor)
        mymenu_option.add_cascade(label = "language",menu = mymenu_option_language)
        mymenu_puzzle.add_command(label = 'count triangle',command = None)
        mymenu_help.add_command(label = 'Help',command = None)
        #==========main menu========================================
        file_menu = mymenu.add_cascade(label = "File",underline=1,menu = mymenu_file)
        tool_menu = mymenu.add_cascade(label = "tool",menu = mymenu_tool)                                                                                        
        option_menu = mymenu.add_cascade(label = "option",menu = mymenu_option)
        #puzzle_menu = mymenu.add_cascade(label = 'Puzzle',menu = mymenu_puzzle)
        help_menu = mymenu.add_cascade(label = 'Help',menu = mymenu_help)

        #about_menu = mymenu.add_cascade(label = 'About',menu = mymenu_about)
        where.config(menu = mymenu)



    def open_addquestion(self):
        self.add_to_treeview()
        self.SmallBox.destroy()
        self.CreateQuestionAdderPanel(self.master)
        
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
        
        self.row_entry = Entry(self.f2,font=('Calibri (Body)',15),insertwidth=0,bd=6,bg='white')
        self.row_entry.grid(column=0,row=0,padx=20)
        
        go_icon = PhotoImage(file='icon\\go.png')
        
        b=Button(self.f2,image=go_icon,relief=FLAT,bg='slategray1',command=self.open_addquestion)
        b.grid(column=1,row=0)
        b.image=go_icon
        
###==========================================================================#########        
    """from the begining of the line up the coment 'add to add_to_treeview endes here'
    is the code that add row on the user Question treeview"""

    
    def add_to_treeview(self):
        
        #the following code is to create variable and add row tomporarly(not permanently)
        if not os.path.exists('VariableCollector\\VariableCollector1.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector1')
            variable_collector['rowname1'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname1'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector2.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector2')
            variable_collector['rowname2'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname2'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector3.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector3')
            variable_collector['rowname3'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname3'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector4.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector4')
            variable_collector['rowname4'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname4'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector5.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector5')
            variable_collector['rowname5'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname5'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector6.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector6')
            variable_collector['rowname6'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname6'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector7.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector7')
            variable_collector['rowname7'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname7'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector8.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector8')
            variable_collector['rowname8'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname8'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector9.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector9')
            variable_collector['rowname9'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname9'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector10.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector10')
            variable_collector['rowname10'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname10'])
            variable_collector.close()

        elif not os.path.exists('VariableCollector\\VariableCollector11.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector11')
            variable_collector['rowname11'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname11'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector12.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector12')
            variable_collector['rowname12'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname12'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector13.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector13')
            variable_collector['rowname13'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname13'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector14.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector14')
            variable_collector['rowname14'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname14'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector15.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector15')
            variable_collector['rowname15'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname15'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector16.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector16')
            variable_collector['rowname16'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname16'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector17.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector17')
            variable_collector['rowname17'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname17'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector18.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector18')
            variable_collector['rowname18'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname18'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector19.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector19')
            variable_collector['rowname19'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname19'])
            variable_collector.close()
        elif not os.path.exists('VariableCollector\\VariableCollector20.bak'):
            variable_collector = shelve.open('VariableCollector\\VariableCollector20')
            variable_collector['rowname20'] = self.row_entry.get()
            self.tree_userQuestion.insert("", index=END , text=variable_collector['rowname20'])
            variable_collector.close()    


##############################################################


        #this repeatedly writen code is to check whether the variable collector is finished or not
        #we can write this kinds of code by using for loop but it this code is not comfort
        elif os.path.exists('VariableCollector\\VariableCollector1.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()#this code is wrong in syntax  but it has very big purpose
        elif os.path.exists('VariableCollector\\VariableCollector2.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector3.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector4.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector5.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector6.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector7.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector8.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector9.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector10.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector11.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector12.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector13.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector14.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector15.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector16.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector17.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector18.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector19.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
        elif os.path.exists('VariableCollector\\VariableCollector20.bak'):
            messagebox.showerror('error',"you haven't enough space\n delete minimum of one to add")
            self.Adder.Qpanel.destroy()
            




    #this 'atstart' function is used to save the row when the software also closed(permanently)
    def atstart(self):
        
        if os.path.exists('VariableCollector\\VariableCollector1.bak'):
            file = shelve.open('VariableCollector\\VariableCollector1')
            self.tree_userQuestion.insert("", index=END , text=file['rowname1'])  
            self.pass_rowname1=file['rowname1']
            file.close()
   
        if os.path.exists('VariableCollector\\VariableCollector2.bak'):
            file = shelve.open('VariableCollector\\VariableCollector2')
            self.tree_userQuestion.insert("", index=END , text=file['rowname2'])
            self.pass_rowname2=file['rowname2']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector3.bak'):
            file = shelve.open('VariableCollector\\VariableCollector3')
            self.tree_userQuestion.insert("", index=END , text=file['rowname3'])
            self.pass_rowname3=file['rowname3']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector4.bak'):
            file = shelve.open('VariableCollector\\VariableCollector4')
            self.tree_userQuestion.insert("", index=END , text=file['rowname4'])
            self.pass_rowname4=file['rowname4']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector5.bak'):
            file = shelve.open('VariableCollector\\VariableCollector5')
            self.tree_userQuestion.insert("", index=END , text=file['rowname5'])
            self.pass_rowname5=file['rowname5']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector6.bak'):
            file = shelve.open('VariableCollector\\VariableCollector6')
            self.tree_userQuestion.insert("", index=END , text=file['rowname6'])
            self.pass_rowname6=file['rowname6']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector7.bak'):
            file = shelve.open('VariableCollector\\VariableCollector7')
            self.tree_userQuestion.insert("", index=END , text=file['rowname7'])
            self.pass_rowname7=file['rowname7']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector8.bak'):
            file = shelve.open('VariableCollector\\VariableCollector8')
            self.tree_userQuestion.insert("", index=END , text=file['rowname8'])
            self.pass_rowname8=file['rowname8']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector9.bak'):
            file = shelve.open('VariableCollector\\VariableCollector9')
            self.tree_userQuestion.insert("", index=END , text=file['rowname9'])
            self.pass_rowname9=file['rowname9']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector10.bak'):
            file = shelve.open('VariableCollector\\VariableCollector10')
            self.tree_userQuestion.insert("", index=END , text=file['rowname10'])
            self.pass_rowname10=file['rowname10']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector11.bak'):
            file = shelve.open('VariableCollector\\VariableCollector11')
            self.tree_userQuestion.insert("", index=END , text=file['rowname11'])
            self.pass_rowname11=file['rowname11']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector12.bak'):
            file = shelve.open('VariableCollector\\VariableCollector12')
            self.tree_userQuestion.insert("", index=END , text=file['rowname12'])
            self.pass_rowname12=file['rowname12']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector13.bak'):
            file = shelve.open('VariableCollector\\VariableCollector13')
            self.tree_userQuestion.insert("", index=END , text=file['rowname13'])
            self.pass_rowname13=file['rowname13']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector14.bak'):
            file = shelve.open('VariableCollector\\VariableCollector14')
            self.tree_userQuestion.insert("", index=END , text=file['rowname14'])
            self.pass_rowname14=file['rowname14']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector15.bak'):
            file = shelve.open('VariableCollector\\VariableCollector15')
            self.tree_userQuestion.insert("", index=END , text=file['rowname15'])
            self.pass_rowname15=file['rowname15']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector16.bak'):
            file = shelve.open('VariableCollector\\VariableCollector16')
            self.tree_userQuestion.insert("", index=END , text=file['rowname16'])
            self.pass_rowname16=file['rowname16']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector17.bak'):
            file = shelve.open('VariableCollector\\VariableCollector17')
            self.tree_userQuestion.insert("", index=END , text=file['rowname17'])
            self.pass_rowname17=file['rowname17']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector18.bak'):
            file = shelve.open('VariableCollector\\VariableCollector18')
            self.tree_userQuestion.insert("", index=END , text=file['rowname18'])
            self.pass_rowname18=file['rowname18']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector19.bak'):
            file = shelve.open('VariableCollector\\VariableCollector19')
            self.tree_userQuestion.insert("", index=END , text=file['rowname19'])
            self.pass_rowname19=file['rowname19']
            file.close()
        if os.path.exists('VariableCollector\\VariableCollector20.bak'):
            file = shelve.open('VariableCollector\\VariableCollector20')
            self.tree_userQuestion.insert("", index=END , text=file['rowname20'])
            self.pass_rowname20=file['rowname20']
            file.close()





            
        if not os.path.exists('VariableCollector\\VariableCollector1.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector2.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector3.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector4.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector5.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector6.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector7.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector8.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector9.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector10.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector11.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector12.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector13.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector14.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector15.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector16.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector17.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector18.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector19.bak'):
            return
        if not os.path.exists('VariableCollector\\VariableCollector20.bak'):
            return


            
          
        """==============add to add_to_treeview endes here=================="""



    
    """from he begining of this line up to the comment'creating Question adder panel ends here ',
    the following function is to createQuestion adder panel ends here """

    def CreateQuestionAdderPanel(self,where):
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
        self.BtnSave_all = Button(f3,text='Save all',font=('arial',13,'bold'),bd=4,
                              bg='DeepSkyBlue4',fg='white',relief=FLAT,command=self.permanetly_Save_theQuestion)
        self.BtnSave_all.grid(column=1,row=0,padx=10)
        self.BtnSave = Button(f3,text='Save this',font=('arial',13,'bold'),bd=4,
                              bg='DeepSkyBlue4',fg='white',relief=FLAT,command=self.temporarly_Save_theQuestion)
        self.BtnSave.grid(column=0,row=0,padx=10)
        self.BtnClear = Button(f3,text='Clear',font=('arial',13,'bold'),bd=4,
                              bg='DeepSkyBlue4',fg='white',relief=FLAT,command=self.clear)
        self.BtnClear.grid(column=2,row=0,padx=10)
        self.BtnExit = Button(f3,text='Exit',font=('arial',13,'bold'),bd=4,
                              bg='DeepSkyBlue4',fg='white',relief=FLAT,command=self.exitingQuestionPanel,padx=10)
        self.BtnExit.grid(column=3,row=0,padx=10)
    
        #======binding hover color======
        self.BtnSave_all.bind('<Enter>',self.btnsave_all_enter)
        self.BtnSave_all.bind('<Leave>',self.btnsave_all_leave)
        
        self.BtnSave.bind('<Enter>',self.btnsave_enter)
        self.BtnSave.bind('<Leave>',self.btnsave_leave)
        
        self.BtnClear.bind('<Enter>',self.btnclear_enter)
        self.BtnClear.bind('<Leave>',self.btnclear_leave)
        
        self.BtnExit.bind('<Enter>',self.btnexit_enter)
        self.BtnExit.bind('<Leave>',self.btnexit_leave)
    def exitingQuestionPanel(self):
       file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
       file.write('')
       file.close()
       self.Qpanel.destroy()    
        #=====function hover color======
    def btnsave_all_enter(self,e):
        self.BtnSave_all.config(bg='DeepSkyBlue3')
    def btnsave_all_leave(self,e):
        self.BtnSave_all.config(bg='DeepSkyBlue4')        
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

    def temporarly_Save_theQuestion(self):
        self.question=self.var_q.get()
        self.choice_a=self.var_a.get()
        self.choice_b=self.var_b.get()
        self.choice_c=self.var_c.get()
        self.choice_d=self.var_d.get()
        if self.question == '':
            messagebox.showerror('error','the question is not inserted!')
        elif self.choice_a == '' or self.choice_b == '' or self.choice_c == '' or self.choice_d == '':
            ask = messagebox.showerror('error','all choices are not inserted!')
        #__________________________________________________________    
        else:
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
                file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
                read_previuosfile = file.read()
                file.close()
                if len(read_previuosfile) > 0:
                    file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','a')
                    file.write('\n'+'===')
                    file.write('\n'+self.question)
                    file.write('\n'+'    '+'A.'+self.choice_a)
                    file.write('\n'+'    '+'B.'+self.choice_b)
                    file.write('\n'+'    '+'C.'+self.choice_c)
                    file.write('\n'+'    '+'D.'+self.choice_d)
                    file.close()
                    messagebox.showinfo('add question','this question saved temporarly')
                elif len(read_previuosfile) == 0:
                    file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                    file.write('\n'+self.question)
                    file.write('\n'+'    '+'A.'+self.choice_a)
                    file.write('\n'+'    '+'B.'+self.choice_b)
                    file.write('\n'+'    '+'C.'+self.choice_c)
                    file.write('\n'+'    '+'D.'+self.choice_d)
                    messagebox.showinfo('add question','this question saved temporarly')
    def permanetly_Save_theQuestion(self):
        if not os.path.exists('UserQuestions\\UserQuestions1.txt'):
            
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions1.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')
        elif not os.path.exists('UserQuestions\\UserQuestions2.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions2.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')    
        elif not os.path.exists('UserQuestions\\UserQuestions3.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions3.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')
       #================================================
        elif not os.path.exists('UserQuestions\\UserQuestions4.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions4.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions5.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions5.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions6.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions6.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions7.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions7.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions8.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions8.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions9.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions9.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions10.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions10.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions11.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions11.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions12.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions12.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions13.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions13.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions14.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions14.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions15.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions15.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions16.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions16.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions17.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions17.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions18.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions18.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions19.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions19.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')

        elif not os.path.exists('UserQuestions\\UserQuestions20.txt'):
            tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','r')
            read_tempo_file = tempo_file.read()
            if len(read_tempo_file) == 0:
                messagebox.showerror('error','insert atleast one question')
            else:    
                file = open('UserQuestions\\UserQuestions20.txt','w')
                file.write(read_tempo_file)
                tempo_file.close()
                tempo_file = open('UserQuestions\\temporary_question_store\\temporary_question_store.txt','w')
                tempo_file.write('')
                tempo_file.close()
                file.close()
                messagebox.showinfo('info','your question\nhave permanently saved')
        self.Qpanel.destroy()
        #_________________________________________________________________       
    def clear(self):
        self.var_q.set('')
        self.var_a.set('')
        self.var_b.set('')
        self.var_c.set('')
        self.var_d.set('')     

"""==============creating Question adder panel ends here======================"""
# def main():
#     window = Tk()
#     app = Home(window)
#     window.mainloop()
# if __name__ == '__main__':
#     main()
