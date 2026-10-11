from playwright.sync_api import expect

def nastroyit_mok(page, status, message):
    def obrabotka(zapros):
        status_text = "ok" if status == 200 else "error"
        zapros.fulfill(
            status=status,
            content_type="application/json",
            body=f'{{"status": "{status_text}", "message": "{message}"}}'
        )
    page.route("**/api/buy", obrabotka)

def test_successful_buy(page):
    nastroyit_mok(page, 200, "Товар успешно куплен")

    page.goto("https://example.com")  # заглушка

    with page.expect_response("**/api/buy") as otvet_info:
        page.click("button:has-text('Купить')")

    otvet = otvet_info.value
    assert otvet.status == 200
    expect(page.get_by_text("Товар успешно куплен")).to_be_visible()


def test_not_enough_money(page):
    nastroyit_mok(page, 400, "Недостаточно средств")

    page.goto("https://example.com")

    with page.expect_response("**/api/buy") as otvet_info:
        page.click("button:has-text('Купить')")

    otvet = otvet_info.value
    assert otvet.status == 400
    expect(page.get_by_text("Недостаточно средств")).to_be_visible()


def test_server_error(page):
    nastroyit_mok(page, 500, "Ошибка сервера")
    page.goto("https://example.com")

    with page.expect_response("**/api/buy") as otvet_info:
        page.click("button:has-text('Купить')")

    otvet = otvet_info.value
    assert otvet.status == 500
    expect(page.get_by_text("Ошибка сервера")).to_be_visible()