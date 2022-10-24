import pynput

def on_press(key):
    if key == pynput.keyboard.KeyCode.from_char("a") or key == pynput.keyboard.KeyCode.from_char("A"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('4')

    elif key == pynput.keyboard.KeyCode.from_char("e") or key == pynput.keyboard.KeyCode.from_char("E"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('3')

    elif key == pynput.keyboard.KeyCode.from_char("ı") or key == pynput.keyboard.KeyCode.from_char("I"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('1')

    elif key == pynput.keyboard.KeyCode.from_char("o") or key == pynput.keyboard.KeyCode.from_char("O"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('0')

    elif key == pynput.keyboard.KeyCode.from_char("s") or key == pynput.keyboard.KeyCode.from_char("S"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('5')

    elif key == pynput.keyboard.KeyCode.from_char("i") or key == pynput.keyboard.KeyCode.from_char("İ"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('1')

    elif key == pynput.keyboard.KeyCode.from_char("g") or key == pynput.keyboard.KeyCode.from_char("G"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('6')

    elif key == pynput.keyboard.KeyCode.from_char("b") or key == pynput.keyboard.KeyCode.from_char("B"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('8')

    elif key == pynput.keyboard.KeyCode.from_char("q"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('Q')

    elif key == pynput.keyboard.KeyCode.from_char("w"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('W')

    elif key == pynput.keyboard.KeyCode.from_char("r"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('R')

    elif key == pynput.keyboard.KeyCode.from_char("t"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('T')

    elif key == pynput.keyboard.KeyCode.from_char("y"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('Y')

    elif key == pynput.keyboard.KeyCode.from_char("u"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('U')

    elif key == pynput.keyboard.KeyCode.from_char("p"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('P')

    elif key == pynput.keyboard.KeyCode.from_char("ğ"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('Ğ')

    elif key == pynput.keyboard.KeyCode.from_char("ü"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('Ü')

    elif key == pynput.keyboard.KeyCode.from_char("d"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('D')

    elif key == pynput.keyboard.KeyCode.from_char("f"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('F')

    elif key == pynput.keyboard.KeyCode.from_char("h"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('H')

    elif key == pynput.keyboard.KeyCode.from_char("j"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('J')

    elif key == pynput.keyboard.KeyCode.from_char("k"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('K')

    elif key == pynput.keyboard.KeyCode.from_char("l"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('L')

    elif key == pynput.keyboard.KeyCode.from_char("ş"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('Ş')

    elif key == pynput.keyboard.KeyCode.from_char("z"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('Z')

    elif key == pynput.keyboard.KeyCode.from_char("x"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('X')

    elif key == pynput.keyboard.KeyCode.from_char("c"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('C')

    elif key == pynput.keyboard.KeyCode.from_char("v"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('V')

    elif key == pynput.keyboard.KeyCode.from_char("n"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('N')

    elif key == pynput.keyboard.KeyCode.from_char("m"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('M')

    elif key == pynput.keyboard.KeyCode.from_char("ö"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('Ö')

    elif key == pynput.keyboard.KeyCode.from_char("ç"):
        pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
        pynput.keyboard.Controller().press('Ç')

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
