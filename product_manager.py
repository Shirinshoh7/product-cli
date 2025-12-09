class ProductManager:
    def __init__(self, filename):
        self.filename = filename

    def _read_all(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
            return [line.strip() for line in lines]
        except FileNotFoundError:
            return []

    def _write_all(self, lines):
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write("\n".join(lines))

    def add_product(self, name, price):
        lines = self._read_all()
        lines.append(f"{name} — {price}"),
        self._write_all(lines)

    def edit_product(self, name, new_price):
        lines = self._read_all()
        for i in range(len(lines)):
            if lines[i].startswith(name + " —"):
                lines[i] = f"{name} — {new_price}"
                break
        self._write_all(lines)

    def delete_product(self, name):
        lines = self._read_all()
        new_lines = [line for line in lines if not line.startswith(name + " —")]
        self._write_all(new_lines)

    def total_sum(self):
        lines = self._read_all()
        total = 0
        for line in lines:
            try:
                price = int(line.split("—")[1].strip())
                total += price
            except:
                pass
        return total
