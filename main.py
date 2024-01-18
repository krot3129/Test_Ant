from collections import deque

def sum_of_digits(num):
    """
    Считает сумму цифр числа.

    Parameters:
    - num (int): Число, сумму цифр которого нужно посчитать.

    Returns:
    - int: Сумма цифр числа.
    """
    return sum(int(digit) for digit in str(num))

def is_accessible(x, y):
    """
    Проверяет, доступны ли координаты (x, y) в соответствии с условием, что сумма цифр x и y не превышает 25.

    Parameters:
    - x (int): Координата x.
    - y (int): Координата y.

    Returns:
    - bool: True, если координаты доступны, иначе False.
    """
    return sum_of_digits(x) + sum_of_digits(y) <= 25

def ant_moves(x, y):
    """
    Реализует алгоритм поиска в ширину для определения количества достижимых ячеек муравьем.

    Parameters:
    - x (int): Начальная координата x.
    - y (int): Начальная координата y.

    Returns:
    - int: Количество достижимых ячеек из начальной позиции.
    """
    visited_cells = set()
    queue = deque([(x, y)])

    while queue:
        current_x, current_y = queue.popleft()

        if is_accessible(current_x, current_y) and (current_x, current_y) not in visited_cells:
            visited_cells.add((current_x, current_y))

            # Перемещение вверх
            if current_y + 1 >= 0:
                queue.append((current_x, current_y + 1))
            # Перемещение вниз
            if current_y - 1 >= 0:
                queue.append((current_x, current_y - 1))
            # Перемещение влево
            if current_x - 1 >= 0:
                queue.append((current_x - 1, current_y))
            # Перемещение вправо
            queue.append((current_x + 1, current_y))

    return len(visited_cells)

start_position = (1000, 1000)
result = ant_moves(*start_position)
print(result)
