from django import forms

from edc_base.modelform_mixins import (
    CommonCleanModelFormMixin, ApplicableValidationMixin,
    RequiredFieldValidationMixin)

from .models import ClinicEligibility, EnrollmentLoss


class SubjectModelFormMixin(CommonCleanModelFormMixin,
                            ApplicableValidationMixin,
                            RequiredFieldValidationMixin,
                            forms.ModelForm):

    pass


class ClinicEligibilityForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super(ClinicEligibilityForm, self).clean()
        try:
            if self.instance.is_consented:
                raise forms.ValidationError('Household member for this checklist has been consented. '
                                            'Eligibility checklist may not be edited')
        except AttributeError:
            pass
        if cleaned_data.get('has_identity') == 'No' and cleaned_data.get('identity'):
            raise forms.ValidationError('You indicated the patient did not provide '
                                        'an identity but identity is provided. Please correct.')
        if cleaned_data.get('has_identity') == 'Yes' and not cleaned_data.get('identity'):
            raise forms.ValidationError('You indicated the patient did has provided '
                                        'an identity but no identity has been provided. Please correct.')
        if cleaned_data.get('identity'):
            if not self.instance:
                self._meta.model.check_for_known_identity(
                    cleaned_data.get('identity'), forms.ValidationError)

        self._meta.model.check_for_consent(
            cleaned_data.get('identity'), forms.ValidationError)

        return cleaned_data

    class Meta:
        model = ClinicEligibility
        fields = '__all__'


class EnrollmentLossForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super(EnrollmentLossForm, self).clean()

        return cleaned_data

    class Meta:
        model = EnrollmentLoss
        fields = '__all__'
