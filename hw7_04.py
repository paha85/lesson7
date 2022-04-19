import os

result = {}
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        size = os.stat(os.path.abspath(file)).st_size
        count = 1
        while True:
            if size <= 10 * count:
                if 10 * count in result:
                    result[10 * count] = result[10 * count] + 1
                else:
                    result[10 * count] = 1
                break
            count = count * 10
print(result)
