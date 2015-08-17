# -*- coding: UTF-8 -*-


import sys
import os

import unittest


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


from logic.json_to_obj import JsonToObj
from logic.organ import Organ
from logic.organ_factory import OrganFactory


class TestJsonToObj(unittest.TestCase):

    def setUp(self):
        self.klass = Organ
        self.json_to_obj = JsonToObj(Organ)

    def test_object_creation(self):
        args = {'name': 'TestOrgan',
                'args': [['arg0'],
                         ['arg1', 'arg0 + hello'],
                         ['arg2', 'arg1 + arg1']]
                }

        obj = JsonToObj(self.klass, args).create_obj()
        self.assertIsInstance(obj, Organ)

    def test_str_to_expr(self):
        string = 'arg + hello - 4'
        indexes = {'arg': 0}
        out = self.json_to_obj._str_to_expr(string=string, indexes=indexes)

        self.assertEqual(out, 'self.args[0] + self._get_value_from_mediator("hello")')


class TestOrganFactory(unittest.TestCase):

    def test_many_organs_creation(self):
        organs = {'organs': [{'name': 'Heart',
                              'args': [['aorta'],
                                       ['KDO', 'aorta + LP * 2'],
                                       ['OAK'],
                                       ['LP'],
                                       ['MGP', 'aorta + OAK + bsa'],
                                       ['KDRLG']],
                              },
                             {'name': 'Pancreas',
                              'args': [['arg0', 'arg1+arg2+arg3*arg4'],
                                       ['arg1', 'arg2 + arg1 + from_mediator'],
                                       ['arg2'],
                                       ['arg3'],
                                       ['arg4']]}]}

        organ_factory = OrganFactory(organs['organs'])
        self.assertEqual(len(organ_factory.organs), len(organs['organs']))
        self.assertIsInstance(organ_factory.organs[0], Organ)
        self.assertIsInstance(organ_factory.organs[1], Organ)


if __name__ == '__main__':
    unittest.main()