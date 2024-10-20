import os
import datetime
import subprocess

# Folder where I put the Results
LOG_DIR = "/home/eduardo/Área de trabalho/atividade1compass/logs"
ONLINE_LOG = os.path.join(LOG_DIR, "nginx_online.log")
OFFLINE_LOG = os.path.join(LOG_DIR, "nginx_offline.log")

# DATE And TIME
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#Validate the status of service
service = "nginx"
status_command = ["systemctl", "is-active", service]

try:
    status_output = subprocess.check_output(status_command).strip().decode('utf-8')

    if status_output == "active":
        
        with open(ONLINE_LOG, "a") as online_file:
            online_file.write(f"{current_time} - {service} - ONLINE - O serviço está rodando\n")
    else:
        with open(OFFLINE_LOG, "a") as offline_file:
            offline_file.write(f"{current_time} - {service} - OFFLINE - O serviço não está rodando\n")

except subprocess.CalledProcessError:
    with open(OFFLINE_LOG, "a") as offline_file:
        offline_file.write(f"{current_time} - {service} - OFFLINE - Erro ao verificar o status do serviço\n")
