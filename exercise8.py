import heapq

def min_cost_of_cable_connection(cable_lengths):
    heapq.heapify(cable_lengths)  # Створення купи з довжин кабелів

    total_cost = 0

    while len(cable_lengths) > 1:
        # Об'єднання двох найменших кабелів
        min1 = heapq.heappop(cable_lengths)
        min2 = heapq.heappop(cable_lengths)

        # Витрати на з'єднання
        connection_cost = min1 + min2
        total_cost += connection_cost

        # Додаємо новий кабель до купи
        heapq.heappush(cable_lengths, connection_cost)

    return total_cost

# Приклад використання
cable_lengths = [4, 3, 2, 6]
result = min_cost_of_cable_connection(cable_lengths)
print("Мінімальні витрати на з'єднання кабелів:", result)
