import unittest
from unittest.mock import MagicMock, Mock, patch
import sys
sys.path.append('../src/')
import demo_lambda as demo


class TestDemoLambda(unittest.TestCase):
    def setUp(self):
        self.code = demo

    def test_main_success(self):
        with patch.object(self.code, "process_data", return_value="success"):
            event = {'event_id': 'test_event_id', 'event_name': 'test_event_name'}
            result = self.code.main(event, MagicMock())
        assert result == 'success'

    def test_main_failure(self):
        event = {'event_name': 'test_event_name'}
        result = self.code.main(event, MagicMock())
        assert result == "failure"