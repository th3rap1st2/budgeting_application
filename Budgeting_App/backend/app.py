from flask import Flask, render_template, request
import json, os

app = Flask(__name__,
             template_folder='../frontend/templates', 
             static_folder='../frontend/static')

transactions = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/existing')
def existing():
    return render_template('existing.html')

@app.route('/register_2', methods=['POST'])
def register_2():
    name = request.form.get('name').title()
    email = request.form.get('email')

    user_info = {
        "name": name, 
        "email": email
    }
    return render_template('register_2.html', name=name)



if __name__ == '__main__':
    app.run(debug=True)