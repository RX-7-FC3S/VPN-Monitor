# coding: utf-8
import os
import re
import time

xl2tpd_status = {}
user = []


def status():

    xl2tpd_log = os.popen('sudo cat /var/log/syslog | grep -E "Call established with | Connection closed to .* serial"').readlines()

    if xl2tpd_log:
        xl2tpd_log = xl2tpd_log[-1]
        print(xl2tpd_log)

        if 'Call established with' in xl2tpd_log:
            item = {
                "ip": re.search('((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}', xl2tpd_log).group(),
                "start_time": re.search('^[A-Z]{1}[a-z]{1,10}\s{1}\d{2}\s{1}\d{2}:\d{2}:\d{2}', xl2tpd_log).group()
            }
            if item not in user:
                user.append(item)
        if 'Connection closed to' in xl2tpd_log:
            ip = re.search('((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}', xl2tpd_log).group()
            for item in user:
                if item['ip'] == ip:
                    user.remove(item)

    xl2tpd_status.update(user=user)
    return xl2tpd_status


