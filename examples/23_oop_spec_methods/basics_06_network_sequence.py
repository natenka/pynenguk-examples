from ipaddress import ip_network


class Network:
    def __init__(self, network, mask):
        self.network = network
        self.mask = mask
        net = ip_network(f"{self.network}/{self.mask}")
        self.hosts = [str(ip) for ip in net.hosts()]

    def __str__(self):
        return f"{self.network}/{self.mask}"

    def __repr__(self):
        return f"Network('{self.network}', {self.mask})"

    def __len__(self):
        return len(self.hosts) + 2

    def __getitem__(self, index):
        print(f"__getitem__ {index=}")
        return self.hosts[index]


if __name__ == "__main__":
    net1 = Network("10.1.1.0", 29)
    print(net1)
    print(net1.hosts)
    print(net1[0])
    print(net1[-1])
    print(net1[0:4])
    print("10.1.1.1" in net1)
    for ip in net1:
        print(ip)
