
Nginx Server Status Monitor

Este script em Python monitora o status do servidor Nginx, registrando o status atual do serviço em arquivos de log. Ele é executado continuamente, verificando o status do Nginx a cada 20 segundos e gerando logs separadamente para status "ONLINE" e "OFFLINE".

Funcionalidades

- Verifica periodicamente o status do serviço Nginx.
- Registra o status em arquivos de log separados para monitoramento fácil.
- Permite configurar a frequência de verificação, com a opção padrão de 20 segundos.

Configuração

1. Diretórios de Log:
   - O script utiliza diretórios específicos para armazenar os logs de status. No código, você pode definir o caminho onde deseja salvar esses logs:
   ```python
   LOG_DIR = "/caminho/para/seu/diretorio/logs"
   ONLINE_LOG = os.path.join(LOG_DIR, "nginx_online.log")
   OFFLINE_LOG = os.path.join(LOG_DIR, "nginx_offline.log")
   ```
   - Substitua `"/caminho/para/seu/diretorio/logs"` pelo caminho onde deseja salvar os logs.

2. Permissões:
   - Verifique se você possui permissões de escrita no diretório de log especificado.
   - O script utiliza `systemctl` para verificar o status do Nginx. Certifique-se de ter permissões de execução para esse comando.

Como Usar

1. Clone o Repositório:
   ```bash
   git clone https://github.com/seu-usuario/nginx-status-checker.git
   cd nginx-status-checker
   ```

2. Execute o Script:
   ```bash
   python3 script.py
   ```
   - O script será executado continuamente e registrará o status do Nginx a cada 20 segundos nos arquivos de log configurados.

Logs de Status

Os logs serão salvos em dois arquivos separados:
- **nginx_online.log**: contém entradas quando o serviço está em funcionamento.
- **nginx_offline.log**: contém entradas para status "OFFLINE" ou erros ao tentar verificar o status.

Exemplo de Log

```
2024-11-01 12:00:00 - nginx - ONLINE - O serviço está rodando
2024-11-01 12:05:00 - nginx - OFFLINE - O serviço não está rodando
2024-11-01 12:10:00 - nginx - OFFLINE - Erro ao verificar o status do serviço
```

Contribuições

Contribuições são bem-vindas! Abra uma *issue* ou envie um *pull request* para melhorias.

