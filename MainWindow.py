from  Enums import *
from  CustomObjects import *
import os
from  time import *
#import ctypes.
from ctypes import *
from Interops import *
from PGWlib import *


#######################################################################
# execução da inicialização e instalação 

#inicializa DLL
ret = myPGWebLib.PW_iInit()
print("ret PW_iInit() =")

print(ret)

TesteInstalacao()
#TesteIsNull()
#TesteVersion()
#PrintResultParams()
getTransactionResult()
