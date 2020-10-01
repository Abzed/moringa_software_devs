from app import create_app, db
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
<<<<<<< HEAD
from app.models import User
from flask_security import SQLAlchemyUserDatastore, Security
=======
from app.models import User, Role, Department, Comment, Post
>>>>>>> 4cbc2fd231db511c159a52d7d5e414d8955219d6

app = create_app('development')
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)

<<<<<<< HEAD

@manager.shell
def make_shell_context():
    return dict(app=app, db=db,User=User)
=======
@manager.shell
def make_shell_context():
    return dict(app=app, db=db,User=User,Role=Role,Department=Department,Comment=Comment, Post=Post)
>>>>>>> 4cbc2fd231db511c159a52d7d5e414d8955219d6

manager.add_command('server', Server)
@manager.command
def test():
    import unittest
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(test)

if __name__ == '__main__':
    manager.run()