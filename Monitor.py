import subprocess


class Monitor():
    def __init__(self):
        pass

    def detect_devices(self, cider_network):
        
        # nmap command to find devices
        cmd = f'sudo nmap -sn {cider_network}'
        nmap_original_msg = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)

        nmap_original_msg = str(nmap_original_msg.stdout)
        connected_devices_split_lst = nmap_original_msg.split('\n')

        # getting only devices mac addresses
        connected_devices_mac_lst = []
        for line in connected_devices_split_lst:
            if 'MAC Address' in line:
                connected_devices_mac_lst.append(line.split()[2])

        return nmap_original_msg, connected_devices_mac_lst