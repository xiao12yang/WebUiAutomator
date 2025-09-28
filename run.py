import shutil

import pytest

if __name__ == "__main__":
    pytest.main()
    shutil.copy('./environment.xml','./report/temp')