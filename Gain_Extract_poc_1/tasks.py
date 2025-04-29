from playwright.sync_api import sync_playwright
import datetime
import os

def run():
    today = datetime.date.today()
    year = str(today.year)
    month = "1"  # January (You can make it dynamic if needed)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        # Login
        page.goto("https://ikm.uat.gaindms.com/")
        page.fill("input[name='txtDealerCode']", "CR001")
        page.press("input[name='txtDealerCode']", "Tab")
        page.select_option("select[name='ddlBranch']", "72")
        page.fill("input[name='txtUserName']", "kadmin")
        page.press("input[name='txtUserName']", "Tab")
        page.fill("input[name='txtPassword']", "")
        page.click("input[name='btnLogin']")

        # Navigate to the report
        page.get_by_role("link", name=" MIS ").click()
        page.get_by_role("link", name=" Vehicle Reports").click()

        page.locator("#TableContent").get_by_text("Target vs Achieved Report").click()

        # Wait for popup and click "View Report"
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.get_by_role("link", name=" View Report").click()

        # Select Month and Year
        page.select_option("select[name='ctl00$cpMain$MonthNo']", month)
        page.fill("input[name='ctl00$cpMain$YearNo']", year)

        # Open Report in New Tab
        with page.expect_popup() as popup_info:
            page.get_by_role("link", name=" View Report").click()
        report_page = popup_info.value

        # Download Excel
        with report_page.expect_download() as download_info:
            report_page.get_by_role("button", name="Export to Excel").click()
        download = download_info.value

        # Save the download
        filename = f"Target_vs_Achieved_{year}_{month.zfill(2)}.xlsx"
        download.save_as(os.path.join("output", filename))
        print(f"Downloaded: output/{filename}")

        context.close()
        browser.close()


if __name__ == "__main__":
    run()
