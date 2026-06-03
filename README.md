# PYfetch
## Подобная программа fastfetch'а на python
***
**Использование:**
```bash
PYfetch.py [-h] [--only {pc,user,desktop,other}] [--no-art] [--custom-art CUSTOM_ART] [--logo {windows,macos,linux}]
```

**Значения аргументов:**
- `--only` - показ определенной информации
- `--no-art` - без ascii арта
- `--logo` - определенный логотип (macos, linux, windows)
- `--custom-art` - кастомный ascii арт (пока не работает)

***

## Установка

**Через pip:**
```bash
pip install pyneofetch --break-system-packages
pyfetch # пока что название будет pyFETCH, потом сменю
```
**Напрямую с GitHub:**
```bash
git clone https://github.com/Amnez3a/PYfetch/releases/download/release_ver/PYfetch # бинарный файл
sudo mv PYfetch /usr/local/bin/ # /bin/ || ~/.local/bin/
```
