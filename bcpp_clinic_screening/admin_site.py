from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'BCPP Clinic'
    site_header = 'BCPP Clinic'
    index_title = 'BCPP Clinic'
    site_url = '/bcpp_clinic_screening/list/'


bcpp_clinic_screening_admin = AdminSite(name='bcpp_clinic_screening_admin')
