import asyncio
from typing import Iterable

from aiohttp import ContentTypeError
from tqdm.asyncio import tqdm

from bot.zootools import ZooToolsAPI, ZooToolsAccount
from bot.anticaptcha import TurnstileProxyless
from bot.config import CONFIG
from bot.proxy import Proxy
from bot.input import PROXIES
from bot.logger import logger


async def register_zootools_account(account: ZooToolsAccount, invite_code: str):
    async with TurnstileProxyless() as solver:
        solver.set_key(CONFIG.ANTICAPTCHA_API_KEY)
        solver.set_website_url(f"https://form.zootools.co/go/{CONFIG.FORM_ID}")
        solver.set_website_key(CONFIG.SITE_KEY)

        logger.info(f"{account} Solving captcha...")
        g_response = await solver.solve_and_return_solution()
        if g_response == 0:
            logger.error(f"{account} Solving task finished with an error. AntiCaptcha error code: {solver.error_code}")
            return
        else:
            logger.debug(f"{account} Captcha token: {g_response}")

    async with ZooToolsAPI() as zootools:
        try:
            data = await zootools.enter_raffle(
                CONFIG.FORM_ID,
                invite_code,
                account.email,
                account.wallet.address,
                g_response,
                proxy=account.proxy,
            )
            logger.debug(f"{account} {data}")
            logger.success(f"{account} Invited!")
        except ContentTypeError as e:
            logger.error(f"{account} Вместо JSON ответ пришел в TEXT/HTML")
            return


async def _generate_accounts_and_process_for_proxy(
        proxy: Proxy,
        invite_code: str,
        number_of_accounts: int,
):
    for _ in range(number_of_accounts):
        account = ZooToolsAccount.generate(proxy)
        await register_zootools_account(account, invite_code)


async def _register_accounts(invite_code: str, number_of_accounts: int, proxies: Iterable[Proxy]):
    proxies = list(proxies)
    proxies_count = len(proxies)

    # Determine the number of accounts to create for each proxy
    accounts_per_proxy = number_of_accounts // proxies_count
    remaining_accounts = number_of_accounts % proxies_count

    # Launch a coroutine for each proxy to generate and process accounts
    tasks = []
    for i, proxy in enumerate(proxies):
        # Distribute remaining accounts among first few proxies
        accounts_count = accounts_per_proxy + (i < remaining_accounts)

        task = _generate_accounts_and_process_for_proxy(proxy, invite_code, accounts_count)
        tasks.append(task)

    await tqdm.gather(*tasks)


def register_accounts(invite_code: str, number_of_accounts: int):
    asyncio.run(_register_accounts(invite_code, number_of_accounts, PROXIES))
