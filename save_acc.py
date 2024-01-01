def add_acc(tuples, file_path):
    with open(file_path, 'a') as f:
        # Записываем кортежи в файл
        f.write(str(tuples) + '\n')


# Открываем файл для чтения
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = tuple(line.strip() for line in file)
        return lines
    except FileNotFoundError:
        with open(file_path, 'w') as f:
            f.write(str("") + '\n')
            read_file(file_path)
