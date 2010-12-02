# This is a part of Fetcher @ http://github.com/KenjiTakahashi/Fetcher/
# Karol "Kenji Takahashi" Wozniak (C) 2010
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# -*- coding: utf-8 -*-

import urllib2
import threadpool
from gzip import GzipFile
from cStringIO import StringIO
from xml.dom import minidom
from PyQt4.QtCore import QThread,pyqtSignal
# yeah, I need just exception, thanks Discogs for bad formatted xml
# and other junks (bad urls? Hey! I took them from you!) I love you guys!
from xml.parsers.expat import ExpatError

class Bandsensor(object):
    def __init__(self, artists, albums):
        self.artists = artists
        self.albums = albums
        self.results = {}
    def sense(self, data):
        url = data + u'?f=xml&api_key=95b787be0c'
        request = urllib2.Request(url)
        request.add_header(u'Accept-Encoding', u'gzip')
        try:
            temp = urllib2.urlopen(request).read()
            try:
                data = GzipFile(fileobj = StringIO(temp)).read()
            except IOError:
                data = temp
        except urllib2.HTTPError:
            pass
        else:
            try:
                xml = minidom.parseString(data)
            except ExpatError:
                pass
            else:
                albums = []
                years = []
                types = [u'CD, Album', u'LP, Album', u'CD, Album, RE', u'LP, Album, RE']
                for r in xml.getElementsByTagName(u'release'):
                    album = r.firstChild.firstChild.data
                    if r.childNodes[1].firstChild.data in types and album not in albums:
                        albums.append(album)
                        if len(r.childNodes) > 3:
                            years.append(r.childNodes[3].firstChild.data)
                for album in albums:
                    for eAlbum in self.albums:
                        if album.lower() == eAlbum[u'album'].lower():
                            return {url: (albums, years)}
    def finish(self, _, result):
        if result:
            self.results.update(result)
    def run(self):
        requests = threadpool.makeRequests(self.sense, self.artists, self.finish)
        main = threadpool.ThreadPool(5)
        for req in requests:
            main.putRequest(req)
        main.wait()
        values = {}
        for data, (albums, _) in self.results.items():
            for album in albums:
                for eAlbum in self.albums:
                    if album.lower() == eAlbum[u'album'].lower():
                        if data in values.keys():
                            values[data] += 1
                        else:
                            values[data] = 1
        if values.keys():
            best = values.keys()[0]
            for k, v in values.items():
                if v > values[best]:
                    best = k
            return (best, self.results[best])

class Discogs(QThread):
    errors = pyqtSignal(unicode, unicode, unicode, unicode)
    stepped = pyqtSignal(unicode)
    def __init__(self, library, releases, behaviour):
        QThread.__init__(self)
        self.library=library
        self.releases = releases
        self.behaviour = behaviour
    def parse(self, elem):
        request = urllib2.Request(elem[u'url'][u'discogs'])
        request.add_header(u'Accept-Encoding',u'gzip')
        try:
            temp=urllib2.urlopen(request).read()
            try:
                data=GzipFile(fileobj=StringIO(temp)).read()
            except IOError:
                data=temp
        except urllib2.HTTPError:
            result={u'choice':u'error',u'elem':elem}
        else:
            xml=minidom.parseString(data)
            releases=[]
            years=[]
            types = [u'CD, Album', u'LP, Album', u'CD, Album, RE', u'LP, Album, RE']
            for r in xml.getElementsByTagName(u'release'):
                if r.childNodes[1].firstChild.data in types and r.firstChild.firstChild.data not in releases:
                    releases.append(r.firstChild.firstChild.data)
                    if len(r.childNodes)>3:
                        years.append(r.childNodes[3].firstChild.data)
            result={
                    u'choice':u'',
                    u'elem':elem,
                    u'albums':releases,
                    u'years':years
                    }
        return result
    def work(self,elem):
        self.stepped.emit(elem[u'artist'])
        if elem[u'url'] and u'discogs' in elem[u'url'].keys():
            result=self.parse(elem)
        else:
            artist=urllib2.quote(elem[u'artist'].encode(u'latin-1')).replace(u'%20',u'+')
            request=urllib2.Request(u'http://www.discogs.com/search?type=all&q='+artist+u'&f=xml&api_key=95b787be0c')
            request.add_header(u'Accept-Encoding',u'gzip')
            try:
                temp=urllib2.urlopen(request).read()
                try:
                    data=GzipFile(fileobj=StringIO(temp)).read()
                except IOError:
                    data=temp
            except urllib2.HTTPError:
                result={u'choice':u'error',u'elem':elem[u'artist']}
            else:
                try:
                    xml=minidom.parseString(data)
                except ExpatError:
                    result = {u'choice': u'error', u'elem': elem[u'artist']}
                else:
                    tag=xml.firstChild.firstChild
                    # Yeah, it's bad, it's ugly, just like discogs site and API is...
                    artists = [t.getElementsByTagName(u'uri')[0].firstChild.data
                            for t in tag.getElementsByTagName(u'result')
                            if elem[u'artist'] in t.getElementsByTagName(u'title')[0].firstChild.data\
                                    and u'artist' in t.getElementsByTagName(u'uri')[0].firstChild.data]
                    sensor = Bandsensor(artists, elem[u'albums'])
                    data = sensor.run()
                    if data:
                        result = {
                                u'choice': data[0],
                                u'elem': elem,
                                u'albums': data[1][0],
                                u'years': data[1][1]
                                }
                    else:
                        result = {u'choice': u'no_band', u'elem': elem[u'artist']}
        return result
    def done(self,_,result):
        def exists(a,albums):
            for alb in albums:
                if a.lower()==alb[u'album'].lower():
                    return True
            return False
        def exists2(a, albums):
            for album in albums:
                if a.lower() == album.lower():
                    return True
            return False
        if result[u'choice']==u'no_band':
            self.errors.emit(u'discogs.com',
                    u'errors',
                    result[u'elem'],
                    u'No such band has been found')
        elif result[u'choice']!=u'error':
            elem=self.library[self.library.index(result[u'elem'])]
            if result[u'choice']:
                elem[u'url'][u'discogs'] = result[u'choice']
            message = u'Nothing has been changed'
            for a,y in map(None,result[u'albums'],result[u'years']):
                for album in elem[u'albums']:
                    if not album[u'digital'] and not album[u'analog']\
                            and not exists2(album[u'album'], result[u'albums']):
                        message = u'Something has been removed'
                        del elem[u'albums'][elem[u'albums'].index(album)]
                if not exists(a,elem[u'albums']):
                    message = u'Something has been added'
                    elem[u'albums'].append({
                        u'album': a,
                        u'date': y and y or u'0',
                        u'tracks': [],
                        u'digital': False,
                        u'analog': False
                        })
                self.errors.emit(u'discogs.com', u'info',
                        elem[u'artist'], message)
        else:
            self.errors.emit(u'discogs.com',
                    u'errors',
                    result[u'elem'],
                    u'An unknown error occured (no internet?)')
    def run(self):
        if not self.behaviour:
            temp = [lib for lib in self.library
                    if not lib[u'url'] or u'discogs' in lib[u'url'].keys()]
            if temp:
                requests = threadpool.makeRequests(self.work, temp, self.done)
            else:
                requests = None
        else:
            requests = threadpool.makeRequests(self.work, self.library, self.done)
        if requests:
            main=threadpool.ThreadPool(5)
            for req in requests:
                main.putRequest(req)
            main.wait()
