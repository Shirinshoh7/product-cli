import sys
from product_manager import ProductManager

def main():
    if len(sys.argv) < 3:
        print("Использование: python main.py product.txt действие [параметры]")
        return

    filename = sys.argv[1]
    action = sys.argv[2]
    manager = ProductManager(filename)

    if action == "add":
        name = sys.argv[3]
        price = int(sys.argv[4])
        manager.add(name, price)

    elif action == "update":
        name = sys.argv[3]
        price = int(sys.argv[4])
        manager.update(name, price)

    elif action == "delete":
        name = sys.argv[3]
        manager.delete(name)

    elif action == "total":
        print("Общая сумма:", manager.total())

    else:
        print("Неизвестное действие")
  

if __name__ == "__main__":
    main()
