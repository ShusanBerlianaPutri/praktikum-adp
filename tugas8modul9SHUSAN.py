import time
import os
from termcolor import cprint

def loading_screen():
    os.system("cls")
    cprint("====================================", "cyan")
    cprint("   SELAMAT DATANG DI APLIKASI HEBAT ", "cyan")
    cprint("====================================", "cyan")
    cprint("        (^_^)                       ", "yellow")
    time.sleep(2)
    print()
    cprint("Sedang memulai aplikasi, mohon ditunggu!", "green")
    print()

    for i in range(5):
        titik = "."* (i * 2 + 1)
        cprint("Memuat" + titik, "green")
        time.sleep(0.5)
    print()
    cprint("Pemprosesan selesai!","cyan")
    print()
    cprint("Aplikasi berhasil dimuat!, selamat menggunakan!", "green")  

loading_screen()
