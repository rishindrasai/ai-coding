# Contact Manager using Array and Linked List

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __repr__(self):
        return f"Contact({self.name}, {self.phone}, {self.email})"


class Node:
    def __init__(self, contact):
        self.contact = contact
        self.next = None


class ArrayContactManager:
    def __init__(self):
        self.contacts = []
    
    def add(self, contact):
        self.contacts.append(contact)
    
    def search(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
    
    def delete(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts.pop(i)
                return True
        return False
    
    def display(self):
        return self.contacts


class LinkedListContactManager:
    def __init__(self):
        self.head = None
    
    def add(self, contact):
        new_node = Node(contact)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def search(self, name):
        current = self.head
        while current:
            if current.contact.name == name:
                return current.contact
            current = current.next
        return None
    
    def delete(self, name):
        if not self.head:
            return False
        
        if self.head.contact.name == name:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next:
            if current.next.contact.name == name:
                current.next = current.next.next
                return True
            current = current.next
        return False
    
    def display(self):
        contacts = []
        current = self.head
        while current:
            contacts.append(current.contact)
            current = current.next
        return contacts


if __name__ == "__main__":
    # Test Array Implementation
    print("=== Array Contact Manager ===")
    array_mgr = ArrayContactManager()
    array_mgr.add(Contact("Alice", "123-4567", "alice@email.com"))
    array_mgr.add(Contact("Bob", "234-5678", "bob@email.com"))
    print("Search Bob:", array_mgr.search("Bob"))
    array_mgr.delete("Alice")
    print("After delete:", array_mgr.display())
    
    # Test Linked List Implementation
    print("\n=== Linked List Contact Manager ===")
    ll_mgr = LinkedListContactManager()
    ll_mgr.add(Contact("Alice", "123-4567", "alice@email.com"))
    ll_mgr.add(Contact("Bob", "234-5678", "bob@email.com"))
    print("Search Bob:", ll_mgr.search("Bob"))
    ll_mgr.delete("Alice")
    print("After delete:", ll_mgr.display())
    
    # Efficiency Comparison
    print("\n=== Efficiency Analysis ===")
    print("Array: Insert O(1), Search O(n), Delete O(n)")
    print("Linked List: Insert O(n), Search O(n), Delete O(n)")