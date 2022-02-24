import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

tie = .5

class Funciones_Globales():

	def __init__(self,driver):
		self.driver = driver

	def tiempo(self,tie):
		t = time.sleep(tie)
		return t

	def navegar(self,url,tie):
		self.driver.get(url)
		self.driver.maximize_window()
		print("Página abierta: " + str(url))
		t = time.sleep(tie)
		return t

	def text_xpath(self,xpath,texto,tie):
		val = self.driver.find_element_by_xpath(xpath)
		val.clear()
		val.send_keys(texto)
		t = time.sleep(tie)
		return t

	def text_xpath_val(self,xpath,text,tie):
		try:

			val = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,xpath)))
			val = self.driver.execute_script("arguments[0].scrollIntoView(0);",val)
			val = self.driver.find_element_by_xpath(xpath)
			val.clear()
			val.send_keys(text)
			print("Escribiendo en el campo {} el texto {} ".format(xpath,text))
			t = time.sleep(tie)
			return t
		except TimeoutException as ex:
			print(ex.msg)
			print("El Elemento no se encontro"+ xpath)

	def click_xpath_val(self,xpath,tie):
		try:
			val = WebDriverWait(self.driver,.02).until(EC.visibility_of_element_located((By.XPATH,xpath)))
			val = self.driver.execute_script("arguments[0].scrollIntoView(0);",val)
			val = self.driver.find_element_by_xpath(xpath)
			val.click()
			print("\nDamos click en el campo {}".format(xpath))

			t = time.sleep(tie)
			return t
		except TimeoutException as ex:
			print(ex.msg)
			print("El Elemento no se encontro "+ xpath)

	def click_id_val(self,id,tie):
		try:
			val = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,id)))
			val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
			val = self.driver.find_element_by_id(id)
			val.click()
			print("Damos click en el campo {}".format(id))
			t = time.sleep(tie)
			return t
		except TimeoutException as ex:
			print(ex.msg)
			print("El Elemento no se encontro "+ id)

	def salida(self):
		print("Termina la prueba Exitosamente....")

	# Funcion Radio y Check por xpath multiselect mia
	def check_xpath_multiselect(self, xpath, tie):
		try:
			val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
			val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
			val = self.driver.find_element_by_xpath(xpath)
			val.click()

			print("Click en el elemento {} ".format(xpath))
			# val.send_keys(text)
			t = time.sleep(tie)
			return t
		except TimeoutException as ex:
			print(ex.msg)
			print("El Elemento no se encontro " + xpath)

