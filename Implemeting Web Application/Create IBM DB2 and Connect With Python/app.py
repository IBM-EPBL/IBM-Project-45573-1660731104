from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import re

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ydc23824;PWD=RHxHgH1rnTluiY9S", '','')

app = Flask(__name__)  
app.secret_key = 'a'


@app.route("/")
def home():
    return render_template('HOME.html')

@app.route('/signup')
def new_student():
    return render_template('SIGNUP.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method =='POST' :

        NAME = request.form['NAME']
        EMAIL = request.form['EMAIL']
        PASSWORD = request.form['PASSWORD']

        sql = "SELECT * FROM DETAILS WHERE NAME =?"
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,NAME)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

        if account:
            return render_template('SIGNUP.html', msg="You are already have a member with same name.")
        else:
            insert_sql = "INSERT INTO DETAILS VALUES (?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, NAME)
            ibm_db.bind_param(prep_stmt, 2, EMAIL)
            ibm_db.bind_param(prep_stmt, 4, PASSWORD)
            ibm_db.execute(prep_stmt)

        return render_template('SIGNUP.html', " DETAILS data saved successfully...")

    


@app.route('/loginin/')
def login():
     DETAILS = []
    sql = "SELECT * FROM  DETAILS"
    stmt = ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:

        DETAILS.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)
        
        
    if  DETAILS:
        return render_template("login.html", DETAILS = DETAILS)
    
@app.route('/delete/<name>')
def delete(name):
    sql = f"SELECT * FROM DETAILS WHERE NAME='{escape(name)}'"
    print(sql)
    stmt = ibm_db.exec_immediate(conn, sql)
    DETAILS = ibm_db.fetch_row(stmt)
    print("The Name is : ", DETAILS)
    if DETAILS:
        sql = f"DELETE FROM DETAILS WHERE NAME='{escape(name)}'"
        print(sql)
        stmt = ibm_db.exec_immediate(conn,sql)
   
    
    DETAILS = []
    sql = "SELECT * FROM DETAILS"
    stmt = ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        DETAILS.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)
    if DETAILS:
        return render_template("index.html", DETAILS = DETAILS, msg = "Delete Successfully...")
    
    
    return "Success...."

    

