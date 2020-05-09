from typing import List
from dataclasses import dataclass
from google.cloud import datastore


@dataclass
class Qulink:
    name: str
    url: str

    def delete_qulink(self):
        datastore_client = datastore.Client()
        query = datastore_client.query(kind='qulink')
        query.add_filter('name', '=', self.name)
        query.add_filter('url', '=', self.url)
        entities = query.fetch()
        for entity in entities:
            datastore_client.delete(entity.key)

    @classmethod
    def create_qulink(cls, name, url):
        datastore_client = datastore.Client()
        entity = datastore.Entity(key=datastore_client.key('qulink'))
        entity.update({'name': name,'url': url})
        datastore_client.put(entity)
        return cls(name=name, url=url)

    @classmethod
    def get_qulink_by_name(cls, name):
        datastore_client = datastore.Client()
        query= datastore_client.query(kind='qulink')
        query.add_filter('name', '=', name)
        qulinks = query.fetch(limit=1)
        qulink = [qulink for qulink in qulinks][0]
        return cls(name=qulink['name'], url=qulink['url']) 

@dataclass
class QulinksRecord:
    qulinks_record: List[Qulink]

    @classmethod
    def fetch_qulinks(cls):
        datastore_client = datastore.Client()
        query = datastore_client.query(kind='qulink')
        queried_qulinks = query.fetch()
        qulinks = [Qulink(name=qulink['name'], url=qulink['url']) for qulink in queried_qulinks]
        return cls(qulinks)
