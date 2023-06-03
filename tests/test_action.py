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

def test_erro_ao_escrever_o_nome_do_argumento_errado():
    with raises(
        TypeError,
        match=(
            "ActionTest got an unexpected"
            " keyword argument 'invalid_arg'")
    ):
        ActionTest(invalid_arg=0)

def test_sem_argumetos_continua_com_padroes(action_test):
    assert action_test.attribute_a == 'ABC'
    assert action_test.attribute_b == 123
    assert action_test.attribute_c == True

def test_argumentos_nomeados_ao_instaciar_a_class():
    action_test = ActionTest(
        attribute_a='OPQ',
        attribute_b=False,
        attribute_c=495,
    )

    assert action_test.attribute_a == 'OPQ'
    assert action_test.attribute_b == False
    assert action_test.attribute_c == 495

def test_argumentos_posicionais_ao_instaciar_a_classe():
    action_test = ActionTest('GFH', 123456, False + True)

    assert action_test.attribute_a == 'GFH'
    assert action_test.attribute_b == 123456
    assert action_test.attribute_c == True + False

def test_definicao_padrao(action_test):
    action_test.attribute_a = 'CBA'
    action_test.attribute_b = 321
    action_test.attribute_c = False

    assert action_test.attribute_a == 'CBA'
    assert action_test.attribute_b == 321
    assert action_test.attribute_c == False

def test_alterar_argumentos_e_atributos():
    action_test = ActionTest(
        'string',
        attribute_b=0,
        attribute_c=False
    )

    action_test.attribute_c = None
    action_test.attribute_a = 1001011

    assert action_test.attribute_a == 1001011
    assert action_test.attribute_b == 0
    assert action_test.attribute_c == None
