import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QInputDialog, QMessageBox, QLineEdit, QHBoxLayout, QGroupBox, QGridLayout
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt
# Back End
def change_dns():
    sudo_password, ok = QInputDialog.getText(None, "Senha do sudo", "Digite a senha do sudo:", QLineEdit.Password)
    if ok and sudo_password:
        interface = "Wi-Fi"
        dns1 = "8.8.8.8"
        dns2 = "1.1.1.1"
        command = f"echo {sudo_password} | sudo -S networksetup -setdnsservers {interface} {dns1} {dns2}"
        try:
            os.system(command)
            custom_messagebox("Sucesso", f"DNS alterado para {dns1} e {dns2}.", "logo-ifood-512.png")
        except Exception as e:
            custom_messagebox("Erro", f"Ocorreu um erro ao alterar o DNS: {e}", "logo-ifood-512.png")
    else:
        custom_messagebox("Aviso", "Senha não fornecida. Ação cancelada.", "logo-ifood-512.png")
def clear_system_cache():
    sudo_password, ok = QInputDialog.getText(None, "Senha do usuário", "Digite a senha do usuário:", QLineEdit.Password)
    if ok and sudo_password:
        command = 'sudo rm -rf /Library/Caches/*'
        os.system(f'echo {sudo_password} | sudo -S {command}')
        custom_messagebox("Sucesso", "Cache do sistema limpo.", "logo-ifood-512.png")
    else:
        custom_messagebox("Aviso", "Senha não fornecida. Ação cancelada.", "logo-ifood-512.png")
def clear_user_cache():
    os.system('rm -rf ~/Library/Caches/*')
    custom_messagebox("Sucesso", "Cache do usuário limpo.", "logo-ifood-512.png")
def clear_chrome_cache():
    cache_path = os.path.expanduser('~/Library/Caches/Google/Chrome/Default/Cache')
    if os.path.exists(cache_path):
        os.system(f'rm -rf {cache_path}')
        custom_messagebox("Sucesso", "Cache do Google Chrome limpo.", "logo-ifood-512.png")
    else:
        custom_messagebox("Aviso", "Cache do Google Chrome não encontrado.", "logo-ifood-512.png")
def uninstall_google_chrome():
    try:
        sudo_password, ok = QInputDialog.getText(None, "Senha do sudo", "Digite a senha do sudo:", QLineEdit.Password)
        if ok and sudo_password:
            subprocess.run(["pkill", "Google Chrome"], check=True)
            command = 'sudo rm -rf /Applications/Google\\ Chrome.app'
            os.system(f'echo {sudo_password} | sudo -S {command}')
            subprocess.run(["rm", "-rf", os.path.expanduser("~/Library/Application Support/Google/Chrome")], check=True)
            custom_messagebox("Sucesso", "Google Chrome foi desinstalado com sucesso.", "logo-ifood-512.png")
        else:
            custom_messagebox("Aviso", "Senha não fornecida. Ação cancelada.", "logo-ifood-512.png")
    except subprocess.CalledProcessError as e:
        custom_messagebox("Erro", f"Ocorreu um erro ao desinstalar o Google Chrome: {e}", "logo-ifood-512.png")
def restart_core_audio():
    sudo_password, ok = QInputDialog.getText(None, "Senha do sudo", "Digite a senha do sudo:", QLineEdit.Password)
    if ok and sudo_password:
        try:
            # Comando para reiniciar o Core Audio
            command = 'sudo killall coreaudiod'
            os.system(f'echo {sudo_password} | sudo -S {command}')
            custom_messagebox("Sucesso", "Core Audio reiniciado com sucesso.", "logo-ifood-512.png")
        except Exception as e:
            custom_messagebox("Erro", f"Erro ao reiniciar o Core Audio: {e}", "logo-ifood-512.png")
    else:
        custom_messagebox("Aviso", "Senha não fornecida. Ação cancelada.", "logo-ifood-512.png")
def reinstall_camera_drivers():
    sudo_password, ok = QInputDialog.getText(None, "Senha do sudo", "Digite a senha do sudo:", QLineEdit.Password)
    if ok and sudo_password:
        try:
            # Comandos para reiniciar o serviço da câmera e remover arquivos de configuração
            commands = [
                'sudo killall VDCAssistant',
                'sudo killall AppleCameraAssistant',
                'sudo rm -rf /Library/Preferences/com.apple.iokit.AVCVideoCap.plist',
                'sudo rm -rf /Library/Preferences/com.apple.iokit.BroadcomBluetoothHostControllerUSBTransport.plist'
            ]
            for command in commands:
                os.system(f'echo {sudo_password} | sudo -S {command}')
            custom_messagebox("Sucesso", "Drivers da câmera reinstalados com sucesso.", "logo-ifood-512.png")
        except Exception as e:
            custom_messagebox("Erro", f"Erro ao reinstalar os drivers da câmera: {e}", "logo-ifood-512.png")
    else:
        custom_messagebox("Aviso", "Senha não fornecida. Ação cancelada.", "logo-ifood-512.png")
def install_forticlient_vpn():
    sudo_password, ok = QInputDialog.getText(None, "Senha do sudo", "Digite a senha do sudo:", QLineEdit.Password)
    if ok and sudo_password:
        try:
            # Comando para instalar o FortiClient VPN
            command = 'sudo apt-get install forticlient'
            os.system(f'echo {sudo_password} | sudo -S {command}')
            custom_messagebox("Sucesso", "FortiClient VPN instalado com sucesso.", "logo-ifood-512.png")
        except Exception as e:
            custom_messagebox("Erro", f"Erro ao instalar o FortiClient VPN: {e}", "logo-ifood-512.png")
    else:
        custom_messagebox("Aviso", "Senha não fornecida. Ação cancelada.", "logo-ifood-512.png")
