import unittest

from app import app


class SolutionTestCase(unittest.TestCase):

    def test_solution_succeed(self):
        tester = app.test_client(self)
        request_body = {
            "leaves_pos": [5, 4, 4, 7, 4, 1, 9, 1, 1, 5, 6, 2, 7, 10, 2, 8, 7, 8, 7, 8, 6, 6, 9, 4, 8, 2, 8, 9, 7, 6, 9,
                           4, 6, 3, 10, 9, 7, 2, 7, 2, 5, 7, 6, 9, 5, 1, 10, 4, 9, 3, 3, 10, 8, 6, 1, 9, 8, 3, 7, 10,
                           10, 2, 8, 10, 9, 1, 2, 7, 6, 8, 3, 7, 3, 10, 2, 5, 1, 5, 7, 6, 4, 4, 4, 1, 6, 6, 6, 1, 3, 5,
                           1, 4, 8, 6, 7, 3, 4, 1, 7, 3],
            "river_size": 10
        }
        response = tester.post(json=request_body, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "time_to_jump": 33,
            "message": "The frog can start to jump at 33 seconds"
        })

    def test_solution_wrong_request(self):
        tester = app.test_client(self)
        request_body = {
            "wrong_field": [5, 4, 4, 7, 4, 1, 9, 1, 1, 5, 6, 2, 7, 10, 2, 8, 7, 8, 7, 8, 6, 6, 9, 4, 8, 2, 8, 9, 7, 6,
                            9,
                            4, 6, 3, 10, 9, 7, 2, 7, 2, 5, 7, 6, 9, 5, 1, 10, 4, 9, 3, 3, 10, 8, 6, 1, 9, 8, 3, 7, 10,
                            10, 2, 8, 10, 9, 1, 2, 7, 6, 8, 3, 7, 3, 10, 2, 5, 1, 5, 7, 6, 4, 4, 4, 1, 6, 6, 6, 1, 3, 5,
                            1, 4, 8, 6, 7, 3, 4, 1, 7, 3],
            "wrong": 10
        }
        response = tester.post(json=request_body, content_type='application/json')
        self.assertEqual(response.status_code, 422)

    def test_solution_wrong_value(self):
        tester = app.test_client(self)
        request_body = {
            "leaves_pos": [5, 4, 4, 7, 4, 1, 9, 1, 1, 5, 6, 2, 7, 10, 2, 8, 7, 8, 7, 8, 6, 6, 9, 4, 8, 2, 8, 9, 7, 6, 9,
                           4, 6, 3, 10, 9, 7, 2, 7, 2, 5, 7, 6, 9, 5, 1, 10, 4, 9, 3, 3, 10, 8, 6, 1, 9, 8, 3, 7, 10,
                           10, 2, 8, 10, 9, 1, 2, 7, 6, 8, 3, 7, 3, 10, 2, 5, 1, 5, 7, 6, 4, 4, 4, 1, 6, 6, 6, 1, 3, 5,
                           1, 4, 8, 6, 7, 3, 4, 1, 7, 3],
            "river_size": 100000000000
        }
        response = tester.post(json=request_body, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_solution_fail_to_jump(self):
        tester = app.test_client(self)
        request_body = {
            "leaves_pos": [5, 4, 4, 7, 4, 1, 9, 1, 1, 5, 6, 2, 7, 10, 2, 8, 7, 8, 7, 8, 6, 6, 9, 4, 8, 2, 8, 9, 7, 6, 9,
                           4, 6, 3, 10, 9, 7, 2, 7, 2, 5, 7, 6, 9, 5, 1, 10, 4, 9, 3, 3, 10, 8, 6, 1, 9, 8, 3, 7, 10,
                           10, 2, 8, 10, 9, 1, 2, 7, 6, 8, 3, 7, 3, 10, 2, 5, 1, 5, 7, 6, 4, 4, 4, 1, 6, 6, 6, 1, 3, 5,
                           1, 4, 8, 6, 7, 3, 4, 1, 7, 3],
            "river_size": 100
        }
        response = tester.post(json=request_body, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "time_to_jump": -1,
            "message": "The frog can't jump to another river side"
        })

    def test_solution_fail_to_jump_2(self):
        tester = app.test_client(self)
        request_body = {
            "leaves_pos": [5, 4, 4, 7, 4, 1, 9, 1, 1, 5, 6, 2, 7, 10, 2, 8, 7, 8, 7, 8, 6, 6, 9, 4, 8, 2, 8, 9, 7, 6, 9,
                           4, 6, 3, 10, 9, 7, 2, 7, 2, 5, 7, 6, 9, 5, 1, 10, 4, 9, 3, 3, 10, 8, 6, 1, 9, 8, 3, 7, 10,
                           10, 2, 8, 10, 9, 1, 2, 7, 6, 8, 3, 7, 3, 10, 2, 5, 1, 5, 7, 6, 4, 4, 4, 1, 6, 6, 6, 1, 3, 5,
                           1, 4, 8, 6, 7, 3, 4, 1, 7, 3],
            "river_size": 20
        }
        response = tester.post(json=request_body, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "time_to_jump": -1,
            "message": "The frog can't jump to another river side"
        })


if __name__ == '__main__':
    unittest.main()
