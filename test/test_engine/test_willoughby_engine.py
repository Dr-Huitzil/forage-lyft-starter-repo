import unittest

from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_milage = 60001
        last_service_milage = 0
        engine = WilloughbyEngine(current_milage, last_service_milage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_milage = 60000
        last_service_milage = 0
        engine = WilloughbyEngine(current_milage, last_service_milage)
        self.assertFalse(engine.needs_service())