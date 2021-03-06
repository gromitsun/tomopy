#!/usr/bin/env python
# -*- coding: utf-8 -*-

# #########################################################################
# Copyright (c) 2015, UChicago Argonne, LLC. All rights reserved.         #
#                                                                         #
# Copyright 2015. UChicago Argonne, LLC. This software was produced       #
# under U.S. Government contract DE-AC02-06CH11357 for Argonne National   #
# Laboratory (ANL), which is operated by UChicago Argonne, LLC for the    #
# U.S. Department of Energy. The U.S. Government has rights to use,       #
# reproduce, and distribute this software.  NEITHER THE GOVERNMENT NOR    #
# UChicago Argonne, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR        #
# ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  If software is     #
# modified to produce derivative works, such modified software should     #
# be clearly marked, so as not to confuse it with the version available   #
# from ANL.                                                               #
#                                                                         #
# Additionally, redistribution and use in source and binary forms, with   #
# or without modification, are permitted provided that the following      #
# conditions are met:                                                     #
#                                                                         #
#     * Redistributions of source code must retain the above copyright    #
#       notice, this list of conditions and the following disclaimer.     #
#                                                                         #
#     * Redistributions in binary form must reproduce the above copyright #
#       notice, this list of conditions and the following disclaimer in   #
#       the documentation and/or other materials provided with the        #
#       distribution.                                                     #
#                                                                         #
#     * Neither the name of UChicago Argonne, LLC, Argonne National       #
#       Laboratory, ANL, the U.S. Government, nor the names of its        #
#       contributors may be used to endorse or promote products derived   #
#       from this software without specific prior written permission.     #
#                                                                         #
# THIS SOFTWARE IS PROVIDED BY UChicago Argonne, LLC AND CONTRIBUTORS     #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT       #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS       #
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL UChicago     #
# Argonne, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,        #
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,    #
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;        #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT      #
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN       #
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE         #
# POSSIBILITY OF SUCH DAMAGE.                                             #
# #########################################################################

"""
Module for deprecated function warnings.
"""

from __future__ import absolute_import, division, print_function

import logging
logger = logging.getLogger(__name__)


__author__ = "Doga Gursoy"
__copyright__ = "Copyright (c) 2015, UChicago Argonne, LLC."
__docformat__ = 'restructuredtext en'
__all__ = ['adaptive_segment',
           'apply_mask',
           'apply_padding',
           'correct_drift',
           'diagnose_center',
           'downsample2d',
           'downsample3d',
           'optimize_center',
           'phase_retrieval',
           'region_segment',
           'remove_background',
           'simulate',
           'stripe_removal',
           'threshold_segment',
           'upsample2d',
           'upsample2df',
           'zinger_removal']


def adaptive_segment(*args, **kwargs):
    logger.warning('Deprecated function.')


def apply_mask(*args, **kwargs):
    logger.warning('Deprecated function.')


def apply_padding(*args, **kwargs):
    logger.warning('Deprecated function. Use apply_pad instead.')


def correct_drift(*args, **kwargs):
    logger.warning('Deprecated function. Use correct_air instead.')


def diagnose_center(*args, **kwargs):
    logger.warning('Deprecated function. Use write_center instead.')


def downsample2d(*args, **kwargs):
    logger.warning('Deprecated function. Use downsample instead.')


def downsample3d(*args, **kwargs):
    logger.warning('Deprecated function. Use downsample instead.')


def optimize_center(*args, **kwargs):
    logger.warning('Deprecated function. Use find_center instead.')


def phase_retrieval(*args, **kwargs):
    logger.warning('Deprecated function. Use retrieve_phase instead.')


def region_segment(*args, **kwargs):
    logger.warning('Deprecated function.')


def remove_background(*args, **kwargs):
    logger.warning('Deprecated function.')


def simulate(*args, **kwargs):
    logger.warning('Deprecated function. Use project instead.')


def stripe_removal(*args, **kwargs):
    logger.warning(
        'Deprecated function. Use remove_stripe1 or remove_stripe2 instead.')


def threshold_segment(*args, **kwargs):
    logger.warning('Deprecated function.')


def upsample2d(*args, **kwargs):
    logger.warning('Deprecated function. Use upsample instead.')


def upsample2df(*args, **kwargs):
    logger.warning('Deprecated function. Use upsample instead.')


def zinger_removal(*args, **kwargs):
    logger.warning('Deprecated function. Use remove_zinger instead.')
