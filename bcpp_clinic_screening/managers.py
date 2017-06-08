from django.db import models


class EligibilityManager(models.Manager):

    def get_by_natural_key(self, eligibility_identifier):
        return self.get(
            eligibility_identifier=eligibility_identifier
        )
