from vmanage.api.authentication import Authentication
from vmanage.api.device import Device
from vmanage.data.template_data import TemplateData
from vmanage.api.device_templates import DeviceTemplates
from vmanage.api.feature_templates import FeatureTemplates
from vmanage.api.monitor_network import MonitorNetwork
from vmanage.api.central_policy import CentralPolicy
from vmanage.api.certificate import Certificate
from vmanage.api.http_methods import HttpMethods
from vmanage.api.local_policy import LocalPolicy
from vmanage.api.policy_definitions import PolicyDefinitions
from vmanage.api.policy_lists import PolicyLists
from vmanage.api.policy_updates import PolicyUpdates
from vmanage.api.security_policy import SecurityPolicy
from vmanage.api.utilities import Utilities
from vmanage.api.settings import Settings


def main():
    print("Authentication")
    print_methods(dir(Authentication))
    print("\n\n\nCentral Policy")
    print_methods(dir(CentralPolicy))
    print("\n\n\nCertificate")
    print_methods(dir(Certificate))
    print("\n\n\nDevice")
    print_methods(dir(Device))
    print("\n\n\nDevice Templates")
    print_methods(dir(DeviceTemplates))
    print("\n\n\nFeature Templates")
    print_methods(dir(FeatureTemplates))
    print("\n\n\nHTTP Methods")
    print_methods(dir(HttpMethods))
    print("\n\n\nLocal Policy")
    print_methods(dir(LocalPolicy))
    print("\n\n\nMonitor Network")
    print_methods(dir(MonitorNetwork))
    print("\n\n\nPolicy Definitions")
    print_methods(dir(PolicyDefinitions))
    print("\n\n\nPolicy Lists")
    print_methods(dir(PolicyLists))
    print("\n\n\nPolicy Updates")
    print_methods(dir(PolicyUpdates))
    print("\n\n\nSecurity Policy")
    print_methods(dir(SecurityPolicy))
    print("\n\n\nUtilities")
    print_methods(dir(Utilities))
    print("\n\n\nSettings")
    print_methods(dir(Settings))
    print("\n\n\nTemplate Data")
    print_methods(dir(TemplateData))


def print_methods(dir_list):
    for line in dir_list:
        if left(line, 1) != "_":
            print(line)


def left(s, amount):
    return s[:amount]


def right(s, amount):
    return s[-amount:]


def mid(s, offset, amount):
    return s[offset:offset + amount]


if __name__ == "__main__":
    main()
