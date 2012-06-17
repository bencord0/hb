import os
import sys
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

requirements_filename = sys.path.join(os.environ.get('OPENSHIFT_REPO_DIR', ''), 'requirements.txt')

setup(name='hb',
    version='0.0.1',
    description='Django Server Heartbeat App',
    author='Ben Cordero',
    author_email='bmc@linux.com',
    install_requires = parse_requirements(requirements_filename),
    dependency_links = parse_dependency_links(requirements_filename),    
)
