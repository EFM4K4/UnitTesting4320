import unittest
import stockDataVisualizer

class testStockDataVisualizer(unittest.TestCase):

    stringChart = '1 2'
    stringTime = '1 2 3 4'
    stringDates = '%Y-%m-%d'
    stringGraph = '1 2 3 4'


    def setUpClass(self):
        print('setupClass')

    def tearDownClass(self):
        print('teardownClass')


    def test_askCharts(self):
        self.assertTrue('1 2')


    def test_askTimeSeries(self):
        self.assertEqual('1 2 3 4')

    def test_checkDates(self):
        self.assertEqual('%Y-%m-%d')

    def test_generateGraph(self):
        self.assertEqual('1 2 3 4')

    def test_main(self):
        self.assertEqual(stockDataVisualizer)

    


    if __name__ == '__main__':
        unittest.main()