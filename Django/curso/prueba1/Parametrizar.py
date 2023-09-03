import re
import time
import random
import pytest
import sys
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import funciones_globales
from confi_test import set_up , set_up_val_num,set_up_val_pass

#pytest confi_test.py -s -v
#pytest sesion3.py -s -v --browser-channel=chrome -n 4
#playwright codegen https://www.saucedemo.com/v1/
#pytest -s -v Parametrizar.py -n 3 --html=reportes1.html --self-contained-html --capture=tee-sys
#pytest Parametrizar.py -s -v -n2 --template=html1/index.html --report=reporte_tres.html
#https://pypi.org/project/pytest-html/
#https://pypi.org/project/pytest-reporter-html1/

tiempo=0.5
ruta="Proyecto_2/Django/"  
pdf1="C:/Proyecto_2/Django/curso/prueba1/pdf/Pensión Juan Agosto 2023.pdf"
url="https://www.saucedemo.com/v1/"

# def test_sesion1(set_up)-> None:
#     page=set_up
#     f=funciones_globales(page)
#     #f.validar_texto("Swag Labs")
    
# def test_sesion2(set_up)-> None:
#     page=set_up
#     f=funciones_globales(page)
#     #f.validar_texto("Swag Labs")
    
#     f.click("(//button[contains(@class,'btn_primary btn_inventory')])[1]",tiempo)
#     f.click("(//button[contains(@class,'btn_primary btn_inventory')])[3]",tiempo)
#     f.esperar(2)
    
# def test_sesion3(set_up)-> None:
#     page=set_up
#     f=funciones_globales(page)
#     #f.validar_texto("Swag Labs")
    
#     f.click("//button[contains(.,'Open Menu')]",tiempo)
#     f.click("//a[contains(@id,'link')][@class='bm-item menu-item'][contains(.,'Reset App State')]",tiempo)
#     f.esperar(2)
    
# def test_sesion4(set_up)-> None:
#     page=set_up
#     f=funciones_globales(page)
#     #f.validar_texto("Swag Labs")
    
    
#     f.click("//button[contains(.,'Close Menu')]",tiempo)
#     f.esperar(3)
#     f.click("(//button[contains(@class,'btn_primary btn_inventory')])[1]",tiempo)
#     f.click("(//button[contains(@class,'btn_primary btn_inventory')])[3]",tiempo)
#     f.esperar(3)
#     f.click("//button[contains(.,'Open Menu')]",tiempo)
#     f.click("//a[contains(@id,'link')][@class='bm-item menu-item'][contains(.,'Logout')]",tiempo)
#     f.esperar(2)
    
def test_sesion_val_nombre(set_up_val_num):
    page=set_up_val_num
    f=funciones_globales(page)
    texto=f.validar_texto("//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this service')]","Epic sadface: Username and password do not match any user in this service",tiempo)
    print(texto)
    texto_esperar="Epic sadface: Username and password do not match any user in this servicee" 
    assert texto_esperar in str(texto),"error nombre"
    f.esperar(3)
    
def test_sesion_val_password(set_up_val_pass):
    page=set_up_val_pass
    f=funciones_globales(page)
    texto=f.validar_texto("//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this service')]","Epic sadface: Username and password do not match any user in this service",tiempo)
    print(texto)
    texto_esperar="Epic sadface: Username and password do not match any user in this service" 
    assert texto_esperar in str(texto),"error nombre"
    f.esperar(3)