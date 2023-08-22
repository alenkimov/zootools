# zootools.co forms script
[ [Telegram канал](https://t.me/cum_insider) ]

- [Запуск под Windows](#Запуск-под-Windows)
- [Запуск под Ubuntu](#Запуск-под-Ubuntu)
- [Работа со скриптом](#Работа-со-скриптом)


## Запуск под Windows
- Установите [Python 3.11](https://www.python.org/downloads/windows/). Не забудьте поставить галочку напротив "Add Python to PATH".
- Установите пакетный менеджер [Poetry](https://python-poetry.org/docs/) вручную по [этой инструкции](https://teletype.in/@alenkimov/poetry).
- Установите MSVC и Пакет SDK для Windows по [этой инструкции](https://teletype.in/@alenkimov/web3-installation-error). Без этого при попытке установить библиотеку web3 будет возникать ошибка "Microsoft Visual C++ 14.0 or greater is required".
- Установите [git](https://git-scm.com/download/win). Это позволит с легкостью получать обновления скрипта командой `git pull`
- Откройте консоль в удобном месте...
  - Склонируйте (или [скачайте](https://github.com/alenkimov/zootools/archive/refs/heads/master.zip)) этот репозиторий:
    ```bash
    git clone https://github.com/alenkimov/zootools
    ```
  - Перейдите в папку проекта:
    ```bash
    cd zootools
    ```
  - Установите требуемые зависимости следующей командой или запуском файла `INSTALL.bat`:
    ```bash
    poetry install
    ```
  - Запустите скрипт следующей командой или запуском файла `START.bat`:
    ```bash
    poetry run python start.py
    ```


## Запуск под Ubuntu
- Обновите систему:
```bash
sudo apt update && sudo apt upgrade -y
```
- Установите [git](https://git-scm.com/download/linux) и screen:
```bash
sudo apt install screen git -y
```
- Установите Python 3.11 и зависимости для библиотеки web3:
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.11 python3.11-dev build-essential libssl-dev libffi-dev -y
ln -s /usr/bin/python3.11/usr/bin/python
```
- Установите [Poetry](https://python-poetry.org/docs/):
```bash
curl -sSL https://install.python-poetry.org | python -
export PATH="/root/.local/bin:$PATH"
```
- Склонируйте этот репозиторий:
```bash
git clone https://github.com/alenkimov/zootools
```
- Перейдите в папку проекта:
```bash
cd zootools
```
- Установите требуемые библиотеки:
```bash
poetry install
```
- Запустите скрипт:
```bash
poetry run python start.py
```


## Работа со скриптом
После первого запуска в папке проекта появятся:
- Папка `input` с файлом `proxies.txt`
- В папке `config` файл `config.toml`

В файл `proxies.txt` нужно поместить прокси. 
Поддерживаются большинство форматов.

Основной файл конфигурации это `config.toml`. Вот самые важные настройки, о которых стоит знать:
- `ANTICAPTCHA_API_KEY`: API ключ сервиса [AntiCaptcha](http://getcaptchasolution.com/tmb2cervod)
- `FORM_ID`: ID формы, который можно взять из ссылки формы.
По умолчанию `bLFJhrGfkOoEQgt3I3LR`,
что ссылается на форму [reveel](https://form.zootools.co/go/bLFJhrGfkOoEQgt3I3LR)
- `SITE_KEY`: sitekey для решения капчи. По умолчанию `0x4AAAAAAABCOgX4x6RvmA0a`,
что ссылается на форму [reveel](https://form.zootools.co/go/bLFJhrGfkOoEQgt3I3LR)

При запуске скрипт спросит инвайт код и количество рефералов, которое нужно накрутить.
