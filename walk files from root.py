from subprocess import run, PIPE
import os


def print_files(location):
    result = run(f'ls "{location}"', stdout=PIPE, stderr=PIPE)
    files = result.stdout.decode().split('\n')[:-1]

    dirs = []
    for file in files:
        full_path = os.path.join(location, file)
        if os.path.isfile(full_path):
            print(location + "-->" + file)
        else:
            dirs.append(full_path)
    for d in dirs:
        print_files(d)


dir_path = "C:\\Python Tests\\Py-Notes"
print_files(dir_path)
