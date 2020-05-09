from flask import Flask, render_template, redirect
from qulinks.models.qulinks_record import QulinksRecord, Qulink

app = Flask(__name__) 

@app.route('/')
def root():
    qulinks =  QulinksRecord.fetch_qulinks()
    return render_template('index.html', qulinks=qulinks)

@app.route('/prod/v1/qu/<name>')
def redirect_to_qulink(name):
    qulink = Qulink.get_qulink_by_name(name)
    return redirect(qulink.url)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
