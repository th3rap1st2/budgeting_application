from flask import Flask, render_template, request, session, redirect, url_for
import json, os
import budget


app = Flask(__name__,
             template_folder='../frontend/templates', 
             static_folder='../frontend/static')

app.secret_key = os.environ.get('SECRET_KEY', 'fallback-dev-key')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():

    return render_template('register.html')

@app.route('/register_2', methods=['GET', 'POST'])
def register_2():

    if 'balance' in request.form and 'budget' in request.form:
        balance = float(request.form.get('balance'))
        budget_amount = float(request.form.get('budget'))  # get the stuff from the form

        name = session.get('name')  # get the data from the session 
        email = session.get('email')

        if budget_amount > balance:
            return render_template('register_2.html', name=name, budget_error="Budget cannot exceed current balance")

      
        user = budget.User(name, email)
        budget_app = budget.BudgetApp(user, balance, budget_amount) # create objects 

        user_data = {
            "user": user.to_dict(),
            "current_balance": budget_app.current_balance,
            "transactions": budget_app.transactions,
            "total_transactions": budget_app.total_transactions
        } # make a json file with all the information 

        with open('user_data.json', 'w') as file:
            json.dump(user_data, file) # add the information into it 

        return redirect(url_for('existing'))  # redirect user into the existing url
     
    name = session.get('name')
    return render_template('register_2.html', name=name)


@app.route('/existing')
def existing():
    return render_template('existing.html')

if __name__ == '__main__':
    app.run(debug=True)