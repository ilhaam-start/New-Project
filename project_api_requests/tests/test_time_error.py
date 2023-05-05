from unittest.mock import Mock
from lib.time_error import *

def test_calls_API_to_show_time_difference():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime": 1683291712}
    timer_mock = Mock()
    timer_mock.time.return_value = 1683291914.5
    timeerror = TimeError(requester_mock, timer_mock)
    assert timeerror.error() == -202.5