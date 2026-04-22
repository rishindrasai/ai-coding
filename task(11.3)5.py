from collections import defaultdict, deque
from datetime import datetime, timedelta

# ============================================
# DATA STRUCTURES & JUSTIFICATION TABLE
# ============================================
"""
Feature                 | Data Structure      | Justification
------------------------|-------------------|--------------------------------------------------
Attendance Tracking     | Dictionary         | O(1) lookup by student ID; efficient updates
Event Registration      | Set                | Fast membership testing; prevents duplicates
Library Borrowing       | Deque               | FIFO order for return queue; efficient operations
Bus Scheduling          | Priority Queue      | Route priority; efficient dispatch sequencing
Cafeteria Order Queue   | Queue (Deque)      | FIFO ordering; fair service; efficient add/remove
"""

# 1. ATTENDANCE TRACKING (Dictionary)
class AttendanceTracker:
    def __init__(self):
        self.attendance = defaultdict(lambda: {"present": 0, "absent": 0, "total": 0})
    
    def mark_attendance(self, student_id, status):
        """Mark attendance for a student (present/absent)"""
        self.attendance[student_id]["total"] += 1
        if status.lower() == "present":
            self.attendance[student_id]["present"] += 1
        else:
            self.attendance[student_id]["absent"] += 1
    
    def get_attendance_percentage(self, student_id):
        """Calculate attendance percentage"""
        data = self.attendance[student_id]
        if data["total"] == 0:
            return 0
        return (data["present"] / data["total"]) * 100

# 2. EVENT REGISTRATION (Set)
class EventRegistration:
    def __init__(self, event_name):
        self.event_name = event_name
        self.registered_students = set()
    
    def register_student(self, student_id):
        """Register student for event"""
        if student_id not in self.registered_students:
            self.registered_students.add(student_id)
            return True
        return False
    
    def unregister_student(self, student_id):
        """Unregister student from event"""
        self.registered_students.discard(student_id)
    
    def get_registered_count(self):
        return len(self.registered_students)

# 3. LIBRARY BORROWING (Deque)
class LibraryBorrow:
    def __init__(self):
        self.borrow_queue = deque()
        self.borrowed_books = {}
    
    def borrow_book(self, student_id, book_name, due_days=14):
        """Add book borrowing record"""
        due_date = datetime.now() + timedelta(days=due_days)
        record = {"student_id": student_id, "book": book_name, "due_date": due_date}
        self.borrow_queue.append(record)
        self.borrowed_books[student_id] = record
        return f"Book '{book_name}' borrowed. Due: {due_date.date()}"
    
    def return_book(self, student_id):
        """Process book return (FIFO)"""
        if student_id in self.borrowed_books:
            del self.borrowed_books[student_id]
            return "Book returned successfully"
        return "No record found"

# 4. BUS SCHEDULING (Priority Queue - using list with sorting)
class BusScheduling:
    def __init__(self):
        self.bus_queue = []  # [(priority, timestamp, route, bus_id)]
        self.dispatch_counter = 0
    
    def schedule_bus(self, route, priority, bus_id):
        """Schedule bus with priority (lower number = higher priority)"""
        self.bus_queue.append((priority, self.dispatch_counter, route, bus_id))
        self.dispatch_counter += 1
        self.bus_queue.sort(key=lambda x: (x[0], x[1]))
    
    def dispatch_next_bus(self):
        """Dispatch highest priority bus"""
        if self.bus_queue:
            return self.bus_queue.pop(0)
        return None

# 5. CAFETERIA ORDER QUEUE (Queue - Deque)
class CafeteriaQueue:
    def __init__(self):
        self.order_queue = deque()
    
    def add_order(self, student_id, items):
        """Add order to queue (FIFO)"""
        order = {"student_id": student_id, "items": items, "timestamp": datetime.now()}
        self.order_queue.append(order)
        return f"Order added. Queue length: {len(self.order_queue)}"
    
    def process_next_order(self):
        """Process next order in queue"""
        if self.order_queue:
            order = self.order_queue.popleft()
            return f"Processing order for Student {order['student_id']}: {order['items']}"
        return "No orders in queue"
    
    def get_queue_length(self):
        return len(self.order_queue)

# ============================================
# DEMONSTRATION
# ============================================
if __name__ == "__main__":
    # Test Attendance
    tracker = AttendanceTracker()
    tracker.mark_attendance("S001", "present")
    tracker.mark_attendance("S001", "present")
    tracker.mark_attendance("S001", "absent")
    print(f"S001 Attendance: {tracker.get_attendance_percentage('S001'):.1f}%")
    
    # Test Event Registration
    event = EventRegistration("Tech Fest 2024")
    event.register_student("S001")
    event.register_student("S002")
    print(f"Event Registrations: {event.get_registered_count()}")
    
    # Test Library Borrowing
    library = LibraryBorrow()
    print(library.borrow_book("S001", "Python Guide"))
    
    # Test Bus Scheduling
    bus = BusScheduling()
    bus.schedule_bus("Route A", 2, "B001")
    bus.schedule_bus("Route B", 1, "B002")
    print(f"Next bus: {bus.dispatch_next_bus()}")
    
    # Test Cafeteria Queue
    cafeteria = CafeteriaQueue()
    print(cafeteria.add_order("S001", ["Pizza", "Coke"]))
    print(cafeteria.add_order("S002", ["Burger", "Fries"]))
    print(cafeteria.process_next_order())