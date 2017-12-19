from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('child_jinja.html',name='Rajesh')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4500,debug=True)