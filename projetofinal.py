import os
import subprocess
import tkinter as tk
import gdown
from tkinter import Label, simpledialog, messagebox, Toplevel
from PIL import Image, ImageTk
# Suprimir aviso de depreciação do Tk
os.environ['TK_SILENCE_DEPRECATION'] = '1'
def create_gui():
    root = tk.Tk()
    root.title("Gerenciador de Cache e Aplicativos")
    root.geometry("400x400")
    root.config(bg="white")
    texto_orientacao = Label(root, text="Clique no que deseja fazer", bg="white")
    texto_orientacao.pack(pady=10)
    tk.Button(root, text="Limpar Cache do Sistema", font=("poppins", 16, "bold"), bg="blue", fg="white", command=clear_system_cache).pack(pady=5)
    tk.Button(root, text="Limpar Cache do Usuário", font=("poppins", 16, "bold"), bg="blue", fg="white", command=clear_user_cache).pack(pady=5)
    tk.Button(root, text="Limpar Cache do Google Chrome", font=("poppins", 16, "bold"), bg="blue", fg="white", command=clear_chrome_cache).pack(pady=5)
    tk.Button(root, text="Desinstalar Google Chrome", font=("poppins", 16, "bold"), bg="blue", fg="white", command=uninstall_google_chrome).pack(pady=5)
    tk.Button(root, text="Instalar Google Chrome", font=("poppins", 16, "bold"), bg="blue", fg="white", command=install_chrome_with_homebrew).pack(pady=5)
    tk.Button(root, text="Desinstalar Slack", font=("poppins", 16, "bold"), bg="blue", fg="white", command=uninstall_slack).pack(pady=5)
    tk.Button(root, text="Instalar Slack", font=("poppins", 16, "bold"), bg="blue", fg="white", command=install_slack_with_homebrew).pack(pady=5)
    tk.Button(root, text="Instalar Fortclient", font=("poppins", 16, "bold"), bg="blue", fg="white", command=install_fortclient).pack(pady=5)
    root.mainloop()
# Função para criar uma messagebox personalizada com imagem
def custom_messagebox(title, message, image_path):
    top = Toplevel()
    top.title(title)
    # Carregar a imagem
    try:
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)
        # Criar um label para a imagem
        img_label = Label(top, image=img)
        img_label.image = img  # Manter uma referência para evitar coleta de lixo
        img_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível carregar a imagem: {e}")
        top.destroy()
        return
    # Criar um label para a mensagem
    msg_label = Label(top, text=message)
    msg_label.pack(pady=10)
    # Criar um botão OK para fechar a janela
    ok_button = tk.Button(top, text="OK", command=top.destroy)
    ok_button.pack(pady=10)
    # Centralizar a janela na tela
    top.update_idletasks()
    width = top.winfo_width()
    height = top.winfo_height()
    x = (top.winfo_screenwidth() // 2) - (width // 2)
    y = (top.winfo_screenheight() // 2) - (height // 2)
    top.geometry(f'{width}x{height}+{x}+{y}')
    # Tornar a janela modal
    top.grab_set()
    top.wait_window()
# Funções backend
# Limpar cache do sistema
def clear_system_cache():
    sudo_password = simpledialog.askstring("Senha do sudo", "Digite a senha do sudo:", show='*')
    if sudo_password:
        command = 'sudo rm -rf /Library/Caches/*'
        os.system(f'echo {sudo_password} | sudo -S {command}')
        messagebox.showinfo("Sucesso", "Cache do sistema limpo.")
    else:
        messagebox.showwarning("Aviso", "Senha não fornecida. Ação cancelada.")
# Limpar cache do usuário
def clear_user_cache():
    os.system('rm -rf ~/Library/Caches/*')
    messagebox.showinfo("Sucesso", "Cache do usuário limpo.")
# Limpar cache do Chrome
def clear_chrome_cache():
    # Caminho do cache do Google Chrome no macOS
    cache_path = os.path.expanduser('~/Library/Caches/Google/Chrome/Default/Cache')
    if os.path.exists(cache_path):
        os.system(f'rm -rf {cache_path}')
        messagebox.showinfo("Sucesso", "Cache do Google Chrome limpo.")
    else:
        messagebox.showwarning("Aviso", "Cache do Google Chrome não encontrado.")
# Desinstalar o Google Chrome
def uninstall_google_chrome():
    try:
        sudo_password = simpledialog.askstring("Senha do sudo", "Digite a senha do sudo:", show='*')
        if sudo_password:
            subprocess.run(["pkill", "Google Chrome"], check=True)
            command = 'sudo rm -rf /Applications/Google\\ Chrome.app'
            os.system(f'echo {sudo_password} | sudo -S {command}')
            subprocess.run(["rm", "-rf", os.path.expanduser("~/Library/Application Support/Google/Chrome")], check=True)
            messagebox.showinfo("Sucesso", "Google Chrome foi desinstalado com sucesso.")
        else:
            messagebox.showwarning("Aviso", "Senha não fornecida. Ação cancelada.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao desinstalar o Google Chrome: {e}")
# Instalar Fortclient
def install_fortclient():
    try:
        output = 'fortclient.gz'  # ou 'meu_pacote.tar.gz'
        # Baixar o arquivo
        gdown.download('https://drive.google.com/drive/folders/1pSByYA53xR1ESRCzxyAf2hpNiuxjnImK', output, quiet=False)
        # Instalar o pacote
        sudo_password = simpledialog.askstring("Senha do sudo", "Digite a senha do sudo:", show='*')
        if sudo_password:
            command = f'pip install {output}'
            os.system(f'echo {sudo_password} | sudo -S {command}')
            messagebox.showinfo("Sucesso", "Fortclient instalado com sucesso.")
        else:
            messagebox.showwarning("Aviso", "Senha não fornecida. Ação cancelada.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao instalar o fortclient: {e}")
# Reinstalar o Google Chrome
def install_chrome_with_homebrew():
    try:
        subprocess.run(["brew", "install", "--cask", "google-chrome"], check=True)
        messagebox.showinfo("Sucesso", "Google Chrome instalado com sucesso.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao instalar o Google Chrome: {e}")
# Desinstalar o Slack
def uninstall_slack():
    try:
        sudo_password = simpledialog.askstring("Senha do sudo", "Digite a senha do sudo:", show='*')
        if sudo_password:
            subprocess.run(["pkill", "Slack"], check=True)
            command = 'sudo rm -rf /Applications/Slack.app'
            os.system(f'echo {sudo_password} | sudo -S {command}')
            subprocess.run(["rm", "-rf", os.path.expanduser("~/Library/Application Support/Slack")], check=True)
            messagebox.showinfo("Sucesso", "Slack foi desinstalado com sucesso.")
        else:
            messagebox.showwarning("Aviso", "Senha não fornecida. Ação cancelada.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao desinstalar o Slack: {e}")
# Reinstalar o Slack
def install_slack_with_homebrew():
    try:
        subprocess.run(["brew", "install", "--cask", "slack"], check=True)
        messagebox.showinfo("Sucesso", "Slack instalado com sucesso.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao instalar o Slack: {e}")
# Interface gráfica com Tkinter - Frontend
if __name__ == "__main__":
    create_gui()
