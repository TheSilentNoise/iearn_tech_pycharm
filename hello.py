from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)

@app.route("/hello/<name>")
def Hello_World(name):
        return "Hello World %s" %name

@app.route("/hello/<int:postid>")
def show_blog(postid):
        return "Blog Number %d" %postid

@app.route("/hello/<name>/<int:postid>")
def show_hello_name(name,postid):
        return "This is your post number %d" %postid

@app.route("/hello/<float:revisionid>")
def revision_show(revisionid):
        return "Revision Number %f" %revisionid

##################### Cannonical URL #####################
@app.route('/flask')
def hello_flask():
        return "Hello Flask"

@app.route('/hello/')
def hello_test():
        return "Hello Python"

####################### URL Redirection ######################

@app.route('/admin')
def hello_admin():
        return "Hello Admin"

@app.route('/guest/<guestname>')
def hello_guest(guestname):
        return "Hello %s as Guest" %guestname

@app.route('/user/<name>')
def hello_user(name):
        if name=='admin':
                return redirect(url_for('hello_admin'))
        else:
                return redirect(url_for('hello_guest',guestname = name))

#################### Templates #########################

@app.route('/template')
def template():
        return '<html><body><h1>Hello Template</h1></body></html>'

@app.route('/render')
def index():
        return render_template('hello.html')

@app.route('/render/<user>')
def hello_render(user):
        return render_template('hello.html',name = user)

@app.route('/render/<user>/<int:score>')
def marks_share(user,score):
        return render_template('hello.html',name = user, marks = score)

@app.route('/render/marksheet/<user>')
def marks_table(user):
        dict = {'English':96,'Maths':89,'ENVS':91}
        return render_template('marks_template.html',name = user, result = dict)

#################### Flask Static Files #####################
@app.route('/render/jsaction')
def jsaction():
        return render_template('index.html')

#################### Flask Request Object ###################
@app.route('/student')
def student():
        return render_template('student.html')

@app.route('/student/result', methods=['POST','GET'])
def result():
        if request.method == 'POST':
                result = request.form
                return render_template('result.html',result = result)

##################### Flask cookies ####################
@app.route('/cookie')
def cookieS():
        return render_template('cookie.html')

@app.route('/cookie/set')
def cookieSet():
        if request.method == 'POST':
            user = request.form['nm']

        resp = make_response(render_template('readCookie.html'))
        resp.set_cookie('userId',user)
        return resp

@app.route('/cookie/get')
def cookieGet():
        name = request.cookies.get('userId')
        return '<h1> Welcome '+name+'</h1>'
####################### Main Function #########################

if __name__=='__main__':
        app.run(host='0.0.0.0',debug = True)