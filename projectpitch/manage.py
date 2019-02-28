from app import create_app,db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import User

# Creating app instance
app = create_app('production')


manager = Manager(app)
manager.add_command('server',Server)
manager.add_command(server',Server))
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User ,pitch =pitch,comment = comment, vote = vote)
if __name__ == '__main__':
    manager.run()