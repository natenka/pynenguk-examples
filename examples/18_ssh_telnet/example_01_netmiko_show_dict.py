from pprint import pprint
from netmiko import Netmiko, NetmikoBaseException
from paramiko.ssh_exception import SSHException
import yaml


def get_show_output(device_params, show_list):
    if type(show_list) == str:
        show_list = [show_list]

    cmd_output_dict = {}
    try:
        with Netmiko(**device_params) as ssh:
            ssh.enable()
            for cmd in show_list:
                out = ssh.send_command(cmd)
                cmd_output_dict[cmd] = out
        return cmd_output_dict
    except (NetmikoBaseException, SSHException) as error:
        print(error)


if __name__ == "__main__":
    cmd_list = ["sh clock", "sh ip int br"]
    with open("devices.yaml") as f:
        device_list = yaml.safe_load(f)
    for device in device_list:
        result = get_show_output(device, cmd_list)
        pprint(result, width=120)
