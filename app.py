from flask import Flask, render_template, request, redirect, url_for
from models import Patient, waiting_queue, seen_today
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    queue_list = [p.get_info() for p in waiting_queue]
    total_seen = len(seen_today)
    today_date = datetime.now().strftime("%d %B %Y")
    
    return render_template('index.html', 
                           queue=queue_list, 
                           total_seen=total_seen,
                           today_date=today_date)

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

# NEW ROUTE - Serve next patient (FIFO)
@app.route('/serve')
def serve():
    if waiting_queue:
        next_patient = waiting_queue.popleft()   # FIFO - first patient out
        next_patient.seen = True
        next_patient.arrival_time = datetime.now().strftime("%H:%M:%S")  # update time when served
        seen_today.append(next_patient)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)