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

import os
import re
from setuptools import setup

def parse_requirements(file_name):
    requirements = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'(\s*#)|(\s*$)', line):
            continue
        if re.match(r'\s*-e\s+', line):
            requirements.append(re.sub(r'\s*-e\s+.*#egg=(.*)$', r'\1', line))
        elif re.match(r'\s*-f\s+', line):
            pass
        else:
            requirements.append(line)
    return requirements

def parse_dependency_links(file_name):
    dependency_links = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'\s*-[ef]\s+', line):
            dependency_links.append(re.sub(r'\s*-[ef]\s+', '', line))
    return dependency_links

requirements_filename = os.path.join(os.environ.get('OPENSHIFT_REPO_DIR', ''), 'requirements.txt')

setup(name='hb',
    version='0.0.1',
    description='Django Server Heartbeat App',
    author='Ben Cordero',
    author_email='bmc@linux.com',
    install_requires = parse_requirements(requirements_filename),
    dependency_links = parse_dependency_links(requirements_filename),    
)
