TAX_RATE = 0.15
DISCOUNT_RATE = 0.10

sales = []


def get_string(prompt):
    """Get a non-empty string from the user"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(" Input cannot be empty, Please try again.")


def get_positive_float(prompt):
    """Get a positive float from the user"""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print(" Value must be greater than zero, Please try again.")
        except ValueError:
            print(" Invalid input. Please enter a numeric value (e.g. 5000.00).")


def get_positive_int(prompt):
    """Get a positive integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("  Quantity must be at least 1, Please try again.")
        except ValueError:
            print(" Invalid input. Please enter a whole number (e.g. 3).")


def add_sale():
    print("\n-- Add Sale --")
    name = get_string("Product name: ")
    price = get_positive_float("Unit price (SLL): ")
    qty = get_positive_int("Quantity sold: ")

    subtotal = price * qty
    discount = subtotal * DISCOUNT_RATE if qty >= 5 else 0
    tax = (subtotal - discount) * TAX_RATE
    total = (subtotal - discount) + tax

    sales.append({"product": name, "qty": qty, "total": total})

    print(f"\n  Subtotal : SLL {subtotal:,.2f}")
    print(f"  Discount : SLL {discount:,.2f}")
    print(f"  Tax(15%) : SLL {tax:,.2f}")
    print(f"  TOTAL    : SLL {total:,.2f}")


def view_sales():
    print("\n-- Sales Records --")
    if not sales:
        print("  No records yet.")
        return
    for i, s in enumerate(sales, 1):
        print(f"  {i}. {s['product']} | Qty: {s['qty']} | Total: SLL {s['total']:,.2f}")


def summary():
    print("\n-- Summary --")
    if not sales:
        print("  No records yet.")
        return
    total_rev = sum(s["total"] for s in sales)
    print(f"  Transactions : {len(sales)}")
    print(f"  Total Revenue: SLL {total_rev:,.2f}")
    print(f"  Average Sale : SLL {total_rev / len(sales):,.2f}")


def main():
    print("  Small Business Sales Calculator SL")
    while True:
        print("\n1. Add Sale\n2. View Sales\n3. Summary\n4. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_sale()
        elif choice == "2":
            view_sales()
        elif choice == "3":
            summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print(" Invalid choice, Please enter 1, 2, 3, or 4.")


main()