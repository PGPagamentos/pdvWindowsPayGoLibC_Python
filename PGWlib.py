from  Enums import *
from  CustomObjects import *
import os
from  time import *
#import ctypes.
from ctypes import *
from Interops import *

myPGWebLib = None



# cria objeto de acesso a DLL
myPGWebLib = PGWebLibrary()





def AddMandatoryParams():
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


def iExecGetDataInstall(vstGetData,iNumParam):
      i = 0
      j = 0 
      iKey = 0 
      iRet = 0
      
      szAux       = (c_char * 1024)()
      szDspMsg    = (c_char * 128)()
      szMsgPinPad = (c_char * 34)()
      
      ulEvent=0

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
              

              
            for j in  range(vstGetData[i].bNumOpcoesMenu-1): 
                print("\n%d - %s", j, vstGetData[i].vszTextoMenu[j])

            
            iKey = input("\n\nSELECIONE A OPCAO:")

            iKey = int(iKey)

            print("\n", iKey)
              

            iRet = myPGWebLib.pPW_iAddParam(vstGetData[i].wIdentificador, vstGetData[i].vszValorMenu[iKey])
            
            if(iRet != 0):
              print("\nERRO AO ADICIONAR PARAMETRO...")

          
        
        
          
        # fim de E_PWDAT.PWDAT_TYPED


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
              
      return E_PWRET.PWRET_OK.value
  # fim de iExecGetDataInstall


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
   AddMandatoryParams()
   
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
   AddMandatoryParams()
   
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
   AddMandatoryParams()
   
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


def getTransactionResult():
    
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
             print(item.name, " = " , szAux.value.decode())



    





