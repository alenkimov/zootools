from bot.proxy import Proxy
from bot.paths import PROXIES_TXT

PROXIES: set[Proxy] = Proxy.from_file(PROXIES_TXT)
