#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test_irkcmd.py

import checkgip as checkgip
import pytest

def test_checkMain():
    ret = checkgip.checkMain()
    assert ret == 0

def test_loadSettings():
    ret = checkgip.loadSettings()
    assert ret != ''
