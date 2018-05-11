#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 02/04/2018.

import ConfigParser


conf = ConfigParser.ConfigParser()

conf.read("format.conf")

print conf.get("default","conn_str")