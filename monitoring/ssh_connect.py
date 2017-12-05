import paramiko
import json

import subprocess

import time
from paramiko.ssh_exception import NoValidConnectionsError

import socket
def test():
        HOST = '192.168.202.105'    # The remote host
        PORT = 3333            # The same port as used by the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'{"id":0,"jsonrpc":"2.0","method":"miner_getstat1"}')
            data = s.recv(1024)
            r = json.loads(data.decode("utf-8"))['result']
        print(repr(data))
        print(r)

        id = '{"id":0,"jsonrpc":"2.0","method":"miner_getstat1"}'
        rigcomm = "echo '" + id + "' | netcat 192.168.202.105 3333"
        # t = subprocess.call(rigcomm, shell=True)
        PIPE = subprocess.PIPE
        t = subprocess.Popen(rigcomm, shell=True, stdin=PIPE, stdout=PIPE,
                             stderr=subprocess.STDOUT, close_fds=True, cwd='/home/')

        c = t.stdout.read()

        # весь массив, возвращённый c клэймора
        returned = json.loads(c.decode("utf-8"))['result']
        print(returned)
#
# def test():
#         id = '{"id":0,"jsonrpc":"2.0","method":"miner_getstat1"}'
#         rigcomm = "echo '"+id+"' | netcat 192.168.202.105 3333"
#         # t = subprocess.call(rigcomm, shell=True)
#         PIPE = subprocess.PIPE
#         t = subprocess.Popen(rigcomm, shell=True, stdin=PIPE, stdout=PIPE,
#                          stderr=subprocess.STDOUT, close_fds=True, cwd='/home/')
#
#         c=t.stdout.read()
#
#         # весь массив, возвращённый c клэймора
#         returned = json.loads(c.decode("utf-8"))['result']
#         print(returned)
#
#         claymore_version=returned[0].split(';')[0]
#         print(claymore_version)
#
#         claymore_uptime=returned[1].split(';')[0]
#         print(claymore_uptime)
#
#         hr_base = returned[3].split(';')
#         sum_hr_base = 0
#         # for i in hr_base:
#         #     sum_hr_base = round(sum_hr_base + (int(i)/1000),3)
#         # print (sum_hr_base)
#         sum_hr_base = sum([round(float(int(i) / 1000), 3) for i in hr_base])
#         hr_details_base = '; '.join([str(int(hr_base[i])/1000) + 'Mh/s' for i in range(len(hr_base))])
#         print(sum_hr_base)
#         print(hr_details_base)
#
#         hr_sec = returned[5].split(';')
#         if hr_sec[0] != 'off':
#             sum_hr_sec = ([round(float(int(i) / 1000), 3) for i in hr_sec])
#             hr_details_sec = '; '.join([str(int(hr_sec[i]) / 1000) + 'Mh/s' for i in range(len(hr_sec))])
#         else:
#             sum_hr_sec = 0
#             hr_details_sec = ''
#         print (sum_hr_sec)
#         print(hr_details_sec)
#
#         cooling = returned[6].split(';')
#         temperature, fun_speed = '; '.join([str(cooling[i]) + 'C' for i in range(len(cooling)) if i % 2 == 0]), \
#                                  '; '.join([str(cooling[i]) + '%' for i in range(len(cooling)) if i % 2 != 0])
#         print(temperature)
#         print(fun_speed)
#
#         pools = str(returned[7])
#         print(pools)

    # for i in a:
    #     print(i)


# from monitoring.models import Worker

