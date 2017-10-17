#!/usr/bin/env python
from flask_script import Manager,Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User
from gevent.wsgi import WSGIServer

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

#app.jinja_env.trim_blocks = True
@manager.command
def deploy(deploy_type):
    from flask.ext.migrate import upgrade
    from app.models import User
    # upgrade database to the latest version
    upgrade()
if __name__ == '__main__':
    #manager.run()  #db tool
    http_server = WSGIServer(('0.0.0.0', 80), app)
    http_server.serve_forever()
