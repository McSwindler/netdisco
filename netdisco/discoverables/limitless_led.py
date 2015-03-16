""" Discovers Limitless LED WiFi bridges. """

from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """ Adds support for discovering Limitless LED WiFi bridges. """

    def info_from_entry(self, entry):
        """ Returns the most important info from a uPnP entry. """
        device = entry.description.find('device')
        
        print entry

        return (device.find('friendlyName').text,
                entry.description.find('URLBase').text)

    def get_entries(self):
        """ Get all the Limitless LED uPnP entries. """
        return self.find_by_device_description({
            "manufacturer": "Hi-flying electronics technology Co."
        })
