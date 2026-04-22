'''def merge_sort(arr):
    """
    Sorts a list in ascending order using the Merge Sort algorithm.

    Time Complexity: O(n log n), where n is the number of elements in the list.
    Space Complexity: O(n), due to the use of temporary arrays during merging.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: A new sorted list.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test cases
if __name__ == "__main__":
    test_cases = [
        [],
        [1],
        [5, 2, 9, 1, 5, 6],
        [3, 2, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [7, 7, 7, 7],
    ]

    for idx, case in enumerate(test_cases):
        sorted_case = merge_sort(case)
        print(f"Test case {idx+1}: Input: {case} -> Sorted: {sorted_case}")
'''
'''
"""Write a Python program to implement a Queue using lists.

Requirements:
- Follow FIFO principle
- Include:
  enqueue(item)
  dequeue()
  peek()
  size()

- Handle empty queue cases
- Add comments and test cases"""
class Queue:
    """A Queue implementation using lists following FIFO principle."""
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.pop(0)
    
    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue")
        return self.items[0]
    
    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0


# Test cases
if __name__ == "__main__":
    q = Queue()
    
    # Test enqueue
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(f"Queue size after enqueuing 3 items: {q.size()}")  # Output: 3
    
    # Test peek
    print(f"Front item (peek): {q.peek()}")  # Output: 10
    
    # Test dequeue
    print(f"Dequeued item: {q.dequeue()}")  # Output: 10
    print(f"Queue size after dequeue: {q.size()}")  # Output: 2
    
    # Test with remaining items
    print(f"Next front item: {q.peek()}")  # Output: 20
    
    # Empty the queue
    q.dequeue()
    q.dequeue()
    print(f"Queue empty: {q.is_empty()}")  # Output: True
    
    # Test error handling
    try:
        q.dequeue()
    except IndexError as e:
        print(f"Error caught: {e}")
'''

'''
"""Write a Python program to implement a Singly Linked List.

Requirements:
- Create Node class (data, next)
- Create LinkedList class

Methods:
  insert(data)
  display()

- Add docstrings and comments
- Demonstrate with sample data"""
class Node:
    """A node in the singly linked list."""
    def __init__(self, data):
        """Initialize a node with data and next pointer."""
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list implementation."""
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
    
    def insert(self, data):
        """Insert a new node with data at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        """Print all elements in the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")


# Demonstrate with sample data
if __name__ == "__main__":
    ll = LinkedList()
    
    # Insert sample data
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    ll.insert(20)
    
    # Display the linked list
    print("Linked List:")
    ll.display()
'''
'''
"""Write a Python program to implement a Hash Table using chaining.

Requirements:
- Use list of lists
- Include:
  insert(key, value)
  search(key)
  delete(key)

- Handle collisions using chaining
- Add comments and test cases"""
class HashTable:
    """Hash table implementation using chaining to handle collisions."""
    
    def __init__(self, size=10):
        """Initialize hash table with given size."""
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """Generate hash value for a given key."""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        # Check if key already exists and update it
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Add new key-value pair to the chain
        self.table[index].append((key, value))
    
    def search(self, key):
        """Search for a key and return its value, or None if not found."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        return False
    
    def display(self):
        """Display the hash table."""
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")


# Test cases
if __name__ == "__main__":
    ht = HashTable(5)
    
    # Test insert
    print("--- Testing Insert ---")
    ht.insert("name", "Alice")
    ht.insert("age", 25)
    ht.insert("city", "NYC")
    ht.insert("country", "USA")
    ht.insert("job", "Engineer")
    ht.display()
    
    # Test search
    print("\n--- Testing Search ---")
    print(f"Search 'name': {ht.search('name')}")
    print(f"Search 'age': {ht.search('age')}")
    print(f"Search 'unknown': {ht.search('unknown')}")
    
    # Test delete
    print("\n--- Testing Delete ---")
    ht.delete("age")
    print(f"After deleting 'age': {ht.search('age')}")
    ht.display()
    
    # Test update
    print("\n--- Testing Update ---")
    ht.insert("name", "Bob")
    print(f"Updated 'name': {ht.search('name')}")
'''
'''

"""Write a Python program to implement a Graph using adjacency list.

Requirements:
- Methods:
  add_vertex(vertex)
  add_edge(v1, v2)
  display()

- Use dictionary for adjacency list
- Add comments and example graph"""
class Graph:
    """A simple graph implementation using adjacency list"""
    
    def __init__(self):
        """Initialize an empty graph using a dictionary"""
        self.graph = {}
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, v1, v2):
        """Add an edge between two vertices (undirected)"""
        if v1 not in self.graph:
            self.add_vertex(v1)
        if v2 not in self.graph:
            self.add_vertex(v2)
        
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    
    def display(self):
        """Display the graph adjacency list"""
        print("Graph Adjacency List:")
        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {neighbors}")


# Example usage
if __name__ == "__main__":
    g = Graph()
    
    # Add vertices
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    
    # Add edges
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    
    # Display graph
    g.display()
'''

