import asyncio
from playwright.async_api import async_playwright, expect
from fake_useragent import FakeUserAgent


async def async_work():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            channel='chrome',
            headless=False,
            args=["--start-maximized"]
        )
        user_agent = FakeUserAgent().random
        print('UA полученный: ', user_agent)
        context = await browser.new_context(no_viewport=True, user_agent=user_agent)
        page = await context.new_page()
        await page.goto('https://whatmyuseragent.com/')

        el = page.locator("#ua")
        await expect(el).to_be_visible()
        ua = await el.inner_text()
        print('UA на странице: ', ua)
        await browser.close()


asyncio.run(async_work())
