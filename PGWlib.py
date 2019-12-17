from  Enums import *
from  CustomObjects import *
import os
from  time import *
#import ctypes.
from  ctypes import *
from  Interops import *
from  DialogTypedData import *
from  DialogMenuClass  import * 
from  DialogMessage    import *
from time import *
from DialogConfirmationWindow import *
from DialogSelectUserDataWindow import *

myPGWebLib = None


listaParametros = []

# cria objeto de acesso a DLL
myPGWebLib = PGWebLibrary()

MainWindow  = ""



def AddMandatoryParamsOld():
   # Adiciona os parâmetros obrigatórios

   myPGWebLib.PW_iAddParam(E_PWINFO.PWINFO_AUTDEV.value, "NTK Solutions Ltda")
   myPGWebLib.PW_iAddParam(E_PWINFO.PWINFO_AUTVER.value, "1.0")
   myPGWebLib.PW_iAddParam(E_PWINFO.PWINFO_AUTNAME.value, "PDVS")
   myPGWebLib.PW_iAddParam(E_PWINFO.PWINFO_AUTCAP.value, "28")
   #myPGWebLib.PW_iAddParam(E_PWINFO.PWINFO_AUTHTECHUSER.value, "PGWEBLIBTEST")

   #  // Adiciona os parâmetros obrigatórios
   #gstHwFuncs.pPW_iAddParam(E_PWINFO.PWINFO_AUTDEV, "SETIS AUTOMACAO E SISTEMA LTDA");
   #gstHwFuncs.pPW_iAddParam(E_PWINFO.PWINFO_AUTVER, "1.0");
   #gstHwFuncs.pPW_iAddParam(E_PWINFO.PWINFO_AUTNAME, "PGWEBLIBTEST");
   #gstHwFuncs.pPW_iAddParam(E_PWINFO.PWINFO_AUTCAP, "15");
   #gstHwFuncs.pPW_iAddParam(E_PWINFO.PWINFO_AUTHTECHUSER, "PGWEBLIBTEST");

   #myPGWebLib.PW_iAddParam(E_PWINFO.PWINFO_AUTDEV.value, 'AUTOMACAO DE SISTEMAS')
   #myPGWebLib.PW_iAddParam(E_PWINFO.PWINFO_AUTVER.value, '2.0.0')
   #myPGWebLib.PW_iAddParam(E_PWINFO.PWINFO_AUTNAME.value, 'PAYGOTESTE')
   #myPGWebLib.PW_iAddParam(E_PWINFO.PWINFO_AUTCAP.value, '15')
   #myPGWebLib.PW_iAddParam(E_PWINFO.PWINFO_AUTHTECHUSER.value, 'PAYGOTESTE')

################
#adiciona os parametros obrigatorios
def addMandatoryParameters(top):
 
    addParameter(E_PWINFO.PWINFO_AUTNAME.name, E_PWINFO.PWINFO_AUTNAME.value, "PDVS",top);
    addParameter(E_PWINFO.PWINFO_AUTVER.name,  E_PWINFO.PWINFO_AUTVER.value, "1.0",top);
    addParameter(E_PWINFO.PWINFO_AUTDEV.name,  E_PWINFO.PWINFO_AUTDEV.value, "NTK Solutions Ltda",top);
    addParameter(E_PWINFO.PWINFO_AUTCAP.name,  E_PWINFO.PWINFO_AUTCAP.value, "28",top);  

# fim de addMandatoryParameters2
 

# metodo para adicao de parametros
def addParameter(sParName, iParId, sParVal, top = None): 
  Cobj = PW_Parameter(sParName, iParId, sParVal)
  strItem = sParName + '(' + str(iParId) +  ')' + ':' + sParVal
  listaParametros.append(Cobj)
  if(top != None):
      top.InsereParametro(strItem)
  print(listaParametros)
  
 #ParametersListStore.AppendValues(par.ToString());	

# fim de addParameter

##################

def DelParameter(iIndice): 
    o = listaParametros.pop(iIndice)
    print(o) 


def CleanParameterList(): 
    o = listaParametros.clear()
    print(listaParametros) 






########################################################
def PrintResultParams():
      szAux = (c_char * 10000)() # aloca um array de 10000 char
      iRet=0
      i = 0

      # Percorre todos os números inteiros, exibindo o valor do parâmetro PWINFO_XXX
      # sempre que o retorno for de dados disponível
      # Essa implementação foi feita desta forma para facilitar o exemplo, a função
      # PW_iGetResult() deve ser chamada somente para informações documentadas, as
      # chamadas adicionais causarão lentidão no sistema como um todo.
      
      for i in E_PWINFO:
      
        #if(i.value == E_PWINFO.PWINFO_PPINFO):
        #    continue

        iRet = myPGWebLib.PW_iGetResult( i.value, szAux, sizeof(szAux))
        if( iRet == E_PWRET.PWRET_OK.value):
        
            #InputCR(szAux)
            print( "\n", pszGetInfoDescription(i.value),"=", i.value,"\n", szAux)

            #// Caso seja um parâmetro necessário para a confirmação da transação
            #// o armazena na estrutura existente para essa finalidade.
            #switch(i)
            #{
            #   case(PWINFO_REQNUM):
            #      strcpy( gstConfirmData.szReqNum, szAux)
            #      break
            #
            #   case(PWINFO_AUTEXTREF):
            #      strcpy( gstConfirmData.szHostRef, szAux)
            #      break
            #
            #   case(PWINFO_AUTLOCREF):
            #      strcpy( gstConfirmData.szLocRef, szAux)
            #      break
            #
            #   case(PWINFO_VIRTMERCH):
            #      strcpy( gstConfirmData.szVirtMerch, szAux)
            #      break
            #
            #   case(PWINFO_AUTHSYST):
            #      strcpy( gstConfirmData.szAuthSyst, szAux)
            #      break
            #
        
      
      print("\n") 




