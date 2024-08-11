import asyncio
import re

from playwright.async_api import async_playwright, expect


async def example_wait():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            channel='chrome',
            headless=False,
            args=["--start-maximized"]
        )
        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()
        await page.goto('https://whatmyuseragent.com/')

        # получаем User Agent
        ua = page.get_by_role("heading", name=re.compile("Mozilla", re.IGNORECASE))

        # проверяем что элемент прикреплен к странице
        await expect(ua).to_have_count()

        # достаем текст
        ua_text = await ua.inner_text()
        print(ua_text)

        await browser.close()


asyncio.run(example_wait())
