# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from unittest import TestCase

import os

from auxlib.packaging import get_version
# from auxlib.packaging import (_get_version_from_pkg_info, _is_git_dirty, _get_most_recent_git_tag,
#                               _get_git_hash, is_git_repo)
# from auxlib.path import ROOT_PATH


# class TestPackaging(TestCase):
#
#     def test_version_string(self):
#         try:
#             test_version = str(random.randint(0,1e6))
#             with open('.version', 'w') as f:
#                 f.write(test_version)
#             assert _get_version_from_pkg_info('tests') == test_version
#         finally:
#             if os.path.exists('.version'):
#                 os.remove('.version')
#
#     def test_is_git_dirty(self):
#         result = _is_git_dirty(os.getcwd())
#         assert result is True or result is False
#
#
#     def test_get_git_hash(self):
#         hash = _get_git_hash(os.getcwd())
#         assert len(hash) == 7
#
#     def test_not_git_repo(self):
#         assert not is_git_repo(ROOT_PATH)


class TestPackagingNotGitRepo(TestCase):

    def setUp(self):
        super(TestPackagingNotGitRepo, self).setUp()
        self.cwd = os.getcwd()
        os.chdir('/')

    def tearDown(self):
        super(TestPackagingNotGitRepo, self).tearDown()
        os.chdir(self.cwd)

    def test_get_most_recent_git_tag_no_repo(self):
        tag = get_version(os.getcwd())
        assert tag is None

