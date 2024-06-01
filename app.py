from flask import Flask,render_template
#from keras.models import load_model
#from keras.preprocessing import image

app = Flask(__name__)



@app.route("/",methods=['GET','POST'])
def main():
    return render_template("home.html")

@app.route("/index.html",methods=['GET','POST'])
def find():
    return render_template("index.html")

@app.route("/login_page")
def login():
    return render_template("login.html")

@app.route("/some.html")
def sample():
    return render_template("some.html")

if __name__ == '__main__':
    app.run(debug=True)

