from app import create_app, db
from app.model_admin import User
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand


app = create_app('development')
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)

manager.add_command('server', Server)
@manager.command
def test():
    import unittest
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(test)

if __name__ == '__main__':
    manager.run()