import unittest
from markdown_adapter import run_markdown
 
class TestMarkdownPy(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_non_marked_lines(self):
        '''
        Non-marked lines should only get 'p' tags around all input
        '''
        self.assertEqual(
                run_markdown('this line has no special handling'),
                'this line has no special handling</p>')
 
    def test_em(self):
        '''
        Lines surrounded by asterisks should be wrapped in 'em' tags
        '''
        self.assertEqual(
                run_markdown('*this should be wrapped in em tags*'),
                '<p><em>this should be wrapped in em tags</em></p>')
 
    def test_strong(self):
        '''
        Lines surrounded by double asterisks should be wrapped in 'strong' tags
        '''
        self.assertEqual(
                run_markdown('**this should be wrapped in strong tags**'),
                '<p><strong>this should be wrapped in strong tags</strong></p>')

    def test_h1(self):
        '''
        Lines started by # should be wrapped in <h1> tags
        '''
        self.assertEqual(
                run_markdown('#this should be wrapped in strong tags'),
                '<h1>this should be wrapped in strong tags</h1>')

    def test_h2(self):
        '''
        Lines started by ## should be wrapped in <h2> tags
        '''
        self.assertEqual(
                run_markdown('##this should be wrapped in strong tags'),
                '<h2>this should be wrapped in strong tags</h2>')
                
    def test_h3(self):
        '''
        Lines started by ### should be wrapped in <h3> tags
        '''
        self.assertEqual(
                run_markdown('###this should be wrapped in strong tags'),
                '<h3>this should be wrapped in strong tags</h3>')

    def test_blockquote(self):
        '''
        Lines with > should be wrapped in <blockquote> tags
        '''
        self.assertEqual(
                run_markdown('>this should be wrapped in strong tags'),
                '<blockquote>this should be wrapped in strong tags</blockquote>')
 
if __name__ == '__main__':
    unittest.main()
