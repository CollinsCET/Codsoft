def main():
  # Initialize empty to-do list
  tasks = []

  while True:
    print("\nTo-Do List:")
    # Print tasks with numbering
    for i, task in enumerate(tasks):
      print(f"{i+1}. {task}")

    print("\nOptions:")
    print("1. Add Task")
    print("2. Mark Task Done")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      # Add task
      new_task = input("Enter new task: ")
      tasks.append(new_task)
      print("Task added successfully!")
    elif choice == '2':
      # Mark task done
      if not tasks:
        print("No tasks to mark as done!")
        continue
      try:
        index = int(input("Enter the number of the task to mark done: ")) - 1
        if index < 0 or index >= len(tasks):
          print("Invalid task number!")
          continue
        tasks.pop(index)  # Remove task from list
        print("Task marked as done!")
      except ValueError:
        print("Invalid input! Please enter a number.")
    elif choice == '3':
      # Exit
      print("Exiting...")
      break
    else:
      print("Invalid choice!")

if __name__ == "__main__":
  main()

