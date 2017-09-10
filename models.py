import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='275265zt',
                             db='gd_blog',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
def addUser(sys_user,login_id,password,registertime):
    sql = "INSERT INTO sys_user (sys_user, login_id,password,registertime) VALUES ('%s','%s','%s','%s')"%(sys_user,login_id,password,registertime)
    cursor.execute(sql)
    connection.commit()
    cursor.close()

def addTestUser(id,name):
    sql = "INSERT INTO test_table (id,name) VALUES ('%s','%s')"%(id,name)
    cursor.execute(sql)
    connection.commit()
    cursor.close()

def addTestUserTest(name,password):
    sql = "INSERT INTO test_table2 (name,password) VALUES ('%s','%s')"%(name,password)
    cursor.execute(sql)
    connection.commit()
    cursor.close()