from  Enums import *
from  CustomObjects import *
import os
from  time import *
#import ctypes.
from ctypes import *

# Classe que carrega a DLL
class PGWebLibrary:
  
  def __init__(self):
    
    #busca o diretório onde está o executavel 
    self.me = os.path.abspath(os.path.dirname(__file__))
    
    #cria o diretório PGWebLib
    directory = "PGWebLib"
  
    # Parent Directory path 
    parent_dir = self.me
      
    # Path 
    path = os.path.join(parent_dir, directory) 
      
    
    if(os.path.exists(path) != True):
        os.mkdir(path) 

    self.aux_path  = os.path.join(self.me,  "PGWebLib.dll")
    self.path_init = os.path.join(self.me,  "PGWebLib")
    self.PGWebLib_dll = CDLL(self.aux_path)
  #fim de __init__

  def PW_iInit(self):
      self.PW_iInitObj          = self.PGWebLib_dll.PW_iInit
      self.PW_iInitObj.restype  = c_short
      self.PW_iInitObj.argtypes = [c_char_p]
      self.b_path_init = self.path_init.encode('utf-8')
      
      return self.PW_iInitObj(c_char_p(self.b_path_init))
  #fim de PW_iInit

  def PW_iNewTransac(self,bOper):
      self.PW_iNewTransactObj          = self.PGWebLib_dll.PW_iNewTransac
      self.PW_iNewTransactObj.restype  = c_short
      self.PW_iNewTransactObj.argtypes = [c_byte]
      return self.PW_iNewTransactObj(c_byte(bOper))
  #fim de PW_iNewTransac

  def PW_iAddParam(self,wParam,pszValue):
      self.PW_iAddParamObj          = self.PGWebLib_dll.PW_iAddParam
      self.PW_iAddParamObj.restype  = c_short
      self.PW_iAddParamObj.argtypes = [c_int16,c_char_p]
      pszValueAux = pszValue.encode('utf-8')
      return self.PW_iAddParamObj(c_int16(wParam),c_char_p(pszValueAux))
  #fim de PW_iAddParam

  def PW_iExecTransac(self,vstParam, iNumParam):
        self.PW_iExecTransacObj          = self.PGWebLib_dll.PW_iExecTransac
        self.PW_iExecTransacObj.restype  = c_short
        self.PW_iExecTransacObj.argtypes = [POINTER((PW_GetData *11)),POINTER(c_int)]
        ret = self.PW_iExecTransacObj(byref(vstParam),byref(c_int(iNumParam)))
        return ret
  #fim de PW_iExecTransac

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
  #fim de PW_iGetResult

  def PW_iPPRemoveCard(self):
      self.PW_iPPRemoveCardObj          = self.PGWebLib_dll.PW_iPPRemoveCard
      self.PW_iPPRemoveCardObj.restype  = c_short
      self.PW_iPPRemoveCardObj.argtypes = []

      ret = self.PW_iPPRemoveCardObj()
      return ret
  #fim de PW_iPPRemoveCard
  
  def PW_iPPEventLoop(self, pszDisplay, ulDisplaySize):
      self.PW_iPPEventLoopObj          = self.PGWebLib_dll.PW_iPPEventLoop
      self.PW_iPPEventLoopObj.restype  = c_short
      self.PW_iPPEventLoopObj.argtypes = [c_char_p,c_uint32]

      ret = self.PW_iPPEventLoopObj(pszDisplay,c_uint32(ulDisplaySize))
      return ret
  #fim de PW_iPPEventLoop

  def PW_iPPGoOnChip(self, uiIndex):
      self.PW_iPPGoOnChipObj          = self.PGWebLib_dll.PW_iPPGoOnChip
      self.PW_iPPGoOnChipObj.restype  = c_short
      self.PW_iPPGoOnChipObj.argtypes = [c_uint16]
      ret = self.PW_iPPGoOnChipObj(c_uint16(uiIndex))
      return ret
  #fim de PW_iPPGoOnChip

  def PW_iPPFinishChip(self, uiIndex):
      self.PW_iPPFinishChipObj          = self.PGWebLib_dll.PW_iPPFinishChip
      self.PW_iPPFinishChipObj.restype  = c_short
      self.PW_iPPFinishChipObj.argtypes = [c_uint16]
      ret = self.PW_iPPFinishChipObj(c_uint16(uiIndex))
      return ret
  #fim de PW_iPPFinishChip

  def PW_iPPConfirmData(self, uiIndex):
      self.PW_iPPConfirmDataObj          = self.PGWebLib_dll.PW_iPPConfirmData
      self.PW_iPPConfirmDataObj.restype  = c_short
      self.PW_iPPConfirmDataObj.argtypes = [c_uint16]
      ret = self.PW_iPPConfirmDataObj(c_uint16(uiIndex))
      return ret
  #fim de PW_iPPConfirmData

  def PW_iPPGetPIN(self, uiIndex):
      self.PW_iPPGetPINObj          = self.PGWebLib_dll.PW_iPPGetPIN
      self.PW_iPPGetPINObj.restype  = c_short
      self.PW_iPPGetPINObj.argtypes = [c_uint16]
      ret = self.PW_iPPGetPINObj(c_uint16(uiIndex))
      return ret
  #fim de PW_iPPGetPIN

  def PW_iPPGetData(self, uiIndex):
      self.PW_iPPGetDataObj          = self.PGWebLib_dll.PW_iPPGetData
      self.PW_iPPGetDataObj.restype  = c_short
      self.PW_iPPGetDataObj.argtypes = [c_uint16]
      ret = self.PW_iPPGetDataObj(c_uint16(uiIndex))
      return ret
  #fim de PW_iPPGetData

  def PW_iPPGetCard(self, uiIndex):
      self.PW_iPPGetCardObj          = self.PGWebLib_dll.PW_iPPGetCard
      self.PW_iPPGetCardObj.restype  = c_short
      self.PW_iPPGetCardObj.argtypes = [c_uint16]
      ret = self.PW_iPPGetCardObj(c_uint16(uiIndex))
      return ret
  #fim de PW_iPPGetCard


  def PW_iConfirmation(self,ulResult,pszReqNum, pszLocRef,pszExtRef,pszVirtMerch,pszAuthSyst):
      self.PW_iConfirmationObj          = self.PGWebLib_dll.PW_iConfirmation
      self.PW_iConfirmationObj.restype  = c_short
      self.PW_iConfirmationObj.argtypes = [c_uint32,c_char_p,c_char_p,c_char_p,c_char_p,c_char_p]

      pszReqNumAux    = pszReqNum.encode('utf-8')
      pszLocRefAux    = pszLocRef.encode('utf-8')
      pszExtRefAux    = pszExtRef.encode('utf-8')
      pszVirtMerchAux = pszVirtMerch.encode('utf-8')
      pszAuthSystAux  = pszAuthSyst.encode('utf-8')
  
      return self.PW_iConfirmationObj(c_uint32(ulResult),c_char_p(pszReqNumAux),c_char_p(pszLocRefAux),c_char_p(pszExtRefAux),
                                  c_char_p(pszVirtMerchAux),c_char_p(pszAuthSystAux))

  #fim de  PW_iConfirmation   
       
  def PW_iPPDisplay(self,pszMsg):
      self.PW_iPPDisplayObj          = self.PGWebLib_dll.PW_iPPDisplay
      self.PW_iPPDisplayObj.restype  = c_short
      self.PW_iPPDisplayObj.argtypes = [c_char_p]
      pszMsgAux = pszMsg.encode('utf-8')
      return self.PW_iPPDisplayObj(c_char_p(pszMsgAux))
  #fim de PW_iPPDisplay

  #PW_iPPGetUserData(short uiMessageId, short bMinLen, short bMaxLen, short iToutSec, 
  # StringBuilder pszData)

  def PW_iPPGetUserData(self,uiMessageId, bMinLen, bMaxLen,  iToutSec, pszData):
      self.PW_iPPGetUserDataObj          = self.PGWebLib_dll.PW_iPPGetUserData
      self.PW_iPPGetUserDataObj.restype  = c_short
      self.PW_iPPGetUserDataObj.argtypes = [c_short, c_short, c_short, c_short, POINTER(c_char)]
      
      ret = self.PW_iPPGetUserDataObj(c_short(uiMessageId), c_short(bMinLen), c_short(bMaxLen), c_short(iToutSec),pszData)
      
      return ret
  #fim de PW_iPPGetUserData




  # fim de PGWebLibrary: