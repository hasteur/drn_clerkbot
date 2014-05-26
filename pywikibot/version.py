# -*- coding: utf-8  -*-
""" Module to determine the pywikipedia version (tag, revision and date) """
#
# (C) Merlijn 'valhallasw' van Deen, 2007-2014
# (C) xqt, 2010-2014
# (C) Pywikipedia bot team, 2007-2013
#
# Distributed under the terms of the MIT license.
#
__version__ = '$Id: 257dcaca369202050289177ffd149534d0aa0e92 $'

import os
import sys
import time
import datetime
import urllib
import subprocess

cache = None


class ParseError(Exception):
    """ Parsing went wrong """


def _get_program_dir():
    _program_dir = os.path.normpath(os.path.split(os.path.dirname(__file__))[0])
    return _program_dir


def getversion():
    data = dict(getversiondict())  # copy dict to prevent changes in 'chache'
    try:
        hsh2 = getversion_onlinerepo()
        hsh1 = data['hsh']
        data['cmp_ver'] = 'OUTDATED' if hsh1 != hsh2 else 'ok'
    except Exception:
        data['cmp_ver'] = 'n/a'
    data['hsh'] = data['hsh'][:7]  # make short hash from full hash
    return '%(tag)s (%(hsh)s, %(rev)s, %(date)s, %(cmp_ver)s)' % data


def getversiondict():
    global cache
    if cache:
        return cache
    try:
        _program_dir = _get_program_dir()
        if os.path.isdir(os.path.join(_program_dir, '.svn')):
            (tag, rev, date, hsh) = getversion_svn(_program_dir)
        else:
            (tag, rev, date, hsh) = getversion_git(_program_dir)
    except ParseError:
        try:
            (tag, rev, date, hsh) = getversion_nightly()
        except ParseError:
            try:
                version = getfileversion('wikipedia.py')
                if not version:
                    # fall-back in case everything breaks (should not be used)
                    import wikipedia
                    version = getfileversion(wikipedia.__file__[:-1])

                file, hsh_short, date, ts = version.split(' ')
                tag = 'wikipedia.py'
                rev = '-1 (unknown)'
                ts = ts.split('.')[0]
                date = time.strptime('%sT%s' % (date, ts), '%Y-%m-%dT%H:%M:%S')
                hsh = hsh_short + ('?' * 33)   # enhance the short hash w. '?'
            except:
                # nothing worked; version unknown (but suppress exceptions)
                # the value is most likely '$Id' + '$', it means that
                # wikipedia.py got imported without using svn at all
                return dict(tag='', rev='-1 (unknown)', date='0 (unknown)',
                            hsh='(unknown)')

    datestring = time.strftime('%Y/%m/%d, %H:%M:%S', date)
    cache = dict(tag=tag, rev=rev, date=datestring, hsh=hsh)
    return cache


