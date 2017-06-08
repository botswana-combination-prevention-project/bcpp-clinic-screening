from django.db import models


class EligibilityManager(models.Manager):

    def get_by_natural_key(self, eligibility_identifier):
        return self.get(
            eligibility_identifier=eligibility_identifier
        )


class EnrollmentLossManager(models.Manager):

    def get_by_natural_key(self, eligibility_identifier):
        return self.get(
            subject_eligibility__eligibility_identifier=eligibility_identifier
        )
