# This file is part of hb.
#
# hb is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# hb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with hb.  If not, see <http://www.gnu.org/licenses/>.

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


