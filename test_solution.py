# space_travel_game.py

credits = 100  # Global variable for the player's credits

def purchase_item(cost):
    """
    Deduct 'cost' from global credits if there are enough credits.
    Return True if successful, otherwise False.
    """
    global credits
    if credits >= cost:
        credits -= cost
        return True
    else:
        return False

def solve_riddle():
    """
    Puzzle #1: A modulo-based math riddle.
    (57 % 6) * 2 -> (57 divided by 6 leaves remainder 3) * 2 = 6
    Returns True if the user guesses 6, otherwise False.
    """
    print("\nPuzzle #1: To unlock the door, solve this riddle:")
    print("A code is hidden in this expression: (57 % 6) * 2")
    print("Hint: 57 % 6 = 3, then multiplied by 2 equals ?")

    user_answer = input("What is your answer? ")
    user_answer = int(user_answer)  # Convert input string to integer

    if user_answer == 6:
        return True
    else:
        return False

def solve_logic_puzzle():
    """
    Puzzle #2: Tests logical operators.
    X = True, Y = False
    Expression: (X and not Y) or (Y and not X)
    Evaluate:
      X and not Y -> True and not False -> True
      Y and not X -> False and not True -> False
    So overall expression -> True or False -> True

    Returns True if the user enters 'true', otherwise False.
    """
    print("\nPuzzle #2: Logic Operators Challenge!")
    print("Given X = True and Y = False, evaluate this expression:")
    print("(X and not Y) or (Y and not X)")
    print("Type 'True' or 'False' as your answer.")

    user_answer = input("Your answer: ").lower()

    if user_answer == "true":
        return True
    else:
        return False

def check_fuel_choice(fuel_amount):
    """
    Check if the chosen fuel amount is valid:
    - If fuel_amount < 0 -> 'impossible'
    - If fuel_amount > 100 -> 'risky'
    - Otherwise -> 'safe'
    """
    if fuel_amount < 0:
        return "impossible"
    elif fuel_amount > 100:
        return "risky"
    else:
        return "safe"

def main():
    global credits

    print("Welcome, Space Traveler!")
    user_name = input("What is your name, adventurer? ")

    print(f"\nGreetings, {user_name}!")
    print(f"You start with {credits} credits. Spend them wisely.")

    # --- Station Choice ---
    print("\nYou approach a space station. You can either buy fuel or buy food.")
    choice = input("Type 'fuel' or 'food': ").lower()

    if choice == "fuel":
        fuel_input = input("How many units of fuel would you like to buy? ")
        fuel_input = int(fuel_input)

        fuel_safety = check_fuel_choice(fuel_input)
        if fuel_safety == "impossible":
            print("You can't buy negative fuel!")
        elif fuel_safety == "risky":
            print("That's a lot of fuel, but let's see if you can afford it...")
        else:
            print("That seems like a safe choice.")

        # Each unit of fuel costs 2 credits
        total_cost = fuel_input * 2
        if purchase_item(total_cost):
            print(f"You bought {fuel_input} units of fuel for {total_cost} credits.")
        else:
            print("You don't have enough credits for that much fuel.")

    elif choice == "food":
        food_cost = 30
        print(f"Buying food costs {food_cost} credits.")
        if purchase_item(food_cost):
            print("You have purchased a food supply.")
        else:
            print("Not enough credits to buy food.")

    else:
        print("You decided not to buy anything at this station.")

    # --- Puzzle #1 (Mod Riddle) ---
    print("\nA locked door blocks your path to the next sector.")
    first_puzzle_result = solve_riddle()
    if first_puzzle_result:
        print("Door unlocked! You proceed forward into the next sector.")
    else:
        print("Wrong answer! An alarm sounds, and the normal route is blocked!")
        print("However, you notice a hidden corridor leading to an alternate path...")
        print("You must solve another puzzle to bypass security on this hidden path.")
        second_puzzle_result = solve_logic_puzzle()
        if second_puzzle_result:
            print("You successfully bypassed the security with your logic skills!")
        else:
            print("Your logic puzzle attempt fails, and guards catch you. Game Over!")
            return

    # --- Final Decision (Gate A or Gate B) ---
    print("\nYou reach a final checkpoint with two gates:")
    print("Gate A: Costs 20 credits to open.")
    print("Gate B: Costs 50 credits to open but comes with bonus fuel.")

    gate_choice = input("Which gate do you choose? (A/B): ").upper()

    if gate_choice == "A":
        if credits >= 20:
            purchase_item(20)
            print("You open Gate A and continue on your journey. Success!")
        else:
            print("You don't have enough credits for Gate A. Stuck!")
    elif gate_choice == "B":
        if credits >= 50:
            purchase_item(50)
            print("You open Gate B, and you receive bonus fuel. Success!")
        else:
            print("You can't afford Gate B. Stuck!")
    else:
        print("You chose neither gate. The journey ends here.")

    # --- Final Status ---
    print(f"\n{user_name}, your final credit balance is {credits}.")
    if credits > 50:
        print("Excellent resource management!")
    elif credits > 0 and credits <= 50:
        print("You made it, but you're running low on credits!")
    else:
        print("You're broke, but at least you traveled far!")

# Run the game only if this file is being executed as the main script
if __name__ == "__main__":
    main()
