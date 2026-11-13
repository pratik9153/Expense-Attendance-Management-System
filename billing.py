
from validators import get_text, get_float, get_int

bills = []

TAX_RATE = 0.18


def calculate_discount(subtotal):

    if subtotal >= 10000:
        return 0.15

    elif subtotal >= 5000:
        return 0.10

    elif subtotal >= 1000:
        return 0.05

    else:
        return 0.0


def calculate_tax(taxable_amount):

    return taxable_amount * TAX_RATE


def generate_invoice():

    customer = get_text("Enter customer name: ")

    bill_no = f"B-{len(bills) + 1:04d}"

    items = []

    while True:

        name = input("\nEnter item name (done to finish): ").strip()

        if name.lower() == "done":
            break

        if not name:
            print("Item name cannot be empty.")
            continue

        price = get_float("Enter unit price: ", 0.01)

        quantity = get_int("Enter quantity: ", 1)

        line_total = price * quantity

        items.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "line_total": line_total
        })

    if not items:
        print("No items added.")
        return

    subtotal = sum(item["line_total"] for item in items)

    discount_rate = calculate_discount(subtotal)

    discount_amount = subtotal * discount_rate

    taxable_amount = subtotal - discount_amount

    tax_amount = calculate_tax(taxable_amount)

    grand_total = taxable_amount + tax_amount

    invoice = {
        "bill_no": bill_no,
        "customer": customer,
        "items": items,
        "subtotal": round(subtotal, 2),
        "discount_rate": discount_rate,
        "discount_amount": round(discount_amount, 2),
        "taxable_amount": round(taxable_amount, 2),
        "tax_amount": round(tax_amount, 2),
        "grand_total": round(grand_total, 2)
    }

    bills.append(invoice)

    print_invoice(invoice)


def print_invoice(invoice):

    print("\n============== INVOICE ==============")

    print("Bill No:", invoice["bill_no"])
    print("Customer:", invoice["customer"])

    print("-------------------------------------")

    print(
        f"{'Item':<15}{'Price':>9}"
        f"{'Qty':>6}{'Total':>11}"
    )

    for item in invoice["items"]:

        print(
            f"{item['name']:<15}"
            f"{item['price']:>9.2f}"
            f"{item['quantity']:>6}"
            f"{item['line_total']:>11.2f}"
        )

    print("-------------------------------------")

    print(f"Subtotal: {invoice['subtotal']:.2f}")

    print(
        f"Discount ({invoice['discount_rate']:.0%}): "
        f"-{invoice['discount_amount']:.2f}"
    )

    print(f"Taxable Amount: {invoice['taxable_amount']:.2f}")

    print(f"Tax (18%): {invoice['tax_amount']:.2f}")

    print("-------------------------------------")

    print(f"GRAND TOTAL: {invoice['grand_total']:.2f}")

    print("Thank you for your purchase!")


def billing_menu():

    while True:

        print("\n--- BILLING SYSTEM ---")
        print("1. Generate Invoice")
        print("2. View All Bills")
        print("3. Back")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            generate_invoice()

        elif choice == "2":

            if not bills:
                print("No bills available.")

            else:
                for invoice in bills:
                    print_invoice(invoice)

        elif choice == "3":
            break

        else:
            print("Invalid choice.")
