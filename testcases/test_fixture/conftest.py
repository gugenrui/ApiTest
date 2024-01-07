import pytest


@pytest.fixture(scope="session")
def t_session():
    print("我是session级的fixture")


@pytest.fixture(scope="function")
def t_func1():
    print("我是func1级别fixture")


@pytest.fixture(scope="function")
def t_func2():
    print("我是func2级别fixture")


@pytest.fixture(scope="function")
def get_params():
    parmas = {
        "shouji": "15705187072",
        "appkey": "0c818521d38759e1"
    }
    return parmas


@pytest.fixture(scope="function")
def func():
    print("我是前置步骤")
    yield "ggr"
    print("我是后置步骤")


@pytest.fixture(scope="function")
def use_fixture1():
    print("我现在使用use_fixtures1")


@pytest.fixture(scope="function")
def use_fixture2():
    print("我现在使用use_fixtures2")


@pytest.fixture(params=["数据1", "数据2"], ids=["case1", "case2"])
def params_fixture(request):
    return request.param
