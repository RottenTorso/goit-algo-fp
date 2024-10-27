import random
import matplotlib.pyplot as plt

# Кількість симуляцій
num_simulations = 100000

# Ініціалізація словника для підрахунку сум
sums_count = {i: 0 for i in range(2, 13)}

# Функція для симуляції кидків двох кубиків
def simulate_dice_rolls(num_simulations):
    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sums_count[dice_sum] += 1

# Виконання симуляції
simulate_dice_rolls(num_simulations)

# Обчислення ймовірностей
probabilities = {sum_: (count / num_simulations) * 100 for sum_, count in sums_count.items()}

# Виведення результатів у вигляді таблиці
print("|Сума|Імовірність|")
print("--------------------")
for sum_, probability in probabilities.items():
    print(f"|{sum_}|{probability:.2f}%|")

# Побудова графіку
plt.bar(probabilities.keys(), probabilities.values(), color='blue')
plt.xlabel('Сума')
plt.ylabel('Імовірність (%)')
plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
plt.savefig('Figure_1.png')  # Збереження графіку як зображення
plt.show()

# Порівняння з аналітичними розрахунками
analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67,
    8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

print("\nПорівняння з аналітичними розрахунками:")
print("|Сума|Імовірність (Монте-Карло)|Імовірність (Аналітична)|")
print("--------------------------------------------------------")
for sum_ in range(2, 13):
    monte_carlo_prob = probabilities[sum_]
    analytical_prob = analytical_probabilities[sum_]
    print(f"|{sum_}|{monte_carlo_prob:.2f}%|{analytical_prob:.2f}%|")