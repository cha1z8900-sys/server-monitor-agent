import multiprocessing
import time

def cpu_stress():
    while True:
        x = 99999 * 99999

if __name__ == "__main__":
    print("🔥 Нагружаем CPU на 15 секунд...")
    
    # Запускаем столько процессов сколько ядер у твоего CPU
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=cpu_stress)
        p.start()
        processes.append(p)
    
    time.sleep(15)  # Держим нагрузку 15 секунд
    
    for p in processes:
        p.terminate()
    
    print("✅ Готово, нагрузка снята")