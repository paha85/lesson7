import shutil

source_dir = r'/Users/pahaboo/PycharmProjects/lesson7/my_project/mainapp/mainapp'
destination_dir = r'/Users/pahaboo/PycharmProjects/lesson7/my_project/templates/mainapp'
shutil.copytree(source_dir, destination_dir)

source_dir = r'/Users/pahaboo/PycharmProjects/lesson7/my_project/authapp/authapp'
destination_dir = r'/Users/pahaboo/PycharmProjects/lesson7/my_project/templates/authapp'
shutil.copytree(source_dir, destination_dir)

