import sys
from Monitor import Monitor

monitor = Monitor()

connected_devices = monitor.detect_devices(cider_network=sys.argv[1])
print(connected_devices)