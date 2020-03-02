# from pymysql import install_as_MySQLdb
#
# install_as_MySQLdb()
# 这里跟教程不一样 解决的错误为
# django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.
import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()