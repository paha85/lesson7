import os


def project_start(dir_name):
    dir_path = os.path.join(dir_name, 'settings', '../mainapp', '../adminapp', '../authapp')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


path_name = input('Pls enter preferred path name: ')
project_start(path_name)
