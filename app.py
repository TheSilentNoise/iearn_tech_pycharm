# Prerequisite : from cmd, run the command " pip install flask-mysql "

from flask import Flask, render_template, request,json
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'silent_noise'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/showSignUp')
def signUpShow():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUpRegister():
    if request.method == 'POST':
        _name = request.form['inputName']
        print (_name)
        _email = request.form['inputEmail']
        print(_email)
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            #return json.dumps({'html': '<span>All fields good !!</span>'})

            conn = mysql.connect()
            cursor = conn.cursor()
            query = "INSERT INTO user_info (user_name, user_username, user_password) VALUES('"+_name+"','"+_email+"','"+_password+"');"
            #print(query)
            cursor.execute(query)
            conn.commit()


            return json.dumps({'html':'<span>User Creation Successful</span>'})
            conn.close()
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/showSignIn')
def signInShow():
    return render_template('signin.html')


@app.route('/signIn', methods=['POST'])
def signInLogin():
    if request.method == 'POST':
        _email = request.form['inputEmail']
        print(_email)
        _password = request.form['inputPassword']
        print(_password)

    if _email and _password:
        conn = mysql.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM user_info WHERE user_username = '"+_email+"' AND '"+_password+"';"
        print(query)
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
        username = ""
        userId = ""
        for row in data:
            print "%s " % row[1]
            username = row[1]
            userId = row[0]

        if data is None:
            return json.dumps({'html':'<span>Login UnSuccessful</span>'})
            conn.close()
        else:
            return render_template('UserProfile.html', name = username, id = userId)
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
