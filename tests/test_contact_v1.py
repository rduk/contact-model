from contact_model import app
import unittest
import json


class TestIntegrations(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_homepage_status_code(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_all_contact_model_get_status_code(self):
        resp = self.app.get('/api/v1/allcontacts')
        self.assertEqual(resp.status_code, 200)

    def test_all_contact_model_post_status_code(self):
        res= self.app.post('/api/v1/allcontacts',
                 data=dict(uname='adamdavis',
                      email='adam.davis@email.com',
                      fname='Adam',
                      sname='Davis'))
        # there is a redirection in post method, hence we get status code 302 (and not 200)
        self.assertEqual(res.status_code, 302)

    def test_all_contact_model_get_status(self):
        res_post= self.app.post('/api/v1/allcontacts',
                 data=dict(uname='jack1',
                      email='jack1@email.com',
                      fname='Jack',
                      sname='One'))
        res_get= self.app.get('/api/v1/allcontacts/jack1')
        self.assertEqual(res_get.status_code, 200)

    def test_all_contact_model_get_content(self):
        res_post= self.app.post('/api/v1/allcontacts',
                 data=dict(uname='tom1',
                      email='tom1@email.com',
                      fname='Tom',
                      sname='One'))
        res_get= self.app.get('/api/v1/allcontacts/tom1')
        data_get = (json.loads(res_get.data))
        self.assertEqual(data_get['user']['uname'], 'tom1')

    def test_all_contact_model_post_content(self):
        res_post= self.app.post('/api/v1/allcontacts',
                 data=dict(uname='adam1',
                      email='adam1@email.com',
                      fname='Adam',
                      sname='One'))
        res_post = self.app.get('/api/v1/allcontacts/adam1')
        data_post = (json.loads(res_post.data))
        self.assertEqual(data_post['user']['uname'], 'adam1')

    def test_contact_model_put_content(self):
        # testing the data inserted in previous function
        res_post= self.app.post('/api/v1/allcontacts',
                 data=dict(uname='adam2',
                      email='adam2@email.com',
                      fname='adam',
                      sname='two'))
        res_put = self.app.put('/api/v1/allcontacts/adam2',
                 data=dict(email='new_adam_two@email.com',
                      fname='Adam',
                      sname='Banks'))
        res_put = self.app.get('/api/v1/allcontacts/adam2')
        data_put = (json.loads(res_put.data))
        self.assertEqual(data_put['user']['sname'], 'Banks')


    def test_contact_model_del_content(self):
        # testing the data inserted in previous function
        res_post= self.app.post('/api/v1/allcontacts',
                 data=dict(uname='adam3',
                      email='adam3@email.com',
                      fname='adam',
                      sname='three'))
        del_req = self.app.delete('/api/v1/allcontacts/adam3')
        res_del = self.app.get('/api/v1/allcontacts/adam3')
        self.assertEqual(res_del.status_code, 404)


if __name__ == '__main__':
    unittest.main()

