from tkinter import *
from tkinter import ttk
class PhysicalConstant:
    def __init__(self,master):
        self.master = master
        self.constbox = Toplevel(self.master)
        self.constbox.resizable(width=False,height=False)
        self.constbox.transient(self.master)
        self.constbox.title('physical constant')
        self.constbox.config(bg='slategray1')
        y = ((self.constbox.winfo_screenheight()) / 2) - 282
        x = ((self.constbox.winfo_screenwidth()) / 2) - 270
        self.constbox.geometry(("350x350+" + str(int(x)) + "+" + str(int(y))))
        Label(self.constbox,text='Physical constants',font = ('Cambria(Headings)',13,'bold'),bg='slategray1').pack()
        self.const_treeview()

    def const_treeview(self):
        self.const_var = StringVar()
        self.const_tree = ttk.Treeview(self.constbox,selectmode=BROWSE,columns=("quanta"))

        self.const_tree.column(0, anchor=CENTER)
        self.const_tree.heading('#0',text='Physical constant')
        self.const_tree.heading('#1', text='Symbol')
        self.const_tree.pack(expand = True,fill=Y)
        self.const_tree.bind("<<TreeviewSelect>>",
              lambda event: self.valueAdder(self.const_tree.item(self.const_tree.selection())['text']))
        self.const_frame = Frame(self.constbox,bg='white')
        self.const_frame.pack(fill=X)

        #self.const_label = Label(self.const_frame, textvariable=self.const_var,font=('areal',15))
        #self.const_label.pack(fill=X)

        # operning the small images

        p1 = PhotoImage(file='icon\\me.png')
        me = Label(self.const_tree, image=p1, bg='white')
        me.place(x=290, y=85)
        me.image = p1
        #---------------
        p2 = PhotoImage(file='icon\\mp.png')
        mp = Label(self.const_tree, image=p2, bg='white')
        mp.place(x=290, y=105)
        mp.image = p2
        # ---------------
        p3 = PhotoImage(file='icon\\Eo.png')
        Eo = Label(self.const_tree, image=p3, bg='white')
        Eo.place(x=290, y=145)
        Eo.image = p3
        # ---------------
        p4 = PhotoImage(file='icon\\mo.png')
        mo = Label(self.const_tree, image=p4, bg='white')
        mo.place(x=290, y=167)
        mo.image = p4
        # ---------------
        p4 = PhotoImage(file='icon\\Me2.png')
        Me = Label(self.const_tree, image=p4, bg='white')
        Me.place(x=290, y=205)
        Me.image = p4
        # ---------------
        p5 = PhotoImage(file='icon\\Re.png')
        me = Label(self.const_tree, image=p5, bg='white')
        me.place(x=290, y=225)
        me.image = p5
        # inserting values
        self.const_tree.insert("",index=END ,text='Acceleration due to gravity',value='g')
        self.const_tree.insert("", index=END, text='Gravitational constant', value='G')
        self.const_tree.insert("", index=END, text='Speed of light in vacuum', value='c')
        self.const_tree.insert("", index=END, text='Electron mass', value='')
        self.const_tree.insert("", index=END, text='Proton mass', value='')
        self.const_tree.insert("", index=END, text='Elementary charge', value='e')
        self.const_tree.insert("", index=END, text='Permittivity of free space', value='')
        self.const_tree.insert("", index=END, text='Permeability of free space', value='')
        self.const_tree.insert("", index=END, text='Universal gas constant', value='R')
        self.const_tree.insert("", index=END, text="Earth's mass", value='')
        self.const_tree.insert("", index=END, text="Earth's radius", value='')

    def image_placer(self,imgfile_name):
        opened_img = PhotoImage(file=imgfile_name)
        imglbl=Label(self.const_frame,image=opened_img)
        imglbl.grid(column=0,row=0)
        imglbl.image=opened_img
    def valueAdder(self,rowname):
        if rowname == 'Acceleration due to gravity':
            self.image_placer("image\constant\g.PNG")
        elif rowname ==  'Gravitational constant':
            self.image_placer("image\constant\G2.PNG")
        elif rowname ==  'Speed of light in vacuum':
            self.image_placer("image\constant\c.PNG")
        elif rowname ==  'Electron mass':
            self.image_placer("image\constant\me.PNG")
        elif rowname ==  'Proton mass':
            self.image_placer("image\constant\mp.PNG")
        elif rowname ==  'Elementary charge':
            self.image_placer("image\constant\e.PNG")
        elif rowname ==  'Permittivity of free space':
            self.image_placer("image\constant\Eo.PNG")
        elif rowname ==  'Permeability of free space':
            self.image_placer("image\constant\mo.PNG")
        elif rowname ==  'Universal gas constant':
            self.image_placer("image\constant\R.PNG")
        elif rowname ==  "Earth's mass":
            self.image_placer("image\constant\Me2.PNG")
        elif rowname ==  "Earth's radius":
            self.image_placer("image\constant\Re.PNG")
        #inserting value


#root=Tk()
#a=PhysicalConstant(root)
#root.mainloop()