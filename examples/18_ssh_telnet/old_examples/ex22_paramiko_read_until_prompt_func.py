import paramiko
import time
from pprint import pprint
import socket
import re


def cisco_send_show_commands(
    host, username, password, enable_pass, commands, max_read=60000,
    pause=0.5,
):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=host,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )
    with client.invoke_shell() as ssh:
        ssh.settimeout(2)

        ssh.send("enable\n")
        ssh.send(f"{enable_pass}\n")
        time.sleep(pause)
        ssh.recv(max_read)
        ssh.send(f"terminal length 0\n")
        time.sleep(pause)
        read_output = ssh.recv(max_read).decode("utf-8")
        prompt = re.search(r"\S+#", read_output).group()

        if type(commands) == str:
            commands = [commands]
        result = {}
        for cmd in commands:
            ssh.send(f"{cmd}\n")
            output = read_until_prompt(ssh, prompt)
            result[cmd] = output
        return result


def read_until_prompt(ssh, prompt, pause=0.2, max_read=60000):
    command_output = ""
    ssh.settimeout(5)
    while True:
        time.sleep(pause)
        try:
            part = ssh.recv(max_read).decode("utf-8")
        except socket.timeout:
            break
        command_output += part
        if prompt in part:
            break
    return command_output


if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    for ip in ip_list:
        out = cisco_send_show_commands(
            ip, "cisco", "cisco", "cisco", ["sh ip int br", "sh clock"]
        )
        #pprint(out)
        break
