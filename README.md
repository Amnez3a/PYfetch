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

### Перевод скрипта в Bin'арный файл

```bash
pip install pyinstaller # ( CLI )
# pip install auto-py-to-exe ( GUI)

# создание бинарного файла ( в одном файле )
pyinstaller --onefile PYfetch.py
```