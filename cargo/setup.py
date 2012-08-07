
import peachpy
from cargo.tool import Tool

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

class Config(object):
	pass

class NetworkConfig(Config):

	template = IFACE_TEMPLATE

	def __init__(self):
		self.config = {
			'address': '10.0.0.1',
			'netmask': '255.255.255.0',
		}

	def manual_update(self):
		for key in self.config:
			new = raw_input('{0} [{1}]: '.format(key, self.config[key]))
			if new: self.config[key] = new

	def __str__(self):
		return self.template.format(self.config)

class SetupTool(Tool):

	def __init__(self):
		self.configs = [NetworkConfig(),
                                ]

	@peachpy.expose
	def index(self):
		print 'Welcome to the TXC setup utility.'
		print STEPS
		for config in self.configs:
			config.manual_update()
		return ''

	#def network_options(self):
		
