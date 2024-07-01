import pyautogui
import time
import pygetwindow as gw

op=int(input("Qual deseja realizar? 1-Janelas abertas ou 2-Posição do mouse"))

if op == 1:
    print("Janelas encontradas:")
    for window in gw.getAllTitles():
        print(window)

else:
    def should_stop():
        return pyautogui.position() == (0, 0)  # Condição de parada (por exemplo, quando o cursor estiver na posição [0, 0])

    with open('saida.txt', 'w') as f:
        while not should_stop():
            position = pyautogui.position()
            f.write('{}\n'.format(position))
            time.sleep(1)
