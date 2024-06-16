import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
        if choice == "off":
            break

        elif choice == "report":
            for resource, amount in resources.items():
                if resource in ["bread", "ham"]:
                    unit = "slice(s)"  ##if resource is bread or ham, list it in slices
                else:
                    unit = "pounds"  ##if resource is cheese, list in pounds
                print(f" {resource.capitalize()}: {amount} {unit}")

        elif choice in ["small", "medium", "large"]:  ##if choice is a size
            sandwich = recipes[choice]  ##creating sandwich variable for size

            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):  ##if there are sufficient ingredients
                coins = cashier_instance.process_coins()  ##variable to complete transaction
                if cashier_instance.transaction_result(coins, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid choice. Please choose again")

if __name__=="__main__":
    main()
