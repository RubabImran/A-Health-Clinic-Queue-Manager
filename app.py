from flask import Flask, render_template, request, redirect, url_for
from models import Patient, waiting_queue, seen_today, served_stack, reset_demo
from datetime import datetime

app = Flask(__name__)

# HOME PAGE - Professional landing
@app.route('/')
def home():
    return render_template('index.html')

# QUEUE PAGE
@app.route('/queue')
def queue():
    queue_list = [p.get_info() for p in waiting_queue]
    total_seen = len(seen_today)
    total_registered = len(waiting_queue) + total_seen
    today_date = datetime.now().strftime("%d %B %Y")
    last_served = served_stack[-1].get_info() if served_stack else "None yet"
    
    return render_template('queue.html',
                           queue=queue_list,
                           total_seen=total_seen,
                           total_registered=total_registered,
                           today_date=today_date,
                           last_served=last_served)

# REGISTER PAGE
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        symptoms = request.form['symptoms']
        
        new_patient = Patient(name, age, symptoms)
        waiting_queue.append(new_patient)
        return redirect('/queue')   # After register → go to queue page
    
    return render_template('register.html')

# Actions
@app.route('/serve')
def serve():
    if waiting_queue:
        p = waiting_queue.popleft()
        p.seen = True
        p.arrival_time = datetime.now().strftime("%H:%M:%S")
        seen_today.append(p)
        served_stack.append(p)
    return redirect('/queue')

@app.route('/undo')
def undo():
    if served_stack:
        p = served_stack.pop()
        p.seen = False
        waiting_queue.appendleft(p)
        seen_today.remove(p)
    return redirect('/queue')

@app.route('/reset')
def reset():
    reset_demo()
    return redirect('/queue')

if __name__ == '__main__':
    app.run(debug=True)