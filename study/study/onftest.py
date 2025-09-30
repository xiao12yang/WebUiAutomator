import pytest

@pytest.fixture(scope='function',autouse=True)
def study_fixture():
    print('study start')

    yield
    print('study end')