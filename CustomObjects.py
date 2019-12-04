import os
#import ctypes
from ctypes import *


PWMENU_MAXINTENS = 40




class PW_Parameter:
    
    def __init__(self, Name, Code, Value):
        self.parameterName = Name
        self.parameterCode = Code
        self.parameterValue = Value
    


class PW_Operations(Structure):
    _fields_=[("bOperType",c_ubyte),
              ("szText"   ,c_char *21),
              ("szValue"  ,c_char *21)]
            
class PW_GetData(Structure):
   _fields_=[   
               ("wIdentificador",c_ushort),
               ("bTipoDeDado",c_ubyte),
               ("szPrompt",c_char * 84),
               ("bNumOpcoesMenu",c_ubyte),     
               ("vszTextoMenu",(c_char * 41) * PWMENU_MAXINTENS),
               ("vszValorMenu",(c_char * 256) * PWMENU_MAXINTENS),
               ("szMascaraDeCaptura",c_char * 41),
               ("bTiposEntradaPermitidos",c_ubyte),
               ("bTamanhoMinimo",c_ubyte),
               ("bTamanhoMaximo",c_ubyte),
               ("ulValorMinimo",c_ulong),
               ("ulValorMaximo",c_ulong),
               ("bOcultarDadosDigitados",c_ubyte),
               ("bValidacaoDado",c_ubyte),
               ("bAceitaNulo",c_ubyte),
               ("szValorInicial",c_char * 41),
               ("bTeclasDeAtalho",c_ubyte),
               ("szMsgValidacao",c_char   * 84),
               ("szMsgConfirmacao",c_char * 84),
               ("szMsgDadoMaior",c_char   * 84),    
               ("szMsgDadoMenor",c_char   * 84),
               ("bCapturarDataVencCartao",c_ubyte),
               ("ulTipoEntradaCartao",c_ulong),
               ("bItemInicial",c_ubyte),
               ("bNumeroCapturas",c_ubyte),
               ("szMsgPrevia",c_char * 84),
               ("bTipoEntradaCodigoBarras",c_ubyte),
               ("bOmiteMsgAlerta",c_ubyte),
               ("bIniciaPelaEsquerda",c_ubyte),
               ("bNotificarCancelamento",c_ubyte),
               ("bAlinhaPelaDireita",c_ubyte)
            ]



##############################
