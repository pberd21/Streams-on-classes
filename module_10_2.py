from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        days = 0

        while enemies > 0:
            days += 1
            sleep(1)
            enemies = max(0, enemies - self.power)
            print(f"{self.name} сражается {days} день(дня)..., осталось {enemies} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

if __name__ == "__main__":
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print("Все битвы закончились!")