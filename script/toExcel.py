import pandas as pd
import os
from pathlib import Path
from glob import glob
import subprocess

arquivos = glob('script/GIA_JSON/*.json')

g = 1

uniq_df = pd.DataFrame()

for i in arquivos:
    df = pd.read_json(i, orient='index')
    df = pd.DataFrame(df)
    uniq_df = pd.concat([uniq_df, df], axis=1, ignore_index=False)
    df.to_excel(f"script/GIA_XLSX/GIA{g}.xlsx")
    g = g + 1 

uniq_df = uniq_df.transpose()
uniq_df.drop(columns=['suporte'], inplace=True)
uniq_df.replace(",", "")

uniq_df.to_excel('GIAs.xlsx',sheet_name='Planilha', index=False)  

print("----------------- planilhas criadas -----------------")