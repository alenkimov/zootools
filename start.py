import questionary

from bot.author import TG_LINK
from bot.scripts import register_accounts
from bot.config import CONFIG, CONFIG_TOML
from bot.input import PROXIES, PROXIES_TXT
from bot.logger import logger, setup_logger


def main():
    setup_logger(CONFIG.LOGGING_LEVEL)

    if not PROXIES:
        logger.error(f"Put your proxies into {PROXIES_TXT}")
        return

    if not CONFIG.ANTICAPTCHA_API_KEY:
        logger.error(f"Put your AntiCaptcha API Token into {CONFIG_TOML}")
        return

    print(f"Telegram: {TG_LINK}")
    invite_code = questionary.text("Enter invite code:").ask()
    number_of_accounts = questionary.text("Enter accounts number:").ask()
    number_of_accounts = int(number_of_accounts)
    register_accounts(invite_code, number_of_accounts)


if __name__ == '__main__':
    main()
