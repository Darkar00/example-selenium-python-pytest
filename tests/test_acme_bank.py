from applitools.selenium import Eyes, Target
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def test_log_into_bank_account(webdriver: Chrome, eyes: Eyes) -> None:

  # Load the main page.
  webdriver.get("https://demo.saleor.io/default-channel")
  eyes.check(Target.window().fully().with_name("Main page").layout())
