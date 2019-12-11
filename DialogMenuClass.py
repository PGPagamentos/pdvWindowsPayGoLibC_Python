from  tkinter import *

class DialogMenuClass:

    
    def __init__(self, parent,itemsforlistbox,mensagem):

        top = self.top = Toplevel(parent)

        
        Label(top, text=mensagem).pack()

        self.valor = ""
        mylistbox=Listbox(top,width= 50,font=('courier',10))
        mylistbox.bind('<<ListboxSelect>>',self.CurSelect)
        mylistbox.pack()

        for items in itemsforlistbox:
            mylistbox.insert(END,items)

        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

        ######################################################
        # centraliza a janela
        # Obtem a altura e largura da janela
        windowWidth = parent.winfo_reqwidth()
        windowHeight = parent.winfo_reqheight()
        print("Width",windowWidth,"Height",windowHeight)
        
        # Obtem a posicao central
        positionRight = int(parent.winfo_screenwidth()/2 - windowWidth/2)
        positionDown  = int(parent.winfo_screenheight()/2 - windowHeight/2)
        
        # centraliza a janela
        top.geometry("+{}+{}".format(positionRight, positionDown))



    def ok(self):

        print ("value is", self.valor)
        self.top.destroy()

    def CurSelect(self,event):
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        print(picked)
        self.valor = selection[0]


    
############################
# codigo de teste da classe
#
#from tkinter import*
#root=Tk()
#sizex = 600
#sizey = 400
#posx  = 20
#posy  = 10
#root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))


#itemsforlistbox=['one','two','three','four','five','six','seven','eight 8888888888888888888888888888888888888888888']

#d = DialogMenuData(root,itemsforlistbox,'selecione a opcao:')

#root.wait_window(d.top)
#print(d.valor)


#root.mainloop()

#############################













