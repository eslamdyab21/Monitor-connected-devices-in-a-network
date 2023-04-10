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

        devices_mac_name_dict = self.map_mac_to_names(connected_devices_mac_lst)

        for mac_address, name in devices_mac_name_dict.items():
            print(mac_address + ' ---> ' + name)
    


    def map_mac_to_names(self, connected_devices_mac_lst):
        devices_mac_name_dict = {}
        # record known devices that are in the .mac2names.txt file 
        with open('.mac2names.txt','r') as file_handler:
            for line in file_handler.readlines():
                mac_address, name = line.split()
                mac_address = mac_address.upper()

                if mac_address in connected_devices_mac_lst:
                    devices_mac_name_dict[mac_address] = name


        # record unknown devices
        for mac_address in connected_devices_mac_lst:
            if mac_address not in devices_mac_name_dict.keys():
                devices_mac_name_dict[mac_address] = '***Unknown***'


        return devices_mac_name_dict
