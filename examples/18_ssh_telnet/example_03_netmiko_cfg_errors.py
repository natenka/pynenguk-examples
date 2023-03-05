from pprint import pprint
from netmiko import Netmiko, NetmikoBaseException, ConfigInvalidException
from paramiko.ssh_exception import SSHException
import yaml


def configure_net_devices(device_params, commands):
    try:
        with Netmiko(**device_params) as ssh:
            ssh.enable()
            cmd_output = ssh.send_config_set(commands, error_pattern="%")
        return cmd_output
    except ConfigInvalidException:
        raise
    except (NetmikoBaseException, SSHException) as error:
        print(error)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        device_list = yaml.safe_load(f)
    r1 = device_list[0]
    result = configure_net_devices(r1, "lging 10.1.1.1")
    pprint(result)
