from  tkinter import *

class DialogMessage:

    def __init__(self, parent,mensagem):

        top = self.top = Toplevel(parent)

        top.title('Mensagem Informativa')
        Label(top, width= 60,wraplength=400,font =('curier',11) ,text=mensagem).pack()
        
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
        self.top.destroy()


############################
#root=Tk()
#sizex = 600
#sizey = 400
#posx  = 20
#posy  = 10
#root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))


#itemsforlistbox=['one','two','three','four','five','six','seven','eight 8888888888888888888888888888888888888888888']

#d = DialogMessage(root,'aaaaaaaaaaaaaaaaaaaaaatestand a mensagem asdf asdfasdfasd fas df asd fas7457457474574567 xbxcbxcbxcvbxcvbxcbxcbxcbxcbqqqqqqqqqqqqqqqqqqqqqqqqqqq')

#root.wait_window(d.top)
#print(d.valor)


#root.mainloop()

#############################




