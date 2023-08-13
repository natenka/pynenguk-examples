import time


for num in range(10):
    print(num, end=" ", flush=True)
    time.sleep(0.5)
print()

# for num in range(15, 0, -1):
#     print(f"\r{num:<3}", end="", flush=True)
#     time.sleep(0.5)
