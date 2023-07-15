import unittest
from iterative1 import binarySearch

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        test_cases = [
            #Test Case 1
            {
                "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
                "target": 33,
                "expected":3
            },
            #TestCase 2
            {
                "array": [1, 5, 23, 111],
                "target": 111,
                "expected":3
            },
            #Test Case 3
            {
                "array": [1, 5, 23, 111],
                "target": 5,
                "expected" : 1
            },
            #Test Case 4
            {
                "array": [1, 5, 23, 111],
                "target": 35,
                "expected" : -1
            },
            #Test Case 5
            {
                "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
                "target": 0,
                "expected" : 0
            },
            #Test Case 6
            {
                "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
                "target": 1,
                "expected" : 1
            },       
            #Test Case 7
            {
                "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
                "target": 21,
                "expected" : 2
            },
            #Test Case 8
            {   
                "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
                "target": 45,
                "expected" : 4
            },
            #Test Case 9
            {
                "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
                "target": 61,
                "expected" : 6
            },
            #Test Case 10
            {
                "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
                "target": 71,
                "expected" : 7
            },
            #Test Case 11
            {
                "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
                "target": 72,
                "expected": 8
            },
            #Test Case 12
            {
                "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
                "target": 73,
                "expected": 9
            },
            #Test Case 13
            {
                "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
                "target": 70, 
                "expected" : -1
            },
            #Test Case 14
            {
                "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355],
                "target": 355,
                "expected" : 10
            },   
            #Test Case 15
            {
                "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355],
                "target": 354,
                "expected" : -1
            },
            #Test Case 16
            {
                "array": [1, 5, 23, 111],
                "target": 120,
                "expected" : -1
            },
            #Test Case 17
            {
                "array": [5, 23, 111],
                "target": 3,
                "expected" : -1
            }
        ]

        for test_case in test_cases:
            arr = test_case["array"]
            x = test_case["target"]
            expected = test_case["expected"]
            result = binarySearch(arr, x)
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
