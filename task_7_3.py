
import shutil
import os


dir_ = os.path.abspath(os.curdir)


if not os.path.exists('my_project'):
    os.mkdir(f'{dir_}/my_project')


if not os.path.exists('my_project/settings'):
    os.mkdir(f'{dir_}/my_project/settings')
with open('my_project/settings/__init__.py', 'tw') as file_1:
    pass
with open('my_project/settings/dev.py', 'tw') as file_1:
    pass
with open('my_project/settings/prod.py', 'tw') as file_1:
    pass


if not os.path.exists('my_project/mainapp'):
    os.mkdir(f'{dir_}/my_project/mainapp')
with open('my_project/mainapp/__init__.py', 'tw') as file_1:
    pass
with open('my_project/mainapp/models.py', 'tw') as file_1:
    pass
with open('my_project/mainapp/views.py', 'tw') as file_1:
    pass

if not os.path.exists('my_project/mainapp/templates'):
    os.mkdir(f'{dir_}/my_project/mainapp/templates')
if not os.path.exists('my_project/mainapp/templates/mainapp'):
    os.mkdir(f'{dir_}/my_project/mainapp/templates/mainapp')
with open('my_project/mainapp/templates/mainapp/base.html', 'tw') as file_1:
    pass
with open('my_project/mainapp/templates/mainapp/index.html', 'tw') as file_1:
    pass


try:
    shutil.copytree('my_project/mainapp', 'my_project/authapp')
    shutil.copytree('my_project/settings', 'my_project/templates/settings')
    shutil.copytree('my_project/mainapp', 'my_project/templates/mainapp')
    shutil.copytree('my_project/authapp', 'my_project/templates/authapp')
except FileExistsError:
    print()
