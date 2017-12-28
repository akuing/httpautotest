# coding=utf-8
"""
author:
date:
brief:
"""
import os
import unittest


def all_case():
    file_name = os.path.dirname(os.path.realpath(__file__))
    case_path = os.path.join(file_name, "case")
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTests(test_case)
    return testcase

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(all_case())
