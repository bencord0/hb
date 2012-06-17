mysql_createdb_string="""
create database %(NAME)s;
grant usage on %(NAME)s.* to %(USER)s
    identified by '%(PASSWORD)s';
grant all privileges on %(NAME)s.* to %(USER)s;
"""
postgres_createdb_string="""
create user %(USER)s password '%(PASSWORD)s';
create database %(NAME)s owner %(USER)s;
"""

from hb.settings import DATABASES
import subprocess
if 'mysql' in DATABASES['default']['ENGINE']:
    print "using mysql"
    p = subprocess.Popen("mysql -u root -p",
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
    p.communicate(input=mysql_createdb_string % DATABASES['default'])

if 'postgres' in DATABASES['default']['ENGINE']:
    print "using postgres"
    p = subprocess.Popen("psql -U postgres",
            shell=True,
            stdin=subprocess.PIPE,
        )
    p.communicate(input=postgres_createdb_string % DATABASES['default'])


