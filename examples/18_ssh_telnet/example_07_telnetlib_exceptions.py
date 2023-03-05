from pprint import pprint
import telnetlib


def get_cisco_show_output(host, username, password, enable_pass, command):
    try:
        with telnetlib.Telnet(host, timeout=5) as t:
            t.read_until(b'Username:')
            t.write(f"{username}\n".encode("utf-8"))
            t.read_until(b'Password')
            t.write(f"{password}\n".encode("utf-8"))
            login_output = t.read_until(b'>', timeout=5).decode("utf-8")
            if "Login invalid" in login_output:
                raise ConnectionError(f"Authentication failed on device {host}")

            t.write(b"enable\n")
            t.read_until(b'Password')
            t.write(f"{enable_pass}\n".encode("utf-8"))
            enable_output = t.read_until(b'#', timeout=5).decode("utf-8")
            if "Password" in enable_output:
                raise ConnectionError(f"Enable authentication failed on device {host}")

            t.write(b"terminal length 0\n")
            boutput = t.read_until(b'#', timeout=5)

            t.write(f"{command}\n".encode("utf-8"))
            boutput = t.read_until(b'#', timeout=5)
            output = boutput.decode("utf-8").replace("\r\n", "\n")
            return output
    except OSError as error:
        print(error)


if __name__ == "__main__":
    out = get_cisco_show_output("192.168.100.1", "cisco", "cisco", "cisco", "sh ip int br")
    pprint(out, width=120)
