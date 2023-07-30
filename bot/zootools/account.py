from better_web3 import Wallet

from bot.utils import generate_email
from bot.proxy import Proxy


class ZooToolsAccount:
    wallet:      Wallet
    proxy:       Proxy | None

    def __init__(
            self,
            wallet: Wallet,
            email: str,
            *,
            proxy: Proxy = None,
    ):
        self.wallet = wallet
        self.email = email
        self.proxy = proxy
        self.proxy.linked_accounts.append(self)

    @classmethod
    def generate(cls, proxy: Proxy = None) -> "ZooToolsAccount":
        wallet = Wallet.generate()
        email = generate_email()
        return cls(wallet, email, proxy=proxy)

    def __str__(self):
        return str(self.proxy)
