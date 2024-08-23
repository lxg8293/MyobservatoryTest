import os

import pytest

if __name__ == '__main__':
    pytest.main(['--clean-alluredir','./testcases/test9day.py', '-s', '-v', '--alluredir=allure-results'])
    os.system('allure generate -c -o allure-reports')
