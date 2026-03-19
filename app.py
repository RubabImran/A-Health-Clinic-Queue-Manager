from flask import Flask, render_template, request, redirect, url_for
from models import Patient, waiting_queue, seen_today   # Import everything we made in Step 2
from datetime import datetime

app = Flask(__name__)

# HOME PAGE - shows queue and seen today
@app.route('/')
def home():
    # Convert queue to list so we can show it nicely
    queue_list = [p.get_info() for p in waiting_queue]
    total_seen = len(seen_today)
    today_date = datetime.now().strftime("%d %B %Y")
    
    return render_template('index.html', 
                           queue=queue_list, 
                           total_seen=total_seen,
                           today_date=today_date)

# REGISTER PAGE - form to add patient
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        symptoms = request.form['symptoms']
        
        new_patient = Patient(name, age, symptoms)
        waiting_queue.append(new_patient)   # Add to Queue (FIFO)
        
        return redirect(url_for('home'))   # Go back to home after adding
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)