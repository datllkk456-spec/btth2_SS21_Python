import logging

# ================= CONFIG LOGGING =================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ================= CUSTOM EXCEPTIONS =================
class ItemNotFoundError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


# ================= DATA =================
DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}

current_order = []


# ================= FUNCTIONS =================
def view_menu():
    """Hiển thị thực đơn"""
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, item in DRINK_MENU.items():
        print(f"[{code}] - {item['name']} - {item['price']:,} VNĐ")


def normalize_code(drink_code: str) -> str:
    """Chuẩn hóa mã sản phẩm"""
    return drink_code.strip().upper()


def add_to_order(drink_code: str, quantity: int):
    """
    Thêm món vào giỏ hàng
    Raises:
        ItemNotFoundError
        InvalidQuantityError
    """
    drink_code = normalize_code(drink_code)

    if drink_code not in DRINK_MENU:
        raise ItemNotFoundError(drink_code)

    if quantity <= 0:
        raise InvalidQuantityError(quantity)

    current_order.append({
        "code": drink_code,
        "quantity": quantity
    })

    logging.info(f"Added {quantity} of {drink_code} to order")
    print(f"Đã thêm {quantity} x {DRINK_MENU[drink_code]['name']} vào giỏ hàng.")


def calculate_total(order=None):
    """Tính tổng tiền giỏ hàng"""
    if order is None:
        order = current_order

    total = 0
    for item in order:
        code = item["code"]
        qty = item["quantity"]
        total += DRINK_MENU[code]["price"] * qty

    return total


def view_order():
    """Hiển thị giỏ hàng"""
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
    """Thanh toán giỏ hàng"""
    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    total = calculate_total()

    print("\n--- THANH TOÁN ---")
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")

    confirm = input(f"Xác nhận thanh toán {total:,} VNĐ? (y/n): ").strip().lower()

    if confirm == "y":
        current_order.clear()
        logging.info("Checkout successful")
        print("Thanh toán thành công. Giỏ hàng đã được làm trống.")
    elif confirm == "n":
        print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
    else:
        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")


def logout():
    """Thoát chương trình"""
    logging.info("Cashier logged out. System shutdown.")
    print("Đã thoát ca làm việc. Hẹn gặp lại!")