def PrintReturnDescription(iReturnCode,pszDspMsg):

    if(iReturnCode == E_PWRET.PWRET_OK):
       print("\nRetorno = PWRET_OK")
       
    elif(iReturnCode == E_PWRET.PWRET_INVCALL):
       print("\nRetorno = PWRET_INVCALL")
      
    elif(iReturnCode == E_PWRET.PWRET_INVPARAM):
       print("\nRetorno = PWRET_INVPARAM")
       
    
    elif(iReturnCode == E_PWRET.PWRET_NODATA):
       print("\nRetorno = PWRET_NODATA")
       
    
    elif(iReturnCode == E_PWRET.PWRET_BUFOVFLW):
       print("\nRetorno = PWRET_BUFOVFLW")
       
    elif(iReturnCode == E_PWRET.PWRET_MOREDATA):
       print("\nRetorno = PWRET_MOREDATA")
    
    elif(iReturnCode == E_PWRET.PWRET_DLLNOTINIT):
       print("\nRetorno = PWRET_DLLNOTINIT")
       
    elif(iReturnCode == E_PWRET.PWRET_NOTINST):
       print("\nRetorno = PWRET_NOTINST")
       
    elif(iReturnCode == E_PWRET.PWRET_TRNNOTINIT):
       print("\nRetorno = PWRET_TRNNOTINIT")
      
    elif(iReturnCode == E_PWRET.PWRET_NOMANDATORY):
       print("\nRetorno = PWRET_NOMANDATORY")
    
    elif(iReturnCode == E_PWRET.PWRET_TIMEOUT):
       print("\nRetorno = PWRET_TIMEOUT")
       
    elif(iReturnCode == E_PWRET.PWRET_CANCEL):
       print("\nRetorno = PWRET_CANCEL")
    
    elif(iReturnCode == E_PWRET.PWRET_FALLBACK):
       print("\nRetorno = PWRET_FALLBACK")
    
    elif(iReturnCode == E_PWRET.PWRET_DISPLAY):
       print("\nRetorno = PWRET_DISPLAY")
       InputCR(pszDspMsg)
       print("\n%s", pszDspMsg)
       
    elif(iReturnCode == E_PWRET.PWRET_NOTHING):
       print(".")
       
    elif(iReturnCode == E_PWRET.PWRET_FROMHOST):
       print("\nRetorno = ERRO DO HOST")
       
    elif(iReturnCode == E_PWRET.PWRET_SSLCERTERR):
       print("\nRetorno = PWRET_SSLCERTERR")
       
    elif(iReturnCode == E_PWRET.PWRET_SSLNCONN):
       print("\nRetorno = PWRET_SSLNCONN")
       
    else:
       print("\nRetorno = OUTRO ERRO =", iReturnCode)
       
  # Imprime os resultados disponíveis na tela caso seja fim da transação
    if( iReturnCode != E_PWRET.PWRET_MOREDATA and iReturnCode!=E_PWRET.PWRET_DISPLAY and 
        iReturnCode  != E_PWRET.PWRET_NOTHING and iReturnCode!=E_PWRET.PWRET_FALLBACK):
          PrintResultParams()




def InputCR(pszSourceStr):
        mytext = pszSourceStr
        mytext.replace(r"\r", r"\r\n")
        return mytext



def loopPP(timeout = 0):

    import pdvWindowsPayGoLibC_Python_support
    MainWindow  = pdvWindowsPayGoLibC_Python_support.w
    MainWindowRoot = pdvWindowsPayGoLibC_Python_support.root


    
    ret = 99;
    counter = 0;
    
    while True:
    
        ret = E_PWRET.PWRET_TIMEOUT.value;
        if ((counter > timeout) and (timeout > 0)): 
           return ret;

        counter = counter + 1
        sleep(0.5)
        
        displayMessage = create_string_buffer(1000)
        
        
        ret = myPGWebLib.PW_iPPEventLoop(displayMessage, 1000)

        #if (ret == E_PWRET.PWRET_DISPLAY.value):
        #    fdm = DialogMessage(MainWindowRoot,str(displayMessage))
        #    MainWindowRoot.wait_window(fdm.top)

        if ((ret != E_PWRET.PWRET_NOTHING.value) and  (ret != E_PWRET.PWRET_DISPLAY.value)):
            break
   
    
    return ret;





def iExecGetDataInstall(vstGetData,iNumParam):
      i = 0
      j = 0 
      iKey = 0 
      iRet = 0
      
      szAux       = (c_char * 1024)()
      szDspMsg    = (c_char * 128)()
      szMsgPinPad = (c_char * 34)()
      
      ulEvent=0

      import pdvWindowsPayGoLibC_Python_support
      MainWindow  = pdvWindowsPayGoLibC_Python_support.w
      
      # Caso exista uma mensagem a ser exibida antes da captura do próximo dado, a exibe
      if(vstGetData[0].szMsgPrevia != b''):
        #InputCR(vstGetData[0].szMsgPrevia)
        print("\nMensagem = ", vstGetData[0].szMsgPrevia, "\n")
      
      
      # Enquanto houverem dados para capturar
      # inicio do for i in range(iNumParam):
