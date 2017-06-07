from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'BCPP Clinic'
    site_header = 'BCPP Clinic'
    index_title = 'BCPP Clinic'
    site_url = '/clinic_screening/list/'


clinic_screening_admin = AdminSite(name='clinic_screening_admin')
