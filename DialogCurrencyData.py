from  tkinter import *

class DialogCurrencyData:

    def __init__(self, parent,mensagem):

        top = self.top = Toplevel(parent)

        
        Label(top, text=mensagem).pack()

        ##################
        self.valorDinheiro = ''
        self.valor = ''

        self.entryText = StringVar()

        ##################



        self.entry = Entry(top,textvariable=self.entryText,width=70) # entrada de dados
        self.entry.bind("<KeyRelease>",lambda v: top.after(400,self.txtValue_KeyUp))
        self.entry.pack(padx=5)

        self.valor = ""
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
    ########################################
    def insert_str(self,string, str_to_insert, index):
        tam = len(string)
        return string[:index] + str_to_insert + string[index:tam]

    

    def txtValue_KeyUp(self):

        entryTextAux = ''
        saux = ''
        entryTextAux = self.entryText.get()
        
        
        
        entryTextAux  = entryTextAux.replace(',', '')
        entryTextAux  = entryTextAux.replace(' ', '')
        
        if(entryTextAux[0:1] =='00'):
          entryTextAux  = entryTextAux.replace('0', '',1)
        
        if(not entryTextAux.isnumeric()):
          print('nao eh numerico')
          self.entryText.set('')
            
          return
        #self.entryText.set(entryTextAux)2

        self.valor = entryTextAux
        print(self.valor)
        #saux  = entryText.get()
        
        #saux = saux[(len(saux))-1:(len(saux))]
        
        #valor = valor + saux
        

        if (len(self.valor) == 0): 
          entryTextAux = ''
          self.entryText.set(entryTextAux)
        
        elif (len(self.valor) == 1):
          entryTextAux = '0,0' + self.valor
          self.entryText.set(entryTextAux)    
          
        elif (len(self.valor) == 2):
            entryTextAux = '0,' + self.valor
            self.entryText.set(entryTextAux) 
        elif (len(entryTextAux) >= 3):
        
            #entryTextAux = entryText.get()
            #if (entryTextAux.startswith('0,')):
            #    entryTextAux = self.insert_str(entryTextAux, ',', (len(entryTextAux) -2))
            #    entryTextAux = valor.replace('0,','')            
            #    entryText.set(entryTextAux) 
            
            #elif (entryTextAux[0] == '0' and entryTextAux[1] != ','):
            #    entryTextAux = entryTextAux[1:len(entryTextAux)]            
            #    entryText.set(entryTextAux) 
            
            if (entryTextAux.startswith('00')):
                print('entryTextAux.startswith(00)')
                print(entryTextAux)
                entryTextAux = entryTextAux.replace('00','',1)
                entryTextAux = self.insert_str(entryTextAux, ',', (len(entryTextAux) -2))
                
                if(entryTextAux.startswith(',')):
                  entryTextAux = '0' + entryTextAux

                print(entryTextAux)
                self.entryText.set(entryTextAux)

            elif (entryTextAux.startswith('0')):
                print('entryTextAux.startswith(0)')
                print(entryTextAux)
                entryTextAux = entryTextAux.replace('0','',1)
                entryTextAux = self.insert_str(entryTextAux, ',', (len(entryTextAux) -2))
                
                if(entryTextAux.startswith(',')):
                  entryTextAux = '0' + entryTextAux

                self.entryText.set(entryTextAux)
            
            #elif (entryTextAux.startswith('00')):
            
                
            #    entryTextAux = entryTextAux.replace('00','',1)
                
            #    self.entryText.set(entryTextAux)
    
            
            elif (int(float(entryTextAux.replace(',','.'))*100) == 0):
                entryTextAux = '0,00'
                self.entryText.set(entryTextAux)

            else:
              entryTextAux = self.insert_str(entryTextAux, ',', (len(entryTextAux) -2)) 
              self.entryText.set(entryTextAux)  
            
        


        entryTextAux  = entryTextAux.replace(',', '')
        entryTextAux  = entryTextAux.replace(' ', '')
        
        self.valor = entryTextAux

        self.entry.icursor("end")

        # coloca o simbolo relativo a moeda sendo utilizada
        #txtValue.Text = string.Format("0:C", Convert.ToDouble(valorDinheiro))
        #txtValue.Select(txtValue.Text.Length, 0)



    def ok(self):

      print ("value is", self.entry.get())
            
      self.valor  = self.valor.replace(',', '')
      self.valor  = self.valor.replace(' ', '')
        
      self.top.destroy()


############################
#root=Tk()
#sizex = 600
#sizey = 400
#posx  = 20
#posy  = 10
#root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))


#itemsforlistbox=['one','two','three','four','five','six','seven','eight 8888888888888888888888888888888888888888888']

#d = DialogCurrencyData(root,'Digite o valor:')

#root.wait_window(d.top)
#print(d.valor)


#root.mainloop()

#############################




