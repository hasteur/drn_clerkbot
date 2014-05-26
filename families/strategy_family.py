# -*- coding: utf-8  -*-

__version__ = '$Id: adb3574876ff7918b8c7ba072afebb3f9198c11f $'

import family


# The Wikimedia Strategy family
class Family(family.WikimediaFamily):
    def __init__(self):
        super(Family, self).__init__()
        self.name = 'strategy'
        self.langs = {
            'strategy': 'strategy.wikimedia.org',
        }

        self.namespaces[4] = {
            '_default': [u'Strategic Planning', 'Project'],
        }
        self.namespaces[5] = {
            '_default': [u'Strategic Planning talk', 'Project talk'],
        }
        self.namespaces[106] = {
            '_default': [u'Proposal'],
        }
        self.namespaces[107] = {
            '_default': [u'Proposal talk'],
        }

        self.interwiki_forward = 'wikipedia'

    def dbName(self, code):
        return 'strategywiki_p'
