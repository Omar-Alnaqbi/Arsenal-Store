# Arsenal Store - Python Journal Project
# Omar Ali Alnaqbi - OA
# Store prices are sample GBP amounts for this project.

products = [
    ("Arsenal Jersey (Home / Away)", 30),
    ("Arsenal Scarf", 8),
    ("Arsenal Hoodie", 25),
    ("Arsenal Accessories", 7),
    ("Arsenal Package", 60),
    ("Arsenal Museum Visit", 8),
    ("Emirates Stadium Tour", 18)
]
cart = []
from pathlib import Path

# Remember the next order number between program runs.
ORDER_FILE = Path("arsenal_order_counter.txt")


def next_order_number():
    try:
        last = int(ORDER_FILE.read_text().strip())
    except (FileNotFoundError, ValueError):
        last = 0
    number = last + 1
    ORDER_FILE.write_text(str(number))
    return f"ARS-{number:02d}"



def ask_number(message, low, high):
    # Keep asking until a valid menu number is entered.
    while True:
        try:
            number = int(input(message))
            if low <= number <= high:
                return number
        except ValueError:
            pass
        print("Please enter a valid number.")


def show_products():
    # Show all products and visitor experiences.
    print("\n--- ARSENAL STORE ---")
    for index, (name, price) in enumerate(products, 1):
        print(f"{index}. {name} - GBP {price:.2f}")


def add_items():
    # Keep adding products until the customer enters 0.
    while True:
        show_products()
        print("0. Done adding items")
        choice = ask_number("Select item (0-7): ", 0, 7)
        if choice == 0:
            return
        index = choice - 1
        name = products[index][0]
        if index == 0:
            style = ask_number("1. Home  2. Away: ", 1, 2)
            name = "Arsenal Jersey - Home" if style == 1 else "Arsenal Jersey - Away"
        quantity = ask_number("Quantity (1-10): ", 1, 10)
        cart.append((index, quantity, name))
        print(f"Added: {name} x{quantity}")


def checkout():
    # Print a receipt and calculate the optional discount.
    if not cart:
        print("Your cart is empty.")
        return
    subtotal = 0
    print("\n--- YOUR RECEIPT ---")
    for index, quantity, name in cart:
        cost = products[index][1] * quantity
        subtotal += cost
        print(f"{name} x{quantity}: GBP {cost:.2f}")
    answer = input("Apply 10% discount? (Y/N): ").strip().upper()
    discount = subtotal * 0.10 if answer == "Y" else 0
    print(f"Subtotal: GBP {subtotal:.2f}")
    print(f"Discount: GBP {discount:.2f}")
    print(f"Final total: GBP {subtotal - discount:.2f}")
    print(f"Order reference: {next_order_number()}")
    cart.clear()  # Start a fresh cart for the next order.
    input("Press Enter to return to the menu...")


def main():
    # Repeat the menu until the customer chooses Exit.
    print("\nWelcome to Arsenal Store!")
    print("North London Forever!")
    while True:
        print("\n=== ARSENAL STORE ===")
        print("1. View products")
        print("2. Add items to cart")
        print("3. Checkout")
        print("4. Exit")
        choice = ask_number("Choose (1-4): ", 1, 4)
        if choice == 1:
            show_products()
        elif choice == 2:
            add_items()
        elif choice == 3:
            checkout()
        else:
            print("Thank you for visiting Arsenal Store!")
            print("North London Forever!")
            break


if __name__ == "__main__":
    main()
