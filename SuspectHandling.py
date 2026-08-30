import pickle
import os

def display_menu():
	print("""---- Menu ----
1) Add suspect
2) Add accomplice
3) Display all suspects
4) Find potential accomplices
E) Exit""")                

def accomplice(suspect, graph):
	val = [x for x in graph[suspect]]
	a = input("Add accomplice: ")
	val.append(a)
	graph[suspect] = set(val)


def display_all_suspects(graph):
	print("---- All suspects ----")
	for sus in graph:
		print(f"{sus}:")
		for acc in graph[sus]:
			print(f"    {acc}")

def display_suspect(suspect, graph):
	print(f"{suspect}:")
	if suspect in graph:
		for el in graph[suspect]:
			print(f"    {el}")
	else:
		graph[suspect] = set()
		for nm in graph[suspect]:
			print(f"    {nm}")

def find_potential_accomplices(suspect, graph):
	sus_accom = {}
	val = set()
	for known in graph[suspect]:
		if known in graph:
			for possible in graph[known]:
				if possible not in graph[suspect] and possible != suspect:
					val.add(possible)
	
	sus_accom[suspect] = val
	return sus_accom

def display_potential_accomplices(suspect, graph):
	pos = find_potential_accomplices(suspect, graph)
	print()
	print("---- Potential accomplices ----")
	print("Already known accomplices:")
	display_suspect(suspect, graph)
	print()
	print("Potential new accomplices:")
	display_suspect(suspect, pos)

def load_from_file(filename):
	with open(filename, "rb") as f:
		return pickle.load(f)

def save_to_file(graph, filename):
	with open(filename, "wb") as f:
		pickle.dump(graph, f)

def main():
	print("---- Criminals and their accomplices ----")
	filename = input("Enter path to graph file:")

	if os.path.exists(filename):
		graph = load_from_file(filename)
		print("*** Graph loaded from file. ***")
	else:
		graph = {}
		print("*** File not found. Starting with empty graph. ***")
	val = []

	while True:
		print()
		display_menu()
		choice = input("\nEnter a choice:")
		match(choice.upper()):
			case('1'):										#Add a sus
				a = input("Add suspect:")
				if a not in graph:
					graph[a] = set()
				save_to_file(graph, filename)

			case('2'): 										#Add accomplice
				sus = input("Enter suspect:")
				acc = input("Enter accomplice:")
				val = [x for x in graph[sus]]
				val2 = [y for y in graph[acc]]
				val.append(acc)
				val2.append(sus)

				graph[sus] = set(val)
				graph[acc] = set(val2)
				save_to_file(graph, filename)

			case('3'):										#Diplay all sus
				display_all_suspects(graph)
				#save_to_file(graph, filename)
				
			case('4'):										#Find potential acc
				sus = input("Enter suspect's name:")
				display_potential_accomplices(sus, graph)
			
			case('E'):
				print("Exit")
				break
			case _:
				print("Not in options.")
			
if __name__ == '__main__':
	main()

