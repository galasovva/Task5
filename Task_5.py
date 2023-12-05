
from flask import *
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')

@app.route('/athletes/')
def athletes():
    return render_template('athletes.html')

if __name__ == '__main__':
    app.run(debug=True)




