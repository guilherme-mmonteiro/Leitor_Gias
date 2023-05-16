import shutil
import os
import os.path
import fitz
from fitz import Document, Page, Rect
import glob
import pandas as pd

'''Leitor de Gias automatizado para extração de informações'''


"""Como funcionam as coordenadas? 

O Rect pega as cordenadas da pagina pdf no padrão:
    rect = Rect(W, X, Y, Z)
    W = linha de cima do retangulo. A coordenada aqui definida irá mapear a linha superior do retangulo que extrai as informações
    X = linha a esquerda do retangulo. A coordenada aqui definida irá mapear a linha a esquerda do retangulo que extrai as informações
    Y = linha de baixo do retangulo. A coordenada aqui definida irá mapear a linha inferior do retangulo que extrai as informações
    Z = linha a direita do retangulo. A coordenada aqui definida irá mapear a linha a direita do retangulo que extrai as informações"""

arquivos = glob.glob('GIAS/*.pdf') #pega todos os arquivos com extensão pdf dentro da pasta data 

# print(arquivos)
g = 1

VISUALIZE = False
for a in arquivos: #loop para cada arquivo
    input_path = a #arquivo = input_path  
    if a != 'scape.pdf':  
#----------------------------------------------------------------------------------------------------------------------------
        #nome
        doc: Document = fitz.open(input_path) #abre o documento para leitura 
        for i in range(len(doc)): #para cada Pagina documento
            page: Page = doc[i]
            page.clean_contents()
            rect = Rect(110, 179, 195, 195) # coordenadas padrão
            if VISUALIZE:  #se o visualize (linha 20) for = true, gera um documento novo com um quadrado circulando a area que sera extraida nas coordenadas
                page.draw_rect(rect, width=1.5, color=(1, 0, 0)) #cor do quadrado do visualize
            CNPJ = page.get_textbox(rect) # CNPJ = o texto extraído da area do quadrado
            if len(CNPJ) == 0: # se nãop tiver nada para ser extraido
                CNPJ = '.' #CNPJ = .
            # print(CNPJ)
    #----------------------------------------------------------------------------------------------------------------------------
        #contabil
        doc: Document = fitz.open(input_path) #abre o documento para leitura 
        for i in range(len(doc)): #para cada Pagina documento
            page: Page = doc[i]
            page.clean_contents()
            rect = Rect(110, 213, 151, 229) # coordenadas padrão
            if VISUALIZE:  #se o visualize (linha 20) for = true, gera um documento novo com um quadrado circulando a area que sera extraida nas coordenadas
                page.draw_rect(rect, width=1.5, color=(1, 0, 0)) #cor do quadrado do visualize
            data = page.get_textbox(rect) # data = o texto extraído da area do quadrado
            if len(data) == 0: # se nãop tiver nada para ser extraido
                data = '.' #data = .
        #     print(data)
    #----------------------------------------------------------------------------------------------------------------------------
        #base de calculo
        doc: Document = fitz.open(input_path) #abre o documento para leitura 
        for i in range(len(doc)): #para cada Pagina documento
            page: Page = doc[i]
            page.clean_contents()
            rect = Rect(470, 243, 527, 257) # coordenadas padrão
            if VISUALIZE:  #se o visualize (linha 20) for = true, gera um documento novo com um quadrado circulando a area que sera extraida nas coordenadas
                page.draw_rect(rect, width=1.5, color=(1, 0, 0))#cor do quadrado do visualize
            faturamento = page.get_textbox(rect) # faturamento = o texto extraído da area do quadrado
            if len(faturamento) == 0: # se nãop tiver nada para ser extraido
                faturamento = '.' #faturamento = .

            # print(faturamento)
    #----------------------------------------------------------------------------------------------------------------------------
        #debito  
        doc: Document = fitz.open(input_path) #abre o documento para leitura                 
        for i in range(len(doc)): #para cada Pagina documento
            page: Page = doc[i]
            page.clean_contents()
            rect = Rect(470, 282, 526, 296) # coordenadas padrão
            if VISUALIZE: #se o visualize (linha 20) for = true, gera um documento novo com um quadrado circulando a area que sera extraida nas coordenadas
                page.draw_rect(rect, width=1.5, color=(1, 0, 0)) #cor do quadrado do visualize
            debito = page.get_textbox(rect) # Debito = o texto extraído da area do quadrado
            if len(debito) == 0: # se nãop tiver nada para ser extraido
                debito = '.' #Debito = .
            # print(debito)  
    #----------------------------------------------------------------------------------------------------------------------------
            print(f'{data}; {CNPJ}; {faturamento};{debito}') #gera o csv com as informações extraidas 
    #----------------------------------------------------------------------------------------------------------------------------
        if VISUALIZE:#se o visualize (linha 20) for = true
            head, tail = os.path.split(input_path) #pega o nome do arquivo
            viz_name = os.path.join(head, "viz_" + tail) #gera o arquivo novo com "viz_" no final para diferenciar 
            doc.save(viz_name) #salva o documento 
#----------------------------------------------------------------------------------------------------------------------------

# exclui as gias usadas depois que o codigo roda 
dir = 'Gias_usadas/'  
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
# ----------------------------------------------------------------------------------------------------------------------------

#move os arquivos para a pasta gias usadas
for a in arquivos:
    shutil.move(a, 'Gias_usadas/')
#----------------------------------------------------------------------------------------------------------------------------
