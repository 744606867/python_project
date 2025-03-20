from flask import Flask, request, render_template
from request_l import returnData as test
import mysql.connector

class  WithopenPractices:
    def __init__(self,url,name):
        self.name = name
        self.url = url

    def openfile(self):
        with open(self.url+self.name,"r",encoding='utf-8') as file:
         return  file.read()


app = Flask(__name__)

@app.route('/')
def hello_world():
    return test();

@app.route('/test1', methods=['POST'])
def hello_world1():
    return 'SSS';

@app.route('/test/<page>', methods=['GET'])
def hello_world2(page):
    return page;

@app.route('/test/lrl',methods=['POST'])
def hello_world3():
    print("1",request.base_url)
    print("2",request.full_path)
    print("3",request.headers.get('Content-Type'))
    print("4",request.data.decode(encoding='utf-8'))
    print("5",request.host)
    print("6",request.path)
    return request.url;

db = mysql.connector.connect(
    host="192.168.0.126",    # 数据库主机地址
    user="root",         # 数据库用户名
    password="Cosmo_6003", # 数据库密码
    database="mxwi"    # 要连接的数据库名称
)
@app.route('/test/lrl')
def mysqldata():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(type(results))
    return render_template('test.html',results = results)




if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5002)
