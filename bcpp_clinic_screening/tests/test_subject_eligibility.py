from django.test import TestCase, tag

from edc_registration.models import RegisteredSubject

from ..models import SubjectEligibility
from ..tests.screening_tests_helper import ScreeningTestHelper


class TestCreateClinicEligibility(TestCase):

    screening_test_helper = ScreeningTestHelper()

    @tag('eligibility_creation')
    def test_subject_eligibility(self):
        """Test create subject eligibilty.
        """
        self.screening_test_helper.make_eligibility()
        self.assertEqual(SubjectEligibility.objects.all().count(), 1)

    def test_create_registered_subject(self):
        """Test subject eligibilty creates registered subject.
        """
        self.screening_test_helper.make_eligibility()
        self.assertEqual(RegisteredSubject.objects.all().count(), 1)
