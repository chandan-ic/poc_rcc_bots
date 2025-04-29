import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page1 = context.new_page()
    page1.goto("https://ikm.uat.gaindms.com/")
    page1.get_by_role("textbox", name="Dealer code").click()
    page1.get_by_role("textbox", name="Dealer code").fill("CR001")
    page1.get_by_role("textbox", name="Dealer code").press("Tab")
    page1.locator("#BranchSlno").select_option("72")
    page1.get_by_role("textbox", name="User Name").click()
    page1.get_by_role("textbox", name="User Name").fill("kadmin")
    page1.get_by_role("textbox", name="User Name").press("Tab")
    page1.get_by_role("textbox", name="Password").fill("K")
    page1.get_by_role("button", name="Log In").click()
    page1.get_by_role("link", name=" MIS ").click()
    page1.get_by_role("link", name=" Vehicle Reports").click()
    page1.locator("#TableContent #accordion div").filter(has_text="Purchase Supplierwise").locator("div").first.click()
    page1.locator("#TableContent").get_by_text("Supplierwise purchasesList of").click()
    page1.locator("input[name=\"ctl00\\$cpMain\\$FromDat\"]").click()
    page1.locator("#ctl00_cpMain_ClFromDate_prevArrow").click()
    page1.get_by_text("March,").click()
    page1.locator("#ctl00_cpMain_ClFromDate_prevArrow").click()
    page1.get_by_title("March, 2025").click()
    page1.get_by_title("Monday, April 01,").click()
    page1.locator("input[name=\"ctl00\\$cpMain\\$ToDat\"]").click()
    page1.locator("input[name=\"ctl00\\$cpMain\\$ToDat\"]").fill("31/04/2024")
    page1.locator("input[name=\"ctl00\\$cpMain\\$ToDat\"]").press("Tab")
    page1.get_by_role("link", name=" View Report").click()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
