import subprocess

class root:
    subprocess.call('node script/main.js')
    subprocess.call('python script/loop.py')
    subprocess.call('python script/tableTreaterLine.py')
    subprocess.call('python script/toExcel.py')
    subprocess.call('python script/delete.py')

    print('arquivo gerado')