from faker import Faker
from model_mommy.recipe import Recipe

from edc_base.utils import get_utcnow
from edc_constants.constants import YES, FEMALE, POS, NOT_APPLICABLE

from .models import SubjectEligibility


from .constants import ABLE_TO_PARTICIPATE


fake = Faker()

subjecteligibility = Recipe(
    SubjectEligibility,
    report_datetime=get_utcnow,
    age_in_years=27,
    part_time_resident=YES,
    initials='EW',
    gender=FEMALE,
    has_identity=YES,
    hiv_status=POS,
    inability_to_participate=ABLE_TO_PARTICIPATE,
    citizen=YES,
    literacy=YES,
    guardian=NOT_APPLICABLE,
)
