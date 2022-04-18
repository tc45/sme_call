from vmanage.api.authentication import Authentication
from vmanage.api.device import Device
from vmanage.data.template_data import TemplateData
from vmanage.api.device_templates import DeviceTemplates
import tabulate
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os

# Disable Insecure Warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

host = '10.10.20.90'
username = 'admin'
password = 'C1sco12345'
vmanage_port = 8443


def save_to_text(filename, payload):
    if right(filename, 4) != ".txt":
        filename = filename + ".txt"

    text_file = open(filename, 'w')
    text_file.write(payload)
    text_file.close()
    print("File " + filename + " has been saved.")


def print_template_table(templates):
    print("Formatting template output")

    headers = [
        'Template Name',
        'Description',
        'Device Type',
        'Feature Templates',
    ]

    table = []

    for template in templates:
        general_templates = ''
        for subTemplate in template['generalTemplates']:
            general_templates += subTemplate['templateName'] + '\n'

        row = [
            template['templateName'],
            template['templateDescription'],
            template['deviceType'],
            general_templates,
        ]
        table.append(row)

    try:
        print(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
    except UnicodeEncodeError:
        print(tabulate.tabulate(table, headers, tablefmt="grid"))



def print_device_table(devices):
    print("Formatting device output")

    headers = [
        'Host-Name',
        'Device Type',
        'Device ID',
        'Serial Number',
        'System IP',
        'Site ID',
        'Version',
        'Device Model',
        'Template',
    ]

    table = []
    return_list = []

    for device in devices:
        if 'host-name' in device and 'system-ip' in device:
            if not 'template' in device:
                device['template'] = ""
            row = [
                device['host-name'],
                device['deviceType'],
                device['uuid'],
                device['serialNumber'],
                device['system-ip'],
                device['site-id'],
                device['version'],
                device['deviceModel'],
                device['template'],
            ]
            return_row = [
                device['host-name'],
                device['uuid']
            ]
            # if 'template' in device:
            #     row.append(device['template'])
            table.append(row)
            return_list.append(return_row)

    try:
        print(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
    except UnicodeEncodeError:
        print(tabulate.tabulate(table, headers, tablefmt="grid"))
    return return_list


def get_running_config(device_list, template_instantiation):
    for hostname, uuid in device_list:
        device_config = template_instantiation.get_device_running_config(uuid)
        filename = hostname + ".txt"
        save_to_text(filename, device_config)


def main():
    vmanage_host = host
    vmanage_username = username
    vmanage_password = password

    session = Authentication(host=vmanage_host, user=vmanage_username, password=vmanage_password, port=vmanage_port).login()
    #print(session.cookies._cookies[vmanage_host]["/"]["JSESSIONID"])

    # Instantiate new device object to use the Device library
    device = Device(session, vmanage_host, port=vmanage_port)
    # Request list of all vedge devices and store
    device_list = device.get_device_list("vedges")
    # Request list of all vedge devices and store
    controller_list = device.get_device_list("controllers")
    # Print device_list in tabular format
    list_vedges = print_device_table(device_list)
    # Print controller list in tabular format
    list_controllers = print_device_table(controller_list)

    # Extract and print template data
    template_data = TemplateData(session, vmanage_host, port=vmanage_port)
    exported_device_template_list = template_data.export_device_template_list()
    print_template_table(exported_device_template_list)

    device_templates = DeviceTemplates(session, vmanage_host, port=vmanage_port)
    get_running_config(list_vedges, device_templates)
    get_running_config(list_controllers, device_templates)


def left(s, amount):
    return s[:amount]


def right(s, amount):
    return s[-amount:]


def mid(s, offset, amount):
    return s[offset:offset+amount]


if __name__ == "__main__":
    main()

