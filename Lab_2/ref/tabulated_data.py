class TabulatedData:
    """Клас для роботи з табличними значеннями функції."""
    def __init__(self, file_name='in.txt'):
        self.file_name = file_name
        self.data = []

    def tabulate_function(self, func, a, b, num_points):
        """Генерує табличні значення функції та записує у файл."""
        h = (b - a) / num_points
        self.data = [(a + i * h, func(a + i * h)) for i in range(num_points + 1)]
        self.write_to_file()

    def write_to_file(self):
        """Записує табличні значення у файл."""
        with open(self.file_name, 'w') as file:
            for x, y in self.data:
                file.write(f"x={x}, y={y}\n")

    def read_from_file(self):
        """Зчитує табличні значення з файлу."""
        self.data = []
        with open(self.file_name, 'r') as file:
            for line in file.readlines():
                x, y = self.parse_line(line)
                self.data.append((x, y))

    @staticmethod
    def parse_line(line):
        """Розбирає рядок формату 'x=..., y=...'."""
        parts = line.strip().split(', ')
        x = float(parts[0].split('=')[1])
        y = float(parts[1].split('=')[1])
        return x, y
