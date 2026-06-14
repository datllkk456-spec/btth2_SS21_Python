from pos_logic import (
    view_menu,
    add_to_order,
    view_order,
    checkout,
    logout,
    ItemNotFoundError,
    InvalidQuantityError
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

        if choice == "1":
            view_menu()

        elif choice == "2":
            try:
                print("\n--- THÊM MÓN VÀO GIỎ ---")
                code = input("Nhập mã đồ uống: ")
                quantity = int(input("Nhập số lượng: "))

                add_to_order(code, quantity)

            except ValueError:
                print("Vui lòng nhập số lượng là một số nguyên!")
            except ItemNotFoundError as e:
                print("Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!")
            except InvalidQuantityError:
                print("Số lượng phải lớn hơn 0!")

        elif choice == "3":
            view_order()

        elif choice == "4":
            checkout()

        elif choice == "5":
            logout()
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()