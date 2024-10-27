# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    
    return selected_items, total_calories

# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    
    # Таблиця для зберігання максимальних калорій для кожного можливого бюджету
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Заповнюємо таблицю
    for i in range(1, n + 1):
        item_name, details = item_list[i - 1]
        cost = details['cost']
        calories = details['calories']
        
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Відновлюємо оптимальний набір страв
    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, details = item_list[i - 1]
            selected_items.append(item_name)
            w -= details['cost']
    
    total_calories = dp[n][budget]
    return selected_items, total_calories

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Використання жадібного алгоритму
greedy_result = greedy_algorithm(items, budget)
print("Greedy Algorithm Result:", greedy_result)

# Використання алгоритму динамічного програмування
dp_result = dynamic_programming(items, budget)
print("Dynamic Programming Result:", dp_result)