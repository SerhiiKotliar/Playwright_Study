import asyncio

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=["--start-maximized", '--disable-blink-features=AutomationControlled']
        )

        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()

        await page.goto('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
        await page.wait_for_timeout(5000)
        await context.close()


if __name__ == '__main__':
    asyncio.run(main())