import requests
import json
import unittest

URL = 'http://127.0.0.1:3002/predict_bankrupt'

class TestApiPredict(unittest.TestCase):

    def test_predict_1(self):
        data = {
            'data_predicts': [[
                0.716845343,
                0.424389446,
                0.405749772,
                0.370594257,
                0.792423739,
                0.169140588,
                0.207576261,
                0.14730845,
                0.390284354,
                0.118250477,
                0.290201893,
                0.339077007
            ]]
        }
        response = requests.post(URL, data=json.dumps(data))
        response_result = response.json()
        print(response_result)
        self.assertEqual(response.status_code, 200)

    def test_predict_2(self):
        data = {
            'data_predicts': [
                [
                    0.716845343, 0.424389446, 0.405749772, 0.370594257,
                    0.792423739, 0.169140588, 0.207576261, 0.14730845,
                    0.390284354, 0.118250477, 0.290201893, 0.339077007
                ],
                [
                    0.795297136, 0.53821413, 0.516730018, 0.464290937,
                    0.828823654, 0.208943935, 0.171176346, 0.056962827,
                    0.37676002, 0.047775282, 0.28384598, 0.329740148
                ],
                [
                    0.774669697, 0.499018753, 0.472295091, 0.426071272,
                    0.792484204, 0.180580505, 0.207515796, 0.098162065,
                    0.37909292, 0.025346489, 0.290188533, 0.334776851]
            ]
        }
        response = requests.post(URL, data=json.dumps(data))
        response_result = response.json()
        print(response_result)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
