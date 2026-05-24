Queue=[]


def enqueue(element):
    if len(Queue)>5:
        print("Queue is full. Cannot add more elements. Condition: OVERFLOW")
    else:
        Queue.append(element)
        print(f"{element} has been added to the Queue")

def is_empty():
    return len(Queue)==0

def dequeue():
    if is_empty():
        print("Queue is empty. Cannot remove an element. Condition UNDERFLOW")
    else:
        element=Queue.pop(0)
        print(f"{element} has been removed from the Queue")

def size():
    print(f"The size of the Queue is:{len(Queue)}")

def seek():
    if is_empty():
        print("Queue is empty. Cannot seek an element. Condition: UNDERFLOW")
    else:
        print(f"The front element of the Queue is:{Queue[0]}")
