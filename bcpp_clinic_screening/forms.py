from django import forms


from edc_base.modelform_mixins import CommonCleanModelFormMixin
from edc_constants.constants import NO

from .models import SubjectEligibility, EnrollmentLoss


class SubjectModelFormMixin(CommonCleanModelFormMixin, forms.ModelForm):

    pass


class SubjectEligibilityForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        try:
            if self.instance.is_consented:
                raise forms.ValidationError(
                    'Household member for this checklist has been consented. '
                    'Eligibility checklist may not be edited')
        except AttributeError:
            pass
        if cleaned_data.get('has_identity') == NO and cleaned_data.get('identity'):
            raise forms.ValidationError(
                'You indicated the patient did not provide '
                'an identity but identity is provided. Please correct.')
        if cleaned_data.get('has_identity') == 'Yes' and not cleaned_data.get('identity'):
            raise forms.ValidationError(
                'You indicated the patient did has provided '
                'an identity but no identity has been provided. Please correct.')
        if cleaned_data.get('identity'):
            if not self.instance:
                self._meta.model.check_for_known_identity(
                    cleaned_data.get('identity'), forms.ValidationError)

        return cleaned_data

    class Meta:
        model = SubjectEligibility
        fields = '__all__'


class EnrollmentLossForm(SubjectModelFormMixin):

    class Meta:
        model = EnrollmentLoss
        fields = '__all__'
