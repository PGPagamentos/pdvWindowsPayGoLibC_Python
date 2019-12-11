from  tkinter import *
from tkinter import ttk


class DialogConfirmationWindow:

    
    def __init__(self, parent,itemsforcombobox,mensagem):

        top = self.top = Toplevel(parent)

        
        Label(top, text=mensagem).pack()

        #self.e = Entry(top) # entrada de dados
        #self.e.pack(padx=5)

        ###############
        self.cb = ttk.Combobox(top,width = 60, values = itemsforcombobox)

        #self.cb.current(1)
        
        self.cb.pack()
        self.cb.bind('<<ComboboxSelected>>', self.CurSelect)


        ###############
 
        self.valor = ""
        #mylistbox=Listbox(top,width= 50,font=('courier',10))
        #mylistbox.bind('<<ListboxSelect>>',self.CurSelect)
        #mylistbox.pack()

        
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

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
        top.geometry("+{}+{}".format(positionRight, positionDown))



    def ok(self):

        print ("value is", self.valor)
        self.top.destroy()

    def CurSelect(self,event):
        print("New Element Selected")
        print(self.cb.get())
        print(self.cb.current())
        self.valor = self.cb.get()


    
############################
# codig para teste
#from tkinter import*
#root=Tk()
#sizex = 600
#sizey = 400
#posx  = 20
#posy  = 10
#root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))


#itemsforlistbox=['one','two','three','four','five','six','seven','eight']

#d = DialogConfirmationWindow(root,itemsforlistbox,'selecione a opcao:')

#root.wait_window(d.top)
#print(d.valor)


#root.mainloop()

#############################
