from collections import deque

donation_stack = deque()
donation_queue = deque()
donation_events = []

def donate(amount, donor_name):
    donation_queue.append((amount, donor_name))
    donation_stack.append(('donate', amount, donor_name))
    print(f"Donation of RW{amount} received from {donor_name}.")

def undo_donation():
    if donation_stack:
        action, amount, donor_name = donation_stack.pop()
        if action == 'donate':
            donation_queue.remove((amount, donor_name))
            print(f"Undoing donation: RWF{amount} from {donor_name} has been removed.")

def process_donations():
    while donation_queue:
        amount, donor_name = donation_queue.popleft()
        donation_events.append((amount, donor_name))
        
donate(100, "Eric")
donate(50, "RUNI")
donate(20, "ARTHOUR")
undo_donation()
process_donations()
print(donation_stack)