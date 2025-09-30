import pytest

class TestParamsFixture:

    @pytest.mark.parametrize('name',['zhangsan','lisi','wangwu'])
    def test_params_001(self,name):
        print(name)
