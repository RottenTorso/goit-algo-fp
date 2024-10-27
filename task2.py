import turtle

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return
    
    # Малюємо основну гілку
    t.forward(branch_length)
    
    # Малюємо праве піддерево
    t.right(45)
    draw_pythagoras_tree(t, branch_length * 0.707, level - 1)
    
    # Повертаємося до основної гілки
    t.left(90)
    draw_pythagoras_tree(t, branch_length * 0.707, level - 1)
    
    # Повертаємося до початкової позиції та орієнтації
    t.right(45)
    t.backward(branch_length)

def main():
    # Налаштовуємо екран та черепаху
    screen = turtle.Screen()
    screen.title("Фрактал Дерево Піфагора")
    
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Починаємо, дивлячись вгору
    
    # Отримуємо рівень рекурсії від користувача
    level = int(input("Введіть рівень рекурсії: "))
    
    # Малюємо дерево Піфагора
    draw_pythagoras_tree(t, 100, level)
    
    # Завершення
    turtle.done()

if __name__ == "__main__":
    main()