#! /usr/bin/env python

from os import system
from urllib2 import urlopen
from socket import socket
from sys import argv
from time import asctime
from smtplib import SMTP


def tcp_test(server_info):
    cpos = server_info.find(':')
    try:
        sock = socket()
        sock.connect((server_info[:cpos], int(server_info[cpos + 1:])))
        sock.close
        return True
    except:
        return False


def http_test(server_info):
    try:
        data = urlopen(server_info).read()
        if data:
            return True
    except:
        return False


def server_test(test_type, server_info):
    if test_type.lower() == 'tcp':
        return tcp_test(server_info)
    elif test_type.lower() == 'http':
        return http_test(server_info)

smtp = SMTP('mail.vorwaerts-werbung.de')


def notifyUser(smtp, smtp_user, smtp_password, from_email, to_email, msg):
    smtp.login(smtp_user, smtp_password)
    smtp.sendmail(from_email, to_email, msg.as_string())
    smtp.quit()
