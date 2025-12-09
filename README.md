## Требования

Python 3.10+

## Установка

Клонировать репозиторий:

```bash
git clone https://github.com/Shirinshoh7/product-cli
cd product-cli
```

## Формат команды

Все команды выполняются в формате:

```bash
python main.py <имя_файла> <действие> "<Наименование>" [Цена]
```

## Запуск приложения

Добавить продукт:

```bash
python main.py products.txt add "Товар" цена
```

Изменить цену продукта:

```bash
python main.py products.txt edit "Товар" цена
```

Удалить продукт:

```bash
python main.py products.txt delete "Товар" 
```

Посчитать сумму всех продуктов:

```bash
python main.py products.txt sum
```

## Автор
**Shirinshoh Badalov**.
