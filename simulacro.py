"""
Inventory & Sales Management Console App
- English interface
- Modular functions
- Nested dicts and lists
- Preloaded products (>=5)
- Reports: top 3 sold, sales by brand, gross & net income, inventory performance
- Robust input validation and error handling
"""

from datetime import datetime
from collections import defaultdict, Counter
import sys

# -----------------------
# Data structures
# -----------------------
# inventory: product_id -> product dict
inventory = {
    # product_id: {name, brand, category, price, stock, warranty_months, initial_stock}
    1: {"name": "Aurora Headphones", "brand": "Soundix", "category": "Audio", "price": 79.99, "stock": 25, "warranty_months": 12, "initial_stock": 25},
    2: {"name": "Volt Charger 65W", "brand": "Ampere", "category": "Power", "price": 39.50, "stock": 40, "warranty_months": 24, "initial_stock": 40},
    3: {"name": "Nexus 10 Tablet", "brand": "NovaTech", "category": "Computers", "price": 249.00, "stock": 10, "warranty_months": 12, "initial_stock": 10},
    4: {"name": "PixelCam 4K", "brand": "OptiSight", "category": "Cameras", "price": 499.00, "stock": 6, "warranty_months": 24, "initial_stock": 6},
    5: {"name": "HomeSyx SmartPlug", "brand": "HomeSyx", "category": "SmartHome", "price": 19.99, "stock": 60, "warranty_months": 6, "initial_stock": 60},
}

# sales: list of sale records
sales = []
# sale record: {
#   "sale_id", "client", "client_type", "product_id", "product_name", "brand",
#   "quantity", "unit_price", "discount_pct", "date", "gross", "net"
# }

# generate unique IDs
_next_product_id = max(inventory.keys()) + 1
_next_sale_id = 1

# -----------------------
# Helper / Validation
# -----------------------

def safe_int(prompt, min_val=None, max_val=None):
    while True:
        val = input(prompt).strip()
        if val == "":
            print("Input required. Try again.")
            continue
        try:
            n = int(val)
            if min_val is not None and n < min_val:
                print(f"Must be >= {min_val}.")
                continue
            if max_val is not None and n > max_val:
                print(f"Must be <= {max_val}.")
                continue
            return n
        except ValueError:
            print("Invalid integer. Try again.")

def safe_float(prompt, min_val=None, max_val=None):
    while True:
        val = input(prompt).strip()
        if val == "":
            print("Input required. Try again.")
            continue
        try:
            f = float(val)
            if min_val is not None and f < min_val:
                print(f"Must be >= {min_val}.")
                continue
            if max_val is not None and f > max_val:
                print(f"Must be <= {max_val}.")
                continue
            return f
        except ValueError:
            print("Invalid number. Try again.")

def choose_product_id(prompt="Select product id: "):
    while True:
        prod_id = safe_int(prompt)
        if prod_id in inventory:
            return prod_id
        print("Product id not found. Try again.")

def show_inventory(short=False):
    print("\n--- Inventory ---")
    if not inventory:
        print("No products in inventory.")
        return
    print("{:<5} {:<22} {:<12} {:<10} {:<6} {:<8}".format("ID", "Name", "Brand", "Category", "Price", "Stock"))
    for pid, p in inventory.items():
        if short:
            print(f"{pid: <5} {p['name'][:20]: <22} {p['brand'][:10]: <12} {p['category'][:9]: <10} ${p['price']: <6.2f} {p['stock']: <6}")
        else:
            print("{:<5} {:<22} {:<12} {:<10} ${:<8.2f} {:<6} warranty:{}m".format(
                pid, p['name'], p['brand'], p['category'], p['price'], p['stock'], p['warranty_months']
            ))
    print("-----------------\n")

# -----------------------
# Inventory CRUD
# -----------------------

def register_product():
    global _next_product_id
    print("\nRegister new product")
    try:
        name = input("Name: ").strip()
        if not name:
            print("Product name cannot be empty.")
            return
        brand = input("Brand: ").strip()
        if not brand:
            print("Brand cannot be empty.")
            return
        category = input("Category: ").strip() or "General"
        price = safe_float("Unit price (e.g. 49.99): ", min_val=0.0)
        stock = safe_int("Initial quantity in stock: ", min_val=0)
        warranty = safe_int("Warranty (months): ", min_val=0)
    except KeyboardInterrupt:
        print("\nCancelled.")
        return

    inventory[_next_product_id] = {
        "name": name,
        "brand": brand,
        "category": category,
        "price": round(price, 2),
        "stock": stock,
        "warranty_months": warranty,
        "initial_stock": stock
    }
    print(f"Product registered with id {_next_product_id}.")
    _next_product_id += 1

def consult_product():
    show_inventory()
    pid = choose_product_id()
    p = inventory[pid]
    print(f"\nDetails for product id {pid}:")
    for k, v in p.items():
        print(f"  {k}: {v}")

