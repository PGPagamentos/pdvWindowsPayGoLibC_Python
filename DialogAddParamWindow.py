from  tkinter import *
from tkinter import ttk
from  Enums import *

class DialogAddParamWindow:

    
    def __init__(self, parent,itemsforcombobox,mensagem):

        top = self.top = Toplevel(parent)

        self.ValParam = ''


        #labelD.place(relx=0.5, rely=0.5)
 
        Label(top, text=mensagem).place(rely=0.0, relx=0.05)

        Label(top, text="Valor do Parametro:").place(rely=0.0, relx=0.65)
        ###############


        self.cb = ttk.Combobox(top,width = 50, values = itemsforcombobox)

        #self.cb.current(1)
        
        self.cb.place(rely=0.2, relx=0.05)
        self.cb.bind('<<ComboboxSelected>>', self.CurSelect)

        
        self.EntryValParam = Entry(top) # entrada de dados
        self.EntryValParam.place(rely=0.2, relx=0.65)
        self.EntryValParam.config(width=25)
        self.EntryValParam.insert(0,'0')

        
        ###############
 
        self.param = ""
        
        
        
        b = Button(top, text="OK", command=self.ok)
        b.config(width=10)
        b.place(rely=0.6, relx=0.45)


        ######################################################
        # centraliza a janela
        # Obtem a altura e largura da janela
        windowWidth = top.winfo_reqwidth() 
        windowHeight = top.winfo_reqheight()
        print("Width",windowWidth,"Height",windowHeight)
        
        # Obtem a posicao central
        positionRight = int(top.winfo_screenwidth()/2 - windowWidth/2)
        positionDown  = int(top.winfo_screenheight()/2 - windowHeight/2)
        
        # centraliza a janela
        #top.geometry("+{}+{}".format(positionRight *2 , positionDown *2))
        top.wm_geometry("%dx%d+%d+%d" % (600, 100, positionRight, positionDown)) 


    def ok(self):

        print ("value is", self.valor)
        self.param = self.cb.get()
        print(self.EntryValParam.get())
        self.ValParam = self.EntryValParam.get()
        self.top.destroy()

    def CurSelect(self,event):
        print("New Element Selected")
        print(self.cb.get())
        print(self.cb.current())
        self.valor = self.cb.get()
        print(self.EntryValParam.get())
        self.ValParam = self.EntryValParam.get()
        


    
############################
# codig para teste
#from tkinter import*
#root=Tk()
#sizex = 300
#sizey = 300
#posx  = 20
#posy  = 10
#root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))




#itemsforlistbox=['one','two','three','four','five','six','seven','eight']

#d = DialogAddParamWindow(root,itemsforlistbox,'selecione a opcao:')

#root.wait_window(d.top)
#print(d.param)
#print(d.ValParam)
#print(d.min)


#root.mainloop()

#############################
