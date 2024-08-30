import pyautogui
import time
import pygetwindow as gw
import tkinter as tk
from tkinter import messagebox, scrolledtext

def listar_janelas_abertas_terminal():
    """Lista todas as janelas abertas no sistema no terminal."""
    print("Janelas encontradas:")
    for window in gw.getAllTitles():
        print(window)

def registrar_posicao_mouse_terminal():
    """Registra a posição do mouse até que a posição seja (0, 0) no terminal."""
    def should_stop():
        return pyautogui.position() == (0, 0)
    
    print("Registrando a posição do mouse. Mova o cursor para (0, 0) para parar.")
    with open('saida.txt', 'w') as f:
        while not should_stop():
            position = pyautogui.position()
            f.write('{}\n'.format(position))
            print(f"Posição registrada: {position}")
            time.sleep(1)
    print("Gravação de posição do mouse interrompida. Veja 'saida.txt' para os resultados.")

def listar_janelas_abertas():
    """Lista todas as janelas abertas no sistema e exibe em uma janela de texto."""
    janela_resultados = tk.Toplevel(root)
    janela_resultados.title("Janelas Abertas")
    
    texto = scrolledtext.ScrolledText(janela_resultados, wrap=tk.WORD, width=40, height=10)
    texto.pack(padx=10, pady=10)
    
    texto.insert(tk.END, "Janelas encontradas:\n")
    for window in gw.getAllTitles():
        texto.insert(tk.END, f"{window}\n")

def registrar_posicao_mouse():
    """Registra a posição do mouse até que a posição seja (0, 0) e exibe instruções e posições em tempo real."""
    def should_stop():
        return pyautogui.position() == (0, 0)

    janela_instrucoes = tk.Toplevel(root)
    janela_instrucoes.title("Monitor de Posição do Mouse")

    instrucao = tk.Label(janela_instrucoes, text="Registrando a posição do mouse. Mova o cursor para (0, 0) para parar.")
    instrucao.pack(padx=10, pady=10)

    texto = scrolledtext.ScrolledText(janela_instrucoes, wrap=tk.WORD, width=40, height=10)
    texto.pack(padx=10, pady=10)

    def atualizar_posicao_mouse():
        """Função para atualizar a posição do mouse em tempo real."""
        if should_stop():
            messagebox.showinfo("Processo Concluído", "Gravação de posição do mouse interrompida. Veja 'saida.txt' para os resultados.")
            janela_instrucoes.destroy()
            return
        position = pyautogui.position()
        texto.insert(tk.END, f'Posição atual: {position}\n')
        texto.see(tk.END)
        with open('saida.txt', 'a') as f:
            f.write('{}\n'.format(position))
        janela_instrucoes.after(1000, atualizar_posicao_mouse)  # Atualiza a cada segundo

    with open('saida.txt', 'w') as f:  # Limpa o arquivo antes de começar a gravar
        pass
    
    atualizar_posicao_mouse()  # Inicia a atualização da posição do mouse

def iniciar_gui():
    """Inicia a interface gráfica do usuário."""
    global root
    root = tk.Tk()
    root.title("Monitor de Atividades")

    label = tk.Label(root, text="Escolha uma ação:", font=("Helvetica", 14))
    label.pack(pady=10)

    botao_janelas = tk.Button(root, text="Listar Janelas Abertas", command=listar_janelas_abertas, bg="#4CAF50", fg="white", font=("Helvetica", 12), width=25)
    botao_janelas.pack(pady=5)

    botao_mouse = tk.Button(root, text="Registrar Posição do Mouse", command=registrar_posicao_mouse, bg="#008CBA", fg="white", font=("Helvetica", 12), width=25)
    botao_mouse.pack(pady=5)

    root.geometry("400x200")
    root.mainloop()

def main():
    """Função principal para iniciar o programa no terminal ou GUI."""
    escolha = input("Deseja usar a interface gráfica? (s/n): ").lower()
    if escolha == 's':
        iniciar_gui()
    else:
        while True:
            try:
                op = int(input("Qual deseja realizar? 1-Janelas abertas ou 2-Posição do mouse: "))
                if op == 1:
                    listar_janelas_abertas_terminal()
                    break
                elif op == 2:
                    registrar_posicao_mouse_terminal()
                    break
                else:
                    print("Por favor, digite 1 ou 2.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número (1 ou 2).")

if __name__ == "__main__":
    main()
