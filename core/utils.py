import os
import platform

from django.conf import settings


TZ_OFFSET_TO_NAME = {
    '+14:00': 'Etc/GMT-14',
    '+13:00': 'Etc/GMT-13',
    '+12:00': 'Etc/GMT-12',
    '+11:00': 'Etc/GMT-11',
    '+10:00': 'Etc/GMT-10',
    '+09:00': 'Etc/GMT-9',
    '+08:00': 'Etc/GMT-8',
    '+07:00': 'Etc/GMT-7',
    '+06:00': 'Etc/GMT-6',
    '+05:00': 'Etc/GMT-5',
    '+04:00': 'Etc/GMT-4',
    '+03:00': 'Etc/GMT-3',
    '+02:00': 'Etc/GMT-2',
    '+01:00': 'Etc/GMT-1',
    '+00:00': 'Etc/GMT',
    '-01:00': 'Etc/GMT+1',
    '-02:00': 'Etc/GMT+2',
    '-03:00': 'Etc/GMT+3',
    '-04:00': 'Etc/GMT+4',
    '-05:00': 'Etc/GMT+5',
    '-06:00': 'Etc/GMT+6',
    '-07:00': 'Etc/GMT+7',
    '-08:00': 'Etc/GMT+8',
    '-09:00': 'Etc/GMT+9',
    '-10:00': 'Etc/GMT+10',
    '-11:00': 'Etc/GMT+11',
    '-12:00': 'Etc/GMT+12',
}


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def load_icu(connection, **kwargs):
    # if (connection.vendor != 'sqlite' or platform.system() != 'Linux'
    #         or platform.machine() != 'x86_64'):
    #     return
    # connection.connection.enable_load_extension(True)
    # connection.connection.load_extension(
    #     os.path.join(settings.BASE_DIR, 'libSqliteIcu.so'))
    if connection.vendor != 'sqlite':
        return
    if platform.system() == 'Linux' and platform.machine() == 'x86_64':
        connection.connection.enable_load_extension(True)
        connection.connection.load_extension(
            os.path.join(settings.BASE_DIR, 'libSqliteIcu.so'))
    elif platform.system() == 'Windows' and platform.machine() == 'AMD64':
        connection.connection.enable_load_extension(True)
        connection.connection.load_extension(
            os.path.join(settings.BASE_DIR, 'libSqliteIcu.dll'))
    else:
        return
