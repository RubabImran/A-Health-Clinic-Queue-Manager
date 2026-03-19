from flask import Flask, render_template, request, redirect, url_for
from models import Patient, waiting_queue, seen_today, served_stack, reset_demo
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    queue_list = [p.get_info() for p in waiting_queue]
    total_seen = len(seen_today)
    total_registered = len(waiting_queue) + len(seen_today)
    today_date = datetime.now().strftime("%d %B %Y")
    
    last_served = served_stack[-1].get_info() if served_stack else "None yet"
    
    return render_template('index.html', 
                           queue=queue_list, 
                           total_seen=total_seen,
                           total_registered=total_registered,
                           today_date=today_date,
                           last_served=last_served)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        symptoms = request.form['symptoms']
        
        new_patient = Patient(name, age, symptoms)
        waiting_queue.append(new_patient)
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/serve')
def serve():
    if waiting_queue:
        next_patient = waiting_queue.popleft()
        next_patient.seen = True
        next_patient.arrival_time = datetime.now().strftime("%H:%M:%S")
        seen_today.append(next_patient)
        served_stack.append(next_patient)   # Push to Stack for undo
    return redirect(url_for('home'))

@app.route('/undo')
def undo():
    if served_stack:
        last_patient = served_stack.pop()   # Pop from Stack (LIFO)
        last_patient.seen = False
        waiting_queue.appendleft(last_patient)  # Put back to front of queue
        seen_today.remove(last_patient)
    return redirect(url_for('home'))

@app.route('/reset')
def reset():
    reset_demo()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)