"""
Space Traveler: A Mini Text Adventure (Extended)
-----------------------------------------------
Fill in the missing code (<FILL IN>) to complete this game scenario with TWO puzzles 
and a branching storyline.

Skills tested:
- Variables and assignment
- Data types, type conversion
- print(), input()
- Math operators (including modulo)
- Scope, global variable usage
- if/else/elif, comparison, and/or/not
- Branching logic
"""

# Global variable tracking your credits
credits = <FILL IN>  # e.g., 100

def purchase_item(cost):
    """
    Deduct the item cost from global credits and return True if the purchase is successful.
    Return False if there aren't enough credits.
    """
    global credits
    if <FILL IN>:  # e.g., credits >= cost
        credits = credits - cost
        return True
    else:
        return False
    
def check_fuel_choice(fuel_amount):
    """
    If the player tries to buy more than 100 units of fuel, it's 'risky'.
    If the player enters a negative amount, it's 'impossible'.
    Otherwise, return 'safe'.
    """
    if <FILL_IN>:  # if fuel_amount < 0
        return "impossible"
    elif <FILL_IN>:  # if fuel_amount > 100
        return "risky"
    else:
        return "safe"


def solve_riddle():
    """
    Puzzle #1: Asks a modulo-based math riddle.
    Returns True if correct, otherwise False.
    """
    print("\nPuzzle #1: To unlock the door, solve this riddle:")
    print("A code is hidden in this expression: (57 % 6) * 2")
    print("Hint: Use the modulo operator to find the remainder of 57 / 6, then multiply by 2.\n")

    user_answer = input("What is the result of (57 % 6) * 2 ? ")
    user_answer = <FILL IN>  # convert to int

    # 57 % 6 = 3, then 3 * 2 = 6 is the correct answer
    if user_answer == <FILL IN>:  # correct numeric answer
        return True
    else:
        return False


def solve_logic_puzzle():
    """
    Puzzle #2: Tests knowledge of logical operators.
    Returns True if correct, otherwise False.

    Puzzle: We have two statements:
      X = True
      Y = False
    The puzzle asks: "What is the result of (X and not Y) or (Y and not X)?"
    Evaluate carefully:
      - X and not Y --> True and not False = True
      - Y and not X --> False and not True = False
    So overall: True or False = True
    """
    print("\nPuzzle #2: Logic Operators Challenge!")
    print("Given X = True and Y = False, evaluate this expression:")
    print("(X and not Y) or (Y and not X)")
    print("Type 'True' or 'False' as your answer.\n")

    user_answer = input("Your answer: ").lower()

    # The correct result is "true"
    if user_answer == <FILL IN>:  # e.g., "true"
        return True
    else:
        return False



def main():
    global credits

    print("Welcome, Space Traveler!")
    user_name = input("What is your name, adventurer? ")

    print(f"\nGreetings, {user_name}!")
    print(f"You start with {credits} credits. Spend them wisely.")

    # 1. Station Choice
    print("\nYou approach a space station. You can either buy fuel or buy food.")
    choice = input("Type 'fuel' or 'food': ").lower()

    if choice == "fuel":
        fuel_input = input("How many units of fuel would you like to buy? ")
        fuel_input = <FILL IN>  # convert to int

        fuel_safety = check_fuel_choice(fuel_input)
        if fuel_safety == "impossible":
            print("You can't buy negative fuel!")
        elif fuel_safety == "risky":
            print("That's a lot of fuel, but let's see if you can afford it...")
        else:
            print("That seems like a safe choice.")

        # Each unit of fuel costs 2 credits
        total_cost = fuel_input * <FILL IN>  # cost per unit (likely 2)
        if purchase_item(total_cost):
            print(f"You bought {fuel_input} units of fuel for {total_cost} credits.")
        else:
            print("You don't have enough credits for that much fuel.")

    elif choice == "food":
        # A constant cost for food
        food_cost = 30
        print(f"Buying food costs {food_cost} credits.")
        if purchase_item(food_cost):
            print("You have purchased a food supply.")
        else:
            print("Not enough credits to buy food.")
    else:
        print("You decided not to buy anything at this station.")

    # 2. Puzzle #1 (Mod Riddle)
    print("\nA locked door blocks your path to the next sector.")
    first_puzzle_result = solve_riddle()
    if first_puzzle_result:
        print("Door unlocked! You proceed forward into the next sector.")
    else:
        print("Wrong answer! An alarm sounds, and the normal route is blocked!")
        print("However, you notice a hidden corridor leading to an alternate path...")
        # 2.5. Alternate Path: Puzzle #2 (Logic Puzzle)
        print("You must solve another puzzle to bypass security on this hidden path.")
        second_puzzle_result = solve_logic_puzzle()
        if second_puzzle_result:
            print("You successfully bypassed the security with your logic skills!")
        else:
            print("Your logic puzzle attempt fails, and guards catch you. Game Over!")
            return  # End the game here if the second puzzle is also failed

    # 3. Final Decision (Gate A or Gate B)
    # If the first puzzle was solved OR the second puzzle was solved, 
    # the player continues to the final gates.
    print("\nYou reach a final checkpoint with two gates:")
    print("Gate A: Costs 20 credits to open.")
    print("Gate B: Costs 50 credits to open but comes with bonus fuel.")

    gate_choice = input("Which gate do you choose? (A/B): ").upper()

    if gate_choice == "A":
        if <FILL IN>:  # check if you have at least 20 credits
            purchase_item(20)
            print("You open Gate A and continue on your journey. Success!")
        else:
            print("You don't have enough credits for Gate A. Stuck!")
    elif gate_choice == "B":
        # If you have enough credits, you can open Gate B.
        # Maybe you get bonus fuel or some reward.
        if credits >= 50:
            <FILL_IN>  # e.g., purchase_item(50)
            print("You open Gate B, and you receive bonus fuel. Success!")
        else:
            print("You can't afford Gate B. Stuck!")
    else:
        print("You chose neither gate. The journey ends here.")

    # 4. Final Status
    print(f"\n{user_name}, your final credit balance is {credits}.")
    if credits > 50:
        print("Excellent resource management!")
    elif credits > 0 and credits <= 50:
        print("You made it, but you're running low on credits!")
    else:
        print("You're broke, but at least you traveled far!")

# Standard main check
if __name__ == "__main__":
    main()
