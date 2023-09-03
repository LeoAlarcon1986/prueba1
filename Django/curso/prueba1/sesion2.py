import re
import time
import random
import pytest
import sys
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import funciones_globales
from confi_test import set_up

#pytest confi_test.py -s -v
#playwright codegen https://www.saucedemo.com/v1/

tiempo=0.5
ruta="Proyecto_2/Django/"  
pdf1="C:/Proyecto_2/Django/curso/prueba1/pdf/Pensión Juan Agosto 2023.pdf"
url="https://www.saucedemo.com/v1/"

def test_sesion1(set_up)-> None:
    page=set_up
    f=funciones_globales(page)
    #f.validar_texto("Swag Labs")
    
def test_sesion2(set_up)-> None:
    page=set_up
    f=funciones_globales(page)
    #f.validar_texto("Swag Labs")
    
    f.click("(//button[contains(@class,'btn_primary btn_inventory')])[1]",tiempo)
    f.click("(//button[contains(@class,'btn_primary btn_inventory')])[3]",tiempo)
    f.esperar(2)
    
def test_sesion3(set_up)-> None:
    page=set_up
    f=funciones_globales(page)
    #f.validar_texto("Swag Labs")
    
    f.click("//button[contains(.,'Open Menu')]",tiempo)
    f.click("//a[contains(@id,'link')][@class='bm-item menu-item'][contains(.,'Reset App State')]",tiempo)
    f.esperar(2)
    
def test_sesion4(set_up)-> None:
    page=set_up
    f=funciones_globales(page)
    #f.validar_texto("Swag Labs")
    
    
    f.click("//button[contains(.,'Close Menu')]",tiempo)
    f.esperar(3)
    f.click("(//button[contains(@class,'btn_primary btn_inventory')])[1]",tiempo)
    f.click("(//button[contains(@class,'btn_primary btn_inventory')])[3]",tiempo)
    f.esperar(3)
    f.click("//button[contains(.,'Open Menu')]",tiempo)
    f.click("//a[contains(@id,'link')][@class='bm-item menu-item'][contains(.,'Logout')]",tiempo)
    f.esperar(2)