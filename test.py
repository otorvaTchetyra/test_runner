import unittest
from runner import Runner  

class TestRunner(unittest.TestCase):

    def test_walk(self):
        runner = Runner("Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")
        
        for _ in range(10):
            runner1.run()  # from first runner we are calling method 'run'
            runner2.walk()  # from second runner we are  calling method  'walk'

        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()



