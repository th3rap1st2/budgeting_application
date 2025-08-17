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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session['name'] = (request.form.get('name').strip()).title()
        session['email'] = request.form.get('email').strip()
        # session stores the name and email across everything 
        
        return redirect(url_for('register_2'))

    return render_template('register.html')

@app.route('/register_2', methods=['GET', 'POST'])
def register_2():

    if 'balance' in request.form and 'budget' in request.form:
        name = session.get('name')  # get the data from the session 
        email = session.get('email')

        try:
            balance = float(request.form.get('balance').strip())
            budget_amount = float(request.form.get('budget').strip())  # get the information from the form

            if balance < 0 or budget_amount < 0:
                raise ValueError('Number cannot be negative!')

        except ValueError:  
            return render_template('register_2.html', name=name, budget_error="Please enter a valid number.")

        if budget_amount > balance:  # check if the monthly budget doesn't exceed the current balance 
            return render_template('register_2.html', name=name, budget_error="Budget cannot exceed current balance.")
      
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
     
    name = session.get('name', 'Guest')
    return render_template('register_2.html', name=name)


@app.route('/existing')
def existing():
    return render_template('existing.html')

if __name__ == '__main__':
    app.run(debug=True)