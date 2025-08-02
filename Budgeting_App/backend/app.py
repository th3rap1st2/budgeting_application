from flask import Flask, render_template, request, jsonify

app = Flask(__name__,
             template_folder='../frontend/templates', 
             static_folder='../frontend/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/existing')
def existing():
    return render_template('existing.html')


if __name__ == '__main__':
    app.run(debug=True)