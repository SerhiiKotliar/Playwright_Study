import asyncio
import re

from playwright.async_api import async_playwright, expect


async def example_get_by_role():
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
        ua = await page.get_by_role("heading", name=re.compile("Mozilla", re.IGNORECASE)).text_content()
        print(ua)

        # получаю кнопку для копирования
        copy_button = await page.get_by_role('link', name='copy').inner_html()
        print(copy_button)

        # получаю текст логотипа
        logo_text = await page.get_by_role('link', name=re.compile("WhatMy", re.IGNORECASE)).inner_text()
        print(logo_text)

        # пробежимся по всем значениям списка что есть на странице
        for li in await page.get_by_role('listitem').all():
            text = await li.inner_text()
            print(text)

        await browser.close()


async def example_get_by_locator():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            channel='chrome',
            headless=False,
            args=["--start-maximized"]
        )
        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()
        await page.goto('https://whatmyuseragent.com/')

        ua = await page.locator('#ua').text_content()
        print(ua)

        # пробежимся по всем значениям списка что есть на странице
        for li in await page.locator('li').all():
            text = await li.inner_text()
            print(text)

        # получим текст с параграфов с классом card-text
        paragraph = await page.locator('p.card-text').all()
        for p in paragraph:
            print(await p.inner_text())

        img = await page.locator('img').get_attribute('src')
        print(img)

        await asyncio.sleep(600)
        await browser.close()


async def example_filter():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            channel='chrome',
            headless=False,
            args=["--start-maximized"]
        )
        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()
        await page.goto('https://whatmyuseragent.com/')

        # получаем текст из элемента списка, содержащий "Country Name"
        el_1 = await page.get_by_role("listitem").filter(has_text="Country Name").inner_text()
        print(el_1)

        # получаем текст из элемента списка, содержащий "Country Name"
        el_2 = await page.locator("li").filter(has_text="Country Name").inner_text()
        print(el_2)

        # получаем 4-й элемент списка не содержащий "Country Name"
        el_3 = await page.locator("li").filter(has_not_text="Country Name").nth(4).inner_text()
        print(el_3)

        el_4 = await page.locator('nav').get_by_role('link').filter(has_text=".com").inner_text()
        print(el_4)
        await asyncio.sleep(600)
        await browser.close()




asyncio.run(example_filter())
