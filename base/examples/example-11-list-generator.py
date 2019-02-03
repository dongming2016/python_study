#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/13 21:52


print([n + m for n in range(0, 11) for m in range(0, 10)])  # range前闭后开
print([n for n in range(10)])
print([s.upper() for s in ['Hl', 'll', 1, 2] if isinstance(s, str)])
