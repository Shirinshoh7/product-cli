import sys
from product_manager import ProductManager

def main():
    if len(sys.argv) < 3:
        print("Использование: python main.py <имя_файла> <действие> [параметры]")
        return

    filename = sys.argv[1]
    action = sys.argv[2]

    manager = ProductManager(filename)

    if action == "add":
        # python main.py products.txt add "Огурцы" 50
        name = sys.argv[3]
        price = int(sys.argv[4])
        manager.add_product(name, price)
        print("Добавлено.")

    elif action == "edit":
        # python main.py products.txt edit "Огурцы" 60
        name = sys.argv[3]
        new_price = int(sys.argv[4])
        manager.edit_product(name, new_price)
        print("Изменено.")

    elif action == "delete":
        # python main.py products.txt delete "Огурцы"
        name = sys.argv[3]
        manager.delete_product(name)
        print("Удалено.")

    elif action == "sum":
        # python main.py products.txt sum
        print("Общая сумма:", manager.total_sum())

    else:
        print("Неизвестное действие!")

if __name__ == "__main__":
    main()
