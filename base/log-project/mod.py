#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/12 23:15

import logging
import submod

logger = logging.getLogger('main.mod')
logger.info('logger of mod sya something ...')

def testLogger():
    logger.debug('this is mod.testLogger...')
    submod.tst()