def update_product():
    show_inventory()
    pid = choose_product_id()
    p = inventory[pid]
    print("Leave blank to keep current value.")
    name = input(f"Name [{p['name']}]: ").strip()
    brand = input(f"Brand [{p['brand']}]: ").strip()
    category = input(f"Category [{p['category']}]: ").strip()
    price_input = input(f"Unit price [{p['price']}]: ").strip()
    stock_input = input(f"Stock [{p['stock']}]: ").strip()
    warranty_input = input(f"Warranty months [{p['warranty_months']}]: ").strip()

    # validations
    if name:
        p['name'] = name
    if brand:
        p['brand'] = brand
    if category:
        p['category'] = category
    if price_input:
        try:
            price = float(price_input)
            if price < 0:
                print("Price must be non-negative; keeping old value.")
            else:
                p['price'] = round(price, 2)
        except ValueError:
            print("Invalid price; keeping old value.")
    if stock_input:
        try:
            stock = int(stock_input)
            if stock < 0:
                print("Stock must be non-negative; keeping old value.")
            else:
                # if adjusting stock, we do not change initial_stock (initial_stock used for performance baseline)
                p['stock'] = stock
        except ValueError:
            print("Invalid stock; keeping old value.")
    if warranty_input:
        try:
            w = int(warranty_input)
            if w < 0:
                print("Warranty must be non-negative; keeping old value.")
            else:
                p['warranty_months'] = w
        except ValueError:
            print("Invalid warranty; keeping old value.")

    print("Product updated.")

def delete_product():
    show_inventory()
    pid = choose_product_id()
    confirm = input(f"Confirm delete product id {pid} ({inventory[pid]['name']})? (y/n): ").strip().lower()
    if confirm == 'y':
        # cautious: cannot delete product if there are sales referencing it (historical integrity)
        referenced = any(s['product_id'] == pid for s in sales)
        if referenced:
            print("Cannot delete product with historical sales records. Consider marking it inactive instead.")
            return
        del inventory[pid]
        print("Product deleted.")
    else:
        print("Deletion cancelled.")

# -----------------------
# Sales
# -----------------------

def calculate_discount_pct(client_type):
    # Example discount rules by client type
    client_type = client_type.lower()
    if client_type == "vip":
        return 10.0  # 10%
    if client_type == "employee":
        return 30.0
    if client_type == "wholesale":
        return 15.0
    return 0.0  # default regular

# we'll show an example lambda for revenue calculation:
revenue_calc = lambda unit_price, qty: round(unit_price * qty, 2)

def register_sale():
    global _next_sale_id
    print("\nRegister a sale")
    try:
        client = input("Client name: ").strip()
        if not client:
            print("Client name required.")
            return
        client_type = input("Client type (regular/vip/employee/wholesale): ").strip().lower() or "regular"
        show_inventory(short=True)
        pid = choose_product_id()
        product = inventory[pid]
        qty = safe_int("Quantity to sell: ", min_val=1)
    except KeyboardInterrupt:
        print("\nCancelled.")
        return

    # Validate stock
    if qty > product['stock']:
        print(f"Insufficient stock. Available: {product['stock']}. Sale aborted.")
        return

    discount_pct = calculate_discount_pct(client_type)
    unit_price = product['price']
    gross = revenue_calc(unit_price, qty)
    discount_amount = round(gross * (discount_pct / 100.0), 2)
    net = round(gross - discount_amount, 2)

    # Update inventory
    product['stock'] -= qty

    sale = {
        "sale_id": _next_sale_id,
        "client": client,
        "client_type": client_type,
        "product_id": pid,
        "product_name": product['name'],
        "brand": product['brand'],
        "quantity": qty,
        "unit_price": unit_price,
        "discount_pct": discount_pct,
        "date": datetime.now(),
        "gross": gross,
        "net": net
    }
    sales.append(sale)
    _next_sale_id += 1

    print(f"Sale recorded. Sale ID: {sale['sale_id']}. Gross: ${gross:.2f} Discount: {discount_pct}% Net: ${net:.2f}")

def consult_sales():
    if not sales:
        print("No sales recorded yet.")
        return
    print("\n--- Sales History ---")
    for s in sales:
        date_str = s['date'].strftime("%Y-%m-%d %H:%M:%S")
        print(f"ID:{s['sale_id']} | {date_str} | {s['client']} ({s['client_type']}) | {s['product_name']} x{s['quantity']} | Gross:${s['gross']:.2f} Net:${s['net']:.2f}")
    print("---------------------\n")

# -----------------------
# Reports
# -----------------------

def top_n_products(n=3):
    # sum quantities sold per product_id
    sold = defaultdict(int)
    for s in sales:
        sold[s['product_id']] += s['quantity']
    if not sold:
        print("No sales to report.")
        return
    sorted_sold = sorted(sold.items(), key=lambda kv: kv[1], reverse=True)
    print(f"\nTop {n} best-selling products:")
    for rank, (pid, qty) in enumerate(sorted_sold[:n], start=1):
        prod = inventory.get(pid, {"name": "Deleted product"})
        print(f"{rank}. {prod['name']} (ID {pid}) — {qty} units sold")
    print()

