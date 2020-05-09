from dataclasses import dataclass
from google.cloud import datastore

datastore_client = datastore.Client()

@dataclass
class Qulink:
    name: str
    url: str

    def store_qulink(self, name, url):
        entity = datastore.Entity(key=datastore_client.key('qulink'))
        entity.update({'name': name,'url': url})
        datastore_client.put(entity)

    @classmethod
    def get_qulink_by_name(cls , name):
        query= datastore_client.query(kind='qulink')
        query.add_filter('name', '=', name)
        qulinks = query.fetch(limit=1)
        qulink = [qulink for qulink in qulinks][0]
        return cls(name=qulink['name'], url=qulink['url']) 
