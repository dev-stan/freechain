import os


def runBot():
    try:
        os.system('cd C:/Users/stan/Desktop/jotaro')
    except:
        print('something went wrong')
    print(f'dir: {os.getcwd()}')
    os.system('python3 main.py')
    print('jotaro started')
    