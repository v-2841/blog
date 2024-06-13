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
