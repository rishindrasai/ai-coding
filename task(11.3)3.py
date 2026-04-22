class TicketStack:
    def __init__(self, max_size=10):
        self.tickets = []
        self.max_size = max_size
    
    def push(self, ticket):
        """Add a ticket to the stack"""
        if self.isFull():
            print("Stack is full! Cannot add more tickets.")
            return False
        self.tickets.append(ticket)
        print(f"Ticket added: {ticket}")
        return True
    
    def pop(self):
        """Remove and return the most recent ticket"""
        if self.isEmpty():
            print("No tickets to resolve.")
            return None
        ticket = self.tickets.pop()
        print(f"Ticket resolved: {ticket}")
        return ticket
    
    def peek(self):
        """View the current ticket without removing it"""
        if self.isEmpty():
            print("No tickets in queue.")
            return None
        return self.tickets[-1]
    
    def isEmpty(self):
        """Check if stack is empty"""
        return len(self.tickets) == 0
    
    def isFull(self):
        """Check if stack is full"""
        return len(self.tickets) >= self.max_size
    
    def size(self):
        """Get current number of tickets"""
        return len(self.tickets)


# Simulate help desk operations
if __name__ == "__main__":
    desk = TicketStack(max_size=10)
    
    # Five tickets being raised
    print("=== Tickets Raised ===")
    desk.push("Ticket #1: Password Reset")
    desk.push("Ticket #2: Network Issue")
    desk.push("Ticket #3: Software Installation")
    desk.push("Ticket #4: Printer Not Working")
    desk.push("Ticket #5: Email Configuration")
    
    # View current ticket
    print(f"\n=== Current Ticket ===")
    print(f"Next to resolve: {desk.peek()}")
    
    # Resolve tickets (LIFO - Last In First Out)
    print(f"\n=== Tickets Resolved ===")
    desk.pop()
    desk.pop()
    desk.pop()
    desk.pop()
    desk.pop()
    
    # Check if stack is empty
    print(f"\n=== Status Check ===")
    print(f"Stack empty: {desk.isEmpty()}")