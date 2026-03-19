# 🏥 HealthQueue - Smart Clinic Patient Management System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

**A beautiful, professional 3-page web application** built with **Flask** for managing clinic patients.

---

## ✨ What is HealthQueue?

HealthQueue is a modern clinic queue management platform that allows:
- **Registering new patients** instantly
- **Viewing live waiting list** (FIFO Queue)
- **Serving patients** one by one
- **Undo last serve** using Stack (LIFO)
- Clean, responsive Material Design UI with smooth animations

Perfect real-world simulation for hospital/clinic reception.

---

## 🎯 Features Implemented (All Assignment Requirements Fulfilled ✅)

- **OOP** → `Patient` class with `__init__` and `get_info()` method
- **Data Structures** → `deque` (FIFO Queue) + List as **Stack** (Undo feature)
- **Standard API** → `datetime` module for timestamps
- **Flask** → 3 clean pages + form handling + data passing
- **Professional UI** → Modern blue Material Design with animations, hover effects & icons

---

## 🚀 How to Run Locally (Beginner Friendly)

1. Download or clone the repository
2. Open the folder in **VS Code**
3. Open Terminal and run these commands one by one:

```bash
python -m venv venv
venv\Scripts\activate
pip install flask
python app.py
```

Open your browser and go to:
http://127.0.0.1:5000
Enjoy! Register patients → Go to Queue → Serve & Undo.

## 🛠 Technologies Used

- Python + Flask
- OOP (Classes)
- Data Structures (Queue + Stack)
- datetime module
- HTML + CSS