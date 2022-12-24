"""
Task 1
class Pizza:
    def __init__(self, order_full, ordered_pizza_number, main_ingredient=None, dough_type=None, souse_type=None):
        self.order_full = order_full
        self.ordered_pizza_number = ordered_pizza_number
        self.main_ingredient = main_ingredient
        self.dough_type = dough_type
        self.souse_type = souse_type

    def pizza_cooking(self):
        for i in self.order_full.keys():
            if i == "Pepperoni":
                self.main_ingredient = "Sousage"
                self.dough_type = "Dough"
                self.souse_type = "Cheese souse"
            elif i == "BBQ":
                self.main_ingredient = "BBQ"
                self.dough_type = "Dough"
                self.souse_type = "Cheese souse"
            elif i == "Seafood":
                self.main_ingredient = "Seafood"
                self.dough_type = "Dough"
                self.souse_type = "Cheese souse"
            for j in range(self.ordered_pizza_number[i]):
                print("Starting cooking...", i)
                print("Added main ingredient:", self.main_ingredient)
                print("Added dough:", self.dough_type)
                print("Added souse:", self.souse_type)
                print(f"Pizza {i} has been cooked!")
                print()
        return None


class Order(Pizza):
    def __init__(self, order_full, ordered_pizza_number):
        self.order_full = order_full
        self.ordered_pizza_number = ordered_pizza_number

    def order_output(self):
        print("Therefore, your final order:")
        with open(r"C:\Users\Игорь\Desktop\ORDER.txt", "r", encoding="utf+8") as order_file:
            order_file_text = order_file.readlines()
            for i in order_file_text:
                print(i.strip())

        final_cost = 0
        for i in self.order_full.keys():
            final_cost += self.order_full[i] * self.ordered_pizza_number[i]

        return final_cost

    def order_writing_in_base(self):
        order_file = open(r"C:\Users\Игорь\Desktop\ORDER.txt", "w+", encoding="utf+8")
        order_file.close()
        order_file = open(r"C:\Users\Игорь\Desktop\ORDER.txt", "a+", encoding="utf+8")
        for i in self.order_full.keys():
            order_line = f"Pizza {i} | Cost: {self.order_full[i]}, | Amount: {self.ordered_pizza_number[i]}"
            order_file.write(order_line + "\n")


class Terminal:
    def __init__(self, order_details=None):
        if order_details is None:
            order_details = {}
        self.order_details = order_details

    def menu_output(self):
        with open(r"C:\Users\Игорь\Desktop\MENU.txt", "r", encoding="utf+8") as menu_file:
            menu_text = menu_file.readlines()
            for i in menu_text:
                print(i.strip())
        return None

    def order_applying(self):
        orders_counter = 0
        pepperoni_counter = 0
        bbq_counter = 0
        seafood_counter = 0
        while True:
            ordered_pizza_number = {'Pepperoni': 0, 'BBQ': 0, 'Seafood': 0}
            choice = 0
            if orders_counter == 0:
                choice = int(input("Which one would you like to order? (1-3 or press 0 to finish): "))
            elif orders_counter > 0:
                choice = int(input("Would you like to another one? (1-3 or press 0 to finish): "))

            if choice == 1:
                pepperoni_counter += 1
                self.order_details["Pepperoni"] = 3990
            elif choice == 2:
                bbq_counter += 1
                self.order_details["BBQ"] = 3500
            elif choice == 3:
                seafood_counter += 1
                self.order_details["Seafood"] = 4100
            elif choice == 0:
                break

            orders_counter += 1

        ordered_pizza_number["Pepperoni"] = pepperoni_counter
        ordered_pizza_number["BBQ"] = bbq_counter
        ordered_pizza_number["Seafood"] = seafood_counter

        return self.order_details, ordered_pizza_number

    def order_confirmation(self):
        decision = int(input("Would you like to confirm your order? (Yes - 1, No - 0): "))
        while True:
            if decision == 1:
                print("Order confirmed!")
                return 1
            elif decision == 0:
                print("Order canceled!")
                return 0
            else:
                print("Wrong command, try again")
                break

    def payment(self):
        payment_decision = int(input("Please, hold your card to pay (Pay - 1, Cancel - 0): "))
        while True:
            if payment_decision == 0:
                print("Payment canceled!")
                return 0
            elif payment_decision == 1:
                print("Payed successfully!")
                return 1
            else:
                print("Wrong command. Try again.")


print("-------------------------------------------------------------")
customer_1 = Terminal()
print("-------------------------------------------------------------")

# Menu output
print("-------------------------------------------------------------")
customer_1.menu_output()
print("-------------------------------------------------------------")

# Order applying
print("-------------------------------------------------------------")
order_details = customer_1.order_applying()
order = Order(order_details[0], order_details[1])
print("-------------------------------------------------------------")

# Order writing in base
print("-------------------------------------------------------------")
order.order_writing_in_base()
print("-------------------------------------------------------------")

# Order output
print("-------------------------------------------------------------")
print("Final cost is:", order.order_output(), "KZT")
print("-------------------------------------------------------------")

# Order confirmation
print("-------------------------------------------------------------")
confirmation = customer_1.order_confirmation()
print("-------------------------------------------------------------")

# Payment test
print("-------------------------------------------------------------")
if confirmation == 1:
    payment_status = customer_1.payment()
    # Pizza cooking
    if payment_status == 1:
        print("-------------------------------------------------------------")
        order.pizza_cooking()
        print("-------------------------------------------------------------")
    elif payment_status == 0:
        print("See you next time!")
elif confirmation == 0:
    print("See you next time!")
print("-------------------------------------------------------------")


Task 2

import random

print("Welcome to the \"Scissors, rock and paper\" game!")
name = input("What's your name?: ")


def player_turn(player_name, players_choices, possible_turns):
    for i in range(len(possible_turns)):
        print(possible_turns[i], f" - {i}", end="")
        if i != len(possible_turns) - 1:
            print(",", end=" ")

    print()
    turn_choice = int(input(player_name + ", this is your turn (choose one of the options above): "))
    players_choices.append(possible_turns[turn_choice])
    print("You've chosen:", players_choices[0])


def computer_turn(players_choices, possible_turns):
    turn_choice = random.randint(0, 2)
    players_choices.append(possible_turns[turn_choice])
    print("Computer's choice:", players_choices[1])


def win_check(player_choices):
    # Rock and Paper
    if player_choices[0] == "Rock" and player_choices[1] == "Paper":
        return 0
    if player_choices[0] == "Paper" and player_choices[1] == "Rock":
        return 1

    # Scissors and Rock
    if player_choices[0] == "Scissors" and player_choices[1] == "Rock":
        return 0
    if player_choices[0] == "Rock" and player_choices[1] == "Scissors":
        return 1

    # Scissors and Paper
    if player_choices[0] == "Paper" and player_choices[1] == "Scissors":
        return 0
    if player_choices[0] == "Scissors" and player_choices[1] == "Paper":
        return 1

    # Draw
    if player_choices[0] == player_choices[1]:
        return 2


stop_game = True
while stop_game:
    player_win_counter = 0
    computer_win_counter = 0
    while (player_win_counter < 3) and (computer_win_counter < 3):
        possible_turns = ["Scissors", "Rock", "Paper"]
        players_choices = []

        # Your turn
        player_turn(name, players_choices, possible_turns)

        # Computer's turn
        computer_turn(players_choices, possible_turns)

        # Check who has won the round
        round_result = win_check(players_choices)
        if round_result == 0:
            computer_win_counter += 1
            print("Computer has won this round!")
            print("It's scores:", computer_win_counter)
        elif round_result == 1:
            player_win_counter += 1
            print("You've won this round!")
            print("Your scores:", player_win_counter)
        elif round_result == 2:
            print("Draw!")
        else:
            print("Something went wrong...")

    if computer_win_counter == 3:
        print("Computer has won this game!")
    elif player_win_counter == 3:
        print("You've won this game!")

    decision_to_continue_or_not = input("Would you like to continue playing? (Yes or No): ")
    if decision_to_continue_or_not == "No":
        stop_game = False
    elif decision_to_continue_or_not == "Yes":
        print("Okay, let's play one more time!")
        print("-------------------------------------------")
    else:
        print("Wrong command. Try again.")
"""