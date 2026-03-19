from flask import Flask, render_template, request, redirect, url_for
from collections import deque
from datetime import datetime
from models import Patient

app = Flask(__name__)

# Data structures
waiting_queue = deque()      # FIFO queue for patients waiting
seen_patients = []           # List of patients already seen

@app.route('/')
def index():
    """Home page – shows waiting list and today's seen count."""
    today = datetime.now().date()
    total_seen_today = sum(
        1 for p in seen_patients 
        if p.seen_time and p.seen_time.date() == today
    )
    # Convert deque to list for easy iteration in the template
    waiting_list = list(waiting_queue)
    return render_template('index.html', 
                           waiting=waiting_list, 
                           total_seen=total_seen_today)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Form to add a new patient to the waiting queue."""
    if request.method == 'POST':
        name = request.form['name'].strip()
        if name:   # basic validation
            new_patient = Patient(name)
            waiting_queue.append(new_patient)
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/see_next', methods=['POST'])
def see_next():
    """Mark the next patient (front of queue) as seen."""
    if waiting_queue:
        patient = waiting_queue.popleft()   # FIFO removal
        patient.mark_seen()
        seen_patients.append(patient)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
