__author__ = 'mrakitin'

import os
import socket
import subprocess

address_to_route = None
qsh_ip = '192.12.90.0'
qsh_ip_mask = '255.255.255.0'


# Find IP address provided by SBU VPN:
ips_dict = {}
for i in socket.getaddrinfo(socket.gethostname(), None):
    ip = i[4][0]
    try:
        socket.inet_aton(ip)
        ipv4 = True
    except socket.error:
        ipv4 = False

    if ipv4:
        key, none, value = socket.gethostbyaddr(ip)
        ips_dict[key] = value[0]

for key in ips_dict.keys():
    if key.find('stonybrook.edu') >= 0:
        address_to_route = ips_dict[key]
        break


# Delete the route first in case it existed:
try:
    cmd_del = ['route', 'delete', qsh_ip]
    out_del = subprocess.check_output(cmd_del, stderr=subprocess.STDOUT)
    status_del = out_del.strip()
    if status_del.find('OK') >= 0:
        print 'Route %s has been deleted.' % (qsh_ip)
    elif status_del.find('The route deletion failed: Element not found.') >= 0:
        # print 'WARNING! ' + status_add
        pass
    else:
        print 'Unknown error occurred during deletion.'
except:
    print 'WARNING! Route %s has not been deleted.' % (qsh_ip)


# Add a new route if the VPN-provided address is found:
if address_to_route:
    cmd = ['route', 'add', qsh_ip, 'mask', qsh_ip_mask, address_to_route]
    try:
        print 'The following command will be executed:\n\n\t%s\n' % (' '.join(cmd))
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        status_add = out.strip()
        if status_add.find('OK') >= 0:
            print 'Addition was successful.\n'
            os.system('route print')
        elif status_add.find('The route addition failed') >= 0:
            print 'ERROR! ' + status_add
        else:
            print 'Unknown error occurred during addition.'
    except:
        pass
else:
    print 'ERROR! The VPN interface is not connected. The route to %s has not been added.' % (qsh_ip)
