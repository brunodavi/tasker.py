from tasker.icons import Misc


def test_icone_de_warning():
    expected_warning = (
        'android.resource://'
        'net.dinglisch.android.taskerm'
        '/drawable/cust_warning'
    )

    assert Misc().WARNING == expected_warning
