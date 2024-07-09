#Task 1: Write a function that lets the user add items to a list
item_list = []

def add_items_to_list():

    while True:
        item = input("Enter an item to add to the list (or type 'done' to finish): ")
        if item.lower() == 'done':
            break
        item_list.append(item)
    return item_list

add_items_to_list()

#Task 2: Include a function to remove items from the list.

def remove_items_from_list(item_list):
 
    while True:
        item = input("What item would you like removed? (or type 'done' to finish): ")
        if item.lower() == 'done':
            break
        if item in item_list:
            item_list.remove(item)
        else:
            print(f"Item '{item}' not in list.")
    return item_list

remove_items_from_list(item_list)

#Task 3: Add a function that prints out the entire list in a formatted way.
def print_list(item_list):
    if not item_list:
        print("the list is empty. ")
    else:
        print("current list of items: ")
        for index, item in enumerate(item_list, start=1):
            print(f"{index}. {item}")

print_list(item_list)