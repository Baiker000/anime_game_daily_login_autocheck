import os
from genshin import GenshinClient, InvalidCookies, AlreadyClaimed

async def do_check():
    cookies = os.getenv('HOYO_API').split(' ')
    for cookie in cookies:
        crumbs = cookie.split(':')
        if len(crumbs[0]) < 2:
            continue
        char_cookies = {'ltuid': crumbs[0], 'ltoken': crumbs[1]}
        character = GenshinClient(char_cookies)
        try:
            await character.claim_daily_reward()
            print('Success')
        except (InvalidCookies, AlreadyClaimed) as e:
            print(e)

import asyncio
asyncio.run(do_check())
