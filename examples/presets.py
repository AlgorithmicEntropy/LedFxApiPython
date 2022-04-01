from LedFxAPI import api

my_api = api.API('192.168.178.27', '8888')

effects = my_api.effects_get_current()
print(effects)

ids = my_api.devices_all_ids()
print(ids)
my_device = ids[0]
effects = my_api.device_get_effect(my_device)

effects = effects['effect']

effect_name = effects['name']
effect_type = effects['type']

presets = my_api.device_get_presets(my_device)

default_presets = list(presets['default_presets'].keys())

preset_obj = {
    'category': 'default_presets',
    'effect_id': effect_type,
    'preset_id': default_presets[3]
}

response = my_api.device_set_preset(my_device, preset_obj)
print(response)