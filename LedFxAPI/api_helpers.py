from enum import Enum

from .api import API


class PresetType(Enum):
    DEFAULT = 'default_presets'
    CUSTOM = 'custom_presets'


class APIHelpers:
    def __init__(self, api: API, enable_preset_helpers=True):
        self._api = api
        self._preset_helpers_enabled = enable_preset_helpers
        if enable_preset_helpers:
            effects = self.get_all_effect_ids()
            preset_type_lookup = {}
            for effect_id in effects:
                default_presets = self.get_presets_for_effect(effect_id, PresetType.DEFAULT)
                for default_preset in default_presets:
                    preset_type_lookup[default_preset] = PresetType.DEFAULT
                custom_presets = self.get_presets_for_effect(effect_id, PresetType.CUSTOM)
                for custom_preset in custom_presets:
                    preset_type_lookup[custom_preset] = PresetType.CUSTOM
            self._preset_lookup = preset_type_lookup

    def get_all_device_ids(self):
        """
        Get the ids of all existing devices

        :return: list of ids
        """
        data = self._api.devices_all_config()
        devices = data['devices']
        return [devices[key]['id'] for key in devices.keys()]

    def get_all_effect_ids(self):
        """
        Get the ids if all effects

        :return: List
        """
        schema = self._api.ledfx_schema()
        return list(schema['effects'].keys())

    def get_presets_for_effect(self, effect_id, preset_type: PresetType):
        """
        Get all presets of given type for the given effect

        :param effect_id: ID of the effect
        :param preset_type: preset type, default_presets or custom_presets
        :return: List
        """
        return list(self._api.effect_get_presets(effect_id)[preset_type.value].keys())

    def get_all_presets_for_effect(self, effect_id):
        """
        Get all presets of for the given effect

        :param effect_id: ID of the effect
        :return: List of all preset ids
        """
        default_presets = list(self._api.effect_get_presets(effect_id)[PresetType.DEFAULT.value].keys())
        custom_presets = list(self._api.effect_get_presets(effect_id)[PresetType.CUSTOM.value].keys())
        return default_presets + custom_presets

    def set_preset(self, virtual_id, effect_id, preset_id):
        if preset_id not in self._preset_lookup.keys():
            raise ValueError("Invalid preset id")
        preset_type = self._preset_lookup[preset_id]
        data = {
            'category': preset_type.value,
            'effect_id': effect_id,
            'preset_id': preset_id
        }
        return self._api.virtual_presets_set(virtual_id, data)

