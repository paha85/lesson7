import shutil
from time import perf_counter
import os

for root,  dirs, files in os.walk('.'):
    print(root, dirs, files)


# def scan_dir(dir, level=0):
#     for name in os.listdir(dir):
#         path = os.path.join(dir, name)
#         if os.path.isfile(path):
#             print(' '*level, path)
#         else:
#             print(' '*level, path)
#             scan_dir(path, level+1)
#
# scan_dir('.')

# shutil.rmtree('parent')
# shutil.copyfileobj()

# os.rename('parent', '..\')

# dir_name = 'new_dir'
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)

# dir_name = os.path.join('folder', 'new_folder2')
# if not os.path.exists(dir_name):
#     os.makedirs(dir_name)

# folder = '.'
# my_files = [os.path.join(folder, item) for item in os.listdir(folder) if os.path.isdir(item)]
# print(*my_files, sep='\n')
# start = perf_counter()
# sm_files = [item for item in os.listdir(folder) if os.stat(item).st_size < 15*2**10]
# sm_files = [item for item in os.scandir(folder) if os.stat(item).st_size < 15*2**10]
# sm_files = [os.path.abspath(item) for item in os.listdir(folder)]

# print(perf_counter() - start)
# print(*sm_files, sep='\n')

# os.path.isfile()