#      iNumParam = 1
      for i in range(0,iNumParam-1):
        # Imprime na tela qual informação está sendo capturada
        
        if(vstGetData[i].wIdentificador != 0):
          print("\nDado a capturar = ", pszGetInfoDescription(vstGetData[i].wIdentificador),"->" ,
            vstGetData[i].wIdentificador, "\n")

        #Captura de acordo com o tipo de captura
        
        # Captura de dado digitado
        # E_PWDAT.PWDAT_TYPED
        if((vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_TYPED.value) or
             (vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_USERAUTH.value)  ):

          print("\nTipo de dados = Digitado =", vstGetData[i].bTipoDeDado )
          print("\nTamanho minimo = %d", vstGetData[i].bTamanhoMinimo )
          print("\nTamanho maximo = %d", vstGetData[i].bTamanhoMaximo)
          print("\nValor atual:%s\n", vstGetData[i].szValorInicial)
        
          if(vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_USERAUTH.value):
             szAux = input("Entre com a senha técnica:")
          else:
             szAux = input(vstGetData[i].szPrompt)
          
          iRet = myPGWebLib.PW_iAddParam(vstGetData[i].wIdentificador, szAux)
          if(iRet != 0 ):
              print("\nERRO AO ADICIONAR PARAMETRO...")

        # Menu de opções
        elif(vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_MENU.value):
            print("\nTipo de dados = MENU")
            #InputCR(vstGetData[i].szPrompt)
            print("\n%s\n", vstGetData[i].szPrompt)

            # Caso só tenha uma opção, escolhe automaticamente
            if( vstGetData[i].bNumOpcoesMenu == 1):
              
                  print("\nMENU COM 1 OPCAO... ADICIONANDO AUTOMATICAMENTE...")
                  iRet = myPGWebLib.pPW_iAddParam(vstGetData[i].wIdentificador, vstGetData[i].vszValorMenu[0])
                  if(iRet != 0):
                    print("\nERRO AO ADICIONAR PARAMETRO...")
                    break
              

              
            for j in  range(vstGetData[i].bNumOpcoesMenu): 
                print("\n%d - %s", vstGetData[i].vszValorMenu[j].value, vstGetData[i].vszTextoMenu[j].value)

            
            iKey = input("\n\nSELECIONE A OPCAO:")

            iKey = int(iKey)

            iKey = iKey - 1

            print("\n", iKey)
            
            param = vstGetData[i].vszValorMenu[iKey].value.decode()
            iRet = myPGWebLib.PW_iAddParam(vstGetData[i].wIdentificador, param)
            
            if(iRet != 0):
              print("\nERRO AO ADICIONAR PARAMETRO...")

          
        
        
          
        # fim de E_PWDAT.PWDAT_TYPED


        '''
        elif(vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_PPREMCRD.value):
            print("\nTipo de dados = PWDAT_PPREMCRD")
            #iRet = myPGWebLib.(i)
            PrintReturnDescription(iRet, szDspMsg)
            
            if(iRet != 0):
              return iRet

            szDspMsg = create_string_buffer(10000)
            # inicio do while
            while True:
            
              iRet =myPGWebLib.PW_iPPEventLoop(szDspMsg, sizeof(szDspMsg))
              #PrintReturnDescription(iRet, szDspMsg)
              
              if(iRet!=E_PWRET.PWRET_OK and iRet!=E_PWRET.PWRET_DISPLAY and iRet!=E_PWRET.PWRET_NOTHING):
                  return iRet
              
              sleep(500)
              
              if(iRet == E_PWRET.PWRET_OK):
                break
            # fim do while
        # fim de E_PWDAT.PWDAT_PPENCPIN
################################
        # Captura da senha criptografada  
        # E_PWDAT.PWDAT_PPENCPIN
        elif(vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_PPENCPIN.value):
            print("\nTipo de dados = SENHA")
            iRet = myPGWebLib.pPW_iPPGetPIN(i)
            PrintReturnDescription(iRet, szDspMsg)
            
            if(iRet != 0):
              return iRet

            # inicio do while
            while True:
            
              iRet =myPGWebLib.pPW_iPPEventLoop(szDspMsg, sizeof(szDspMsg))
              PrintReturnDescription(iRet, szDspMsg)
              
              if(iRet!=E_PWRET.PWRET_OK and iRet!=E_PWRET.PWRET_DISPLAY and iRet!=E_PWRET.PWRET_NOTHING):
                  return iRet
              
              sleep(500)
              
              if(iRet == E_PWRET.PWRET_OK):
                break
            # fim do while
        # fim de E_PWDAT.PWDAT_PPENCPIN
        '''
        

              
      return E_PWRET.PWRET_OK.value
  # fim de iExecGetDataInstall



def iExecGetDataInstallJanelas(vstGetData,iNumParam):
      i = 0
      j = 0 
      iKey = 0 
      ret = 0
      index = 0
      
      szAux       = (c_char * 1024)()
      szDspMsg    = (c_char * 128)()
      szMsgPinPad = (c_char * 34)()
      
      ulEvent=0

      import pdvWindowsPayGoLibC_Python_support
      MainWindow  = pdvWindowsPayGoLibC_Python_support.w
      MainWindowRoot = pdvWindowsPayGoLibC_Python_support.root

      # Caso exista uma mensagem a ser exibida antes da captura do próximo dado, a exibe
      if(vstGetData[0].szMsgPrevia != b''):
        #InputCR(vstGetData[0].szMsgPrevia)
        print("\nMensagem = ", vstGetData[0].szMsgPrevia, "\n")
      
      
      # Enquanto houverem dados para capturar
      # inicio do for i in range(iNumParam):