'''
import heapq

"""For the following hospital system features, choose the best data structure and justify in 2–3 sentences:

1. Patient Check-In System
2. Emergency Case Handling
3. Medical Records Storage
4. Doctor Appointment Scheduling
5. Hospital Room Navigation

Use:
Stack, Queue, Priority Queue, Linked List, BST, Graph, Hash Table, Deque

Write a Python program to implement Emergency Case Handling using a Priority Queue.

Requirements:
- Higher severity → higher priority
- Include:
  add_patient(name, severity)
  treat_patient()

- Use heapq
- Add comments and test cases"""
# Data Structure Choices & Justifications:
# 1. Patient Check-In System → Queue: FIFO order ensures fair processing
# 2. Emergency Case Handling → Priority Queue: Severity-based prioritization for critical patients
# 3. Medical Records Storage → Hash Table: O(1) lookup by patient ID for fast retrieval
# 4. Doctor Appointment Scheduling → BST: Sorted by time enables efficient range queries
# 5. Hospital Room Navigation → Graph: Models hospital layout with rooms as nodes and paths as edges

class EmergencyCaseHandler:
    """Priority Queue implementation for hospital emergency cases"""
    
    def __init__(self):
        self.patients = []  # Min-heap (negate severity for max-heap)
        self.patient_count = 0
    
    def add_patient(self, name, severity):
        """Add patient with severity (1-10, 10=critical)"""
        # Negate severity for max-heap behavior in Python's min-heap
        heapq.heappush(self.patients, (-severity, self.patient_count, name))
        self.patient_count += 1
        print(f"Patient {name} added with severity {severity}")
    
    def treat_patient(self):
        """Remove and treat highest priority patient"""
        if not self.patients:
            print("No patients waiting")
            return None
        
        neg_severity, _, name = heapq.heappop(self.patients)
        severity = -neg_severity
        print(f"Treating {name} (severity: {severity})")
        return name

# Test Cases
if __name__ == "__main__":
    handler = EmergencyCaseHandler()
    
    handler.add_patient("John", 3)
    handler.add_patient("Alice", 9)
    handler.add_patient("Bob", 5)
    handler.add_patient("Carol", 10)
    
    print("\nTreating patients in priority order:")
    handler.treat_patient()  # Carol (10)
    handler.treat_patient()  # Alice (9)
    handler.treat_patient()  # Bob (5)
    handler.treat_patient()  # John (3)
    handler.treat_patient()  # Empty
'''

