from tasker.icons.icon import Icon
from tasker.icons import Misc


def test_warning_icon():
    expected_warning = Icon('cust_warning')
    assert Misc.WARNING == expected_warning
