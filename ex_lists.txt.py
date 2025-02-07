
fruits_vegetables = ["broccoli", "brussel sprouts", "carrots", "bell peppers", "grapes", "peaches", "apples"]
cereal = ["frosted flakes", "granola"]
drinks = ["sprite", "milk","bottled water","root beer", "cream soda","orange fanta", "fruit punch"]

shopping_list = [[fruits_vegetables], [cereal], [drinks]]
user_input = input("what would you like to add to the shopping list:")
shopping_list.append(user_input)
print(shopping_list)
grandmas_order = cereal*3
print(grandmas_order)
remove_item = input("please remove item for the list:")
while True:
    userss_input = input("please remove item from list(or type quit to stop):")
    if userss_input == 'quit':
        break
    shopping_list.remove(userss_input)
    print('current list', shopping_list)




print("updated list:", shopping_list)


























































































