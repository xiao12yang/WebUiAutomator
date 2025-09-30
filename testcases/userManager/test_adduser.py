# import pytest
#
# @pytest.fixture
# def browser():
#     print('测试开始')
#     yield
#     print('测试结束')
#
# @pytest.fixture(params=[1,2,3,4,5,6,7,8,9,10])
# def setup(request):
#     print(request)
#
#
#
#
# class TestAddUser:
#
#
#     # def setup(self):
#     #     print('测试执行前处理')
#     #
#     # def teardown(self):
#     #     print('测试结束后处理')
#
#
#     @pytest.mark.usefixtures('browser')
#     @pytest.mark.smoke
#     def test_add_user_01(self):
#         print('新增用户01')
#
#     def test_add_user_02(self,setup):
#         print('新增用户02')
#
#     # @pytest.mark.skip
#
#     def test_add_user_03(self,browser):
#         print('新增用户03')
#     @pytest.mark.skipif(2 >= 1,reason='跳过')
#     def test_add_user_04(self):
#         print('新增用户04')