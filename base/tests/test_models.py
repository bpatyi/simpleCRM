from django.test import TestCase

from base.models import GeoCoderLog


class GeoCoderLogTester(TestCase):

    def setUp(self):
        self.geo_coder_log = GeoCoderLog.get_today_record()

    def test_get_today_record(self):
        self.assertIsInstance(self.geo_coder_log, GeoCoderLog)

    def test_get_today_record_default_value(self):
        self.assertEqual(self.geo_coder_log.number_of_request, 0)

    def test_get_today_record_get_limit(self):
        if self.geo_coder_log.number_of_request == 0:
            self.assertEqual(self.geo_coder_log.get_limit(), 2500)
        else:
            self.assertEqual(self.geo_coder_log.get_limit(), 2500 - self.geo_coder_log.number_of_request)
