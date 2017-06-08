from dateutil.relativedelta import relativedelta

from django.test import TestCase, tag
from django.utils import timezone

from edc_constants.constants import MALE, NOT_APPLICABLE, YES, POS

from ..constants import ABLE_TO_PARTICIPATE
from ..models import SubjectEligibility


class TestCreateClinicEligibility(TestCase):

    def setUp(self):
        self.options = dict(
            report_datetime=timezone.now(),
            dob=(timezone.now() - relativedelta(years=25)).date(),
            part_time_resident=YES,
            initials='TT',
            gender=MALE,
            has_identity=YES,
            hiv_status=POS,
            identity='12315678',
            confirm_identity='12315678',
            identity_type='OMANG',
            inability_to_participate=ABLE_TO_PARTICIPATE,
            citizen=YES,
            literacy=YES,
            guardian=NOT_APPLICABLE,
            age_in_years=27)

    @tag('eligibility_creation')
    def test_clinic_eligibility(self):
        """Test create clinic eligibilty.
        """
        SubjectEligibility.objects.create(**self.options)
        self.assertEqual(SubjectEligibility.objects.all().count(), 1)
