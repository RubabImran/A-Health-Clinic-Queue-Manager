from datetime import datetime
from collections import deque  # This is Python's built-in Queue (FIFO)

class Patient:
    """This is our Patient class - OOP requirement"""
    
    def __init__(self, name, age, symptoms):
        self.name = name
        self.age = age
        self.symptoms = symptoms
        self.arrival_time = datetime.now().strftime("%H:%M:%S")  # Timestamp - API requirement
        self.seen = False  # Will use later for "seen today"

    def get_info(self):
        """Custom behavior method (this gives you marks)"""
        status = "✅ Seen" if self.seen else "⏳ Waiting"
        return f"{self.name} ({self.age} yrs) - {self.symptoms} | Arrived: {self.arrival_time} | {status}"


# Global Queue (FIFO) - Data Structure requirement
waiting_queue = deque()          # This will hold patients in order (first in = first out)
seen_today = []                  # List to count patients seen today

# Stack for Undo feature (LIFO) - Data Structures requirement
served_stack = []   # This is our Stack

def reset_demo():
    """Helper to clear everything (for testing)"""
    global waiting_queue, seen_today, served_stack
    waiting_queue.clear()
    seen_today.clear()
    served_stack.clear()