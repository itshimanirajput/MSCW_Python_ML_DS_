

from flask import Flask, render_template

MyPage = Flask(__name__, template_folder="Template")


@MyPage.route('/')
def Msg():
    return "<h2>Welcome to Index page of my Application.....</h2>"

@MyPage.route('/AboutUs')
def AboutUs():
    return render_template('AboutUs.html')


@MyPage.route("/test")
def Display():
    return "<h1>Welcome to your first webpage in Python </h1>"

if __name__ == '__main__':
    MyPage.run()