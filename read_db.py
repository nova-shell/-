
"""
方案一
"""


import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
# 理由游标对象执行select语句
cur = db.cursor()
# sql = "select name,age,sex from cls where sex='m';"
# name=input("Name:")
# 组合sql语句
# sql = "select name,hobby from interest where name='%s';"%name
# print(sql)
# sql2="select * from cls order by score desc"
# cur.execute(sql)

sql="select name,age from cls where age>%s and sex=%s"
cur.execute(sql,[17,'m'])

# cur.execute(sql)

# 遍历游标对象获取查询记录

# for i in cur:
#     print(i)
# 获取一个查询结果
# print(cur.fetchone())
# 获取多个查询结果
# print(cur.fetchmany(3))
# 获取所有查询结果
print(cur.fetchall())

cur.close()
db.close()
