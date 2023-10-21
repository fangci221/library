from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:8080/#/dashboard")
    page.get_by_label("帳號").click()
    page.get_by_label("帳號").fill("user1")
    page.get_by_label("帳號").press("Tab")
    page.locator("#password").fill("12345678")
    page.get_by_role("button", name="登入").click()
    page.get_by_role("link", name="館藏查詢").click()
    page.get_by_placeholder("Search").click()
    page.get_by_placeholder("Search").fill("hi")
  
    # Because I can't use all functions by the page I created
    # Please help me to add some actions:
    # 1. add book "hi" to collective

    context.close()
    browser.close()


def main():
    with sync_playwright() as playwright:
        run(playwright)
