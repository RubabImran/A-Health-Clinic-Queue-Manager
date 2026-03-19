# 🏥 Health Clinic Queue Manager
An app to register patients, view the current
waiting list (first-in, first-out), and view the total number of patients seen today.

## What the app does
- Register new patients using HTML form
- View waiting list (First-In First-Out Queue)
- Serve next patient + see total seen today (with datetime timestamp)
- Undo last serve using Stack (LIFO)
- Beautiful, fully working web app

## Features Implemented
- OOP: Patient class with __init__ and get_info()
- Data Structures: Queue (deque) + Stack (list)
- API: datetime for timestamps
- Flask: 4 routes + form + data flow

## How to run locally (for beginners)

1. Download or clone this repo
2. Open folder in VS Code
3. Open terminal and run:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install flask
   python app.py