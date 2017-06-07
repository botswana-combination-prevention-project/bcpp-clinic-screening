from django.apps import AppConfig as DjangoApponfig
from django.conf import settings

from datetime import datetime
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from dateutil.tz import gettz


from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_appointment.facility import Facility
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_constants.constants import FAILED_ELIGIBILITY
from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from edc_lab.apps import AppConfig as BaseEdcLabAppConfig
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig, SubjectType, Cap
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT
from edc_base.utils import get_utcnow
from bcpp_clinic.navbars import navbars


class AppConfig(DjangoApponfig):
    name = 'clinic_screening'
    listboard_template_name = 'clinic_screening/listboard.html'
    dashboard_template_name = 'clinic_screening/dashboard.html'
    base_template_name = 'edc_base/base.html'
    listboard_url_name = 'clinic_screening:listboard_url'
    dashboard_url_name = 'clinic_screening:dashboard_url'
    admin_site_name = 'clinic_screening_admin'
    eligibility_age_adult_lower = 16
    eligibility_age_adult_upper = 64


class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
    use_settings = True
    device_id = settings.DEVICE_ID
    device_role = settings.DEVICE_ROLE


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'BHP066'
    protocol_number = '066'
    protocol_name = 'BCPP'
    protocol_title = 'Botswana Combination Prevention Project'
    subject_types = [
        SubjectType('clinic', 'Research Subject',
                    Cap(model_name='bcpp_clinic.clinicconsent', max_subjects=9999)),
    ]
    study_open_datetime = datetime(2013, 10, 18, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(2018, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))

    @property
    def site_name(self):
        from edc_map.site_mappers import site_mappers
        return site_mappers.current_map_area

    @property
    def site_code(self):
        from edc_map.site_mappers import site_mappers
        return site_mappers.current_map_code


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Ambition'
    institution = 'Botswana-Harvard AIDS Institute'
    copyright = '2017-{}'.format(get_utcnow().year)
    license = None

    def get_navbars(self):
        return navbars
