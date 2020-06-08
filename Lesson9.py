# Program:      Lesson 8
# Section:      CIS122 W1
# Programmer:   Lucas Padgett
# Date:         June 4, 2020
# Purpose:      2 variable lists

# Global Variables
import locale
locale.setlocale( locale.LC_ALL, '')

order_total = 0         
item_count = 0
price = 3.5

def calc_tot(qty):
    return qty * 3.5

################################################################################################################
#list structure
cookie_list = "Savannah Thin-Mints Tag-a-longs Peanut-butter Sandwich".split()

order_list = []

#Banner and main program
print("welcome to the girl scout cookie")
print("ordering program")

cust = input("\nPlease enter your name> ")

#Menu choices

# Asks user to make selection off menu. Input taken from user as string. If user's value is not in accepted choice list, ask again. Return user's choice as string
def disp_menu():

    choice_list = ["a", "d", "m", "q"]

    while True:
        print("\nWhat would you like to do?")
        print("a = add an item")
        print("d = delete an item")
        print("m = display meal so far")
        print("q = quit")
        choice = input("\nmake a selection>")

        if choice in choice_list:
            return choice
        else:
            print("I do not understand that entry. try again.")

def disp_items():
    print("Please choose one of our flavors. Enter the item number to choose:")

    # Will display list of cookie items in format: 1.      Savanaah
    for c in range(len(cookie_list)):
        print("{}.\t{}".format(c+1, cookie_list[c]))

    print()

#add process
def add_process():
    valid_data = False

    while not valid_data:
        disp_items()

        try:
            item = int(input("enter item number>"))

            if 1 <= item <= len(cookie_list):
                valid_data = True

            else:
                print("\nThat was not a valid selection, please try again")

        except Exception as detail:
            print("error: ", detail)

    valid_data = False #boolean flag reset

    while not valid_data: 

        try:
            qty = int(input("enter quantity (between 1-10)>"))

            if 1 <= qty <= 10:
                valid_data = True
            else:
                print("\nThat was not a valid quantity, please try again")

        except Exception as detail:
            print("error: ", detail)
            print("please try again")

    item_total = calc_tot(qty)
    fmt_total = locale.currency(item_total, grouping=True)

    print("\nYou choose: {} boxes of {} for a total of {}".format(
                                                                    qty,
                                                                    cookie_list[item-1],
                                                                    fmt_total)
                                                                )

    print()
                                                            
    valid_data = False

    while not valid_data:
        incl = input("would you like to add this to your order? (y/n)>")
        print()
        if incl.lower() == "y":

            inx = item - 1

            order_list.append([inx, qty])

            valid_data = True
            print("{} was added to your order".format(cookie_list[inx]))

        elif incl.lower() == "n":
            print("{} was not added to your order".format(cookie_list[inx]))
            valid_data = True

        else:
            print("that was not a valid response, please try again")

##delete process##
def del_item():
    if len(order_list) == 0:
        print("\n**you have no items in your order to delete**\n")
    else:
        print("\nDelete an Item")
        disp_order()

        valid_data = False
        while not valid_data:
            try:
                choice = int(input("Please enter the item number you would like to delete>"))
                if 1<= choice <= len(order_list):

                    choice = choice - 1

                    print("\nItem {}. {} with {} boxes will be deleted".format(choice + 1, order_list[choice][0], order_list[choice][1]))

                    del order_list[choice]
                    valid_data = True

            except Exception as detail:
                print("error: ", detail)
                print("please try again")

def disp_order():
    print("Here is your order so far:\n")
    for i in range(len(order_list)):
        print("Order number {}, {} with {} boxes.".format(i + 1, cookie_list[order_list[i][0]], order_list[i][1]))

while True:

    choice = disp_menu()

    if choice == "a":
        add_process()
    elif choice == "d":
        del_item()
    elif choice == "m":
        disp_order()
    elif choice == "q":
        break

    disp_order()

disp_order()
print("Thank you for your order")