import aiohttp
import pyuseragents

from bot.proxy import Proxy


class CustomClientSession(aiohttp.ClientSession):
    def __init__(self, *args, proxy: Proxy = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.proxy = proxy

    async def _request(self, method: str, url, proxy: Proxy = None, **kwargs):
        proxy = proxy or self.proxy
        proxy_url = None
        if proxy: proxy_url = proxy.as_url
        return await super()._request(method, url, proxy=proxy_url, **kwargs)

    def set_random_useragent(self):
        self.headers.update({'user-agent': pyuseragents.random()})


class ZooToolsAPI(CustomClientSession):
    def __init__(self, proxy: Proxy = None, **kwargs):
        headers = {
            'authority': 'audience-consumer-api.zootools.co',
            'accept': '*/*',
            'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer',
            'content-type': 'application/json',
            'origin': 'https://form.zootools.co'
        }

        super().__init__(headers=headers, **kwargs)
        self.proxy = proxy
        self.set_random_useragent()

    async def enter_raffle(
            self,
            form_id: str,
            invite_code: str,
            email: str,
            address: str,
            captcha_token: str,
            proxy: Proxy = None,
    ):
        url = f'https://audience-consumer-api.zootools.co/v3/lists/{form_id}/members'

        payload = {
            'utmSource': '',
            'utmMedium': '',
            'utmCampaign': '',
            'utmTerm': '',
            'utmContent': '',
            'pageReferrer': '',
            'email': email,
            'cryptoAddress': address,
            'hiddenFields': {
                'productId': '',
                'projectId': '',
                'teamId': '',
                'userId': '',
            },
            'captchaToken': captcha_token,
            'referral': invite_code,
        }

        response = await self.request("POST", url, json=payload, proxy=proxy)
        data = await response.json()
        return data
