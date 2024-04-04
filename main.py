# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

import pytest


options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:platformVersion": "9.0",
	"browserName": "",
	"appium:appiumVersion": "1.22.0",
	"appium:deviceName": "Samsung Galaxy S9 FHD GoogleAPI Emulator",
	"appium:deviceOrientation": "portrait",
	"appium:app": "storage:filename=Calculator_8.4 (503542421)_Apkpure.apk",
	"appium:appPackage": "com.google.android.calculator",
	"appium:appActivity": "com.android.calculator2.Calculator",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"sauce:options": {"name": "Appium Desktop Session -- Apr 4, 2024 9:34 AM"},
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

# Acionador do script
if __name__ == '__main__':

		# Conexão com o Sauce Labs, aponta o datacenter, meu usuario e chave
		driver = webdriver.Remote("https://oauth-niettocaroline-f1701:3a790f68-9840-4066-aaec-5de76446274d@ondemand.us-west-1.saucelabs.com:443/wd/hub", options=options)

		resultado_esperado = '13'

		# Realiza a conta
		btn8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="8")
		btn8.click()
		btn_somar = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="plus")
		btn_somar.click()
		btn5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="5")
		btn5.click()
		btn_igual = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="equals")
		btn_igual.click()
		resultado_final = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/result_final")
		assert resultado_final.text == resultado_esperado
		print (resultado_final.text)
		print (resultado_esperado)
		driver.quit()