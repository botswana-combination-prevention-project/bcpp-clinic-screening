from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = 'bcpp_clinic_screening'
    listboard_template_name = 'bcpp_clinic_screening/listboard.html'
    dashboard_template_name = 'bcpp_clinic_screening/dashboard.html'
    base_template_name = 'bcpp_clinic/base.html'
    listboard_url_name = 'bcpp_clinic_screening:listboard_url'
    dashboard_url_name = 'bcpp_clinic_screening:dashboard_url'
    admin_site_name = 'bcpp_clinic_screening_admin'
    eligibility_age_adult_lower = 18
    eligibility_age_adult_upper = 64
    eligibility_age_minor_lower = 16
    eligibility_age_minor_upper = 17
