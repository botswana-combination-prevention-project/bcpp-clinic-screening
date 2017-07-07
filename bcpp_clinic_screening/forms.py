from django import forms

from edc_base.modelform_mixins import CommonCleanModelFormMixin

from .models import SubjectEligibility, EnrollmentLoss


class SubjectModelFormMixin(CommonCleanModelFormMixin, forms.ModelForm):

    pass


class SubjectEligibilityForm(SubjectModelFormMixin):

    class Meta:
        model = SubjectEligibility
        fields = '__all__'


class EnrollmentLossForm(SubjectModelFormMixin):

    class Meta:
        model = EnrollmentLoss
        fields = '__all__'
