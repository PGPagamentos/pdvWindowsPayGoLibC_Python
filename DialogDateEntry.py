from  tkinter import *


class DialogDateEntry():
    def __init__(self, master, message,yearPar=2,frame_look={},  **look ):
        self.bExit = True
        args = dict(relief=SUNKEN, border=1)
        args0 = dict(relief=SUNKEN, border=1)
        args.update(frame_look)
        
        top = self.top = Toplevel(master)
        
        self.valor = ''
        self.label = Label(top, text=message)
        


        args = {'relief': FLAT}
        args.update(look)

        self.entry_1 = Entry(top, width=2, **args)
        
        self.label_ini = Label(top, text=' ', **args)
        self.label_1 = Label(top, text='/', **args)
        self.entry_2 = Entry(top, width=2, **args)
        self.label_2 = Label(top, text='/', **args)
        
        if(yearPar == 4): # ano com 4 digitos
          self.entry_3 = Entry(top, width=4, **args)
        else:
          self.entry_3 = Entry(top, width=2, **args)

        self.label_sep = Label(top, text='  ', **args)

        self.b = Button(top, text="OK")

        self.label.pack(side=TOP,anchor=N)

        self.label_ini.pack(side=LEFT,anchor=W)
        self.entry_1.pack(side=LEFT,anchor=W)
        self.label_1.pack(side=LEFT,anchor=W)
        self.entry_2.pack(side=LEFT,anchor=W)
        self.label_2.pack(side=LEFT,anchor=W)
        self.entry_3.pack(side=LEFT,anchor=W)

        self.label_sep.pack(side=LEFT,anchor=W)
        self.b.pack(pady=10,side=LEFT,anchor=E)


        self.entries = [self.entry_1, self.entry_2, self.entry_3]

        self.entry_1.bind('<KeyRelease>', lambda e: self._check(0, 2))
        self.entry_2.bind('<KeyRelease>', lambda e: self._check(1, 2))

        if(yearPar == 4): # ano com 4 digitos
           self.entry_3.bind('<KeyRelease>', lambda e: self._check(2, 4))
        else: 
           self.entry_3.bind('<KeyRelease>', lambda e: self._check(2, 2))
        
        
        self.b.bind('<Button-1>', lambda e: self.ok())

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
        top.wm_geometry("%dx%d+%d+%d" % (220, 80, positionRight, positionDown)) 

    def _backspace(self, entry):
        cont = entry.get()
        entry.delete(0, END)
        entry.insert(0, cont[:-1])

    def _check(self, index, size):
        entry = self.entries[index]
        next_index = index + 1
        next_entry = self.entries[next_index] if next_index < len(self.entries) else None
        data = entry.get()

        if len(data) > size or not data.isdigit():
            self._backspace(entry)
        if len(data) >= size and next_entry:
            next_entry.focus()

    def get(self):
        return [e.get() for e in self.entries]

    def ok(self):        
      self.bExit = False    
      val_list = self.get()  
      print('teste de data:')
      print(val_list)

      val_aux = ''
      for item in val_list:
        print(item)
        val_aux = val_aux + item
      print(val_aux)
      self.valor = val_aux

      self.top.destroy()

if __name__ == '__main__':        
    win = Tk()
    win.title('DateEntry demo')

    dentry = DialogDateEntry(win, 'entre com a data:',4,font=('Courier', 16, NORMAL), border=0)

    win.wait_window(dentry.top)
    print(dentry.valor)
    print('valor :' + dentry.valor)
    
    win.mainloop()