# Front End
class LoadingDialog(QWidget):
    def __init__(self, message="Carregando..."):
        super().__init__()
        self.setWindowTitle("Aguarde")
        self.setFixedSize(200, 200)
        self.setModal(True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.QWidget)
        layout = QVBoxLayout()
        self.label = QLabel(message, self)
        self.label.setAlignment(Qt.AlignCenter)
def create_gui():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Gerenciador de Cache e Aplicativos")
    window.setFixedSize(1140, 570)
    # Adicionando imagem de fundo
    
    window.setStyleSheet(f"""
        QWidget {{
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        QLabel {{ font-size: 18px; font-weight: bold; color: #D32F2F; }}
        QPushButton {{
            font: bold 14px; background-color: #D32F2F; color: white; border-radius: 12px; padding: 15px;
            margin-bottom: 10px; border: none; transition: all 0.3s;
        }}
        QPushButton:hover {{ background-color: #B71C1C; transform: scale(1.05); }}
        QPushButton:pressed {{ background-color: #E57373; transform: scale(0.98); }}
        QGroupBox {{ background-color: #FFFFFF; border-radius: 10px; padding: 20px; margin-bottom: 20px; }}
        QGroupBox::title {{ font-size: 20px; color: #D32F2F; }}
        QMessageBox {{ font-size: 16px; }}
    """)
    main_layout = QVBoxLayout()
    # Layout superior com logo e texto
    top_layout = QHBoxLayout()
    top_layout.setAlignment(Qt.AlignCenter)
    image_label = QLabel()
    pixmap = QPixmap("logo-ifood-512.png")
    pixmap = pixmap.scaled(130, 130, Qt.KeepAspectRatio)
    image_label.setPixmap(pixmap)
    image_label.setAlignment(Qt.AlignLeft)
    texto_orientacao = QLabel("iTech Auto Suporte")
    texto_orientacao.setAlignment(Qt.AlignCenter)
    texto_orientacao.setFixedSize(400, 130)  # Define o mesmo tamanho da imagem
    texto_orientacao.setStyleSheet("font-size: 40px; font-weight: bold; color: #D32F2F;")
    # Adicionando widgets ao layout superior
    top_layout.addWidget(image_label, alignment=Qt.AlignLeft)
    top_layout.addSpacing(30)  # Espaçamento entre imagem e texto
    top_layout.addWidget(texto_orientacao, alignment=Qt.AlignCenter)
    main_layout.addLayout(top_layout)
    # Layout de 3 colunas (Cache, Aplicativos, Ajustes do Sistema)
    grid_layout = QGridLayout()
    # GroupBox para Gerenciamento de Cache
    cache_group = QGroupBox("Gerenciamento de Cache")
    cache_layout = QVBoxLayout()
    cache_buttons = [
        ("Limpar o Sistema", clear_system_cache, "data-cleaning_5143301.png"),
        ("Limpar Cache do Usuário", clear_user_cache, "programmer_560277.png"),
        ("Limpar o Google Chrome", clear_chrome_cache, "trash_7263081.png"),
    ]
    for text, func, icon in cache_buttons:
        button = create_button_with_icon(text, func, icon)
        cache_layout.addWidget(button)
    cache_group.setLayout(cache_layout)
    grid_layout.addWidget(cache_group, 0, 0)
    # GroupBox para Gerenciamento de Aplicativos
    app_group = QGroupBox("Gerenciamento de Aplicativos")
    app_layout = QVBoxLayout()
    app_buttons = [
        ("Reparar Google Chrome", uninstall_google_chrome, "google-symbol_2875331.png"),
        ("Reparar VPN", install_forticlient_vpn, "vpn_5322131.png")
    ]
    for text, func, icon in app_buttons:
        button = create_button_with_icon(text, func, icon)
        app_layout.addWidget(button)
    app_group.setLayout(app_layout)
    grid_layout.addWidget(app_group, 0, 1)
    # GroupBox para Ajustes do Sistema
    system_group = QGroupBox("Ajustes do Sistema")
    system_layout = QVBoxLayout()
    dns_button = create_button_with_icon("Reconfigurar Wifi", change_dns, "wifi_3962035.png")
    audio_button = create_button_with_icon("Reparar Audio", restart_core_audio, "volume_5759566.png")
    camera_button = create_button_with_icon("Reparar Câmera", reinstall_camera_drivers, "videocall_14355311.png")
    system_layout.addWidget(dns_button)
    system_layout.addWidget(audio_button)
    system_layout.addWidget(camera_button)
    system_group.setLayout(system_layout)
    grid_layout.addWidget(system_group, 0, 2)
    main_layout.addLayout(grid_layout)
    window.setLayout(main_layout)
    window.show()
    app.exec_()
# Função para criar botão com ícone ao lado do texto
def create_button_with_icon(text, func, icon_path):
    button_layout = QHBoxLayout()
    button_label = QLabel()
    pixmap = QPixmap(icon_path)
    pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)
    button_label.setPixmap(pixmap)
    button_label.setAlignment(Qt.AlignCenter)
    button = QPushButton(text)
    button.clicked.connect(func)
    button.setFixedHeight(60)
    button.setStyleSheet("margin-left: 10px;")
    button_layout.addWidget(button_label)
    button_layout.addWidget(button)
    container = QWidget()
    container.setLayout(button_layout)
    return container
# Função para criar uma messagebox personalizada com imagem
def custom_messagebox(title, message, image_path):
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    pixmap = QPixmap(image_path)
    pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)
    msg_box.setIconPixmap(pixmap)
    msg_box.exec_()
if __name__ == "__main__":
    create_gui()