# To do List
import os

print('To do List')
tasks = []

filename = 'tasks.txt'
if os.path.exists(filename):
	with open (filename, 'r') as file:
		file_lines = file.readlines()
		for line in file_lines:
			clean_task = line.strip()
			tasks.append(clean_task)

while True:
	print('''
	1. Add Task
	2. Check Tasks
	3. Remove Tasks
	4. Close Program
	''')
	
	choice = int(input('enter the option number:\n'))
	
	if choice == 1:
		new_task = input('Enter a new task:')
		tasks.append(new_task)
		print(f'Task: {new_task}, added successfully!')
		
		with open (filename, 'w') as file:
			for task in tasks:
				file.write(f'{task}\n')
		
	elif choice == 2:
		print('Your Tasks:')
		if not tasks:
			print('No tasks available, try adding one first!')
		else:
			for number, item in enumerate(tasks, start = 1):
				print(f'{number}. {item}')
				
	elif choice == 3:
		print('Your Tasks:')
		if not tasks:
			print('No tasks available, try adding one first!')
		else:
			for number, item in enumerate(tasks, start = 1):
				print(f'{number}. {item}')
				
			num_remover_str = input("Digite o número da tarefa que deseja remover: ")
			if num_remover_str.isdigit():
			    num_remover = int(num_remover_str)
			    if 0 < num_remover <= len(tasks):
			    	task_index = num_remover - 1
			    	task_removed = tasks.pop(task_index)
			    	with open(filename, 'w') as file:
			     	   	for task in tasks:
			          	  	file.write(f"{task}\n")
			    	print(f"Task '{task_removed}' was removed, file saved!.")
			    else:
			        print("Invalid number, no task removed.")
			else:
				print('Invalid option, try a valid number!')
            	
	elif choice == 4:
		print('Closing program, until next time!')
		break
	else:
		print('Invalid option, try a valid option!')