def getversion_git_windows(hsh, path=None):
    _program_dir = path or _get_program_dir()
    rev = None
    try:
        rev = open(os.path.join(_program_dir, 'cache/git'), 'r').read().split("|")[0]
        date = open(os.path.join(_program_dir, 'cache/git'), 'r').read().split("|")[1]
        date = time.strptime(date, "%Y-%m-%d %H:%M:%S")
    except IOError:
        #the code can be found in https://tools.wmflabs.org/pywikibot/gitlog.py
        url = "https://tools.wmflabs.org/pywikibot/gitlog.txt"
        print "Retreving commit log from %s" % url
        ff = urllib.urlopen(url).read().splitlines()
        for line in ff:
            if hsh in line:
                rev = line.split("|")[2]
                date = line.split("|")[0]
                open(os.path.join(_program_dir, 'cache/git'), 'w').write(rev+u"|"+date)
                date = time.strptime(date, "%Y-%m-%d %H:%M:%S")
                return rev, date
    if not rev:
        return "(unknown)", time.strptime("2000-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    return rev, date


def getversion_svn(path=None):
    import httplib
    import xml.dom.minidom
    _program_dir = path or _get_program_dir()
    entries = open(os.path.join(_program_dir, '.svn/entries'))
    version = entries.readline().strip()
    #use sqlite table for new entries format
    if version == "12":
        entries.close()
        from sqlite3 import dbapi2 as sqlite
        con = sqlite.connect(os.path.join(_program_dir, ".svn/wc.db"))
        cur = con.cursor()
        cur.execute("""select
local_relpath, repos_path, revision, changed_date, checksum from nodes
order by revision desc, changed_date desc""")
        name, tag, rev, date, checksum = cur.fetchone()
        cur.execute("select root from repository")
        tag, = cur.fetchone()
        con.close()
        tag = os.path.split(tag)[1]
        date = time.gmtime(date / 1000000)
    else:
        for i in xrange(3):
            entries.readline()
        tag = entries.readline().strip()
        t = tag.split('://')
        t[1] = t[1].replace('svn.wikimedia.org/svnroot/pywikipedia/', '')
        tag = '[%s] %s' % (t[0], t[1])
        for i in xrange(4):
            entries.readline()
        date = time.strptime(entries.readline()[:19], '%Y-%m-%dT%H:%M:%S')
        rev = entries.readline()[:-1]
        entries.close()
    conn = httplib.HTTPSConnection('github.com')
    conn.request('PROPFIND', '/wikimedia/%s/!svn/vcc/default' % tag,
                 "<?xml version='1.0' encoding='utf-8'?>"
                 "<propfind xmlns=\"DAV:\"><allprop/></propfind>",
                 {'Label': rev, 'User-Agent': 'SVN/1.7.5-pywikibot1'})
    resp = conn.getresponse()
    dom = xml.dom.minidom.parse(resp)
    hsh = dom.getElementsByTagName("C:git-commit")[0].firstChild.nodeValue
    rev = 's%s' % rev
    if (not date or not tag or not rev) and not path:
        raise ParseError
    return (tag, rev, date, hsh)


def getversion_git(path=None):
    _program_dir = path or _get_program_dir()
    cmd = 'git'
    rev = None
    date = None
    try:
        subprocess.Popen([cmd], stdout=subprocess.PIPE).communicate()
    except WindowsError:
        # some windows git versions provide git.cmd instead of git.exe
        cmd = 'git.cmd'
        try:
            subprocess.Popen([cmd], stdout=subprocess.PIPE).communicate()
        except:
            #Means git hasn't been installed, no way to get the date, retreving date from gitblit
            hsh = open(os.path.join(_program_dir, '.git/refs/heads/master'), 'r').read().strip(" \n")
            rev, date = getversion_git_windows(hsh, path)
    tag = open(os.path.join(_program_dir, '.git/config'), 'r').read()
    s = tag.find('url = ', tag.find('[remote "origin"]'))
    e = tag.find('\n', s)
    tag = tag[(s + 6):e]
    t = tag.strip().split('/')
    tag = '[%s] %s' % (t[0][:-1], '-'.join(t[3:]))
    if not date:
        info = subprocess.Popen(
            [cmd, '--no-pager', 'log', '-1',
                                   '--pretty=format:"%ad|%an|%h|%H|%d"'
                                   '--abbrev-commit',
                                   '--date=iso'],
            cwd=_program_dir,
            stdout=subprocess.PIPE).stdout.read()
        info = info.split('|')
        date = info[0][:-6]
        date = time.strptime(date.strip('"'), '%Y-%m-%d %H:%M:%S')
        hsh = info[3]  # also stored in '.git/refs/heads/master'
    if not rev:
        rev = subprocess.Popen(
            [cmd, 'rev-list', 'HEAD'],
            cwd=_program_dir,
            stdout=subprocess.PIPE).stdout.read()
        rev = 'g%s' % len(rev.splitlines())
    if (not date or not tag or not rev) and not path:
        raise ParseError
    return (tag, rev, date, hsh)


def getversion_nightly():
    data = open(os.path.join(wikipediatools.get_base_dir(), 'version'))
    tag = data.readline().strip()
    date = time.strptime(data.readline()[:19], '%Y-%m-%dT%H:%M:%S')
    rev = data.readline().strip()
    if not date or not tag or not rev:
        raise ParseError
    return (tag, rev, date, '(unknown)')


def getversion_onlinerepo(repo=None):
    """ Retrieve revision number of framework online repository's svnroot """
    url = repo or 'https://git.wikimedia.org/feed/pywikibot/compat'
    hsh = None
    try:
        buf = urllib.urlopen(url).readlines()
        hsh = buf[13].split('/')[5][:-1]
    except:
        raise ParseError
    return hsh


def getfileversion(filename):
    """ Retrieve revision number of file (__version__ variable containing Id tag)
        without importing it (thus can be done for any file)
    """
    _program_dir = _get_program_dir()
    __version__ = None
    size, mtime = None, None
    fn = os.path.join(_program_dir, filename)
    if os.path.exists(fn):
        for line in open(fn, 'r').readlines():
            if line.find('__version__') == 0:
                exec(line)
                break
        stat = os.stat(fn)
        mtime = datetime.datetime.fromtimestamp(stat.st_mtime).isoformat(' ')
    if mtime and __version__:
        return u'%s %s %s' % (filename, __version__[5:-1][:7], mtime)
    else:
        return None


def get_executing_script():
    """ Get the last path component (tail) and filename of the currently
        executing script. Returns a tuple.
    """
    try:
        script = os.path.abspath(sys.modules['__main__'].__file__)
    except (KeyError, AttributeError):
        script = sys.executable
    path, file = os.path.split(script)
    return (os.path.basename(path), file)