#      iNumParam = 1
      for i in range(0,iNumParam):
        # Imprime na tela qual informação está sendo capturada
        
        if(vstGetData[i].wIdentificador != 0):
          print("\nDado a capturar = ", pszGetInfoDescription(vstGetData[i].wIdentificador),"->" ,
            vstGetData[i].wIdentificador, "\n")

        #Captura de acordo com o tipo de captura
        ret = 0
        # Captura de dado digitado
        # E_PWDAT.PWDAT_TYPED
        if(vstGetData[i].bTipoDeDado == 0):
          return 0
        
        elif((vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_TYPED.value) or
             (vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_USERAUTH.value) or
             (vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_BARCODE.value)  ):

          print("\nTipo de dados = Digitado =", vstGetData[i].bTipoDeDado )
          print("\nTamanho minimo = %d", vstGetData[i].bTamanhoMinimo )
          print("\nTamanho maximo = %d", vstGetData[i].bTamanhoMaximo)
          print("\nValor atual:%s\n", vstGetData[i].szValorInicial)
        
          #rootwindow = pdvWindowsPayGoLibC_Python_support.root
          if(vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_USERAUTH.value):
             d = DialogTypedData(MainWindowRoot,"Entre com a senha técnica:")
             MainWindowRoot.wait_window(d.top)
             print(d.valor)
             szAux = d.valor

          else:
             d = DialogTypedData(MainWindowRoot,vstGetData[i].szPrompt)
             MainWindowRoot.wait_window(d.top)
             print(d.valor)
             szAux = d.valor

          ret = myPGWebLib.PW_iAddParam(vstGetData[i].wIdentificador, szAux)
          if(ret != 0 ):
              print("\nERRO AO ADICIONAR PARAMETRO...")

        # Menu de opções
        elif(vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_MENU.value):
            print("\nTipo de dados = MENU")
            #InputCR(vstGetData[i].szPrompt)
            print("\n%s\n", vstGetData[i].szPrompt)

            # Caso só tenha uma opção, escolhe automaticamente
            if( vstGetData[i].bNumOpcoesMenu == 1):
              
                  print("\nMENU COM 1 OPCAO... ADICIONANDO AUTOMATICAMENTE...")
                  iRet = myPGWebLib.pPW_iAddParam(vstGetData[i].wIdentificador, vstGetData[i].vszValorMenu[0])
                  if(iRet != 0):
                    print("\nERRO AO ADICIONAR PARAMETRO...")
                    break
              

            listaOpcoes = []  
            #for j in  range(vstGetData[i].bNumOpcoesMenu): 
            #    print("\n%d - %s", vstGetData[i].vszValorMenu[j].value, vstGetData[i].vszTextoMenu[j].value)
            
            for j in  range(vstGetData[i].bNumOpcoesMenu): 
                opcao = str(j + 1)
                opcao = opcao + " - " +  vstGetData[i].vszTextoMenu[j].value.decode()
                listaOpcoes.append(opcao)

            
            d = DialogMenuClass(MainWindowRoot,listaOpcoes,vstGetData[i].szPrompt)

            MainWindowRoot.wait_window(d.top)
            print(d.valor)

            iKey = int(d.valor)

            #iKey = iKey - 1

            print("\n", iKey)
            
            param = vstGetData[i].vszValorMenu[iKey].value.decode()
            ret = myPGWebLib.PW_iAddParam(vstGetData[i].wIdentificador, param)
            
            if(ret != 0):
              print("\nERRO AO ADICIONAR PARAMETRO...")

        elif(vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_CARDINF.value):
              #if(vstGetData[i].ulTipoEntradaCartao == 1):
              #    PW_GetData temp = item
              #    temp.wIdentificador = E_PWINFO.PWINFO_CARDFULLPAN.value
              #    ret = getTypedDataFromUser(temp);
              #else:
              ret = myPGWebLib.PW_iPPGetCard(index)
              if (ret == E_PWRET.PWRET_OK.value): ret = loopPP()
              
              MainWindow.Loga('myPGWebLib.PW_iPPGetCard')
              return ret
              
        elif(vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_CARDONL.value):
              ret = myPGWebLib.PW_iPPFinishChip(index)
              
              if (ret == E_PWRET.PWRET_OK.value): ret = loopPP()
              MainWindow.Loga('myPGWebLib.PW_iPPFinishChip')
              return ret
        #fim de E_PWDAT.PWDAT_CARDONL      

        elif(vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_CARDOFF.value):
            ret = myPGWebLib.PW_iPPGoOnChip(index)
            
            if (ret == E_PWRET.PWRET_OK.value): ret = loopPP()
            MainWindow.Loga('myPGWebLib.PW_iPPGoOnChip')
            return ret

        #elif(vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_MENU.value):
        #    return getMenuFromUser(item)

        elif(vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_PPCONF.value):
            ret = myPGWebLib.PW_iPPConfirmData(index)
            
            if (ret == E_PWRET.PWRET_OK.value): ret = loopPP()
            MainWindow.Loga('myPGWebLib.PW_iPPConfirmData')

            return ret

        elif(vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_PPENCPIN.value):
            ret = myPGWebLib.PW_iPPGetPIN(index)
            
            if (ret == E_PWRET.PWRET_OK.value): ret = loopPP()
            MainWindow.Loga('myPGWebLib.PW_iPPGetPIN')
            return ret

        elif(vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_PPENTRY.value):
            ret = myPGWebLib.PW_iPPGetData(index)
            
            if (ret == E_PWRET.PWRET_OK.value): ret = loopPP()
            MainWindow.Loga('myPGWebLib.PW_iPPGetData')
            return ret

        elif(vstGetData[i].bTipoDeDado == E_PWDAT.PWDAT_PPREMCRD.value):
            ret = myPGWebLib.PW_iPPRemoveCard()
            
            if (ret == E_PWRET.PWRET_OK.value): ret = loopPP()
            MainWindow.Loga('myPGWebLib.PW_iPPRemoveCard')
            return ret
        else:
           break
              
      return ret
  # fim de iExecGetDataInstallJanelas



