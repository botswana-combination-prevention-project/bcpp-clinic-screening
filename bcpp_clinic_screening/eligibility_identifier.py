from edc_identifier.simple_identifier import SimpleIdentifier


class EligibilityIdentifier(SimpleIdentifier):

    random_string_length = 5
    identifier_type = 'eligibility_identifier'
    template = 'S{device_id}{random_string}'
    model = 'bcpp_clinic_screening.identifierhistory'
