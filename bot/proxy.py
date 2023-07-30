from pathlib import Path
from typing import TYPE_CHECKING

from better_web3 import Proxy as _Proxy
from better_web3.utils import load_lines

if TYPE_CHECKING:
    from bot.zootools import ZooToolsAccount


class Proxy(_Proxy):
    def __init__(self, *args, number: int = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = number
        self.linked_accounts: list["ZooToolsAccount"] = []

    def __str__(self) -> str:
        if self.number: return f"[{self.number:03}] {super().__str__()}"
        return super().__str__()

    @classmethod
    def from_file(cls, filepath: Path | str) -> set["Proxy"]:
        proxy_lines = load_lines(filepath)
        proxies = set()
        for i, proxy_str in enumerate(proxy_lines, start=1):
            proxy = cls.from_str(proxy_str)
            proxy.number = i
            proxies.add(proxy)
        return proxies
