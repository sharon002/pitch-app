from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Pitch, Comment,UpVote,DownVote


# instances for creating the app
app = create_app('development')
manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command('server', Server)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Pitch=Pitch,Comment=Comment, UpVote=UpVote, DownVote=DownVote)


@manager.command
def test():
    '''
    Run the unit test
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
