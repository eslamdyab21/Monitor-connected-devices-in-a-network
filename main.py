import sys
from Monitor import Monitor

monitor = Monitor()

nmap_original_msg, connected_devices_lst = monitor.detect_devices(cider_network=sys.argv[1])
print(nmap_original_msg)
print('--------------')
print(connected_devices_lst)