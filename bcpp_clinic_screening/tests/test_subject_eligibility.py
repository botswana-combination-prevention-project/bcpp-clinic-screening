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

    def test_create_registered_subject_2(self):
        """Test created registered subject matches the the subject eligibility.
        """
        self.screening_test_helper.make_eligibility()
        subject_eligibility = SubjectEligibility.objects.first()
        registered_subject = RegisteredSubject.objects.first()
        self.assertEqual(
            registered_subject.registration_identifier,
            subject_eligibility.screening_identifier)
        self.assertEqual(
            registered_subject.registration_identifier,
            subject_eligibility.registration_identifier)
        self.assertEqual(
            registered_subject.screening_identifier,
            subject_eligibility.screening_identifier)
