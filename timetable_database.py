import mysql.connector as myc
mysql=myc.connect(host='localhost',user='root',password='12345',database='timetable')
cursor=mysql.cursor()
def connect():
    mysql=myc.connect(host='localhost',user='root',password='12345',database='timetable')
    cursor=mysql.cursor()

if mysql.is_connected():
    print('Database connected')

def insert1211(a,b,c,d,e,f,g,h):
    connect()
    if a==12:
        v="insert into class_12 (days,i,ii,iii,iv,v,vi) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(b,c,d,e,f,g,h)
        cursor.execute(v)
        mysql.commit()
    if a==11:
        v="insert into class_11 (days,i,ii,iii,iv,v,vi) values('{0}','{1}','{2}',{3}','{4}','{5}','{6}')".format(b,c,d,e,f,g,h)
        cursor.execute(v)
        mysql.commit()
    mysql.close()
def  insert10(b,q,w,e,l,t,y,u,f,o):
    connect()
    v="insert into class_10 (days,i,ii,iii,iv,v,vi,vii,viii) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(b,q,w,e,l,t,y,u,f,o)
    cursor.execute(v)
    mysql.commit()
    mysql.close()
    
def update12(A,D,C):
    connect()
    m="update class_12 set "+D+"='{0}' where days='{1}'".format(C,A)
    cursor.execute(m)
    mysql.commit()
    mysql.close()
    
def update11(A,D,C):
    connect()
    m="update class_11 set "+D+"='{0}' where days='{1}'".format(C,A)
    cursor.execute(m)
    mysql.commit()
    mysql.close()
    
def update10(A,D,C):
    connect()
    m="update class_10 set "+D+"='{0}' where days='{1}'"
    cursor.execute(m.format(C,A))
    mysql.commit()
    mysql.close()
    
def  period(a,b):
    connect()
    if a==10:  
        cursor.execute("select * from class_10 where days='{}'".format(b))
        data=cursor.fetchall()
        s='_'*165
        m=int(15)
        w=' '
        for row in data:
            for i in row:
                h=0
                o=len(str(i))
                h=15-o
                print(i,w*h,'|' , end='')
            print('\n')
            print(s)
    if a==11:
        cursor.execute("select * from class_11 where days='{}'".format(b))
        data=cursor.fetchall()
        s='_'*125
        m=int(15)
        w=' '
        for row in data:
            for i in row:
                h=0
                o=len(str(i))
                h=15-o
                print(i,w*h,'|' , end='')
            print('\n')
            print(s)
    if a==12:
        cursor.execute("select * from class_12 where days='{}'".format(b))
        data=cursor.fetchall()
        s='_'*125
        m=int(15) 
        w=' '
        for row in data:
            for i in row:
                h=0
                o=len(str(i))
                h=15-o
                print(i,w*h,'|' , end='')
            print('\n')
            print(s)
    mysql.close()
def show12():
    connect()
    cursor.execute("select * from class_12  order by field(days,'mon','tue','wed','thu','fri','sat')")
    data=cursor.fetchall()
    s='_'*125
    m=int(15)
    w=' '
    for row in data:
        for i in row:
            h=0
            o=len(str(i))
            h=15-o
            print(i,w*h,'|' , end='')
        print('\n')
        print(s)
    mysql.close()
def show11():
    connect()
    cursor.execute("select * from class_11  order by field(days,'mon','tue','wed','thu','fri','sat')")
    data=cursor.fetchall()
    s='_'*125
    m=int(15)
    w=' '
    for row in data:
        for i in row:
            h=0
            o=len(str(i))
            h=15-o
            print(i,w*h,'|' , end='')
        print('\n')
        print(s)
    mysql.close()
def show10():
    connect()
    cursor.execute("select * from class_10  order by field(days,'mon','tue','wed','thu','fri','sat')")
    data=cursor.fetchall()
    s='_'*165
    m=int(15)
    w=' '
    for row in data:
        for i in row:
            h=0
            o=len(str(i))
            h=15-o
            print(i,w*h,'|' , end='')
        print('\n')
        print(s)
    mysql.close()
def delete12(days):
    try:
        cursor.execute("delete from class_12 where days='{0}'".format(days))
        mysql.commit()
        mysql.close()
        return True
    except:
        print('directory name does not exist')
        return False
def delete11 (days):
    try:
        cursor.execute("delete from class_11 where days='{0}'".format(days))
        mysql.commit()    
        mysql.close()
        return True
    except:
        print('directory name does not exist')
        return False
def delete10 (days):
    try:
        cursor.execute("delete from class_10 where days='{0}'".format(days))
        mysql.commit()
        mysql.close()
        return True
    except:
        print('directory name does not exist')
        return False
print('database ok')
#mysql.close()

