def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    #badge_messages = []
    #for name in names:
       # badge_messages.append(f"Hello, my name is {name}.")
    #return badge_messages
    badge_messages = [f"Hello, my name is {name}." for name in names]
    return badge_messages

def assign_rooms(names):
    room_assignments = []
    for index, name in enumerate(names, start=1):
        room_assignment_message = f"Hello, {name}! You'll be assigned to room {index}!"
        room_assignments.append(room_assignment_message)
    return room_assignments    

def printer(names):
    badge_messages = batch_badge_creator(names)
    for message in badge_messages:
        print(message)
    room_assignments = assign_rooms(names)   
    for assignment in room_assignments:
        print(assignment) 
