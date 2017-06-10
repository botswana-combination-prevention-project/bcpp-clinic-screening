# coding=utf-8

from dateutil.relativedelta import relativedelta
from faker import Faker
from model_mommy.recipe import Recipe, seq

from edc_base.utils import get_utcnow
from bcpp_clinic_screening.models import SubjectEligibility
from edc_constants.constants import YES, FEMALE, POS, NOT_APPLICABLE

from .constants import ABLE_TO_PARTICIPATE


fake = Faker()

subjectceligibility = Recipe(
    SubjectEligibility,
    report_datetime=get_utcnow,
    dob=(get_utcnow() - relativedelta(years=25)).date(),
    part_time_resident=YES,
    initials='EW',
    gender=FEMALE,
    has_identity=YES,
    hiv_status=POS,
    identity=seq('12315678'),
    confirm_identity=seq('12315678'),
    identity_type='OMANG',
    inability_to_participate=ABLE_TO_PARTICIPATE,
    citizen=YES,
    literacy=YES,
    guardian=NOT_APPLICABLE,
)