########################################################


########################
# 
def TesteInstalacao():
   # array de 10 posicoes
   #PW_GetData vstParam[10]

   vstParam_11 = (PW_GetData * 11)
   vstParam = vstParam_11()
   iNumParam = 10
   iRet=0

   Ret = E_PWRET.PWRET_NODATA.value

   # Inicializa a transação de instalação
   iRet = myPGWebLib.PW_iNewTransac(E_PWOPER.PWOPER_INSTALL.value)
   
   if( iRet != 0):
      print("\nErro PW_iNewTransac <%d>", iRet)

   # Adiciona os parâmetros obrigatórios
   #AddMandatoryParams()
   
   i=0
   # Loop até que ocorra algum erro ou a transação seja aprovada, capturando dados
   # do usuário caso seja necessário
   while i < 10:
   
      #Coloca o valor 10 (tamanho da estrutura de entrada) no parâmetro iNumParam
      iNumParam = 10

      # Tenta executar a transação
      if(iRet != E_PWRET.PWRET_NOTHING.value):
         print("\n\nPROCESSANDO...\n")
      iRet = myPGWebLib.PW_iExecTransac(vstParam, iNumParam)
      

      #PrintReturnDescription(iRet, None)
      
      if(iRet == E_PWRET.PWRET_MOREDATA.value):
      
        #print("\nNumero de parametros ausentes = %d", iNumParam)
         
          #Tenta capturar os dados faltantes, caso ocorra algum erro retorna
        ret2 = iExecGetDataInstall(vstParam, iNumParam)  
        if( ret2 != 0):
          return ret2
      else:
        return iRet
      i = i + 1
     
  # fim de TesteInstalacao


def TesteInstalacaoJan():
   # array de 10 posicoes
   #PW_GetData vstParam[10]

   
   import pdvWindowsPayGoLibC_Python_support
   MainWindow  = pdvWindowsPayGoLibC_Python_support.w

   MainWindow.Loga("TesteInstalacaoJan()")
   vstParam_11 = (PW_GetData * 11)
   vstParam = vstParam_11()
   iNumParam = 10
   iRet=0

   Ret = E_PWRET.PWRET_NODATA.value

   # Inicializa a transação de instalação
   iRet = myPGWebLib.PW_iNewTransac(E_PWOPER.PWOPER_INSTALL.value)
   
   if( iRet != 0):
      print("\nErro PW_iNewTransac <%d>", iRet)

   # Adiciona os parâmetros obrigatórios
   #AddMandatoryParams()
   
   i=0
   # Loop até que ocorra algum erro ou a transação seja aprovada, capturando dados
   # do usuário caso seja necessário
   while i < 10:
   
      #Coloca o valor 10 (tamanho da estrutura de entrada) no parâmetro iNumParam
      iNumParam = 10

      # Tenta executar a transação
      if(iRet != E_PWRET.PWRET_NOTHING.value):
         print("\n\nPROCESSANDO...\n")
      iRet = myPGWebLib.PW_iExecTransac(vstParam, iNumParam)
      

      #PrintReturnDescription(iRet, None)
      
      if(iRet == E_PWRET.PWRET_MOREDATA.value):
      
        #print("\nNumero de parametros ausentes = %d", iNumParam)
         
          #Tenta capturar os dados faltantes, caso ocorra algum erro retorna
        ret2 = iExecGetDataInstallJanelas(vstParam, iNumParam)  
        if( ret2 != 0):
          return ret2
      else:
        return iRet
      i = i + 1
     
  # fim de TesteVendaJan



########################
# 
def TesteIsNull():
   # array de 10 posicoes
   #PW_GetData vstParam[10]

   vstParam_11 = (PW_GetData * 11)
   vstParam = vstParam_11()
   iNumParam = 11
   iRet=0

   Ret = E_PWRET.PWRET_NODATA.value

   # Inicializa a transação de instalação
   iRet = myPGWebLib.PW_iNewTransac(E_PWOPER.PWOPER_NULL.value)
   
   if( iRet != 0):
      print("\nErro PW_iNewTransac <%d>", iRet)

   # Adiciona os parâmetros obrigatórios
   #AddMandatoryParams()
   
   i=0
   # Loop até que ocorra algum erro ou a transação seja aprovada, capturando dados
   # do usuário caso seja necessário
   while i < 20:
   
      #Coloca o valor 10 (tamanho da estrutura de entrada) no parâmetro iNumParam
      iNumParam = 10

      # Tenta executar a transação
      if(iRet != E_PWRET.PWRET_NOTHING.value):
         print("\n\nPROCESSANDO...\n")
      iRet = myPGWebLib.PW_iExecTransac(vstParam, iNumParam)
      

      #PrintReturnDescription(iRet, None)
      
      if(iRet == E_PWRET.PWRET_MOREDATA.value):
      
        #print("\nNumero de parametros ausentes = %d", iNumParam)
         
        #Tenta capturar os dados faltantes, caso ocorra algum erro retorna
        ret2 = iExecGetDataInstall(vstParam, iNumParam)  
        if( ret2 != 0):
          return ret2
      else:
        return iRet
      i = i + 1
  # fim de TesteIsNull






