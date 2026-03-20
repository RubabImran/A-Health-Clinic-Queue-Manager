# Import necessary modules and classes
from flask import Flask, render_template, request, redirect, url_for
from models import Patient, waiting_queue, seen_today, served_stack, reset_demo
from datetime import datetime

# Create Flask application instance
app = Flask(__name__)

# =========================
# HOME PAGE - Professional landing
# This route renders the homepage of the application
# =========================
@app.route('/')
def home():
    # Render the main landing page template
    return render_template('index.html')

# =========================
# QUEUE PAGE
# Displays current queue, stats, and last served patient
# =========================
@app.route('/queue')
def queue():
    # Convert each patient object in the queue to readable info
    queue_list = [p.get_info() for p in waiting_queue]
    
    # Total number of patients already seen today
    total_seen = len(seen_today)
    
    # Total registered patients = waiting + seen
    total_registered = len(waiting_queue) + total_seen
    
    # Get today's date in readable format
    today_date = datetime.now().strftime("%d %B %Y")
    
    # Get last served patient if available, otherwise show default text
    last_served = served_stack[-1].get_info() if served_stack else "None yet"
    
    # Render queue page with all computed values
    return render_template('queue.html',
                           queue=queue_list,
                           total_seen=total_seen,
                           total_registered=total_registered,
                           today_date=today_date,
                           last_served=last_served)

# =========================
# REGISTER PAGE
# Handles patient registration (GET shows form, POST processes form)
# =========================
@app.route('/register', methods=['GET', 'POST'])
def register():
    # If form is submitted
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        age = int(request.form['age'])
        symptoms = request.form['symptoms']
        
        # Create new patient object
        new_patient = Patient(name, age, symptoms)
        
        # Add patient to the waiting queue
        waiting_queue.append(new_patient)
        
        # Redirect to queue page after registration
        return redirect('/queue')
    
    # If GET request, show registration form
    return render_template('register.html')

# =========================
# SERVE PATIENT
# Removes patient from queue and marks them as served
# =========================
@app.route('/serve')
def serve():
    # Check if there are patients in the queue
    if waiting_queue:
        # Remove patient from front of queue (FIFO)
        p = waiting_queue.popleft()
        
        # Mark patient as seen
        p.seen = True
        
        # Record time patient was served
        p.arrival_time = datetime.now().strftime("%H:%M:%S")
        
        # Add to seen list
        seen_today.append(p)
        
        # Push to stack for undo functionality
        served_stack.append(p)
    
    # Redirect back to queue page
    return redirect('/queue')

# =========================
# UNDO LAST SERVE
# Reverts the last served patient back to the queue
# =========================
@app.route('/undo')
def undo():
    # Check if there is a served patient to undo
    if served_stack:
        # Remove last served patient (LIFO from stack)
        p = served_stack.pop()
        
        # Mark patient as not seen
        p.seen = False
        
        # Put patient back at the front of the queue
        waiting_queue.appendleft(p)
        
        # Remove patient from seen list
        seen_today.remove(p)
    
    # Redirect back to queue page
    return redirect('/queue')

# =========================
# RESET SYSTEM
# Clears all demo data and resets state
# =========================
@app.route('/reset')
def reset():
    # Call helper function to reset all data structures
    reset_demo()
    
    # Redirect back to queue page
    return redirect('/queue')

# =========================
# RUN APPLICATION
# Starts the Flask development server
# =========================
if __name__ == '__main__':
    # Run app in debug mode (auto-reload + error details)
    app.run(debug=True)