import time
import pytest
import allure
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones import Funciones_Globales
from allure_commons.types import AttachmentType

tie = .02

@pytest.fixture()
def log_on_failure(request):    # Funcion donde se cacha algun error de el test
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)

@pytest.fixture(scope='module')
def setup_logout():     # Funcion principal del Test

    print("\nInicia Test")
    global driver, func
    driver = webdriver.Chrome(executable_path="C:/driverchrome/chromedriver.exe")  # Carga driver de Google Chrome
    #driver = webdriver.Chrome(executable_path="C:/FireFox/geckodriver.exe") # Carga Driver de FireFox

    func = Funciones_Globales(driver)  # Se crea el objeto para las Funciones
    func.navegar("http://sanbox.undostres.com.mx", tie) # Abre la pagina a Testear
    driver.maximize_window()  # Maximiza la pagina WEB

def teardown_function(function): # Esta Funcion Finaliza La prueba
    print("Finaliza Test")  # Imprime texto de finalización de la prueba
    driver.close()   # Cierra el Driver usado

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_logout")
def test_Recarga_Celular(): # Funcion de la prueba

    func.click_xpath_val("//input[@suggest='mobile-operator']",tie) # Entra al Menu para elegir Operador
    func.click_xpath_val("//b[contains(.,'Telcel')]",tie)           # Elige el operador Telefonico
    func.text_xpath_val("//input[contains(@onfocus,'mobileFieldFocusHandler(event)')]","8465433546",tie) # Digita el numero Celular
    func.click_xpath_val("//input[contains(@suggest,'mobile-operator_amount')]",tie) # Ingresa al Menu de Recargas
    func.click_xpath_val("//a[@href='javascript:void(0);'][contains(.,'$10Recarga $10')]",tie) # Selecciona la Recarga de 10 pesos
    time.sleep(2)  # Le da tiempo a la prueba para generar un ScreenShot

    allure.attach(driver.get_screenshot_as_png(), name="Recarga_Celular", attachment_type=AttachmentType.PNG) # Se genera ScreenShot de esta pantalla
    func.click_xpath_val("//button[contains(@data-qa,'celular-pay')]",tie) # Da Click en el boton Siguiente

    func.click_xpath_val("(//div[contains(@class,'rotatingGlyContainer')])[2]",tie)     # Selecciona el tipo de pago con Tajeta
    func.check_xpath_multiselect("//span[contains(.,'Usar nueva tarjeta')]",tie)        # Selecciona la opcion nueva tarjeta
    card = driver.find_element_by_xpath("//input[contains(@id,'cardnumberunique')]")    # Selecciona la casilla de nueva tarjeta para digitar el numero
    card.send_keys("4111111111111111"+Keys.TAB+"11"+Keys.TAB+"25")                      # Se Captura número de Tarjeta, mes y año de la Tarjeta
    func.text_xpath_val("//input[contains(@data-qa,'cvv-input')]","111",tie)            # SE introduce el CVV de la Tarjeta
    func.text_xpath_val("//input[contains(@class,'form-control email preventChromeAutofill')]","test@test.com",tie)  # Se introduce el correo electronico
    allure.attach(driver.get_screenshot_as_png(), name="Elegir_Tarjeta", attachment_type=AttachmentType.PNG) # Se genera captura de pantalla de esta
    func.click_xpath_val("(//span[@class='PaymentMethod'][contains(.,'Pagar con Tarjeta')])[2]",tie)    # Se da Click en boton de pagar con tarjeta
    time.sleep(2)  # Se le da tiempo a esta pantalla para hacer la captura de la misma

    func.text_xpath_val("//input[contains(@id,'usrname')]","automatizaciónUDT1@gmail.com",tie)      # Se Ingresa el usuario
    password = driver.find_element_by_xpath("//input[contains(@id,'psw')]")                         # Se busca el elemento password
    password.send_keys("automationUDT123"+Keys.TAB+Keys.BACKSPACE+Keys.ENTER)                       # Se escribe el password
                                                                                                    # y se da TABULADOR para pasar a la casilla
                                                                                                    # de no soy robot y se selecciona con barra espaciador
                                                                                                    # y se da enter para finalizar la recarga
    allure.attach(driver.get_screenshot_as_png(), name="Correo_envio", attachment_type=AttachmentType.PNG) # Se genera la captura de pantalla
    time.sleep(2)       # Se le da tiempo para hacer la caputra de pantalla

if __name__ == '__main__':
    unittest.main()