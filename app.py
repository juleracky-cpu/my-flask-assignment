from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['healthcare_db']
collection = db['users']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect form data
        age = int(request.form['age'])
        gender = request.form['gender']
        income = float(request.form['income'])
        expenses = {
            'utilities': float(request.form.get('utilities', 0)),
            'entertainment': float(request.form.get('entertainment', 0)),
            'school_fees': float(request.form.get('school_fees', 0)),
            'shopping': float(request.form.get('shopping', 0)),
            'healthcare': float(request.form.get('healthcare', 0))
        }
        # Save to MongoDB
        collection.insert_one({
            'age': age,
            'gender': gender,
            'income': income,
            'expenses': expenses
        })
        return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)