#!/usr/bin/env python

from distutils.core import setup

setup(name='nagios-plugins-security-misc',
        description="Simple NRPE scripts to check on various security conditions",
        version='1.0',
        author="Lou Ruppert",
        author_email="himself@louruppert.com",
        scripts=['check_iptables','check_simtec'],
        license="GPL"
)
