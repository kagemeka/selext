import unittest

import selext.webdriver


class Test(unittest.TestCase):
    def test_chrome(self) -> None:
        with selext.webdriver.create_chrome_driver(headless=True) as _:
            ...

    def test_firefox(self) -> None:
        with selext.webdriver.create_firefox_driver(headless=True) as _:
            ...


if __name__ == "__main__":
    unittest.main()
