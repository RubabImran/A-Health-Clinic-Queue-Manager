from datetime import datetime

class Patient:
    """Represents a patient in the clinic queue system."""
    
    def __init__(self, name, registration_time=None):
        self.name = name
        # If no time is given, use the current moment
        self.registration_time = registration_time or datetime.now()
        self.seen_time = None          # Will be set when patient is seen

    def mark_seen(self):
        """Record the moment the patient is taken from the queue."""
        self.seen_time = datetime.now()

    def waiting_duration(self):
        """
        Return the time spent waiting.
        If not yet seen, calculate from registration until now.
        """
        if self.seen_time:
            return self.seen_time - self.registration_time
        return datetime.now() - self.registration_time

    def __repr__(self):
        return f"<Patient {self.name} (registered at {self.registration_time})>"