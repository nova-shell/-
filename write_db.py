import pymysql
db=pymysql.connect(host='localhost',
                   user='root',
                   port=3306,
                   password='123456',
                   database='stu',
                   charset='utf8')
cur=db.cursor()
try:
    # sql="insert into cls values(%s,%s,%s,%s,%s)"
    # sql="update cls set score=98 where id=3"
    # cur.execute(sql,[12,'KK',17,'m',99])
    # sql="delete from cls where id=2"
    # cur.execute(sql)
    list_=[1,3,4]
    sql="update cls set score=score+10 where id=%s;"
    # for i in list_:
    #     cur.execute(sql,[i])
    cur.executemany(sql,list_)  #通过executemany执行大量的sql语句
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
cur.close()
db.close()