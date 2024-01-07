import pytest


@pytest.fixture(scope="session")
def test_session():
    print("我是session级的fixture")

@pytest.fixture(scope="function")
def test_func1():
    print("我是func1级别fixture")

@pytest.fixture(scope="function")
def test_func2():
    print("我是func2级别fixture")