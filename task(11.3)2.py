import heapq
from collections import deque
from enum import Enum

class UserType(Enum):
    STUDENT = 2
    FACULTY = 1

class BookRequest:
    def __init__(self, request_id, user_type, book_title, user_name):
        self.request_id = request_id
        self.user_type = user_type
        self.book_title = book_title
        self.user_name = user_name
    
    def __lt__(self, other):
        # For priority queue: lower priority value = higher priority
        if self.user_type.value != other.user_type.value:
            return self.user_type.value < other.user_type.value
        return self.request_id < other.request_id
    
    def __repr__(self):
        return f"Request(ID:{self.request_id}, {self.user_type.name}, '{self.book_title}', {self.user_name})"

class LibraryBookRequestSystem:
    def __init__(self):
        self.priority_queue = []
        self.request_counter = 0
    
    def enqueue(self, user_type, book_title, user_name):
        """Add a book request to the priority queue"""
        self.request_counter += 1
        request = BookRequest(self.request_counter, user_type, book_title, user_name)
        heapq.heappush(self.priority_queue, request)
        print(f"✓ Enqueued: {request}")
        return request
    
    def dequeue(self):
        """Remove and return the highest priority book request"""
        if not self.priority_queue:
            print("✗ Queue is empty!")
            return None
        request = heapq.heappop(self.priority_queue)
        print(f"✓ Dequeued: {request}")
        return request
    
    def display_queue(self):
        """Display all pending requests"""
        if not self.priority_queue:
            print("Queue is empty!")
            return
        print("\n--- Pending Requests (in priority order) ---")
        for req in sorted(self.priority_queue):
            print(f"  {req}")
        print()

# Test the system
if __name__ == "__main__":
    system = LibraryBookRequestSystem()
    
    print("=== Library Book Request System ===\n")
    
    # Enqueue mixed requests
    print("--- Enqueueing Requests ---")
    system.enqueue(UserType.STUDENT, "Python Guide", "Alice")
    system.enqueue(UserType.FACULTY, "Advanced AI", "Dr. Smith")
    system.enqueue(UserType.STUDENT, "Data Science", "Bob")
    system.enqueue(UserType.FACULTY, "Quantum Computing", "Dr. Johnson")
    system.enqueue(UserType.STUDENT, "Web Development", "Carol")
    
    system.display_queue()
    
    # Dequeue requests (should prioritize faculty)
    print("--- Processing Requests (FIFO within priority) ---")
    system.dequeue()
    system.dequeue()
    system.dequeue()
    system.dequeue()
    system.dequeue()