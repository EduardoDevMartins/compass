

Nginx Server Status Checker

Este script em Python verifica periodicamente o status de um servidor Nginx e gera logs de status a cada 5 minutos. Ele foi projetado para ajudar na supervisão de servidores web, registrando informações sobre a disponibilidade e saúde do Nginx para monitoramento e diagnóstico.

Funcionalidades

- Verifica se o servidor Nginx está em funcionamento.
- Relata logs de status a cada 5 minutos.
- Registra mensagens de erro caso o servidor esteja offline ou inoperante.

Requisitos

- **Python 3.6+**
- Bibliotecas: `requests` (para monitorar status) e `logging` (para gerar logs)

Instalação das Dependências

Para instalar as dependências necessárias, execute:

```bash
pip install requests
```

Como Usar

1. Clone o Repositório:
    ```bash
    git clone https://github.com/seu-usuario/nginx-status-checker.git
    cd nginx-status-checker
    ```

2. Configuração:
   - No código, defina o endereço do servidor Nginx que você deseja monitorar. Exemplo:
     ```python
     SERVER_URL = "http://localhost"  # Substitua pelo IP ou domínio do seu servidor
     ```

3. Executar o Script:
    ```bash
    python nginx_status_checker.py
    ```

O script irá verificar o status do servidor Nginx e registrar os logs de status a cada 20 segundos.

Exemplo de Log de Status

Cada verificação gera um log indicando se o servidor está operacional. Exemplo de log:

```
2024-11-01 12:00:00 - INFO - Servidor Nginx está funcionando normalmente.
2024-11-01 12:05:00 - ERROR - Falha ao conectar ao servidor Nginx.
```



Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.