def sales_by_brand():
    # sum net revenue by brand
    revenue = defaultdict(float)
    for s in sales:
        revenue[s['brand']] += s['net']
    if not revenue:
        print("No sales to report.")
        return
    print("\nSales (net) grouped by brand:")
    for brand, amt in sorted(revenue.items(), key=lambda kv: kv[1], reverse=True):
        print(f" - {brand}: ${amt:.2f}")
    print()

def income_report():
    if not sales:
        print("No sales to report.")
        return
    total_gross = sum(s['gross'] for s in sales)
    total_net = sum(s['net'] for s in sales)
    total_discount = round(total_gross - total_net, 2)
    print("\nIncome report:")
    print(f" - Total gross revenue: ${total_gross:.2f}")
    print(f" - Total discounts:     ${total_discount:.2f}")
    print(f" - Total net revenue:   ${total_net:.2f}")
    print()

def inventory_performance():
    # Evaluate inventory performance using sold vs initial stock, turnover percentage
    if not inventory:
        print("No inventory.")
        return
    # compute times sold per product
    sold = defaultdict(int)
    for s in sales:
        sold[s['product_id']] += s['quantity']

    print("\nInventory performance:")
    for pid, p in inventory.items():
        initial = p.get('initial_stock', 0)
        sold_qty = sold.get(pid, 0)
        remaining = p['stock']
        turnover_pct = (sold_qty / initial * 100) if initial > 0 else 0.0
        status = "OK"
        if remaining == 0:
            status = "OUT OF STOCK"
        elif turnover_pct > 50:
            status = "FAST MOVING"
        elif turnover_pct < 10:
            status = "SLOW MOVING"
        print(f" - {p['name']} (ID {pid}): sold {sold_qty}, init {initial}, left {remaining}, turnover {turnover_pct:.1f}% -> {status}")
    print()

def full_reports_menu():
    while True:
        print("\n--- Reports Menu ---")
        print("1. Top 3 products sold")
        print("2. Sales grouped by brand")
        print("3. Income (gross & net)")
        print("4. Inventory performance")
        print("5. Back to main menu")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            top_n_products(3)
        elif choice == "2":
            sales_by_brand()
        elif choice == "3":
            income_report()
        elif choice == "4":
            inventory_performance()
        elif choice == "5":
            break
        else:
            print("Invalid option.")

# -----------------------
# Utilities & Menu
# -----------------------

def preload_demo_sales():
    """
    Optionally create some demo sales so reports show richer data.
    This is safe — will reduce stock accordingly.
    """
    global _next_sale_id
    demo = [
        {"client": "Alice", "client_type": "vip", "product_id": 1, "quantity": 3},
        {"client": "Bob", "client_type": "regular", "product_id": 2, "quantity": 5},
        {"client": "Charlie Co.", "client_type": "wholesale", "product_id": 5, "quantity": 20},
        {"client": "Diana", "client_type": "employee", "product_id": 3, "quantity": 1},
        {"client": "Eve", "client_type": "regular", "product_id": 4, "quantity": 2},
    ]
    for d in demo:
        pid = d["product_id"]
        if pid not in inventory:
            continue
        p = inventory[pid]
        qty = min(d["quantity"], p["stock"])
        if qty <= 0:
            continue
        discount_pct = calculate_discount_pct(d["client_type"])
        gross = revenue_calc(p["price"], qty)
        net = round(gross * (1 - discount_pct / 100.0), 2)
        p["stock"] -= qty
        sale = {
            "sale_id": _next_sale_id,
            "client": d["client"],
            "client_type": d["client_type"],
            "product_id": pid,
            "product_name": p["name"],
            "brand": p["brand"],
            "quantity": qty,
            "unit_price": p["price"],
            "discount_pct": discount_pct,
            "date": datetime.now(),
            "gross": gross,
            "net": net
        }
        sales.append(sale)
        _next_sale_id += 1

def main_menu():
    print("\nWelcome — Inventory & Sales System")
    # preload some demo sales to allow immediate reporting if user wants
    preload_demo_sales()
    while True:
        try:
            print("\nMain Menu:")
            print("1. Show inventory")
            print("2. Register product")
            print("3. Consult product")
            print("4. Update product")
            print("5. Delete product")
            print("6. Register sale")
            print("7. Consult sales")
            print("8. Reports")
            print("9. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                show_inventory()
            elif choice == "2":
                register_product()
            elif choice == "3":
                consult_product()
            elif choice == "4":
                update_product()
            elif choice == "5":
                delete_product()
            elif choice == "6":
                register_sale()
            elif choice == "7":
                consult_sales()
            elif choice == "8":
                full_reports_menu()
            elif choice == "9":
                print("Goodbye. System shutting down cleanly.")
                break
            else:
                print("Invalid choice, choose a number from the menu.")
        except KeyboardInterrupt:
            print("\nReceived keyboard interrupt. Returning to main menu.")
        except Exception as e:
            # catch-all to prevent abrupt termination
            print(f"An unexpected error occurred: {e}. Returning to main menu.")

if __name__ == "__main__":
    main_menu()
