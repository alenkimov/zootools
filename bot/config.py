from better_web3.utils import load_toml
from pydantic import BaseModel

from bot.logger import LoggingLevel
from bot.paths import CONFIG_TOML


class Config(BaseModel):
    LOGGING_LEVEL: LoggingLevel = "INFO"
    ANTICAPTCHA_API_KEY: str
    FORM_ID: str
    SITE_KEY: str


CONFIG = Config(**load_toml(CONFIG_TOML))
