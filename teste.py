import tkinter as tk
from tkinter import filedialog
import pyautogui
import pyperclip

def selecionar_pasta():
    pasta = filedialog.askdirectory(title="Selecione uma pasta")
    if pasta:
        caminho_entry.delete(0, tk.END)
        caminho_entry.insert(0, pasta)
        pyperclip.copy(pasta)

def colar_caminho():
    pyautogui.hotkey('ctrl', 'v')

# Configuração da janela principal
root = tk.Tk()
root.title("Selecionar Pasta e Colar Caminho")
root.geometry("500x150")

# Botão para selecionar a pasta
botao_selecionar = tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta)
botao_selecionar.pack(pady=10)

# Campo de entrada para exibir o caminho da pasta
caminho_entry = tk.Entry(root, width=60)
caminho_entry.pack(pady=10)

# Botão para colar o caminho
botao_colar = tk.Button(root, text="Colar Caminho", command=colar_caminho)
botao_colar.pack(pady=10)

root.mainloop()