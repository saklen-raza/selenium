# Experiment 11: Testing a JavaScript calculator using Selenium + unittest
import os
import unittest
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By


class CalculatorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/google-chrome"

        cls.driver = webdriver.Chrome(options=options)
        cls.driver.set_window_size(1280, 1050)

        html_file = Path(__file__).resolve().parent / "index.html"

        print("HTML FILE:", html_file)
        print("EXISTS:", html_file.exists())
        print("URI:", html_file.as_uri())
        cls.url = html_file.as_uri()
    def setUp(self):
        print("URL:", self.url)
        self.driver.get(self.url)
        print("CURRENT URL:", self.driver.current_url)
        print("TITLE:", self.driver.title)
        print("SOURCE:", self.driver.page_source[:500])

    def calc(self, a, b, op):
        """Enter two numbers, click an operator button and return the result text."""
        d = self.driver
        d.find_element(By.ID, "num1").send_keys(str(a))
        d.find_element(By.ID, "num2").send_keys(str(b))
        d.find_element(By.ID, op).click()
        return d.find_element(By.ID, "result").text

    def test_1_page_title(self):
        self.assertEqual(self.driver.title, "Simple Calculator")

    def test_2_addition(self):
        self.assertEqual(self.calc(12, 8, "add"), "Result: 20")

    def test_3_subtraction(self):
        self.assertEqual(self.calc(20, 5, "sub"), "Result: 15")

    def test_4_multiplication(self):
        self.assertEqual(self.calc(6, 7, "mul"), "Result: 42")

    def test_5_division(self):
        self.assertEqual(self.calc(15, 4, "div"), "Result: 3.75")

    def test_6_divide_by_zero(self):
        self.assertEqual(self.calc(10, 0, "div"), "Error: Cannot divide by zero")

    def test_7_empty_input(self):
        self.driver.find_element(By.ID, "add").click()
        self.assertEqual(self.driver.find_element(By.ID, "result").text,
                         "Please enter both numbers")

    def test_8_clear_button(self):
        self.calc(3, 4, "add")
        self.driver.find_element(By.ID, "clear").click()
        self.assertEqual(self.driver.find_element(By.ID, "num1").get_attribute("value"), "")
        self.assertEqual(self.driver.find_element(By.ID, "result").text, "")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)