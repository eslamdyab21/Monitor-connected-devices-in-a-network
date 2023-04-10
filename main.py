import sys
from Monitor import Monitor

# ex: python3 main.py 192.168.1.0/24
monitor = Monitor()

monitor.detect_devices(cider_network=sys.argv[1])
