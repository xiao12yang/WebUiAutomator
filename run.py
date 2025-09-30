import shutil
import os
import pytest

if __name__ == "__main__":
    pytest.main()
    shutil.copy('./environment.xml','./report/temp')
    os.system('allure serve ./report/temp')