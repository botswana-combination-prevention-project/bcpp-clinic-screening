from django.test import TestCase, tag

from edc_sync.tests.sync_test_helper import SyncTestHelper


@tag('natural_key')
class TestNaturalKey(TestCase):

    sync_helper = SyncTestHelper()

    def test_natural_key_attrs(self):
        self.sync_helper.sync_test_natural_key_attr('bcpp_clinic_screening')

    def test_get_by_natural_key_attr(self):
        self.sync_helper.sync_test_get_by_natural_key_attr(
            'bcpp_clinic_screening')
