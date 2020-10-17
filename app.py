from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_data():
    username = request.form['username']
    password = request.form['pass']
    if username == 'ashishgaikwad781@gmail.com' and password =='ashish':
        return f'Welcome Username:{username} Password:{password}'
    else:
        return f'Wrong username or Password'



if __name__ == '__main__':
    app.run(debug=True, port=8083)

