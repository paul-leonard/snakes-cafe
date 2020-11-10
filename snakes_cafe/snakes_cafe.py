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

# future stretch task: use this tuple to check and see if item is on menu
# menu_items = ("Wings", Cookies, Spring Rolls, Salmon, Steak, Meat Tornado, A Literal Garden, Ice Cream, Cake, Pie, Coffee, Tea, Unicorn Tears)


while True:
  #request input
  current_order = input('> ')

  #quit if done
  if current_order == "quit":
    break

  #record this order item
  if current_order in order:
    order[current_order] += 1
  else:
    order[current_order] = 1

  #read back this order
  print(f"you want {current_order}")

  #summary of full order
  print("")
  print("""  ***********************************
  **        Your Full Order        **
  ***********************************""")
  for item in order:
    print(f"Qty {order[item]} of {item}")
  print("")