from django.contrib import admin

from edc_base.fieldsets import FieldsetsModelAdminMixin
from edc_base.modeladmin_mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin)
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin

from .admin_site import bcpp_clinic_screening_admin
from .forms import SubjectEligibilityForm, EnrollmentLossForm
from .models import EnrollmentLoss, SubjectEligibility


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'


@admin.register(SubjectEligibility, site=bcpp_clinic_screening_admin)
class SubjectEligibilityAdmin(ModelAdminMixin, FieldsetsModelAdminMixin, admin.ModelAdmin):

    form = SubjectEligibilityForm

    instructions = ['This form is a tool to assist the Interviewer to confirm the '
                    'Eligibility status of the subject. After entering the required items, click SAVE.']

    fields = (
        'report_datetime',
        'first_name',
        'initials',
        'dob',
        'verbal_age',
        'gender',
        'has_identity',
        "citizen",
        "legal_marriage",
        "marriage_certificate",
        "part_time_resident",
        "literacy",
        "guardian",
        'inability_to_participate',
        "hiv_status",
    )

    list_display = (
        'report_datetime', 'gender', 'is_eligible', 'is_consented', 'is_refused')

    list_filter = ('gender', 'is_eligible', 'is_consented',
                   'is_refused', 'report_datetime', 'community')

    radio_fields = {
        'has_identity': admin.VERTICAL,
        "gender": admin.VERTICAL,
        "citizen": admin.VERTICAL,
        "legal_marriage": admin.VERTICAL,
        "marriage_certificate": admin.VERTICAL,
        "part_time_resident": admin.VERTICAL,
        "literacy": admin.VERTICAL,
        "guardian": admin.VERTICAL,
        "inability_to_participate": admin.VERTICAL,
        "hiv_status": admin.VERTICAL,
    }

    search_fields = (
        'first_name',
        'initials',
    )


@admin.register(EnrollmentLoss, site=bcpp_clinic_screening_admin)
class ClinicEnrollmentLossAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = EnrollmentLossForm

    fields = ('clinic_eligibility', 'report_datetime', 'reason')

    list_display = (
        'report_datetime', 'reason', 'user_created',
        'user_modified', 'hostname_created')

    list_filter = ('report_datetime', 'reason', 'user_created',
                   'user_modified', 'hostname_created')

    radio_fields = {}

    instructions = []
