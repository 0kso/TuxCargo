
import peachpy

STEPS = '''
Steps to be done:
=================

- choose IP range
- configure /etc/network/interfaces
- configure nginx
'''

IFACE_TEMPLATE = '''
auto br0
iface br0 inet static
	address 10.0.0.1
	netmask 255.255.255.0
	bridge_ports none
	bridge_stp off
	bridge_fd 0
	bridge_maxwait 5
	post-up echo 1 > /proc/sys/net/ipv4/ip_forward
'''

class TXCConfiguration(object):

	template = IFACE_TEMPLATE

	def __init__(self):
		self.config = {
			'address': '10.0.0.1',
			'netmask': '255.255.255.0',
		}

	def __str__(self):
		return self.template.format(self.config)

class Configure(object):

	def __init__(self):
		self.ask = Ask()

	@peachpy.expose
	def index(self):
		print 'Welcome to the TXC configuration utility.'
		print STEPS
		return ''

	def network_options(self):
