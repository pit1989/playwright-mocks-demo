# Playwright Mocks Demo

Учебный проект, демонстрирующий работу с сетевыми моками в Playwright.

## Что показано
- Перехват запросов через `page.route`
- Подмена ответов сервера (`fulfill`)
- Ожидание ответа через `expect_response`
- Проверка успешных и ошибочных сценариев (200, 400, 500)

## Установка

```bash
pip install -r requirements.txt
playwright install