#
# def test():
#     ssh = paramiko.SSHClient()
#     privkey = paramiko.RSAKey.from_private_key_file('/home/klyaus/.ssh/id_rsa')
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect('vpn.ongrid.pro', username='d.suldin', pkey=privkey)
#     comm = "python3 /opt/script.py"
#     # print("Executing {}".format(comm))
#     # stdin, stdout, stderr = ssh.exec_command(comm)
#     # h = json.loads(stdout.read().decode('utf-8'))
#     # for i in range(len(h)):
#     #     rigip = str(h[i][0])
#     # print(h[i][1])
#     # print(time.strftime('%H:%M:%S', time.gmtime(Worker.objects.filter(name=h[i][1]))))
#
#     print()
#     # try:
#     #     ssh.connect(rigip, username='user', pkey=privkey)
#     id = '{"id":0,"jsonrpc":"2.0","method":"miner_getstat1"}'
#     rigcomm = "echo '"+id+"' | netcat 192.168.201.105 3333"
#     stdin, stdout, stderr = ssh.exec_command(rigcomm)
#     t = stdout.readlines()
#     a=json.loads(t[0])['result'][5].split(';')
#         # b=a['result'][3].split(';')
#     # for i in a:
#     print(a)
#     #     rigcomm = "awk '{print int($1)}' /proc/uptime"
#     #     # print("Executing {}".format(rigcomm))
#     #     stdin, stdout, stderr = ssh.exec_command(rigcomm)
#     #     name = h[i][1]
#     #     uptime = stdout.read().decode('utf-8')
#     #     try:
#     #         old_worker = Worker.objects.get(name=name)
#     #         old_worker.uptime = uptime
#     #         old_worker.save()
#     #     except Worker.DoesNotExist:
#     #         new_worker = Worker()
#     #         new_worker.name = name
#     #         new_worker.uptime = uptime
#     #         new_worker.save()
#     #     print(rigip + ' ' + stdout.read().decode('utf-8'))
#     # print(stdout.readlines())
#     # print("Errors")
#     # print(stderr.read())
#     # except NoValidConnectionsError:
#     #     print(rigip + ' не найден')
#     #     pass  # print(stdout.readlines())  # print("Errors")
# # print(stderr.read())
#
# # print([line.strip() for line in stdout.readlines()])
#
# # commands = ['ssh root@h1-r01 "hostname"']
#
# # for command in commands:
# #     print("Executing {}".format(command))
# #     stdin, stdout, stderr = ssh.exec_command(command)
# #     h = stdout.read()
# #     print(stdout.read())
# #     print("Errors")
# #     print(stderr.read())
# # ssh.close()
#
# # f = open(h, 'r')
# # for line in f:
# #     words = line.split()
# #     print(words)
test()












"""
Django settings for djangoTrade project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from __future__ import absolute_import, unicode_literals
import os

# Celery options
CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'db+sqlite:///result.sqlite'
CELERY_TASK_SERIALIZER = 'json'
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_TIMEZONE = 'Europe/Moscow'
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERYD_MAX_TASKS_PER_CHILD = 5

# AllAuth setting
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

# redis sessions
SESSION_ENGINE = 'redis_sessions.session'

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_INDEX_TABLESPACE = 10

ADMINS = (('Сергей', 'achievement008@gmail.com'),)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1j&=q!62_%51y9!=97n=)bel8+#y+lup1bsy31d%s=sm!9q_c+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['dmitry.ongrid.pro', 'www.dmitry.ongrid.pro', '78.155.207.138']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'trade',
    'tradeBOT',
    'monitoring',
    'user_profile',
    'django_celery_beat',
    'allauth_temp',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.humanize',
    'channels',
    # ... include the providers you want to enable:
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.odnoklassniki',
    # 'allauth.socialaccount.providers.pinterest',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.windowslive',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'djangoTrade.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoTrade.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'trade',
        'USER': 'root',
        'PASSWORD': '',
        'default-character-set': 'utf-8',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

LOGIN_URL = '/accounts/login/'

# yandex money settings
YANDEX_MONEY_CLIENT_ID = '1EB2214C53CF879A9BD8606934B804F93BE9C82604DD9A1ED967F8635CBCD04B'

YANDEX_MONEY_REDIRECT_URI = 'http://portal.ongrid.pro/wallet/'

YANDEX_MONEY_CLIENT_SECRET = 'DD89A956C22739F77FDA276D64E9DF2E711DAA7645BFA5741872C0DA93DA8240EDDB6FBD2500210891396231AF4FB5B2FD90C7C0BB45F51803EAA36105CE508F'

STATIC_ROOT = '/opt/portal_ongrid/static'
MEDIA_ROOT = '/opt/portal_ongrid/media'
MEDIA_URL = '/media/'

# channels

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
        "ROUTING": "djangoTrade.routing.channel_routing",
    },
}

# время очистки тикера
TICKER_HOURS_TO_CLEAR = 1
