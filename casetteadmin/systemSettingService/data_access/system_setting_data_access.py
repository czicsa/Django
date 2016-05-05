from systemSettingService.models import SystemSetting

def get_system_setting_by_resource_key(resource_key):
    return SystemSetting.objects.get(resource_key = resource_key)