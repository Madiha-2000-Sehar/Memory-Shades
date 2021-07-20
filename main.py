from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import mysql.connector
app=Flask(__name__)

"""app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '10mother#_mysql'
app.config['MYSQL_DB'] = 'one'
#mysql=MySQL(app)"""
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        info=request.form
        username=info['uname']
        upassword=info['upassword']
        #print(username)
        mydb = mysql.connector.connect(host="localhost", user="root", password="10mother#_mysql", database="one")
        mycursor = mydb.cursor()
        #cursor.execute('insert into documents(docid,docname) values(%d, %s)', (number, temp))
        #sql = "INSERT INTO memory_shades values(%s,%s)"
        sql="SELECT *FROM memory_shades WHERE username=%s and user_password=%s"
        mycursor.execute(sql, (username, upassword))
        #mycursor.execute(sql)
        result=mycursor.fetchall()
        if result==[]:
            return "<h1>Your User name or password is incorrect, please try again.</h1>"
        print(result)
        #print(mydata[0])
        mydb.commit()
        mydb.close()
        return "<h1>Login successful!!</h1>"
    return render_template("sign_up.html")
if __name__=='__main__':
    app.run()