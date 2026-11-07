import pytest
import re
from playwright.sync_api import Page, expect

def test_open_wikipedia(page: Page):
    page.goto("https://ru.wikipedia.org/")
    
    # Проверяем, что в заголовке ЕСТЬ слово "Википедия" (неважно, что идет дальше)
    expect(page).to_have_title(re.compile("Википедия"))
    # 3. Ищем поле поиска и вводим текст
    search_input = page.get_by_role("searchbox")
    search_input.fill("Python")
    
    # 4. Нажимаем Enter (или кликаем по кнопке поиска)
    search_input.press("Enter")
    
    # 5. Ждем загрузки и проверяем, что в заголовке появилось слово "Python"
    expect(page).to_have_title("Python — Википедия")

# Тест 2: Логин на SauceDemo (новый)
def test_successful_login(page: Page):
    # 1. Открываем сайт
    page.goto("https://www.saucedemo.com/")
    
    # 2. Вводим логин и пароль
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    
    # 3. Кликаем по кнопке "Login"
    page.locator("#login-button").click()
    
    # 4. ПРОВЕРКА: Убеждаемся, что мы попали внутрь
    expect(page.locator(".title")).to_have_text("Products")

        # 👇 ДОБАВЬТЕ ЭТУ СТРОКУ 👇
    # Браузер подождет 3 секунды (3000 мс) перед закрытием
    page.wait_for_timeout(3000) 