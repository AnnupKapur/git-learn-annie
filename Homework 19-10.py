# Step 1: Create a café menu
menu = ["Espresso ☕️", "Americano ☕️🚰", "Latte ☕️🥛", "Cappuccino ☕️🥛", "Flat White ☕️🥛", "Mocha ☕️🍫", "Bubble Tea🧋"]

# Step 2: Print out the menu in a fancy way
print("💖☕✨★｡.*☆ Welcome to the cafe! ★｡.*☆💖☕✨")
print("Here’s the drinks menu:")
print("-" * 40)
for item in menu:
    print(f"• {item}")
print("-" * 40)

# Step 3: Take user orders
orders = []

# .strip() = remove any weird whitespace 
#
# this is a new comment

# this is skittle's updates
# this is another sktitles updates 

while True:
    choice = input("💖☕✨ What would you like to order? ").strip()
    quantity = int(input("💖☕✨ How many would you like? "))

    # Store the order as a tuple (item, quantity)
    orders.append((choice, quantity))

    another = input("💖☕✨ Would you like to order another item? (Yes/No) ").strip().lower()
    if another != "yes":
        break

# Step 4: Print the receipt
print("💖☕✨🧾 Here is your receipt:")
print("=" * 40)
for item, quantity in orders:
    print(f"- {quantity} x {item}")
print("=" * 40) 


message = "💖☕✨Thank you for your purchase 💖☕✨"

# Add a simple "cutesy" style with spacing and symbols
end_message = f"""★｡.*☆ {message} ☆*｡★"""
print(end_message)
