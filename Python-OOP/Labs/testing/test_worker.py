class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_worker_is_initialized_correctly(self):
        worker = Worker('Test name', 1000, 20)

        self.assertEqual('Test name', worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(20, worker.energy)

    def test_rest_method_energy_increment(self):
        worker = Worker('Test name', 1000, 20)

        worker.rest()
        self.assertEqual(21, worker.energy)
        worker.rest()
        self.assertEqual(22, worker.energy)

    def test_work_with_negative_energy_raise(self):
        worker = Worker('Test name', 1000, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

        worker = Worker('Test name', 1000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_money_increment(self):
        worker = Worker('Test name', 1000, 20)

        worker.work()
        self.assertEqual(1000, worker.money)
        worker.work()
        self.assertEqual(2000, worker.money)

    def test_work_energy_decrement(self):
        worker = Worker('Test name', 1000, 20)

        worker.work()
        self.assertEqual(19, worker.energy)
        worker.work()
        self.assertEqual(18, worker.energy)

    def test_get_info_returns_correct(self):
        worker = Worker('Test name', 1000, 20)

        self.assertEqual(f'{worker.name} has saved {worker.money} money.', worker.get_info())


if __name__ == '__main__':
    main()
