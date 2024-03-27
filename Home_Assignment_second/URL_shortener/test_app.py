import unittest
import json
from datetime import datetime
from unittest import TestCase
from app import app, URL, Stats
from models import Session, engine, Base

class TestURLShortener(TestCase):
    def setUp(self):
        self.app = app.test_client()
        Base.metadata.create_all(engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(engine)

    def test_shorten_url(self):
        url = 'https://www.example.com/'
        response = self.app.post('/shorten', data=json.dumps({'url': url}), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('shortcode', data)
        shortcode = data['shortcode']

        # Test if the URL and Stats were saved correctly
        saved_url = self.session.query(URL).filter_by(shortcode=shortcode).first()
        self.assertIsNotNone(saved_url)
        self.assertEqual(saved_url.url, url)

        saved_stats = self.session.query(Stats).filter_by(shortcode=shortcode).first()
        self.assertIsNotNone(saved_stats)
        self.assertIsNotNone(saved_stats.created)
        self.assertIsNone(saved_stats.last_redirect)
        self.assertEqual(saved_stats.redirect_count, 0)

    def test_redirect_url(self):
        url = 'https://www.example.com/'
        shortcode = 'abc123'
        new_url = URL(shortcode=shortcode, url=url)
        new_stats = Stats(shortcode=shortcode, created=datetime.now())
        self.session.add(new_url)
        self.session.add(new_stats)
        self.session.commit()

        response = self.app.get(f'/{shortcode}')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, url)

        # Test if the Stats were updated correctly
        saved_stats = self.session.query(Stats).filter_by(shortcode=shortcode).first()
        self.assertIsNotNone(saved_stats.last_redirect)
        self.assertEqual(saved_stats.redirect_count, 1)


if __name__ == '__main__':
    unittest.main()
