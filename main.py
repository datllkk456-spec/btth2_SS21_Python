from pos_logic import (
    view_menu,
    add_to_order,
    view_order,
    checkout,
    logout
)


def main():
    while True:
        print("\n========== HIGHLANDS MINI POS ==========")
        print("1. Xem thực đơn")
        print("2. Thêm món vào giỏ")
        print("3. Xem giỏ hàng & Tính tổng tiền")
        print("4. Thanh toán & Xóa giỏ hàng")
        print("5. Thoát ca làm việc")
        print("========================================")

        choice = input("Chọn chức năng (1-5): ").strip()

        match choice:
            case "1":
                view_menu()

            case "2":
                try:
                    print("\n--- THÊM MÓN VÀO GIỎ ---")
                    code = input("Nhập mã đồ uống: ")
                    quantity = int(input("Nhập số lượng: "))

                    add_to_order(code, quantity)

                except ValueError as e:
                    print(e)

            case "3":
                view_order()

            case "4":
                checkout()

            case "5":
                logout()
                break

            case _:
                print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()