from pytest import fixture, raises

from tasker.py import Action


class ActionTest(Action):
    _ignored_attribute = None

    attribute_a = 'ABC'
    attribute_b = 123
    attribute_c = True


@fixture
def action_test():
    return ActionTest()


def test__ignore_attribute_nao_existe(action_test):
    with raises(AttributeError):
        action_test._ignored_attribute

def test_definicao_de_atrubutos(action_test):
    action_test.attribute_a = 'CBA'
    action_test.attribute_b = 321
    action_test.attribute_c = False

    assert action_test.attribute_a == 'CBA'
    assert action_test.attribute_b == 321
    assert action_test.attribute_c == False

