import shutil
import os
import os.path
import fitz
from fitz import Document, Page, Rect
import glob
from pdfminer.high_level import extract_pages, extract_text
import pandas as pd

'''Leitor de Gias automatizado para extração de informações'''


"""Como funcionam as coordenadas? 

O Rect pega as cordenadas da pagina pdf no padrão:
    rect = Rect(W, X, Y, Z)
    W = linha de cima do retangulo. A coordenada aqui definida irá mapear a linha superior do retangulo que extrai as informações
    X = linha a esquerda do retangulo. A coordenada aqui definida irá mapear a linha a esquerda do retangulo que extrai as informações
    Y = linha de baixo do retangulo. A coordenada aqui definida irá mapear a linha inferior do retangulo que extrai as informações
    Z = linha a direita do retangulo. A coordenada aqui definida irá mapear a linha a direita do retangulo que extrai as informações"""

open = ('{')
close = ('}')
# arquivos = glob.glob('*.pdf') #pega todos os arquivos com extensão pdf dentro da pasta data 
arquivos = glob.glob('data/*.pdf') #pega todos os arquivos com extensão pdf dentro da pasta data 

# print(arquivos)
g = 1

VISUALIZE = False
for a in arquivos: #loop para cada arquivo
    input_path = a #arquivo = input_path
#----------------------------------------------------------------------------------------------------------------------------
    #data
    doc: Document = fitz.open(input_path) #abre o documento para leitura 
    for i in range(len(doc)): #para cada Pagina documento
        page: Page = doc[i] 
        page.clean_contents()
        rect = Rect(353, 117, 565, 130) # coordenadas padrão
        if VISUALIZE: #se o visualize (linha 20) for = true, gera um documento novo com um quadrado circulando a area que sera extraida nas coordenadas
            page.draw_rect(rect, color=(1, 0, 0)) #cor do quadrado do visualize
        data = page.get_textbox(rect) # data = o texto extraído da area do quadrado
        if len(data) == 0: # se nãop tiver nada para ser extraido 
            data = '.' # data = .
        # print((data).encode())
     
#----------------------------------------------------------------------------------------------------------------------------
    #nome
    doc: Document = fitz.open(input_path) #abre o documento para leitura 
    for i in range(len(doc)): #para cada Pagina documento
        page: Page = doc[i]
        page.clean_contents()
        rect = Rect(29, 147, 565, 160) # coordenadas padrão
        if VISUALIZE:  #se o visualize (linha 20) for = true, gera um documento novo com um quadrado circulando a area que sera extraida nas coordenadas
            page.draw_rect(rect, width=1.5, color=(1, 0, 0)) #cor do quadrado do visualize
        nome = page.get_textbox(rect) # nome = o texto extraído da area do quadrado
        if len(nome) == 0: # se nãop tiver nada para ser extraido
            nome = '.' #nome = .
        # print(nome)
#----------------------------------------------------------------------------------------------------------------------------
    #contabil
    doc: Document = fitz.open(input_path) #abre o documento para leitura 
    for i in range(len(doc)): #para cada Pagina documento
        page: Page = doc[i]
        page.clean_contents()
        rect = Rect(374, 425, 461, 436) # coordenadas padrão
        if VISUALIZE:  #se o visualize (linha 20) for = true, gera um documento novo com um quadrado circulando a area que sera extraida nas coordenadas
            page.draw_rect(rect, width=1.5, color=(1, 0, 0)) #cor do quadrado do visualize
        contabil = page.get_textbox(rect) # contabil = o texto extraído da area do quadrado
        if len(contabil) == 0: # se nãop tiver nada para ser extraido
            contabil = '.' #contabil = .
        # print(contabil)
#----------------------------------------------------------------------------------------------------------------------------
    #base de calculo
    doc: Document = fitz.open(input_path) #abre o documento para leitura 
    for i in range(len(doc)): #para cada Pagina documento
        page: Page = doc[i]
        page.clean_contents()
        rect = Rect(478, 425, 565, 436) # coordenadas padrão
        if VISUALIZE:  #se o visualize (linha 20) for = true, gera um documento novo com um quadrado circulando a area que sera extraida nas coordenadas
            page.draw_rect(rect, width=1.5, color=(1, 0, 0))#cor do quadrado do visualize
        BC = page.get_textbox(rect) # BC = o texto extraído da area do quadrado
        if len(BC) == 0: # se nãop tiver nada para ser extraido
            BC = '.' #BC = .
        # print(BC)
#----------------------------------------------------------------------------------------------------------------------------
    #debito  
    doc: Document = fitz.open(input_path) #abre o documento para leitura                 
    for i in range(len(doc)): #para cada Pagina documento
        page: Page = doc[i]
        page.clean_contents()
        rect = Rect(208, 454, 293, 469) # coordenadas padrão
        if VISUALIZE: #se o visualize (linha 20) for = true, gera um documento novo com um quadrado circulando a area que sera extraida nas coordenadas
            page.draw_rect(rect, width=1.5, color=(1, 0, 0)) #cor do quadrado do visualize
        debito = page.get_textbox(rect) # Debito = o texto extraído da area do quadrado
        if len(debito) == 0: # se nãop tiver nada para ser extraido
            debito = '.' #Debito = .
        # print(debito)  
#----------------------------------------------------------------------------------------------------------------------------
        print(f'{nome}; {data}; {contabil}; {BC}; {debito}') #gera o csv com as informações extraidas 
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
