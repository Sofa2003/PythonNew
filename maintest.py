import multiprocessing 
import time


def is_prime(n):
    """Проверяет, простое ли число"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(numbers):
    """Находит простые числа в списке"""
    return [n for n in numbers if is_prime(n)]

if __name__ == '__main__':
    # Создаем список чисел для проверки
    numbers = list(range(100000, 101000))  # 1000 чисел
    
    print("=== Поиск простых чисел ===")
    print(f"Проверяем {len(numbers)} чисел")
    
    # 1. Обычный способ (один процесс)
    print("\n1. Обычный способ...")
    start = time.time()
    primes_single = find_primes(numbers)
    time_single = time.time() - start
    print(f"Найдено простых: {len(primes_single)}")
    print(f"Время: {time_single:.2f} сек")
    
    # 2. Многопроцессорный способ
    print("\n2. Многопроцессорный способ...")
    start = time.time()
    
    # Разбиваем числа на 4 части
    chunk_size = len(numbers) // 4
    chunks = []
    for i in range(4):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size if i < 3 else len(numbers)
        chunks.append(numbers[start_idx:end_idx])
    
    # Создаем 4 процесса
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(find_primes, chunks)
    
    # Объединяем результаты
    # Строка комментария 
    primes_multi = []
    for chunk_result in results:
        primes_multi.extend(chunk_result)
    
    time_multi = time.time() - start
    print(f"Найдено простых: {len(primes_multi)}")
    print(f"Время: {time_multi:.2f} сек")
    
    print(f"\nУскорение: {time_single/time_multi:.2f}x")