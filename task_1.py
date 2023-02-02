import unittest
import sys

class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f'bird {self.name} can fly'

    def walk(self):
        return f'bird {self.name} can walk'


class FlyingBird(Bird):
    def __int__(self, name, ration):
        self.ration = ration
        Bird.__init__(self, name)


class NoneflyingBird(Bird):
    def __init__(self, name, ration='worms'):
        self.ration = ration
        Bird.__init__(self, name)

    def non_fly(self):
        return f'bird {self.name} can\'t fly'

    def eat(self):
        return f'bird {self.name} can eat {self.ration}'


class SuperBird(FlyingBird, NoneflyingBird):
    def __init__(self, name, ration='bugs'):
        self.ration = ration
        FlyingBird.__init__(self, name)
        NoneflyingBird.__init__(self, name, ration)

    def swim(self):
        return f'bird {self.name} can swim'

#
# duck = Bird("duck")
# duck.fly()
# chicken = SuperBird("Ruti")
# chicken_1 = SuperBird("Guti", "seeds")
# chicken.eat()
# chicken_1.eat()
# ostrich = NoneflyingBird('Guga')
# ostrich.eat()
# ostrich.fly()


class TestBirds(unittest.TestCase):
    def setUp(self) -> None:
        self.test_chicken = SuperBird("Rutti", "testers")
        self.test_ostrich = NoneflyingBird('Guga')

    def test_fly(self):
        self.assertEqual(self.test_chicken.fly(), 'bird Rutti can fly')

    def test_eat(self):
        self.assertIsInstance(self.test_chicken.eat(), str)

    def test_swim(self):
        self.assertNotIsInstance(self.test_chicken.swim(), list)

    @unittest.skip('jast skip it')
    def test_skipped(self):
        self.fail('This function should be skipped')

    @unittest.skipIf(sys.version_info.major < 2,"Skip due to python version")
    def test_walk(self):
        self.assertTrue(self.test_chicken.walk() == 'bird Rutti can walk')

    @unittest.skipUnless(sys.version_info.major < 2,"Skip due to python version")
    def test_non_fly(self):
        self.assertEqual(self.test_ostrich.non_fly(), "bird Guga can't fly")




