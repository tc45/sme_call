from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException
from paramiko.ssh_exception import AuthenticationException
import re

import logging

# minor change 2

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger('netmiko')


device1 = {
    'device_type': 'cisco_ios',
    'host': '172.31.22.134',
    'username': 'local',
    'password': 'local',
}
device2 = {
    'device_type': 'cisco_ios',
    'host': '172.31.22.200',
    'username': 'local',
    'password': 'local',
}
device3 = {
    'device_type': 'cisco_ios',
    'host': '172.31.22.134',
    'username': 'local',
    'password': 'wrongpass',
}

devices = [device1, device2, device3]


def main():
    for device in devices:
        print(f"\n\nAttempting to connect to device at IP/host: {device['host']}")
        # Instantiate object using the connection handler and device dictionary
        try:
            conn = ConnectHandler(**device)

            # Call ‘enable()’ method to elevate privilege
            conn.enable()

            # Call single_command function
            single_command(conn)

            # Call show route function
            show_route(conn)

            # Call multiple command function
            multiple_commands(conn)

        except NetmikoTimeoutException as err:
            print('Device timed out while attempting to connect')
        except NetmikoAuthenticationException as err:
            print('Authentication failed on device.  Try different credentials.')
        except AuthenticationException as err:
            print('Paramiko Authentication failed on device.  Try different credentials.')


def single_command(conn_obj):
    # Execute single command
    output = conn_obj.send_command('show ip int br', use_textfsm=True)
    print(output)

    for interface in output:
        print("Interface: " + interface['intf'])
        print("IP Address: " + interface['ipaddr'])


def show_route(conn_obj):
    # Execute single command
    output = conn_obj.send_command('show ip route', use_textfsm=True)
    #print(output)

    for routes in output:
        protocol = routes['protocol']
        if protocol == "B":
            protocol = "BGP"
        if protocol == "C":
            protocol = "Connected"
        print("Protocol: " + protocol)
        print("IP Address: " + routes['network'] + "/" + routes['mask'])
        print("Next Hop: " + routes['nexthop_ip'])


def multiple_commands(conn_obj):
    # Execute a group of config commands
    config_commands = [
        'interface Ethernet1/1',
        'ip address 10.1.1.1 255.255.255.0',
        'description WAN Interface to MPLS',
        'no shut',
    ]

    output = conn_obj.send_config_set(config_commands)
    output_split = output.split('\n')
    x = 0

    for line in output_split:
        if line != '':
            if re.search('% Invalid input', line) is not None:
                print('WARNING: Command failed to execute properly')
                print(output_split[x-2])
                print(output_split[x-1])
                print(line)
                return False
        x += 1
    print(output)
    return True
#
# # Create local file
# conn.send_command('copy running-config test.txt')
#
# # Check output for string
# if 'Destination filename' in output:
#     # If output found, send carriage return
#     output += conn.send_command_timing('\n')
#
# print(output)


def interactive_command(conn_obj):

    # Execute a command that will have prompts
    command = 'del test.txt'

    # Use ‘send_command_timing’ to enable delay-based command
    output = conn_obj.send_command_timing(command)

    # Check output for string
    if 'Delete filename' in output:
        # If output found, send carriage return
        output += conn_obj.send_command_timing('\n')

        # Check additional output for string.  If found, send ‘y’ and then carriage return
        if 'confirm' in output:
            output += conn_obj.send_command_timing('y\n')

    print(output)


main()




