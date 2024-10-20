#!/usr/bin/env python3
import os
import datetime
import subprocess
import time

# Locais dos diretórios de logs
LOG_DIR = "/home/eduardo/Área de trabalho/atividade1compass/logs"
ONLINE_LOG = os.path.join(LOG_DIR, "nginx_online.log")
OFFLINE_LOG = os.path.join(LOG_DIR, "nginx_offline.log")

# Função para verificar o status do serviço e permitir o loop a cada 5 min
def check_nginx_status():
    # Data e Hora atual
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Verifica o status do serviço Nginx
    service = "nginx"
    status_command = ["systemctl", "is-active", service]

    try:
        # Executa o comando para verificar o status do Nginx
        status_output = subprocess.check_output(status_command).strip().decode('utf-8')

        if status_output == "active":
            # Serviço está rodando
            with open(ONLINE_LOG, "a") as online_file:
                online_file.write(f"{current_time} - {service} - ONLINE - O serviço está rodando\n")
        else:
            # Serviço não está rodando
            with open(OFFLINE_LOG, "a") as offline_file:
                offline_file.write(f"{current_time} - {service} - OFFLINE - O serviço não está rodando\n")

    except subprocess.CalledProcessError:
        # Caso haja algum erro ao executar o comando
        with open(OFFLINE_LOG, "a") as offline_file:
            offline_file.write(f"{current_time} - {service} - OFFLINE - Erro ao verificar o status do serviço\n")

# Loop infinito para executar a cada 20 segundos
while True:
    check_nginx_status()
    # Aguarda 20 segundos
    time.sleep(20)
