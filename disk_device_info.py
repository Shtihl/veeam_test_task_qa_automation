import sys
from subprocess import run, PIPE


def output_info(drive_details):
    return drive_details


def parse_drive_info(drive_info):
    drive_details = list(filter(None, drive_info.split(' ')))
    if drive_details[1] == 'disk':
        return drive_details
    else:
        additional_info = run(
            f'df -h -T {drive_details[0]}',
            shell=True,
            stdout=PIPE,
            encoding='utf-8'
        ).stdout.rstrip()
        return drive_details.extend(additional_info)


def get_drive_info(drive):
    drive_info = run(
        f'lsblk {drive} -d -p -l -n -o name,type,size',
        shell=True,
        stdout=PIPE,
        encoding='utf-8'
    ).stdout.rstrip()
    if 'disk' in drive_info:
        return drive_info
    else:
        additional_info = run(
            f'df -h -T {drive[0]}',
            shell=True,
            stdout=PIPE,
            encoding='utf-8'
        ).stdout.rstrip()
        return drive_info + additional_info


def load_drive_address(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as text_file:
            return text_file.read()
    except FileNotFoundError:
        return 'No such file'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        drive_address = load_drive_address(sys.argv[1])
        print(get_drive_info(drive_address))
    else:
        print('Usage: python driveinfo.py <file_name.txt>')
