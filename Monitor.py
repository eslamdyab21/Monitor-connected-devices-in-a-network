import subprocess


class Monitor():
    def __init__(self):
        pass

    def detect_devices(self, cider_network):
        
        cmd = f'sudo nmap -sn {cider_network}'
        connected_devices = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
        connected_devices = str(connected_devices.stdout)

        connected_devices.find('MAC Address')
        return connected_devices