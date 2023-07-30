from pathlib import Path

from better_web3.utils import copy_file

SCRIPT_DIR = Path(__file__).parent
BASE_DIR = SCRIPT_DIR.parent

CONFIG_DIR = BASE_DIR / "config"
DEFAULT_CONFIG_DIR = CONFIG_DIR / "default"
INPUT_DIR  = BASE_DIR / "input"
INPUT_DIR.mkdir(exist_ok=True)

DEFAULT_CONFIG_TOML = DEFAULT_CONFIG_DIR / "config.toml"
CONFIG_TOML = CONFIG_DIR / "config.toml"
copy_file(DEFAULT_CONFIG_TOML, CONFIG_TOML)

PROXIES_TXT = INPUT_DIR / "proxies.txt"
PROXIES_TXT.touch(exist_ok=True)
