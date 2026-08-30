def print_menu():
	print("""\n--------- Menu ----------
a) Add a new test subject
s) Show all information
r) Read from file
w) Write to file
q) Quit
-------------------------""")	

def new_test_subject():
	print(f"\n{'---- New Test Subject ----':^20}")
	number = input(f"Number:")
	time = int(input("Time:"))
	return (number, time)						#Returns subjects in tuple 

def write_data(test_subjects, filename):
	with open(filename, "w") as f: 				#used "with open as" function so as not to need
		for tup in test_subjects:				#explicitly close the files when done using them
			f.write(f"{tup[0]}\n")				#assigns first value in tuple to Number position
			f.write(f"{tup[1]}\n")				#assigns 2nd value in tuple to Time position

def read_data(filename):						
	test_subjects = []							#Empty list for the tuples to be appended to
	with open(filename, "r") as f: 				#Open file for read
		print("\n*** Data read from file ***")
		for first in f:							#For-loop to go through every line in the file
			second = f.readline()				#secondond to read the next line
			first = first.rstrip()
			second = int(second)
			tup = (first, second)				#add the read lines to a tuple and 
			test_subjects.append(tup)			#append it to the list, rinse/repeat
	return test_subjects

def print_test_subjects(test_subjects):
	print("\n---- Registered test subjects ----")
	for tup in test_subjects:
		print(f"{'Number':<7}:{tup[0]:>5}")
		print(f"{'Time':<7}:{tup[1]:>5}\n")

def main():
	test_subjects = []
	while True:											
		print_menu()
		choice =  input("Your choice:")
		match(choice):
			case('a'):
				test_subjects.append(new_test_subject())
				
			case('s'):
				print_test_subjects(test_subjects)

			case('r'):
				filename = input("\nFilename:")
				try:
					test_subjects = read_data(filename)
				except IOError:
					print("\nError. There was a problem reading the file.\n")

			case('w'):
				filename = input("Filename:")
				write_data(test_subjects, filename)
				print("\n*** Data written to file ***\n")
				
			case('q'):
				break							#Only time to break the loop is when q is entered
			case _:
				print("\nError: Choose from options.\n")

if __name__ == '__main__':
	main()
