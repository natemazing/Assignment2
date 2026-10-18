"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    month_cost = annual_cost / MONTHS_PER_YEAR
    return month_cost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    semester_cost = cost_per_semester(annual_cost)
    day_cost = semester_cost / CLASS_DAYS_PER_SEMESTER
    return day_cost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    semester_cost = cost_per_semester(annual_cost)
    credit_cost = semester_cost / credits
    return credit_cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    credit_cost = cost_per_credit(annual_cost, credits)
    class_cost = credit_cost * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return class_cost


def cost_per_fast_food(cost_of_order, times_per_month):
    """Give back the cost of fast food for a year."""
    food_cost = cost_of_order * times_per_month * MONTHS_PER_YEAR
    return food_cost

# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("Enter the total cost of one year of college: "))
    credits = int(input("Enter how many credits you're taking per semester: "))


    while True:
        # Show your menu here.
        print("1: cost per semester")
        print("2: cost per month")
        print("3: cost per class day")
        print("4: cost per credit")
        print("5: cost per CS1430 class")
        print("6: cost of fast food")
        print("Q: exit")
        choice = input("Choose an option: ")

        if choice == "Q":
            print("Thanks for running the numbers!")
            break
        elif choice == "1":
            cost = cost_per_semester(annual_cost)
            print(f"One semester costs ${cost:.2f}")
        elif choice == "2":
            cost = cost_per_month(annual_cost)
            print(f"One month costs ${cost:.2f}")
        elif choice == "3":
            cost = cost_per_day(annual_cost)
            print(f"One class day costs ${cost:.2f}")
        elif choice == "4":
            cost = cost_per_credit(annual_cost, credits)
            print(f"One credit costs ${cost:.2f}")
        elif choice == "5":
            cost = cost_per_class(annual_cost, credits)
            print(f"One CS1430 class costs ${cost:.2f}")
        elif choice == "5":
            cost = cost_per_class(annual_cost, credits)
            print(f"One CS1430 class costs ${cost:.2f}")
        elif choice == "6":
            cost_of_order = float(input("How much does your usual order cost? "))
            times_per_month = int(input("How often per month do you go out? "))
            cost = cost_per_fast_food(cost_of_order, times_per_month)
            print(f"Your fast food bill this year is: ${cost:.2f}")
        else:
            print("Invalid input. Try again.")
        print("")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
