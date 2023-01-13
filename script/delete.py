import os 
import shutil
import glob

gias = glob.glob('script/data/*pdf')

dirTxt = 'script/GIA_JSON'
for f in os.listdir(dirTxt):
    os.remove(os.path.join(dirTxt, f))

dirCsv = 'script/GIA_XLSX'
for f in os.listdir(dirCsv):
    os.remove(os.path.join(dirCsv, f))

for g in gias:
    shutil.move(g, 'script/Gias_usadas')

print("-------- arquivos excluidos e gias movidas --------")
