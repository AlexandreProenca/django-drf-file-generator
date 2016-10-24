#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from drf_gen.drf_gen import make_admin, make_views, make_urls, make_serializers, extractor_obj


class TestDrfGen(unittest.TestCase):
    '''
    Test basic of main methods
    '''

    def setUp(self):
        global outdir
        outdir = 'tests/drf_gem_build_test'

    def test_extractor(self):
        extractor_obj('tests/core/models.py')
        self.assertEqual(make_admin(outdir), True)

    def test_create_admin(self):
        self.assertEqual(make_admin(outdir), True)

    def test_create_views(self):
        self.assertEqual(make_views(outdir), True)

    def test_create_urls(self):
        self.assertEqual(make_urls(outdir), True)

    def test_create_serializers(self):
        self.assertEqual(make_serializers(outdir), True)

