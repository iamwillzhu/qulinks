import os

from flask import Flask, render_template, redirect
from google.cloud import datastore

app = Flask(__name__) 
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


@app.route('/')
def root():
    qulinks =  get_all_qulinks()

    return render_template('index.html', qulinks=qulinks)

@app.route('/<name>')
def redirect_qulink(name):
    qulinks = get_qulink_by_name(name)
    qulink = [qulink for qulink in qulinks][0]

    return redirect(qulink['url'])

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
