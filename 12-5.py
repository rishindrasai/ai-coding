'''
def merge_sort(arr):
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
''''

def binary_search(arr, target):
    """
    Performs binary search to find the index of 'target' in a sorted list 'arr'.

    Args:
        arr (list): Sorted list of elements.
        target: Element to search for.

    Returns:
        int: Index of 'target' if found, else -1.

    Complexity:
        Best-case: O(1)   - Target is at the middle.
        Average-case: O(log n)
        Worst-case: O(log n)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test cases
if __name__ == "__main__":
    arr1 = [1, 3, 5, 7, 9, 11]
    arr2 = [2, 4, 6, 8, 10]
    arr3 = []
    arr4 = [5]

    print(binary_search(arr1, 7))    # Output: 3
    print(binary_search(arr1, 1))    # Output: 0
    print(binary_search(arr1, 11))   # Output: 5
    print(binary_search(arr1, 12))   # Output: -1
    print(binary_search(arr2, 6))    # Output: 2
    print(binary_search(arr3, 1))    # Output: -1
    print(binary_search(arr4, 5))    # Output: 0
    print(binary_search(arr4, 2))    # Output: -1
'''

'''
from typing import List, Dict, Any
import bisect

# AI Recommendation:
# For searching by appointment ID, Binary Search is suitable if the data is sorted by ID; otherwise, Linear Search.
# For sorting, use Python's built-in sort (Timsort), which is efficient for both time and consultation fee.

# Justification:
# - Binary Search: O(log n) time, fast for sorted lists.
# - Linear Search: O(n) time, simple for unsorted lists.
# - Timsort: O(n log n) time, stable and efficient for real-world data.


class AppointmentManager:
    def __init__(self, appointments: List[Dict[str, Any]]):
        self.appointments = appointments

    def linear_search_by_id(self, appointment_id: str) -> Dict[str, Any]:
        for appt in self.appointments:
            if appt['appointment_id'] == appointment_id:
                return appt
        return None

    def binary_search_by_id(self, appointment_id: str) -> Dict[str, Any]:
        # Assumes appointments are sorted by appointment_id
        ids = [appt['appointment_id'] for appt in self.appointments]
        idx = bisect.bisect_left(ids, appointment_id)
        if idx < len(ids) and ids[idx] == appointment_id:
            return self.appointments[idx]
        return None

    def sort_by_time(self):
        self.appointments.sort(key=lambda x: x['appointment_time'])

    def sort_by_fee(self):
        self.appointments.sort(key=lambda x: x['consultation_fee'])

# Example usage:
if __name__ == "__main__":
    appointments = [
        {'appointment_id': 'A101', 'patient_name': 'John', 'doctor_name': 'Dr. Smith', 'appointment_time': '2024-06-12 10:00', 'consultation_fee': 500},
        {'appointment_id': 'A102', 'patient_name': 'Alice', 'doctor_name': 'Dr. Jones', 'appointment_time': '2024-06-12 09:00', 'consultation_fee': 300},
        {'appointment_id': 'A103', 'patient_name': 'Bob', 'doctor_name': 'Dr. Lee', 'appointment_time': '2024-06-12 11:00', 'consultation_fee': 400},
    ]

    manager = AppointmentManager(appointments)

    # Linear search (unsorted)
    print("Linear Search:", manager.linear_search_by_id('A102'))

    # Sort by appointment_id for binary search
    manager.appointments.sort(key=lambda x: x['appointment_id'])
    print("Binary Search:", manager.binary_search_by_id('A103'))

    # Sort by time
    manager.sort_by_time()
    print("Sorted by Time:", manager.appointments)

    # Sort by fee
    manager.sort_by_fee()
    print("Sorted by Fee:", manager.appointments)
'''
''''

from datetime import datetime

class Booking:
    def __init__(self, ticket_id, passenger_name, train_number, seat_number, travel_date):
        self.ticket_id = ticket_id
        self.passenger_name = passenger_name
        self.train_number = train_number
        self.seat_number = seat_number
        self.travel_date = datetime.strptime(travel_date, "%Y-%m-%d")

    def __repr__(self):
        return (f"Booking(ticket_id={self.ticket_id}, passenger_name={self.passenger_name}, "
                f"train_number={self.train_number}, seat_number={self.seat_number}, "
                f"travel_date={self.travel_date.strftime('%Y-%m-%d')})")

class RailwayReservationSystem:
    def __init__(self):
        self.bookings = []
        self.ticket_index = {}

    def add_booking(self, booking):
        self.bookings.append(booking)
        self.ticket_index[booking.ticket_id] = booking

    # Efficient search: Hash table (dictionary) lookup for ticket ID (O(1) time)
    def search_ticket(self, ticket_id):
        return self.ticket_index.get(ticket_id, None)

    # Efficient sort: Python's built-in sort (Timsort, O(n log n)), stable and fast
    def sort_bookings_by_date(self):
        self.bookings.sort(key=lambda b: b.travel_date)

    def sort_bookings_by_seat(self):
        self.bookings.sort(key=lambda b: b.seat_number)

# Example usage
if __name__ == "__main__":
    system = RailwayReservationSystem()
    system.add_booking(Booking("T001", "Alice", "12345", 12, "2024-07-01"))
    system.add_booking(Booking("T002", "Bob", "12345", 5, "2024-06-30"))
    system.add_booking(Booking("T003", "Charlie", "54321", 8, "2024-07-02"))

    # Search
    print("Search T002:", system.search_ticket("T002"))

    # Sort by date
    system.sort_bookings_by_date()
    print("Sorted by date:", system.bookings)

    # Sort by seat number
    system.sort_bookings_by_seat()
    print("Sorted by seat:", system.bookings)
'''

'''

from datetime import datetime
from typing import List, Dict, Optional

# Data structure for allocation details
class Allocation:
    def __init__(self, student_id: str, room_number: int, floor: int, allocation_date: str):
        self.student_id = student_id
        self.room_number = room_number
        self.floor = floor
        self.allocation_date = datetime.strptime(allocation_date, "%Y-%m-%d")

    def __repr__(self):
        return (f"Allocation(student_id={self.student_id}, room_number={self.room_number}, "
                f"floor={self.floor}, allocation_date={self.allocation_date.date()})")

# Optimized search: Use a dictionary for O(1) lookup by student_id
class HostelManagementSystem:
    def __init__(self):
        self.allocations: List[Allocation] = []
        self.student_index: Dict[str, Allocation] = {}

    def add_allocation(self, allocation: Allocation):
        self.allocations.append(allocation)
        self.student_index[allocation.student_id] = allocation

    def search_by_student_id(self, student_id: str) -> Optional[Allocation]:
        return self.student_index.get(student_id)

    # Optimized sort: Use Python's built-in Timsort (sorted()), which is stable and efficient
    def sort_by_room_number(self) -> List[Allocation]:
        return sorted(self.allocations, key=lambda x: x.room_number)

    def sort_by_allocation_date(self) -> List[Allocation]:
        return sorted(self.allocations, key=lambda x: x.allocation_date)

# Justification:
# - Dictionary indexing allows O(1) search for student_id.
# - Python's sorted() uses Timsort, which is O(n log n) and stable, ideal for sorting records.

# Example usage
if __name__ == "__main__":
    hms = HostelManagementSystem()
    hms.add_allocation(Allocation("S001", 101, 1, "2024-06-01"))
    hms.add_allocation(Allocation("S002", 102, 1, "2024-06-03"))
    hms.add_allocation(Allocation("S003", 201, 2, "2024-06-02"))

    print("Search by student ID S002:", hms.search_by_student_id("S002"))
    print("Sorted by room number:", hms.sort_by_room_number())
    print("Sorted by allocation date:", hms.sort_by_allocation_date())
'''