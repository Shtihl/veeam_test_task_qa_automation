from sys import argv
import hashlib


def check_hash(file_to_check, hash_type, file_hash):
    if hash_type == 'md5':
        hash_check = hashlib.md5()
    if hash_type == 'sha1':
        hash_check = hashlib.sha1()
    if hash_type == 'sha256':
        hash_check = hashlib.sha256()
    try:
        with open(file_to_check, 'rb') as open_file:
            content = open_file.read()
            hash_check.update(content)
    except FileNotFoundError:
        return 'NOT FOUND'
    else:
        if hash_check.hexdigest() == file_hash:
            return 'OK'
        else:
            return 'FAILED'


def parse_file_list(path_to_file, work_dir):
    with open(path_to_file, 'r') as file_list:
        for line in file_list:
            file_entry = line.split()

            file_name = file_entry[0]
            file_hash_type = file_entry[1]
            file_hash = file_entry[2].lower()
            file_path = f'{argv[2]}/{file_name}'

            check_result = check_hash(file_path, file_hash_type, file_hash)

            print(f'{file_path} {check_result}')


if __name__ == '__main__':
    if len(argv) > 2:
        path_to_file = argv[1]
        work_dir = argv[2]
        integrity = parse_file_list(path_to_file, work_dir)
    else:
        print('Usage: python integrity.py <path/to/file> <path/to/dir>')