def TesteVersion():
   # array de 10 posicoes
   #PW_GetData vstParam[10]

   vstParam_11 = (PW_GetData * 11)
   vstParam = vstParam_11()
   iNumParam = 11
   iRet=0

   Ret = E_PWRET.PWRET_NODATA.value

   # Inicializa a transação de instalação
   iRet = myPGWebLib.PW_iNewTransac(E_PWOPER.PWOPER_VERSION.value)
   
   if( iRet != 0):
      print("\nErro PW_iNewTransac <%d>", iRet)

   # Adiciona os parâmetros obrigatórios
   #AddMandatoryParams()
   
   i=0
   # Loop até que ocorra algum erro ou a transação seja aprovada, capturando dados
   # do usuário caso seja necessário
   while i < 10:
   
      #Coloca o valor 10 (tamanho da estrutura de entrada) no parâmetro iNumParam
      iNumParam = 10

      # Tenta executar a transação
      if(iRet != E_PWRET.PWRET_NOTHING.value):
         print("\n\nPROCESSANDO...\n")
      iRet = myPGWebLib.PW_iExecTransac(vstParam, iNumParam)
      

      #PrintReturnDescription(iRet, None)
      
      if(iRet == E_PWRET.PWRET_MOREDATA.value):
      
        #print("\nNumero de parametros ausentes = %d", iNumParam)
         
        #Tenta capturar os dados faltantes, caso ocorra algum erro retorna
        ret2 = iExecGetDataInstall(vstParam, iNumParam)  
        if( ret2 != 0):
          return ret2
      else:
        return iRet
      i = i + 1
  # fim de TesteVersion


def TesteManutencao():
   # array de 10 posicoes
   #PW_GetData vstParam[10]

   vstParam_11 = (PW_GetData * 11)
   vstParam = vstParam_11()
   iNumParam = 11
   iRet=0

   Ret = E_PWRET.PWRET_NODATA.value

   # Inicializa a transação de instalação
   iRet = myPGWebLib.PW_iNewTransac(E_PWOPER.PWOPER_MAINTENANCE.value)
   
   if( iRet != 0):
      print("\nErro PW_iNewTransac <%d>", iRet)

   # Adiciona os parâmetros obrigatórios
   #AddMandatoryParams()
   
   i=0
   # Loop até que ocorra algum erro ou a transação seja aprovada, capturando dados
   # do usuário caso seja necessário
   while i < 10:
   
      #Coloca o valor 10 (tamanho da estrutura de entrada) no parâmetro iNumParam
      iNumParam = 10

      # Tenta executar a transação
      if(iRet != E_PWRET.PWRET_NOTHING.value):
         print("\n\nPROCESSANDO...\n")
      iRet = myPGWebLib.PW_iExecTransac(vstParam, iNumParam)
      

      #PrintReturnDescription(iRet, None)
      
      if(iRet == E_PWRET.PWRET_MOREDATA.value):
      
        #print("\nNumero de parametros ausentes = %d", iNumParam)
         
        #Tenta capturar os dados faltantes, caso ocorra algum erro retorna
        ret2 = iExecGetDataInstallJanelas(vstParam, iNumParam)  
        if( ret2 != 0):
          return ret2
      else:
        return iRet
      i = i + 1
  # fim de TesteManutencao

def TesteVenda():
   # array de 10 posicoes
   #PW_GetData vstParam[10]

   vstParam_11 = (PW_GetData * 11)
   vstParam = vstParam_11()
   iNumParam = 11
   iRet=0

   Ret = E_PWRET.PWRET_NODATA.value

   # Inicializa a transação de instalação
   iRet = myPGWebLib.PW_iNewTransac(E_PWOPER.PWOPER_SALE.value)
   
   if( iRet != 0):
      print("\nErro PW_iNewTransac <%d>", iRet)

   # Adiciona os parâmetros obrigatórios
   #AddMandatoryParams()
   
   i=0
   # Loop até que ocorra algum erro ou a transação seja aprovada, capturando dados
   # do usuário caso seja necessário
   while i < 10:
   
      #Coloca o valor 10 (tamanho da estrutura de entrada) no parâmetro iNumParam
      iNumParam = 10

      # Tenta executar a transação
      if(iRet != E_PWRET.PWRET_NOTHING.value):
         print("\n\nPROCESSANDO...\n")
      iRet = myPGWebLib.PW_iExecTransac(vstParam, iNumParam)
      

      #PrintReturnDescription(iRet, None)
      
      if(iRet == E_PWRET.PWRET_MOREDATA.value):
      
        #print("\nNumero de parametros ausentes = %d", iNumParam)
         
        #Tenta capturar os dados faltantes, caso ocorra algum erro retorna
        ret2 = iExecGetDataInstallJanelas(vstParam, iNumParam)  
        if( ret2 != 0):
          return ret2
      else:
        return iRet
      i = i + 1
  # fim de TesteVenda


#####
def execTrans(cod_trans):

  listaParametros = getTransactionResult()
  ret = startTransaction(cod_trans, listaParametros)

  if (ret != 0):
  
    sError          = ret
    sResultMessage  = getResultMessage();

    # verifica se deu erro de transacao anterior pendente
    if (ret == E_PWRET.PWRET_FROMHOSTPENDTRN.value):
    
      # confirma a transacao que estava pendente
      print("----------------")
      #print("Erro :" + sError + ": result message :" + sResultMessage + " ao executar a transação: " + operation.ToString());

      transactionStatus = E_PWCNF.PWCNF_REV_AUTO_ABORT.value;
      ret = confirmPendTransaction(transactionStatus, getTransactionResult())

      print("----------------")

      #sTranpend = "Erro :" + sError + "-> Confirmando transacao pendente" ;

      #WriteLog (sTranpend)

      #ShowMessageBoxInfo(this, sTranpend);


      LogaTransactionResult()
      return ret

    # fim do if
    else:
    
      print("----------------")
      #sErrorMessage = "Erro :" + sError + " : result message : " + sResultMessage + " ao executar a transação: " + cod_trans

      #print(sErrorMessage)

      #ShowMessageBoxError(this, sErrorMessage);
      LogaTransactionResult()
      
      return ret;
    #fim do else
  

  print("----------------")
  #OKMessage = "Transacao : " + cod_trans + " OK"
  #print (sOKMessage + "\n")

  #ShowMessageBoxOK(this, sOKMessage);
  #LogaTransactionResult();

  return ret;


