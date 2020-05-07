from google.cloud import datastore

datastore_client = datastore.Client()

def store_qulink(name, url):
    entity = datastore.Entity(key=datastore_client.key('qulink'))
    entity.update({
        'name': name,
        'url': url,
    })

    datastore_client.put(entity)


def get_all_qulinks():
    query = datastore_client.query(kind='qulink')
    query.order = ['-name']

    return query.fetch()

def get_qulink_by_name(name):
    query = datastore_client.query(kind='qulink')
    query.add_filter('name', '=', name)
    return query.fetch(limit=1)
