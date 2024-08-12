# Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest.
# В классе пропишите следующие методы:
# test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
# Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance
# этого объекта со значением 50.
# test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
# Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого
# объекта со значением 100.
# test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
# Далее 10 раз у объектов вызываются методы run и walk соответственно.
# Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве
# результатов.  Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.
#
#
# Пример результата выполнения программы:
# Вывод на консоль:
# Ran 3 tests in 0.001s OK

import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        atlet1 = runner.Runner('Piter')
        for i in range(1, 11):
            atlet1.walk()
            dist = atlet1.distance
        self.assertEqual(dist, 50)

    def test_run(self):
        atlet2 = runner.Runner('Kat')
        for i in range(1, 11):
            atlet2.run()
            dist = atlet2.distance
        self.assertEqual(dist, 100)

    def test_challenge(self):
        atlet1 = runner.Runner('Piter')
        atlet2 = runner.Runner('Kat')
        for i in range(1, 11):
            atlet1.walk()
            dist1 = atlet1.distance
            atlet2.run()
            dist2 = atlet2.distance
        self.assertNotEqual(dist1, dist2)

if __name__ == '__main__':
    unittest.main()