####



def startTransaction(operation, paramList):
            
  ret = E_PWRET.PWRET_NODATA.value;
  
  ret = myPGWebLib.PW_iNewTransac(operation);

  
  if (ret != E_PWRET.PWRET_OK.value):
     return ret

  for item in  listaParametros: 
      ret = myPGWebLib.PW_iAddParam(item.parameterCode, item.parameterValue)
      if (ret != 0): return ret
  
  ret = executeTransaction(operation);

  
  return ret;
# fim de StartTransaction




def executeTransaction(code_tran):
   # array de 10 posicoes
   #PW_GetData vstParam[10]

   vstParam_11 = (PW_GetData * 11)
   vstParam = vstParam_11()
   iNumParam = 11
   iRet=0

   import pdvWindowsPayGoLibC_Python_support
   MainWindow  = pdvWindowsPayGoLibC_Python_support.w
   MainWindowRoot = pdvWindowsPayGoLibC_Python_support.root


   Ret = E_PWRET.PWRET_NODATA.value

   # Inicializa a transação de instalação
   #iRet = myPGWebLib.PW_iNewTransac(code_tran)
   
   Nometran = ''
   dicionarioOper = dict()
   for item in E_PWOPER:
       if (item.value == code_tran):
           Nometran = item.name 
       
   mensagem = 'Executando transacao : ' + Nometran
   print(mensagem)
   MainWindow.Loga(mensagem) 
    


   if( iRet != 0):
      print("\nErro PW_iNewTransac <%d>", iRet)

  
   
   i=0
   # Loop até que ocorra algum erro ou a transação seja aprovada, capturando dados
   # do usuário caso seja necessário
   while i < 100:
   
      #Coloca o valor 10 (tamanho da estrutura de entrada) no parâmetro iNumParam
      iNumParam = 10

      # Tenta executar a transação
      if(iRet != E_PWRET.PWRET_NOTHING.value):
         print("\n\nPROCESSANDO...\n")
      iRet = myPGWebLib.PW_iExecTransac(vstParam, iNumParam)
      

      #PrintReturnDescription(iRet, None)
      
      if(iRet == E_PWRET.PWRET_MOREDATA.value):
      
        #print("\nNumero de parametros ausentes = %d", iNumParam)
         
        #Tenta capturar os dados faltantes, caso ocorra algum erro retorna
        ret2 = iExecGetDataInstallJanelas(vstParam, iNumParam)  
        if( ret2 != 0):
          return ret2
      else:
        return iRet
      i = i + 1
  # fim de TesteVenda


def confirmUndoTransactionGen(RetTransaction):

  ret = 0

  import pdvWindowsPayGoLibC_Python_support
  MainWindow  = pdvWindowsPayGoLibC_Python_support.w
  MainWindowRoot = pdvWindowsPayGoLibC_Python_support.root
  
  listTransactionResult = getTransactionResult();
    
  for item in listTransactionResult :

    if((item.parameterCode == E_PWINFO.PWINFO_CNFREQ.value) and (item.parameterValue == '1')):
      
      if (RetTransaction == E_PWRET.PWRET_FROMHOSTPENDTRN.value):        
          transactionStatus = E_PWCNF.PWCNF_REV_AUTO_ABORT.value
          ret = confirmPendTransaction(transactionStatus, listTransactionResult)    
      #fim if
      else:
          dicionarioConf = dict()
          listaConf = []
          for item in E_PWCNF:
              print(item.value," -> ",item.name)
              dicionarioConf[item.name] = item.value
              listaConf.append(item.name)

          cw = DialogConfirmationWindow(MainWindowRoot,listaConf,'Selecione a Opcao de Confirmaçao:')
          transactionStatus = E_PWCNF.PWCNF_REV_AUTO_ABORT.value
          MainWindowRoot.wait_window(cw.top)
          print(cw.valor)
          code_aut = dicionarioConf[cw.valor]

          ret = confirmUndoTransaction(code_aut, listTransactionResult)
      #fim else
  #fim for
  return ret
# fim de confirmUndoTransactionGen



def confirmUndoTransaction(transactionStatus, transactionResponse):

  ret = 99

  pszReqNum = ''
  pszLocRef = ''
  pszExtRef = ''
  pszVirtMerch = ''
  pszAuthSyst = ''




  for item in transactionResponse:

      if(item.parameterCode == E_PWINFO.PWINFO_REQNUM.value):
          pszReqNum = item.parameterValue
      
      elif(item.parameterCode == E_PWINFO.PWINFO_AUTLOCREF.value):
          pszLocRef = item.parameterValue
      
      elif(item.parameterCode == E_PWINFO.PWINFO_AUTEXTREF.value):
          pszExtRef = item.parameterValue
      
      elif(item.parameterCode == E_PWINFO.PWINFO_VIRTMERCH.value):
          pszVirtMerch = item.parameterValue
      
      elif(item.parameterCode == E_PWINFO.PWINFO_AUTHSYST.value):
          pszAuthSyst = item.parameterValue
      
      
  #fim do for

  ret = myPGWebLib.PW_iConfirmation(transactionStatus, pszReqNum, pszLocRef, pszLocRef, pszVirtMerch, pszAuthSyst);
  
  return ret;
