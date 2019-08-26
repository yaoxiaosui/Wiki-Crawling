import DataAnalysis
import unittest
import json
class data_analysis_test(unittest.TestCase):
    def testAge(self):
        data = open('data_test.json').read()
        data = json.loads(data)
        result = DataAnalysis.getAgeGross(data)
        self.assertEqual(result[0][0],19)
        self.assertEqual(result[1][0],22)

    def testhub(self):
        data = open('data_test.json').read()
        data = json.loads(data)
        result = DataAnalysis.findHub(data)
        print(result)
        self.assertEqual(result[0][0], 'Olivia Colman')
        self.assertEqual(result[0][1], 11)