'''
import heapq
from enum import Enum


"""Choose appropriate data structures and justify:

1. Traffic Signal Queue
2. Emergency Vehicle Priority
3. Vehicle Registration Lookup
4. Road Network Mapping
5. Parking Slot Tracking

Output as table with justification
Write a Python program for Emergency Vehicle Priority using Priority Queue.

Requirements:
- Ambulances highest priority
- Include:
  add_vehicle(type, priority)
  process_vehicle()

- Use heapq"""

class VehicleType(Enum):
    AMBULANCE = 1
    FIRE_TRUCK = 2
    POLICE = 3
    REGULAR = 4

class EmergencyVehicleQueue:
    def __init__(self):
        self.queue = []
        self.vehicle_count = 0
    
    def add_vehicle(self, vehicle_type, priority=None):
        if priority is None:
            priority = vehicle_type.value
        self.vehicle_count += 1
        heapq.heappush(self.queue, (priority, self.vehicle_count, vehicle_type.name))
    
    def process_vehicle(self):
        if not self.queue:
            return None
        priority, count, vehicle_type = heapq.heappop(self.queue)
        return f"Processing {vehicle_type} (Priority: {priority})"

# Data structures justification
data_structures = [
    ["Traffic Signal Queue", "Queue (FIFO)", "Vehicles arrive in order, first come first served"],
    ["Emergency Vehicle Priority", "Priority Queue (Min Heap)", "Process ambulances/fire trucks before regular traffic"],
    ["Vehicle Registration Lookup", "Dictionary/Hash Map", "O(1) lookup by registration number"],
    ["Road Network Mapping", "Graph (Adjacency List)", "Represent intersections and roads efficiently"],
    ["Parking Slot Tracking", "Set/Hash Set", "Quick check for available slots, O(1) operations"]
]

print("\n--- Emergency Vehicle Priority System ---\n")

queue = EmergencyVehicleQueue()
queue.add_vehicle(VehicleType.AMBULANCE, 1)
queue.add_vehicle(VehicleType.REGULAR, 4)
queue.add_vehicle(VehicleType.FIRE_TRUCK, 2)
queue.add_vehicle(VehicleType.POLICE, 3)

while queue.queue:
    print(queue.process_vehicle())

'''

from collections import deque
from datetime import datetime

"""Suggest data structures and justify:

1. Shopping Cart
2. Order Processing
3. Top-Selling Products
4. Product Search
5. Delivery Routes

Output in table format
Write a Python program for Order Processing using Queue.

Requirements:
- FIFO order processing
- Include:
  place_order(order)
  process_order()

- Add comments and test cases"""
# Data Structures Recommendation Table
data_structures = [
    ["Shopping Cart", "List/Dictionary", "Fast add/remove items, easy to modify quantities"],
    ["Order Processing", "Queue (FIFO)", "Ensures orders processed in sequence, fair processing"],
    ["Top-Selling Products", "Heap/Priority Queue", "Quick access to top products by sales count"],
    ["Product Search", "Hash Table/Dictionary", "O(1) lookup time for product by ID or name"],
    ["Delivery Routes", "Graph", "Efficiently represent connections between locations"]
]

'''

# Order Processing using Queue
class OrderQueue:
    """FIFO Order Processing System using Queue"""
    
    def __init__(self):
        self.queue = deque()
        self.order_counter = 0
    
    def place_order(self, order):
        """Add order to queue"""
        self.order_counter += 1
        order_details = {
            'order_id': self.order_counter,
            'items': order,
            'timestamp': datetime.now(),
            'status': 'Pending'
        }
        self.queue.append(order_details)
        print(f"✓ Order #{order_details['order_id']} placed: {order}")
    
    def process_order(self):
        """Process order from front of queue (FIFO)"""
        if not self.queue:
            print("No orders to process!")
            return None
        
        order = self.queue.popleft()
        order['status'] = 'Processed'
        print(f"✓ Order #{order['order_id']} processed: {order['items']}")
        return order
    
    def view_queue(self):
        """Display all pending orders"""
        if not self.queue:
            print("Queue is empty")
        else:
            print(f"Pending orders: {len(self.queue)}")
            for order in self.queue:
                print(f"  - Order #{order['order_id']}: {order['items']}")


# Test Cases
print("TEST CASES - Order Processing System\n")

# Test 1: Basic order placement and processing
print("Test 1: FIFO Order Processing")
processor = OrderQueue()
processor.place_order("Laptop, Mouse")
processor.place_order("Keyboard, Monitor")
processor.place_order("USB Cable, Adapter")
processor.view_queue()
print()

processor.process_order()
processor.process_order()
print()

# Test 2: Process empty queue
print("Test 2: Process from Empty Queue")
processor.process_order()
processor.process_order()
print()

# Test 3: Mixed operations
print("Test 3: Mixed Operations")
processor.place_order("Headphones")
processor.place_order("Speaker")
processor.view_queue()
processor.process_order()
processor.view_queue()
'''