import unittest
import basicmvc.model,basicmvc.view,basicmvc.controller
import sys
class BasicTest(unittest.TestCase):

    def test_model_creation(self):
        new_model = basicmvc.model.Model()
        new_model.set('attr1','val1')
        self.assertEqual(new_model.get('attr1'),'val1')
    def print_attr(self,model,k,oldval,x):
        self.assertEqual(x,'val2')

    def test_listening(self):
        v = basicmvc.view.View()
        new_model = basicmvc.model.Model()
        new_model.set('attr1','val1')
        v.bind( 'attr1', self.print_attr)
        new_model.registerObserver(v,'attr1')
        new_model.set('attr1','val2')
