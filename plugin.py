"""
A simple inventory plugin that uses Nmap to get the list of hosts
Jose Vicente Nunez (kodegeek.com@protonmail.com)
"""

from ansible.errors import AnsibleParserError
from ansible.plugins.inventory import BaseInventoryPlugin, Cacheable, Constructable

DOCUMENTATION = r'''
    name: test_plugin
    plugin_type: inventory
    short_description: Returns a dynamic host inventory
    description: Returns a dynamic host inventory, filter machines
    options:
      plugin:
          description: Name of the plugin
          required: true
          choices: ['test_plugin']
'''


class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):
    NAME = 'test_plugin'

    def __init__(self):
        super(InventoryModule, self).__init__()
        self.plugin = None

    def verify_file(self, path: str):
        if super(InventoryModule, self).verify_file(path):
            return path.endswith('yaml') or path.endswith('yml')
        return False
