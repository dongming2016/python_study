#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/17 0:03

import subprocess
print('$ nslooup www.python.org')
r = subprocess.call(['nslooup', 'wwww.python.org'])
print('Exit code:', r)