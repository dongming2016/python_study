#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/12 23:17

import logging


logger = logging.getLogger('main.mod.submod')
logger.info('logger of submod say something...')


def tst():
    logger.info('this is submod.tst()...')
