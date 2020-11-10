print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************""")

order = {}

#use this tuple to check and see if item is on menu
menu_items = ("Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado", "A Literal Garden", "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears")


while True:
  #request input
  current_order = input('> ')

  #quit if done
  if current_order == "quit":
    break

  #these three lines restrict ordering to menu items. Comment them out for open kitchen.
  if current_order not in menu_items:
    print(f"\nSorry, we do not serve {current_order} here.\n")
    continue

  #record this order item
  if current_order in order:
    order[current_order] += 1
  else:
    order[current_order] = 1

  #read back this order
  if order[current_order] > 1:
    print(f"\n** {order[current_order]} orders of {current_order} have been added to your meal **\n")
  else:
    print(f"\n** {order[current_order]} order of {current_order} have been added to your meal **\n")

  #summary of full order
  print("""  ***********************************
  **        Your Full Order        **
  ***********************************""")
  for item in order:
    print(f"      Qty {order[item]} of {item}")
  print("")