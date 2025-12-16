import random
from src.simulation import run_simulation


def main() -> None:
    """
    Точка входа в приложение
    
    Запускает две симуляции работы библиотеки
    с разными seed для генератора случайных чисел
    """
    print("Система управления библиотекой - Лабораторная работа №4")
    print()
    
    seed1 = random.randint(1, 10000)
    run_simulation(steps=20, seed=seed1)
    
    print()
    print("Запуск второй симуляции с другим seed...")
    print()
    
    seed2 = random.randint(1, 10000)
    run_simulation(steps=15, seed=seed2)


if __name__ == "__main__":
    main()
