import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}

current_order = []

def view_menu():
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, item in DRINK_MENU.items():
        print(f"[{code}] - {item['name']} - {item['price']:,} VNĐ")


def normalize_code(drink_code):
    return drink_code.strip().upper()


def add_to_order(drink_code, quantity):
    drink_code = normalize_code(drink_code)

    if drink_code not in DRINK_MENU:
        raise ValueError("Mã đồ uống không hợp lệ!")

    if quantity <= 0:
        raise ValueError("Số lượng phải lớn hơn 0!")

    current_order.append({
        "code": drink_code,
        "quantity": quantity
    })

    logging.info(f"Added {quantity} of {drink_code} to order")
    print(f"Đã thêm {quantity} x {DRINK_MENU[drink_code]['name']} vào giỏ hàng.")


def calculate_total(order=None):
    if order is None:
        order = current_order

    total = 0

    for item in order:
        code = item["code"]
        qty = item["quantity"]

        total += DRINK_MENU[code]["price"] * qty

    return total


def view_order():
    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print("Mã SP | Tên đồ uống        | Đơn giá | Số lượng | Thành tiền")
    print("-" * 60)

    total = 0

    for item in current_order:
        code = item["code"]
        qty = item["quantity"]

        name = DRINK_MENU[code]["name"]
        price = DRINK_MENU[code]["price"]

        subtotal = price * qty
        total += subtotal

        print(f"{code:<5} | {name:<18} | {price:,} | {qty:<8} | {subtotal:,} VNĐ")

    print("-" * 60)
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")


def checkout():
    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    total = calculate_total()

    print("\n--- THANH TOÁN ---")
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")

    confirm = input(
        f"Xác nhận thanh toán {total:,} VNĐ? (y/n): "
    ).strip().lower()

    match confirm:
        case "y":
            current_order.clear()
            logging.info("Checkout successful")
            print("Thanh toán thành công. Giỏ hàng đã được làm trống.")

        case "n":
            print("Đã hủy thao tác thanh toán. Quay lại menu chính.")

        case _:
            print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")


def logout():
    logging.info("Cashier logged out. System shutdown.")
    print("Đã thoát ca làm việc. Hẹn gặp lại!")