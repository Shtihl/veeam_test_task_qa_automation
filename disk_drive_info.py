import sys
from subprocess import run, PIPE


def command_lsblk(drive):
    command = run(
        f'lsblk {drive} -d -p -l -n -o name,type,size',
        shell=True,
        stdout=PIPE,
        encoding='utf-8'
    ).stdout.rstrip().split()
    return command


def command_df(drive):
    command = run(
        f'df -h -T {drive}',
        shell=True,
        stdout=PIPE,
        encoding='utf-8'
    ).stdout.rstrip().split('\n')[1].split()
    return command


def get_drive_info(drive):
    lsblk_out = command_lsblk(drive)
    drive_info = {
        'address': lsblk_out[0],
        'type': lsblk_out[1],
        'size': lsblk_out[2]
    }
    if drive_info['type'] != 'disk':
        df_out = command_df(drive)
        drive_info['avail'] = df_out[4]
        drive_info['fstype'] = df_out[1]
        drive_info['mount'] = df_out[6]
    return drive_info


def load_drive_address(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as text_file:
            return text_file.read()
    except FileNotFoundError:
        return 'No such file'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        drive_address = load_drive_address(sys.argv[1])
        drive_info = get_drive_info(drive_address)
        print(' '.join(drive_info.values()))
    else:
        print('Usage: python disk_drive_info.py <file_name.txt>')
