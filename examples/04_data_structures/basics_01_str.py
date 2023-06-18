from pprint import pprint


line = "test"
text = "interface Tunnel0\n ip address 10.10.10.1 255.255.255.0\n ip mtu 1416"

if True:
    text2 = """
    interface Tunnel0
     ip address 10.10.10.1 255.255.255.0
     ip mtu 1416
    """
print(text2)
pprint(text2, width=120)


line = ("test"
        "hello")
line = (
    "test"
    "hello"
)
print(line)

text3 = (
    "interface Tunnel0\n"
    " ip address 10.10.10.1 255.255.255.0\n"
    " ip mtu 1416\n"
)
print(text3)
pprint(text3)
