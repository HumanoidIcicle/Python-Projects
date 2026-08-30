
title = input("Enter the title of the list: ")
shop_list = []
#shop_list = ""   List stored as string

while True:
    print("Menu:\n1. Add an item.\n2. Print the current list.\n3. Finished\n")
    choice = input("Choose an option 1, 2, or 3: ")

    if choice == "1":
         item = input("Name of item: ")
         shop_list.append(item)
         #shop_list += (item + "\n")    For when list is a string

    elif choice == "2":
        print("\nCurrent list: ")
        for i in shop_list:
            print(i)

    elif choice == "3":
        print("List completed.\n")
        print(f"{'-' * 20:^20}")
        print(f"{title:^20}")
        print(f"{'-' * 20:^20}")

        for j in shop_list:
            print(j)
        break

    else:
        print("Option not on the menu. Choose again.")

