from tasker.icons import Misc


def test_warning_icon():
    expected_warning = (
        'android.resource://'
        'net.dinglisch.android.taskerm'
        '/drawable/cust_warning'
    )

    assert Misc().WARNING == expected_warning
