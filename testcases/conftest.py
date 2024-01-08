import pytest

from utils.log_util import logger


@pytest.fixture(scope="session")
def test_session():
    print("我是session级的fixture")


@pytest.fixture(scope="function")
def test_func1():
    print("我是func1级别fixture")


@pytest.fixture(scope="function")
def test_func2():
    print("我是func2级别fixture")


@pytest.fixture(scope="function", autouse=True)
def fun():
    logger.info("----------------------------------------------------------------------\n开始执行测试用例")
    yield
    logger.info("测试用例执行完毕\n----------------------------------------------------------------------")
