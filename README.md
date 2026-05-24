# python-queue-workflow

# ⏳ Python Queue Workflow Implementation

A lightweight, clean console demonstration of a bounded **Queue** data structure implemented using pure Python. This project highlights foundational data handling built around the **FIFO (First In, First Out)** structural principle.

---

## ⚙️ Core Operations Implemented
* **`enqueue(element)`**: Inserts a new data item at the back of the queue. Includes safety validation to check against a fixed maximum capacity limit to handle structural **Overflow** conditions.
* **`dequeue()`**: Extracts and removes the oldest item from the front of the queue (`Queue.pop(0)`). Includes safety validation to prevent structural **Underflow** conditions.
* **`is_empty()`**: A modular helper function that returns a boolean state evaluating whether the queue is currently empty.
* **`seek()`**: Inspects the current front-most element of the queue (`Queue[0]`) without removing it from the line, backed by defensive validation checks.
* **`size()`**: Dynamically calculates and displays the exact integer count of the items currently waiting in the queue.

---

## 🧠 CS Concepts & Logic Applied
* **FIFO Architecture**: Ensures that the first element added to the sequence is always the first one to be extracted—the core logic driving printer queues, network packet routing, and message streaming pipelines.
* **Bounded Capacity & Edge Guarding**: Features a maximum size ceiling check (`len(Queue) > 5`) alongside empty sequence checks to safely handle both stack-overflow and underflow boundaries before execution.

---

## 🚀 How to Run

1. Make sure you have Python installed, then clone or copy this script.
2. Open your terminal, navigate to the project directory, and start an interactive Python shell:
   ```bash
   python -i Queue.py
