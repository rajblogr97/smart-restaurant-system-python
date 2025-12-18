           #smart-restaurant-system-python      
print ("🔱 Welcome to Smart Restaurant & Hotel 🔱")

# ------------------ MENUS ------------------
food_menu = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
    "Salad": 100
}

drink_menu = {
    "Water": 20,
    "Juice": 80,
    "Soda": 50,
    "Coffee": 70
}

rooms = {
    "Single Room": 800,
    "Double Room": 1500,
    "Suite": 3000
}

orders = []


# ------------------ FUNCTIONS ------------------
def normalize(text):
    return text.strip().lower()


def ai_recommendation():
    food_count = {}

    for order in orders:
        if order["Type"] == "Food":
            food_count[order["Item"]] = food_count.get(order["Item"], 0) + order["Quantity"]

    print ("\n🤖 AI Recommendation:")
    if food_count:
        fav = max(food_count, key=food_count.get)
        print (f"👉 You like **{fav}**. Try adding a drink with it! 🥤")
    else:
        print ("👉 Try our popular combo: Pizza + Cold Drink 🍕🥤")


# ------------------ NORMALIZED MENUS ------------------
food_menu_norm = {k.lower(): (k, v) for k, v in food_menu.items()}
drink_menu_norm = {k.lower(): (k, v) for k, v in drink_menu.items()}
rooms_norm = {k.lower(): (k, v) for k, v in rooms.items()}


# ------------------ MAIN LOOP ------------------
while True:
    print ("\n===== Customer Menu =====")
    print ("1. Order Food")
    print ("2. Order Drinks")
    print ("3. Book a Room")
    print ("4. View All Orders & Bill")
    print ("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    # ---------- FOOD ----------
    if choice == "1":
        print ("\nAvailable Food Items:")
        for item, price in food_menu.items():
            print (f"{item}: ₹{price}")

        user_input = normalize(input("Enter food name: "))

        if user_input in food_menu_norm:
            item_name, price = food_menu_norm[user_input]
            qty = int(input("Enter quantity: "))
            amount = price * qty

            orders.append({
                "Type": "Food",
                "Item": item_name,
                "Quantity": qty,
                "Amount": amount
            })

            print (f"✅ Added {qty} x {item_name} - ₹{amount}")
        else:
            print ("❌ Food item not available")

    # ---------- DRINK ----------
    elif choice == "2":
        print ("\nAvailable Drinks:")
        for item, price in drink_menu.items():
            print (f"{item}: ₹{price}")

        user_input = normalize(input("Enter drink name: "))

        if user_input in drink_menu_norm:
            item_name, price = drink_menu_norm[user_input]
            qty = int(input("Enter quantity: "))
            amount = price * qty

            orders.append({
                "Type": "Drink",
                "Item": item_name,
                "Quantity": qty,
                "Amount": amount
            })

            print (f"✅ Added {qty} x {item_name} - ₹{amount}")
        else:
            print ("❌ Drink not available")

    # ---------- ROOM ----------
    elif choice == "3":
        print ("\nAvailable Rooms:")
        for room, price in rooms.items():
            print (f"{room}: ₹{price} per night")

        user_input = normalize(input("Enter room type: "))

        if user_input in rooms_norm:
            room_name, price = rooms_norm[user_input]
            nights = int(input("Enter number of nights: "))
            amount = price * nights

            orders.append({
                "Type": "Room",
                "Item": room_name,
                "Quantity": nights,
                "Amount": amount
            })

            print (f"🏨 Booked {room_name} for {nights} night(s) - ₹{amount}")
        else:
            print ("❌ Room not available")

    # ---------- BILL ----------
    elif choice == "4":
        if not orders:
            print ("⚠️ No orders placed yet")
        else:
            print ("\n========== FINAL BILL ==========")
            total = 0
            for i, order in enumerate(orders, start=1):
                print (f"{i}. {order['Type']} - {order['Item']} x {order['Quantity']} = ₹{order['Amou>
                total += order["Amount"]

            print ("--------------------------------")
            print (f"💰 Total Amount: ₹{total}")
            print ("================================")

            ai_recommendation()

    # ---------- EXIT ----------
    elif choice == "5":
        print ("\n🙏 Thank you for visiting! Have a great day!")
        break

    else:
        print ("❌ Invalid choice, please try again.")

