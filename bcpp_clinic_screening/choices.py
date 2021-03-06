from django.utils.translation import ugettext_lazy as _

from edc_constants.constants import NOT_APPLICABLE, POS, NEG, IND, UNK, OTHER

from .constants import ABLE_TO_PARTICIPATE, MENTAL_INCAPACITY

VERBALHIVRESULT_CHOICE = (
    (POS, _('HIV Positive')),
    (NEG, _('HIV Negative')),
    (IND, _('Indeterminate')),
    (UNK, _('I am not sure')),
    ('not_answering', _('Don\'t want to answer')),
)

INABILITY_TO_PARTICIPATE_REASON = (
    (ABLE_TO_PARTICIPATE, ('ABLE to participate')),
    (MENTAL_INCAPACITY, ('Mental Incapacity')),
    ('Deaf/Mute', ('Deaf/Mute')),
    ('Too sick', ('Too sick')),
    ('Incarcerated', ('Incarcerated')),
    (OTHER, ('Other, specify.')),
    (NOT_APPLICABLE, ('Not applicable')),
)
