import glob
import shutil

gias = glob.glob('GIAS/*.pdf')

for g in gias:
    shutil.move(g, 'script/data')