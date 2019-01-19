
# Docker image setup for Oracle
# https://hub.docker.com/u/byoung063/content/sub-e37de3ed-e7cd-4720-a57e-a9a54ef657d4

# Needed client tools for python scripts on the Mac
# https://www.oracle.com/technetwork/topics/intel-macsoft-096467.html

# How to setup a connection in Python/Oracle
# https://www.oracle.com/technetwork/articles/dsl/prez-python-queries-101587.html

import cx_Oracle
connection = cx_Oracle.connect('sys','Oradoc_db1', cx_Oracle.makedsn('localhost', 32769,'ORCLCDB'), mode=cx_Oracle.SYSDBA)
connection.version
