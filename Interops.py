from  Enums import *
from  CustomObjects import *
import os
from  time import *
#import ctypes.
from ctypes import *

# Classe que carrega a DLL
class PGWebLibrary:
  # Loading the C shared lib I've just compiled
  def __init__(self):
    #busca o diretório onde está o executavel 
    self.me = os.path.abspath(os.path.dirname(__file__))
    
    #cria o diretório PGWebLib
    directory = "PGWebLib"
  
    # Parent Directory path 
    parent_dir = self.me
      
    # Path 
    path = os.path.join(parent_dir, directory) 
      
    # Create the directory 
    # 'GeeksForGeeks' in 
    # '/home / User / Documents' 
    if(os.path.exists(path) != True):
        os.mkdir(path) 

    self.aux_path  = os.path.join(self.me,  "PGWebLib.dll")
    self.path_init = os.path.join(self.me,  "PGWebLib")
    self.PGWebLib_dll = CDLL(self.aux_path)

  def PW_iInit(self):
      self.PW_iInitObj          = self.PGWebLib_dll.PW_iInit
      self.PW_iInitObj.restype  = c_short
      self.PW_iInitObj.argtypes = [c_char_p]
      self.b_path_init = self.path_init.encode('utf-8')
      
      return self.PW_iInitObj(c_char_p(self.b_path_init))

  def PW_iNewTransac(self,bOper):
      self.PW_iNewTransactObj          = self.PGWebLib_dll.PW_iNewTransac
      self.PW_iNewTransactObj.restype  = c_short
      self.PW_iNewTransactObj.argtypes = [c_byte]
      return self.PW_iNewTransactObj(c_byte(bOper))


  def PW_iAddParam(self,wParam,pszValue):
      self.PW_iAddParamObj          = self.PGWebLib_dll.PW_iAddParam
      self.PW_iAddParamObj.restype  = c_short
      self.PW_iAddParamObj.argtypes = [c_int16,c_char_p]
      pszValueAux = pszValue.encode('utf-8')
      return self.PW_iAddParamObj(c_int16(wParam),c_char_p(pszValueAux))


  def PW_iExecTransac(self,vstParam, iNumParam):
        self.PW_iExecTransacObj          = self.PGWebLib_dll.PW_iExecTransac
        self.PW_iExecTransacObj.restype  = c_short

        
        self.PW_iExecTransacObj.argtypes = [POINTER((PW_GetData *11)),POINTER(c_int)]
        
        
        
        ret = self.PW_iExecTransacObj(byref(vstParam),byref(c_int(iNumParam)))
       

        return ret
  

  def PW_iGetResult(self,cod, szAux, szAuxSize):
      self.PW_iGetResultObj          = self.PGWebLib_dll.PW_iGetResult
      self.PW_iGetResultObj.restype  = c_short

      #steste = create_string_buffer(10000)
      self.PW_iGetResultObj.argtypes = [c_int16, c_char_p, c_uint32]


      #ret = self.PW_iGetResultObj(c_int16(cod),steste,sizeof(steste))
      ret = self.PW_iGetResultObj(c_int16(cod),szAux,szAuxSize)
      #saida = steste.value
      #print("stest = ",saida)
      return ret

  def PW_iPPRemoveCard(self):
      self.PW_iPPRemoveCardObj          = self.PGWebLib_dll.PW_iPPRemoveCard
      self.PW_iPPRemoveCardObj.restype  = c_short
      self.PW_iPPRemoveCardObj.argtypes = []

      ret = self.PW_iPPRemoveCardObj()
      return ret
  
  def PW_iPPEventLoop(self, pszDisplay, ulDisplaySize):
      self.PW_iPPEventLoopObj          = self.PGWebLib_dll.PW_iPPEventLoop
      self.PW_iPPEventLoopObj.restype  = c_short
      self.PW_iPPEventLoopObj.argtypes = [c_char_p,c_uint32]

      ret = self.PW_iPPEventLoopObj(pszDisplay,c_uint32(ulDisplaySize))
      return ret

  






# fim de PGWebLibrary: