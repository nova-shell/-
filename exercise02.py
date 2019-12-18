import pymysql
import re
db=pymysql.connect(host='localhost',
                   user='root',
                   port=3306,
                   passwd='123456',
                   database='dict',
                   charset='utf8')


cur=db.cursor()
f=open('dict.txt')
args_list=[]
for line in f:
    result=re.findall(r"(\S+)\s+(.*)",line)
    args_list.extend(result)
f.close()

sql=("insert into words (word,mean) valuses(%s,%s)");
try:
    cur.executemany(sql,args_list)
    db.commit()
except:
    db.rollback()


cur.close()
db.close()