# -*- coding: utf-8  -*-
"""
Functions for manipulating external links
or querying third-party sites.

"""
#
# (C) Pywikibot team, 2013
#
# Distributed under the terms of the MIT license.
#
__version__ = '$Id: 6094cd93492e9dae21ab99706378b812fe9d46dd $'

import wikipedia as pywikibot
from pywikibot.comms import http

def getInternetArchiveURL(site, url, timestamp=None):
    """Return archived URL by Internet Archive."""
    # See [[:mw:Archived Pages]] and http://archive.org/help/wayback_api.php
    import json
    query = u'http://archive.org/wayback/available?'
    query += u'url='
    query += url
    if not timestamp is None:
        query += u'&timestamp='
        query += timestamp
    if pywikibot.verbose:
        pywikibot.output(u"Requesting query from Internet Archive: %s" % query)
    jsontext = http.request(uri=query, site=site, retry=False, no_hostname=True)
    if "closest" in jsontext:
        data = json.loads(jsontext)
        return data['archived_snapshots']['closest']['url']
    else:
        return None


def getWebCitationURL(site, url, timestamp=None):
    """Return archived URL by Web Citation."""
    # See http://www.webcitation.org/doc/WebCiteBestPracticesGuide.pdf
    from BeautifulSoup import BeautifulStoneSoup
    query = u'http://www.webcitation.org/query?'
    query += u'returnxml=true'
    query += u'&url='
    query += url
    if not timestamp is None:
        query += u'&date='
        query += timestamp
    if pywikibot.verbose:
        pywikibot.output(u"Requesting query from Web Citation: %s" % query)
    xmltext = http.request(uri=query, site=site, retry=False, no_hostname=True)
    if "success" in xmltext:
        data = BeautifulStoneSoup(xmltext)
        return data.find('webcite_url').string
    else:
        return None

