import xml.etree.ElementTree as ET
import ipaddress
from app.validators import Ipv4Validator, Ipv6Validator, CidrValidator

def find_ip_in_ranges(ip, ranges):
    if Ipv4Validator.is_valid(ip):
        ip = ipaddress.IPv4Address(ip)
    elif Ipv6Validator.is_valid(ip):
        try:
            ip = ipaddress.IPv6Address(ip)
        except e:
            return False
    for ip_range in ranges:
        if CidrValidator.is_valid(ip_range['cidr']):
            if ip in ipaddress.ip_network(ip_range['cidr']):
                return ip_range

    return False


def find_cidr_in_ranges(cidr, ranges):
    for ip_range in ranges:
        return False

def confirm(question, default="NOT_SET"):
    question = question + " [y/n] "
    if default != 'NOT_SET':
        question = "{} [{}]".format(question, default)
    response = input(question)
    if not response:
        if default != 'NOT_SET':
            return default
        return confirm(question, default)
    elif response.lower() == 'yes' or response.lower() == 'y':
        return True
    elif response.lower() == 'no' or response.lower() == 'n':
        return False
    else:
        return confirm(question, default)

def str_to_xml(string):
    return ET.fromstring(string)

def print_xml_elem(element, levels=None, index=0):
    space = index*" "*2
    no_levels = False
    if levels == None:
        no_levels = True
    if (index <= levels or no_levels) and ET.iselement(element):
        index = index + 1
        children = element.getchildren()
        print(space + element.tag + str(element.items()) + (":" if children else ""))
        for subelem in element.getchildren():
            # inefficient, need to do level check
            print_xml_elem(subelem, levels=levels, index=index)
