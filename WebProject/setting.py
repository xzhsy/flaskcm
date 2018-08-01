"""
Settings for the polls application.

You can set values of REPOSITORY_NAME and REPOSITORY_SETTINGS in
environment variables, or set the default values in code here.
"""

from os import environ

REPOSITORY_SETTINGS_Han = dict(DATABASE="od_appconf", USERNAME="root",
                           PASSWORD="admin", HOST="211.142.200.22", PORT=53690)

REPOSITORY_SETTINGS = dict(
    DATABASE="od_appconf", USERNAME="idcuser", PASSWORD="123456", HOST="localhost", PORT=3306)
