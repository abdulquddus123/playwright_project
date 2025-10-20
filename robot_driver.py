import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

async def main():
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)  # Set True if you don't want UI
            context = await browser.new_context()
            page = await context.new_page()

            # Step 1: Go to URL
            try:
                await page.goto("https://www.saucedemo.com", timeout=15000)
                print("✅ Page loaded successfully")
            except PlaywrightTimeoutError:
                print("❌ Page took too long to load")
                return

            # Step 2: Type username
            try:
                await page.fill("input[data-test='username']", "standard_user", timeout=5000)
            except PlaywrightTimeoutError:
                print("❌ Username field not found")
                return

            # Step 3: Type password
            try:
                await page.fill("input[data-test='password']", "secret_sauce", timeout=5000)
            except PlaywrightTimeoutError:
                print("❌ Password field not found")
                return

            # Step 4: Click login button
            try:
                await page.click("input[data-test='login-button']", timeout=5000)
                print("✅ Login attempt completed")
            except PlaywrightTimeoutError:
                print("❌ Login button not found")
                return

            # Step 5: Wait for products page
            try:
                await page.wait_for_selector(".inventory_item", timeout=10000)
                print("✅ Logged in successfully")
            except PlaywrightTimeoutError:
                print("❌ Product page didn't load after login")
                return

            # Step 6: Get product price
            try:
                product_name = "Sauce Labs Backpack"
                product_locator = page.locator("//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']")
                price = await product_locator.locator(".inventory_item_price").inner_text()
                print(f"✅ Success! Product '{product_name}' found with price: {price}")
            except Exception:
                print("❌ Failed to locate product or price")
            
            await browser.close()

    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