#fim de confirmUndoTransaction
         
def confirmPendTransaction(transactionStatus,transactionResponse):

    ret = 99;

    pszReqNum    = ''
    pszLocRef    = ''
    pszExtRef    = ''
    pszVirtMerch = ''
    pszAuthSyst  = ''
    

    for item in transactionResponse:
        if(item.parameterCode == E_PWINFO.PWINFO_PNDREQNUM.value):
            pszReqNum = item.parameterValue
      
        elif(item.parameterCode == E_PWINFO.PWINFO_PNDAUTLOCREF.value):
            pszLocRef = item.parameterValue
      
        elif(item.parameterCode == E_PWINFO.PWINFO_PNDAUTEXTREF.value):
            pszExtRef = item.parameterValue
      
        elif(item.parameterCode == E_PWINFO.PWINFO_PNDVIRTMERCH.value):
            pszVirtMerch = item.parameterValue
      
        elif(item.parameterCode == E_PWINFO.PWINFO_PNDAUTHSYST.value):
            pszAuthSyst = item.parameterValue
      
          
    #fim do for

    
    ret = myPGWebLib.PW_iConfirmation(transactionStatus, pszReqNum, pszLocRef, pszLocRef, pszVirtMerch, pszAuthSyst);
    return ret
#fim de confirmPendTransaction



def CaptureWithPinpad():

  param = "";
  minLength = 0
  maxLength = 0
   
  import pdvWindowsPayGoLibC_Python_support
  MainWindow  = pdvWindowsPayGoLibC_Python_support.w
  MainWindowRoot = pdvWindowsPayGoLibC_Python_support.root
  

  dicionarioCaptura = dict()
  listaCaptura = []
  for item in E_PWUserDataMessages:
      print(item.value," -> ",item.name)
      dicionarioCaptura[item.name] = item.value
      listaCaptura.append(item.name)

  selectUserDataWindow = DialogSelectUserDataWindow(MainWindowRoot,listaCaptura,'Selecione a Opcao de Captura:')
  
  MainWindowRoot.wait_window(selectUserDataWindow.top)
  print(selectUserDataWindow.valor)
  
  code_captura = dicionarioCaptura[selectUserDataWindow.valor]

  minLength = int(selectUserDataWindow.min)
  maxLength = int(selectUserDataWindow.max)   
   
  
  if (minLength > 0):
      userTypedValue = ""

      ret , userTypedValue = getInputFromPP(code_captura, minLength, maxLength)

      if (ret != 0):
         mensagem = "Erro ao executar a captura de dado no PINPad"
         fdm = DialogMessage(MainWindowRoot,mensagem)
         MainWindowRoot.wait_window(fdm.top)
      else:
         mensagem = "Dados Capturados no PinPad : " + userTypedValue
         fdm = DialogMessage(MainWindowRoot,mensagem)
         MainWindowRoot.wait_window(fdm.top)
         MainWindow.Loga('-------------------------------------')
         MainWindow.Loga(mensagem)
  #fim do if

# fim de CaptureWithPinpad




def getInputFromPP(messageToDisplay, minLength, MaxLength, timeout = 30):

  
  value = create_string_buffer(10000)
  ret = 0
  userTypedValue =''

  ret = myPGWebLib.PW_iPPGetUserData(messageToDisplay, minLength, MaxLength, timeout, value);
  #Debug.Print(string.Format("CALLED iPPGetUserData COM RETORNO {0}", ret.ToString()));
  

  userTypedValue = value.value.decode()
  #Debug.Print(string.Format("E VALOR {0}", userTypedValue));

  
  
  return ret, userTypedValue
# fim de getInputFromPP

def getTransactionResult():
    
  ListPW_Parameter = []

  message = ''

  value = create_string_buffer(100000)
  
  print('---------------------------------------------------')
  print('Transaction Result:\n\n')
  
  for  item in E_PWINFO:

    getInfoRet=0
    i = 0

    
    getInfoRet = myPGWebLib.PW_iGetResult( item.value, value, len(value))
    
    if (getInfoRet == 0):
      ListPW_Parameter.append(PW_Parameter(item.name, item.value, value.value.decode()))
      print(item.name, " = " , value.value.decode())
  #fim do for 
  
  return ListPW_Parameter

# fim de getTransactionResult


def LogaTransactionResult():
    

    import pdvWindowsPayGoLibC_Python_support
    MainWindow  = pdvWindowsPayGoLibC_Python_support.w
    MainWindowRoot = pdvWindowsPayGoLibC_Python_support.root


    ListPW_Parameter = []

    message = ''

    szAux = create_string_buffer(100000)
    pszAux = c_char_p(addressof(szAux))
    print('---------------------------------------------------')
    print('Transaction Result:\n\n')
    for  item in E_PWINFO:
        
        iRet=0
        i = 0

        
        iRet = myPGWebLib.PW_iGetResult( item.value, szAux, len(szAux))
        
        #if (getInfoRet == 0) ret.Add(new PW_Parameter(item.ToString(), (ushort)item, value.ToString()));
        if (iRet == 0): 
             mensagem = item.name + " = " +  szAux.value.decode()
             print(mensagem)
             MainWindow.Loga(mensagem)


# fim de  LogaTransactionResult

#retorna o parametro PWINFO_RESULTMSG
def getResultMessage():

   
  value = create_string_buffer(100000)
  
  
  getInfoRet = myPGWebLib.PW_iGetResult( E_PWINFO.PWINFO_RESULTMSG.value, value, len(value))
  
  ret =  value.value.decode();               


  return ret;
#fim de getResultMessage



    





