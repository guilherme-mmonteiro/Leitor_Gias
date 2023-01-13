
from lista import lista
import subprocess

output = lista

saida = 1

print(output)

print('----------------- gerando arquivos -----------------')

for i in output:
    lista1 = (f"node script/index.js {i} > script/GIA_JSON/output{saida}.json")
    saida = saida + 1
    subprocess.call(lista1, shell=True)

print('----------------- arquivos gerados -----------------')
    
