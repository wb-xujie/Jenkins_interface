# coding = utf-8
# author = white

import allure


@allure.feature("这是一个测试demo")
class Testdemoe:

    def setup(self):
        pass

    def teardown(self):
        pass

    @allure.story("这是第一条测试用例")
    def test1(self):
        sum = 0
        for i in range(101):
            sum += i
        print("这是第一条测试用例的结果{0}".format(sum))
        assert sum == 5050

    @allure.story("这是第二条测试用例")
    def test2(self):
        test_list = [i for i in range(101) if i%2==0]
        print(test_list)
