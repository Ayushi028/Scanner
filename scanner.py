import pywifi
from pywifi import const
import time

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Get the first wireless interface

    iface.scan()  # Start scanning
    time.sleep(2)  # Wait for scan results

    results = iface.scan_results()

    print(f"{'SSID':<30} {'Signal Strength (dBm)':>20}")
    print("-" * 50)

    for network in results:
        ssid = network.ssid
        signal = network.signal  # Signal strength in dBm
        print(f"{ssid:<30} {signal:>20}")

if __name__ == "__main__":
    scan_wifi()
