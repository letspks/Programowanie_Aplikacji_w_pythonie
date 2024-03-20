print("Hello World")
#help(print)

from os import getcwd
current_path=getcwd()
print(current_path)

import czas
print("1 Aktualny czas z pliku czas.py:", czas.aktualny_czas)
import time
time.sleep(2)
import importlib
print("2 Aktualny czas z pliku czas.py:", czas.aktualny_czas)
importlib.reload(czas)
print("3 Aktualny czas z pliku czas.py:", czas.aktualny_czas)