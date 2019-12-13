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

  #======================================================================================================================================= =
  #  PW_iInit : 
  #
  #  Esta função é utilizada para inicializar a biblioteca, e retorna imediatamente.
  #  Deve ser garantido que uma chamada dela retorne PWRET_OK antes de chamar qualquer outra função.
  #
  #     Entradas:
  #     pszWorkingDir Diretório de trabalho (caminho completo, com final nulo) para uso exclusivo do Pay&Go Web
  #     Saídas: Nenhuma.
  #
  #    Retorno: PWRET_OK .................................. Operação bem sucedida.
  #             PWRET_WRITERR ....................... Falha de gravação no diretório informado.
  #             PWRET_INVCALL ......................... Já foi efetuada uma chamada à função PW_iInit após o carregamento da biblioteca.
  #             Outro ..................................Outro erro de execução (ver “10. Códigos de retorno”, página 78 do Manual).
  #                                                     Uma mensagem de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #============================================================================================================================================

  def PW_iInit(self):
      self.PW_iInitObj          = self.PGWebLib_dll.PW_iInit
      self.PW_iInitObj.restype  = c_short
      self.PW_iInitObj.argtypes = [c_char_p]
      self.b_path_init = self.path_init.encode('utf-8')
      
      return self.PW_iInitObj(c_char_p(self.b_path_init))
  #fim de PW_iInit

  
  
  #=============================================================================================================================================
  #  PW_iNewTransac :
  #  
  #   Esta função deve ser chamada para iniciar uma nova transação através do Pay&Go Web, e retorna imediatamente.
  #
  #   Entradas:
  #   iOper Tipo de transação a ser realizada (PWOPER_xxx, conforme tabela).
  #
  #   Saídas: Nenhuma
  #
  #   Retorno:
  #             PWRET_OK .................................. Transação inicializada.
  #             PWRET_DLLNOTINIT ................... Não foi executado PW_iInit.
  #             PWRET_NOTINST ........................ É necessário efetuar uma transação de Instalação.
  #             Outro ................................ Outro erro de execução (ver “10. Códigos de retorno”, página 78 Manual).
  #                                                    Uma mensagem de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #==============================================================================================================================================

  def PW_iNewTransac(self,bOper):
      self.PW_iNewTransactObj          = self.PGWebLib_dll.PW_iNewTransac
      self.PW_iNewTransactObj.restype  = c_short
      self.PW_iNewTransactObj.argtypes = [c_byte]
      return self.PW_iNewTransactObj(c_byte(bOper))
  #fim de PW_iNewTransac




  #=============================================================================================================================================
  # PW_iAddParam:
  #
  #   Esta função é utilizada para alimentar a biblioteca com as informações da transação a ser realizada,
  #   e retorna imediatamente. Estas informações podem ser:
  #   - Pré-fixadas na Automação;
  #   - Capturadas do operador pela Automação antes do acionamento do Pay&Go Web;
  #   - Capturadas do operador após solicitação pelo Pay&Go Web (retorno PW_MOREDATA por PW_iExecTransac).
  #
  #
  #  Entradas:
  #  wParam   : Identificador do parâmetro (PWINFO_xxx, ver lista completa em “9. Dicionário de dados”, página 72).
  #  pszValue : Valor do parâmetro (string ASCII com final nulo).
  #
  #  Saídas: Nenhuma
  #
  #  Retorno:
  #          PWRET_OK .................................. Parametro Acrescentado com sucesso.
  #          PWRET_INVPARAM .................... O valor do parâmetro é inválido
  #          PWRET_DLLNOTINIT ................... Não foi executado PW_iInit
  #          PWRET_TRNNOTINIT .................. Não foi executado PW_iNewTransac (ver página 14).
  #          PWRET_NOTINST ........................ É necessário efetuar uma transação de Instalação
  #          Outro ........................................... Outro erro de execução (ver “10. Códigos de retorno”, página 78). Uma
  #                                                            mensagem de erro pode ser obtida através da função PW_iGetResult
  #                                                            (PWINFO_RESULTMSG).
  #
  #=============================================================================================================================================
  def PW_iAddParam(self,wParam,pszValue):
      self.PW_iAddParamObj          = self.PGWebLib_dll.PW_iAddParam
      self.PW_iAddParamObj.restype  = c_short
      self.PW_iAddParamObj.argtypes = [c_int16,c_char_p]
      pszValueAux = pszValue.encode('utf-8')
      return self.PW_iAddParamObj(c_int16(wParam),c_char_p(pszValueAux))
  #fim de PW_iAddParam



  #=============================================================================================================================================
  #  PW_iExecTransac:
  #
  #  Esta função tenta realizar uma transação através do Pay&Go Web, utilizando os parâmetros
  #  previamente definidos através de PW_iAddParam. Caso algum dado adicional precise ser informado,
  #  o retorno será PWRET_MOREDATA e o parâmetro pvstParam retornará informações dos dados que
  #  ainda devem ser capturados.
  #
  #  Esta função, por se comunicar com a infraestrutura Pay&Go Web, pode demorar alguns segundos
  #  para retornar.
  #
  #
  #  Entradas:
  #    piNumParam : Quantidade máxima de dados que podem ser capturados de uma vez, caso o retorno
  #    seja PW_MOREDATA. (Deve refletir o tamanho da área de memória apontada por
  #    pvstParam.) Valor sugerido: 9.
  #
  #  Saídas:
  #    pvstParam : Lista e características dos dados que precisam ser informados para executar a transação.
  #    Consultar “8.Captura de dados” (página 65) para a descrição da estrutura
  #    e instruções para a captura de dados adicionais. piNumParam Quantidade de dados adicionais que precisam ser capturados
  #    (quantidade de ocorrências preenchidas em pvstParam
  #
  #    Retorno:
  #        PWRET_OK .................................. Transação realizada com sucesso. Os resultados da transação devem ser obtidos através da função PW_iGetResult.
  #        PWRET_NOTHING ....................... Nada a fazer, fazer as validações locais necessárias e chamar a função PW_iExecTransac novamente.
  #        PWRET_MOREDATA ................... Mais dados são requeridos para executar a transação.
  #        PWRET_DLLNOTINIT ................... Não foi executado PW_iInit.
  #        PWRET_TRNNOTINIT .................. Não foi executado PW_iNewTransac (ver página 14).
  #        PWRET_NOTINST ........................ É necessário efetuar uma transação de Instalação.
  #        PWRET_NOMANDATORY ........... Algum dos parâmetros obrigatórios não foi adicionado (ver página 17).
  #        Outro ........................................... Outro erro de execução (ver “10. Códigos de retorno”, página 78 Manual).
  #                                                          Uma mensagem de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=============================================================================================================================================
  def PW_iExecTransac(self,vstParam, iNumParam):
        self.PW_iExecTransacObj          = self.PGWebLib_dll.PW_iExecTransac
        self.PW_iExecTransacObj.restype  = c_short
        self.PW_iExecTransacObj.argtypes = [POINTER((PW_GetData *11)),POINTER(c_int)]
        ret = self.PW_iExecTransacObj(byref(vstParam),byref(c_int(iNumParam)))
        return ret
  #fim de PW_iExecTransac

  #=========================================================================================================
  #  Funcao     :  PW_iGetResult
  #
  #   Descricao  :  Esta função pode ser chamada para obter informações que resultaram da transação efetuada,
  #                 independentemente de ter sido bem ou mal sucedida, e retorna imediatamente.
  #
  #   Entradas   :  iInfo:	   Código da informação solicitada sendo requisitada (PWINFO_xxx, ver lista completa
  #                             em “9. Dicionário de dados”, página 36).
  #                 ulDataSize:	Tamanho (em bytes) da área de memória apontada por pszData. Prever um tamanho maior
  #                             que o máximo previsto para o dado solicitado.
  #
  #
  #   Saidas     :  pszData:	   Valor da informação solicitada (string ASCII com terminador nulo).
  #
  #   Retorno    :  PWRET_OK	         Sucesso. pszData contém o valor solicitado.
  #                 PWRET_NODATA	   A informação solicitada não está disponível.
  #                 PWRET_BUFOVFLW 	O valor da informação solicitada não cabe em pszData.
  #                 PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #                 PWRET_TRNNOTINIT	Não foi executado PW_iNewTransac (ver página 10).
  #                 PWRET_NOTINST	   É necessário efetuar uma transação de Instalação.
  #                 Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                               de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #                               
  #
  #=========================================================================================================*/
  def PW_iGetResult(self,cod, szAux, szAuxSize):
      self.PW_iGetResultObj          = self.PGWebLib_dll.PW_iGetResult
      self.PW_iGetResultObj.restype  = c_short
      self.PW_iGetResultObj.argtypes = [c_int16, c_char_p, c_uint32]
      ret = self.PW_iGetResultObj(c_int16(cod),szAux,szAuxSize)
      return ret
  #fim de PW_iGetResult

  
  #=========================================================================================================
  # Funcao     :  PW_iPPRemoveCard
  #
  #  Descricao  :  Esta função é utilizada para fazer uma remoção de cartão do PIN-pad.
  #
  #  Entradas   :  não há.
  #
  #  Saidas     :  não há.
  #
  #  Retorno    :  PWRET_OK	         Captura iniciada com sucesso, chamar PW_iPPEventLoop para obter o resultado.
  #                PWRET_INVPARAM	   O valor de uiIndex informado não corresponde a uma captura de dados deste tipo.
  #                PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #                Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                     de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================
  def PW_iPPRemoveCard(self):
      self.PW_iPPRemoveCardObj          = self.PGWebLib_dll.PW_iPPRemoveCard
      self.PW_iPPRemoveCardObj.restype  = c_short
      self.PW_iPPRemoveCardObj.argtypes = []

      ret = self.PW_iPPRemoveCardObj()
      return ret
  #fim de PW_iPPRemoveCard
  
  #=========================================================================================================
  # Funcao     :  PW_iPPEventLoop
  #
  #  Descricao  :  Esta função deverá ser chamada em “loop” até que seja retornado PWRET_OK (ou um erro fatal). Nesse
  #               “loop”, caso o retorno seja PWRET_DISPLAY o ponto de captura deverá atualizar o “display” com as
  #               mensagens recebidas da biblioteca.
  #
  #  Entradas   :  ulDisplaySize	Tamanho (em bytes) da área de memória apontada por pszDisplay.
  #                              Tamanho mínimo recomendado: 100 bytes.
  #
  #  Saidas     :  pszDisplay	   Caso o retorno da função seja PWRET_DISPLAY, contém uma mensagem de texto
  #                              (string ASCII com terminal nulo) a ser apresentada pela Automação na interface com
  #                              o usuário principal. Para o formato desta mensagem, consultar “4.3.Interface com o
  #                              usuário”, página 8.
  #
  #  Retorno    :  PWRET_NOTHING	   Nada a fazer, continuar aguardando o processamento do PIN-pad.
  #               PWRET_DISPLAY	   Apresentar a mensagem recebida em pszDisplay e continuar aguardando o processamento do PIN-pad.
  #               PWRET_OK	         Captura de dados realizada com êxito, prosseguir com a transação.
  #               PWRET_CANCEL	   A operação foi cancelada pelo Cliente no PIN-pad (tecla [CANCEL]).
  #               PWRET_TIMEOUT	   O Cliente não realizou a captura no tempo limite.
  #               PWRET_FALLBACK	   Ocorreu um erro na leitura do cartão, passar a aceitar a digitação do número do cartão, 
  #                                 caso já não esteja aceitando.
  #               PWRET_PPCOMERR	   Falha na comunicação com o PIN-pad.
  #               PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #               PWRET_INVCALL	   Não há captura de dados no PIN-pad em curso.
  #               Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                                 de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================        
  def PW_iPPEventLoop(self, pszDisplay, ulDisplaySize):
      self.PW_iPPEventLoopObj          = self.PGWebLib_dll.PW_iPPEventLoop
      self.PW_iPPEventLoopObj.restype  = c_short
      self.PW_iPPEventLoopObj.argtypes = [POINTER(c_char),c_uint32]

      ret = self.PW_iPPEventLoopObj(pszDisplay,c_uint32(ulDisplaySize))
      return ret
  #fim de PW_iPPEventLoop


  #=========================================================================================================
  # Funcao     :  PW_iPPGoOnChip
  #
  #  Descricao  :  Esta função é utilizada para realizar o processamento off-line (antes da comunicação com o Provedor)
  #               de um cartão com chip no PIN-pad.
  #
  #  Entradas   :  uiIndex	Índice (iniciado em 0) do dado solicitado na última execução de PW_iExecTransac
  #                        (índice do dado no vetor pvstParam).
  #
  #  Saidas     :  não há.
  #
  #  Retorno    :  PWRET_OK	         Captura iniciada com sucesso, chamar PW_iPPEventLoop para obter o resultado.
  #               PWRET_INVPARAM	   O valor de uiIndex informado não corresponde a uma captura de dados deste tipo.
  #               PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #               Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                                 de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================        
  def PW_iPPGoOnChip(self, uiIndex):
      self.PW_iPPGoOnChipObj          = self.PGWebLib_dll.PW_iPPGoOnChip
      self.PW_iPPGoOnChipObj.restype  = c_short
      self.PW_iPPGoOnChipObj.argtypes = [c_uint16]
      ret = self.PW_iPPGoOnChipObj(c_uint16(uiIndex))
      return ret
  #fim de PW_iPPGoOnChip


  #=========================================================================================================
  # Funcao     :  PW_iPPFinishChip
  #
  #  Descricao  :  Esta função é utilizada para finalizar o processamento on-line (após comunicação com o Provedor)
  #               de um cartão com chip no PIN-pad.
  #
  #  Entradas   :  uiIndex	Índice (iniciado em 0) do dado solicitado na última execução de PW_iExecTransac
  #                        (índice do dado no vetor pvstParam).
  #
  #  Saidas     :  não há.
  #
  #  Retorno    :  PWRET_OK	         Captura iniciada com sucesso, chamar PW_iPPEventLoop para obter o resultado.
  #               PWRET_INVPARAM	   O valor de uiIndex informado não corresponde a uma captura de dados deste tipo.
  #               PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #               Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                                 de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================
  def PW_iPPFinishChip(self, uiIndex):
      self.PW_iPPFinishChipObj          = self.PGWebLib_dll.PW_iPPFinishChip
      self.PW_iPPFinishChipObj.restype  = c_short
      self.PW_iPPFinishChipObj.argtypes = [c_uint16]
      ret = self.PW_iPPFinishChipObj(c_uint16(uiIndex))
      return ret
  #fim de PW_iPPFinishChip

  #=========================================================================================================
  # Funcao     :  PW_iPPConfirmData
  #
  #  Descricao  :  Esta função é utilizada para obter do Cliente a confirmação de uma informação no PIN-pad.
  #
  #  Entradas   :  uiIndex	Índice (iniciado em 0) do dado solicitado na última execução de PW_iExecTransac
  #                        (índice do dado no vetor pvstParam).
  #
  #  Saidas     :  não há.
  #
  #  Retorno    :  PWRET_OK	         Captura iniciada com sucesso, chamar PW_iPPEventLoop para obter o resultado.
  #               PWRET_INVPARAM	   O valor de uiIndex informado não corresponde a uma captura de dados deste tipo.
  #               PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #               Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                                 de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================
  def PW_iPPConfirmData(self, uiIndex):
      self.PW_iPPConfirmDataObj          = self.PGWebLib_dll.PW_iPPConfirmData
      self.PW_iPPConfirmDataObj.restype  = c_short
      self.PW_iPPConfirmDataObj.argtypes = [c_uint16]
      ret = self.PW_iPPConfirmDataObj(c_uint16(uiIndex))
      return ret
  #fim de PW_iPPConfirmData

  
  #=========================================================================================================
  # Funcao     :  PW_iPPGetPIN
  #
  #  Descricao  :  Esta função é utilizada para realizar a captura no PIN-pad da senha (ou outro dado criptografado)
  #               do Cliente.
  #
  #  Entradas   :  uiIndex	Índice (iniciado em 0) do dado solicitado na última execução de PW_iExecTransac
  #                        (índice do dado no vetor pvstParam).
  #
  #  Saidas     :  não há.
  #
  #  Retorno    :  PWRET_OK	         Captura iniciada com sucesso, chamar PW_iPPEventLoop para obter o resultado.
  #               PWRET_INVPARAM	   O valor de uiIndex informado não corresponde a uma captura de dados deste tipo.
  #               PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #               Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                                 de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================
  def PW_iPPGetPIN(self, uiIndex):
      self.PW_iPPGetPINObj          = self.PGWebLib_dll.PW_iPPGetPIN
      self.PW_iPPGetPINObj.restype  = c_short
      self.PW_iPPGetPINObj.argtypes = [c_uint16]
      ret = self.PW_iPPGetPINObj(c_uint16(uiIndex))
      return ret
  #fim de PW_iPPGetPIN

  
  #=========================================================================================================
  # Funcao     :  PW_iPPGetData
  #
  #  Descricao  :  Esta função é utilizada para fazer a captura no PIN-pad de um dado não sensível do Cliente..
  #
  #  Entradas   :  uiIndex	Índice (iniciado em 0) do dado solicitado na última execução de PW_iExecTransac
  #                    (índice do dado no vetor pvstParam).
  #
  #  Saidas     :  nao ha.
  #
  #  Retorno    :  PWRET_OK	         Captura iniciada com sucesso, chamar PW_iPPEventLoop para obter o resultado.
  #           PWRET_INVPARAM	   O valor de uiIndex informado não corresponde a uma captura de dados deste tipo.
  #           PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #           Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                             de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================
  def PW_iPPGetData(self, uiIndex):
      self.PW_iPPGetDataObj          = self.PGWebLib_dll.PW_iPPGetData
      self.PW_iPPGetDataObj.restype  = c_short
      self.PW_iPPGetDataObj.argtypes = [c_uint16]
      ret = self.PW_iPPGetDataObj(c_uint16(uiIndex))
      return ret
  #fim de PW_iPPGetData

  #=========================================================================================================
  # Funcao     :  PW_iPPGetCard
  #
  #  Descricao  :  Esta função é utilizada para realizar a leitura de um cartão (magnético, com chip com contato,
  #           ou sem contato) no PIN-pad.
  #
  #  Entradas   :  uiIndex	Índice (iniciado em 0) do dado solicitado na última execução de PW_iExecTransac
  #                    (índice do dado no vetor pvstParam).
  #
  #  Saidas     :  não há.
  #
  #  Retorno    :  PWRET_OK	         Captura iniciada com sucesso, chamar PW_iPPEventLoop para obter o resultado.
  #           PWRET_INVPARAM	   O valor de uiIndex informado não corresponde a uma captura de dados deste tipo.
  #           PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #           Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                             de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================
  def PW_iPPGetCard(self, uiIndex):
      self.PW_iPPGetCardObj          = self.PGWebLib_dll.PW_iPPGetCard
      self.PW_iPPGetCardObj.restype  = c_short
      self.PW_iPPGetCardObj.argtypes = [c_uint16]
      ret = self.PW_iPPGetCardObj(c_uint16(uiIndex))
      return ret
  #fim de PW_iPPGetCard

  #=========================================================================================================
  #
  #Funcao     :  PW_iConfirmation
  #
  #Descricao  :  Esta função informa ao Pay&Go Web o status final da transação em curso (confirmada ou desfeita).
  #              Consultar “7. Confirmação de transação” (página 28) para informações adicionais.
  #
  #Entradas   :  ulStatus:   	Resultado da transação (PWCNF_xxx, ver lista abaixo).
  #              pszReqNum:  	Referência local da transação, obtida através de PW_iGetResult (PWINFO_REQNUM).
  #              pszLocRef:  	Referência da transação para a infraestrutura Pay&Go Web, obtida através de PW_iGetResult (PWINFO_AUTLOCREF).
  #              pszExtRef:  	Referência da transação para o Provedor, obtida através de PW_iGetResult (PWINFO_AUTEXTREF).
  #              pszVirtMerch:	Identificador do Estabelecimento, obtido através de PW_iGetResult (PWINFO_VIRTMERCH).
  #              pszAuthSyst:   Nome do Provedor, obtido através de PW_iGetResult (PWINFO_AUTHSYST).
  #
  #Saidas     :  não há.
  #
  #Retorno    :  PWRET_OK	         O status da transação foi atualizado com sucesso.
  #              PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #              PWRET_NOTINST	   É necessário efetuar uma transação de Instalação.
  #              Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                                de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================
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
       
  #=========================================================================================================
  # Funcao     :  PW_iPPDisplay
  #
  #  Descricao  :  Esta função é utilizada para apresentar uma mensagem no PIN-pad
  #
  #  Entradas   :  pszMsg   Mensagem a ser apresentada no PIN-pad. O caractere ‘\r’ (0Dh) indica uma quebra de linha.
  #
  #  Saidas     :  não há.
  #
  #  Retorno    :  PWRET_OK	         Captura iniciada com sucesso, chamar PW_iPPEventLoop para obter o resultado.
  #                PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #                Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                                 de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================
  def PW_iPPDisplay(self,pszMsg):
      self.PW_iPPDisplayObj          = self.PGWebLib_dll.PW_iPPDisplay
      self.PW_iPPDisplayObj.restype  = c_short
      self.PW_iPPDisplayObj.argtypes = [c_char_p]
      pszMsgAux = pszMsg.encode('utf-8')
      return self.PW_iPPDisplayObj(c_char_p(pszMsgAux))
  #fim de PW_iPPDisplay


  #=========================================================================================================
  # Funcao     :  PW_iGetUserData
  #
  #    Descricao  :  Esta função é utilizada para obter um dado digitado pelo portador do cartão no PIN-pad.
  #
  #    Entradas   :  uiMessageId : Identificador da mensagem a ser exibida como prompt para a captura.
  #                  bMinLen     : Tamanho mínimo do dado a ser digitado.
  #                  bMaxLen     : Tamanho máximo do dado a ser digitado.
  #                  iToutSec    : Tempo limite para a digitação do dado em segundos.
  #
  #    Saídas     :  pszData     : Dado digitado pelo portador do cartão no PIN-pad.
  #
  #    Retorno    :  PWRET_OK	         Operação realizada com êxito.
  #                   PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #                   PWRET_NOTINST	   É necessário efetuar uma transação de Instalação.
  #                   PWRET_CANCEL	   A operação foi cancelada pelo Cliente no PIN-pad (tecla [CANCEL]).
  #                   PWRET_TIMEOUT	   O Cliente não realizou a captura no tempo limite.
  #                   PWRET_PPCOMERR	   Falha na comunicação com o PIN-pad.
  #                   PWRET_INVCALL	   Não é possível capturar dados em um PIN-pad não ABECS.
  #                   Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                                 de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================
  def PW_iPPGetUserData(self,uiMessageId, bMinLen, bMaxLen,  iToutSec, pszData):
      self.PW_iPPGetUserDataObj          = self.PGWebLib_dll.PW_iPPGetUserData
      self.PW_iPPGetUserDataObj.restype  = c_short
      self.PW_iPPGetUserDataObj.argtypes = [c_short, c_short, c_short, c_short, POINTER(c_char)]
      
      ret = self.PW_iPPGetUserDataObj(c_short(uiMessageId), c_short(bMinLen), c_short(bMaxLen), c_short(iToutSec),pszData)
      
      return ret
  #fim de PW_iPPGetUserData


  #=======================================================================================================
  # Funcao     :  PW_iPPAbort
  #
  #  Descricao  :  Esta função pode ser utilizada pela Automação para interromper uma captura de dados no PIN-pad
  #               em curso, e retorna imediatamente.
  #
  #  Entradas   :  não há.
  #
  #  Saidas     :  não há.
  #
  #  Retorno    :  PWRET_OK	         Operação interrompida com sucesso.
  #               PWRET_PPCOMERR	   Falha na comunicação com o PIN-pad.
  #               PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #               Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                                 de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================
  def PW_iPPAbort(self):
      self.PW_iPPAbortObj          = self.PGWebLib_dll.PW_iPPAbort
      self.PW_iPPAbortObj.restype  = c_short
      self.PW_iPPAbortObj.argtypes = []

      ret = self.PW_iPPAbortObj()
      return ret
  #fim de PW_iPPAbort


  #=========================================================================================================
  #   Funcao     :  PW_iIdleProc
  #
  #  Descricao  :  Para o correto funcionamento do sistema, a biblioteca do Pay&Go Web precisa de tempos em tempos
  #                executar tarefas automáticas enquanto não está realizando nenhuma transação a pedido da Automação.
  #
  #  Entradas   :  não há.
  #
  #  Saidas     :  não há.
  #
  #  Retorno    :  PWRET_OK	         Operação realizada com êxito.
  #                PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #                PWRET_NOTINST	   É necessário efetuar uma transação de Instalação.
  #                Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                                  de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================
  def PW_iIdleProc(self):
      self.PW_iIdleProcObj          = self.PGWebLib_dll.PW_iIdleProc
      self.PW_iIdleProcObj.restype  = c_short
      self.PW_iIdleProcObj.argtypes = []

      ret = self.PW_iIdleProcObj()
      return ret
  #fim de PW_iIdleProc


  #===========================================================================
  # Funcao   : PW_iPPGenericCMD
  #
  #  Descricao  :  Realiza comando genérico de PIN-pad.
  #
  #  Entradas   :  uiIndex	Índice (iniciado em 0) do dado solicitado na última execução de PW_iExecTransac
  #                        (índice do dado no vetor pvstParam).
  #
  #  Saidas     :  Não há.
  #
  #  Retorno    :  PWRET_xxx.
  #
  #===========================================================================
  def PW_iPPGenericCMD(self, uiIndex):
      self.PW_iPPGenericCMDObj          = self.PGWebLib_dll.PW_iPPGenericCMD
      self.PW_iPPGenericCMDObj.restype  = c_short
      self.PW_iPPGenericCMDObj.argtypes = [c_uint16]
      ret = self.PW_iPPGenericCMDObj(c_uint16(uiIndex))
      return ret
  #fim de PW_iPPGenericCMD



  #===========================================================================
  # Funcao     : PW_iPPPositiveConfirmation
  #
  #   Descricao  :  Realiza a confirmação positiva de um dado, ou um bloco de dados,
  #                  no PIN-pad
  #   
  #   Entradas   :  uiIndex	Índice (iniciado em 0) do dado solicitado na última execução de PW_iExecTransac 
  #                          (índice do dado no vetor pvstParam).
  #
  #   Saidas     :  Não há.
  #
  #   Retorno    :  PWRET_xxx.
  #
  #===========================================================================
  def PW_iPPPositiveConfirmation(self, uiIndex):
      self.PW_iPPPositiveConfirmationObj          = self.PGWebLib_dll.PW_iPPPositiveConfirmation
      self.PW_iPPPositiveConfirmationObj.restype  = c_short
      self.PW_iPPPositiveConfirmationObj.argtypes = [c_uint16]
      ret = self.PW_iPPPositiveConfirmationObj(c_uint16(uiIndex))
      return ret
  #fim de PW_iPPPositiveConfirmation  


  #===========================================================================
  # Funcao     : PW_iTransactionInquiry
  #
  # Descricao  :  Esta função é utilizada para realizar uma consulta de transações
  #               efetuadas por um ponto de captura junto ao Pay&Go WEB.
  #
  # Entradas   :  pszXmlRequest	Arquivo de entrada no formato XML, contendo as informações
  #                              necessárias para fazer a consulta pretendida.
  #               ulXmlResponseLen Tamanho da string pszXmlResponse.
  #
  # Saidas     :  pszXmlResponse	Arquivo de saída no formato XML, contendo o resultado da consulta
  #                              efetuada, o arquivo de saída tem todos os elementos do arquivo de entrada.
  #
  # Retorno    :  PWRET_xxx. 
  # @@@@
  #
  #===========================================================================
  def PW_iTransactionInquiry(self, pszXmlRequest, pszXmlResponse, ulXmlResponseLen):
      self.PW_iTransactionInquiryObj          = self.PGWebLib_dll.PW_iTransactionInquiry
      self.PW_iTransactionInquiryObj.restype  = c_short
      self.PW_iTransactionInquiryObj.argtypes = [c_byte,c_byte,c_byte]
      ret = self.PW_iTransactionInquiryObj(c_byte(pszXmlRequest), c_byte(pszXmlResponse), c_byte(ulXmlResponseLen))
      return ret
  #fim de PW_iTransactionInquiry  


  #=========================================================================================================
  # Funcao     :  PW_iPPWaitEvent
  #
  #  Descricao  :  Esta função é utilizada para aguardar a ocorrência de um evento no PIN-pad.
  #
  #  Entradas   :  não há.
  #
  #  Saidas     :  pulEvent	         Evento ocorrido.
  #
  #  Retorno    :  PWRET_OK	         Captura iniciada com sucesso, chamar PW_iPPEventLoop para obter o resultado.
  #               PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #               Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                                 de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================
  def PW_iPPWaitEvent(self,vstParam, iNumParam):
        self.PW_iPPWaitEventObj          = self.PGWebLib_dll.PW_iPPWaitEvent
        self.PW_iPPWaitEventObj.restype  = c_short
        self.PW_iPPWaitEventObj.argtypes = [POINTER(c_int)]
        ret = self.PW_iPPWaitEventObj(byref(c_int(iNumParam)))
        return ret
  #fim de PW_iPPWaitEvent


  #=========================================================================================================
  #
  # Funcao     :  PW_iGetOperations
  #
  # Descricao  :  Esta função pode ser chamada para obter quais operações o Pay&Go WEB disponibiliza no momento,
  #              sejam elas administrativas, de venda ou ambas.
  #
  # Entradas   :              bOperType	      Soma dos tipos de operação a serem incluídos na estrutura de
  #                                            retorno (PWOPTYPE_xxx).
  #                          piNumOperations	Número máximo de operações que pode ser retornado. (Deve refletir
  #                                            o tamanho da área de memória apontada por pvstOperations).
  #
  # Saídas     :              piNumOperations	Número de operações disponíveis no Pay&Go WEB.
  #                          vstOperations	   Lista das operações disponíveis e suas características.
  #
  #
  # Retorno    :  PWRET_OK	         Operação realizada com êxito.
  #              PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #              PWRET_NOTINST	   É necessário efetuar uma transação de Instalação.
  #              Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40). Uma mensagem
  #                                de erro pode ser obtida através da função PW_iGetResult (PWINFO_RESULTMSG).
  #
  #=========================================================================================================
  def PW_iGetOperations(self,vstParam, piNumOperations):
        self.PW_iGetOperationsObj          = self.PGWebLib_dll.PW_iGetOperations
        self.PW_iGetOperationsObj.restype  = c_short
        self.PW_iGetOperationsObj.argtypes = [POINTER((PW_Operations *11)),POINTER(c_short)]
        ret = self.PW_iGetOperationscObj(byref(vstParam),byref(c_short(piNumOperations)))
        return ret
  #fim de PW_iGetOperations 


  #=========================================================================================================
  # Funcao     :  PW_iPPGetPINBlock
  #
  #  Descricao  :  Esta função é utilizada para obter o PIN block gerado a partir de um dado digitado pelo usuário no PIN-pad.
  #
  #  Entradas   :  bKeyID	      : Índice da Master Key (para chave PayGo, utilizar o índice “12”).
  #               pszWorkingKey	: Sequência 32 caracteres utilizados para a geração do PIN block (dois valores iguais digitados pelo usuário com duas pszWorkingKey diferentes irão gerar dois PIN block diferentes.
  #               bMinLen	      : Tamanho mínimo do dado a ser digitado (a partir de 4).
  #               bMaxLen     	: Tamanho máximo do dado a ser digitado.
  #               iToutSec    	: Tempo limite para a digitação do dado em segundos.
  #               pszPrompt	   : Mensagem de 32 caracteres (2 linhas com 16 colunas) para apresentação no momento do pedido do dado do usuário.
  #
  #
  #  Saídas     :  pszData        : PIN block gerado com base nos dados fornecidos na função combinados com o dado digitado pelo usuário no PIN-pad.
  #
  #  Retorno    :  PWRET_OK	         Operação realizada com êxito.
  #               PWRET_DLLNOTINIT	Não foi executado PW_iInit.
  #               PWRET_NOTINST	   É necessário efetuar uma transação de Instalação.
  #               PWRET_CANCEL	   A operação foi cancelada pelo Cliente no PIN-pad (tecla [CANCEL]).
  #               PWRET_TIMEOUT	   O Cliente não realizou a captura no tempo limite.
  #               PWRET_PPCOMERR	   Falha na comunicação com o PIN-pad.
  #               Outro	            Outro erro de execução (ver “10. Códigos de retorno”, página 40).
  #
  #@@@
  #
  #=========================================================================================================
  def PW_iPPGetPINBlock(self,bKeyID , pszWorkingKey,  bMaxLen, iToutSec, pszPrompt, pszData):
      self.PW_iPPGetPINBlockObj          = self.PGWebLib_dll.PW_iPPGetPINBlock
      self.PW_iPPGetPINBlockObj.restype  = c_short
      self.PW_iPPGetPINBlockObj.argtypes = [c_short,c_char_p,c_short,c_short,c_char_p,POINTER(c_char)]
      pszWorkingKeyAux = pszWorkingKey.encode('utf-8')
      pszPromptAux = pszPrompt.encode('utf-8')
      return self.PW_iPPGetPINBlockObj(c_short(bKeyID) , c_char_p(pszWorkingKey),  c_short(bMaxLen), c_short(iToutSec), c_char_p(pszPrompt), pszData)
  #fim de PW_iPPGetPINBlock




# fim de PGWebLibrary: