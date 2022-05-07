from enum import Enum

from .raw_api import RawAPI
from .rest_client import ApiError


class PresetType(Enum):
    DEFAULT = 'default_presets'
    CUSTOM = 'custom_presets'


class APIHelpers:
    def __init__(self, api: RawAPI):
        self._api = api
        self._preset_lookup = None

    async def load_helpers(self):
        effects = await self.get_all_effect_ids()
        preset_type_lookup = {}
        for effect_id in effects:
            default_presets = await self.get_presets_for_effect(effect_id, PresetType.DEFAULT)
            if default_presets is not None:
                for default_preset in default_presets:
                    preset_type_lookup[default_preset] = PresetType.DEFAULT
            custom_presets = await self.get_presets_for_effect(effect_id, PresetType.CUSTOM)
            if custom_presets is not None:
                for custom_preset in custom_presets:
                    preset_type_lookup[custom_preset] = PresetType.CUSTOM
        self._preset_lookup = preset_type_lookup

    async def get_all_virtuals(self):
        """
        Get the ids of all existing devices

        :return: list of ids
        """
        data = await self._api.virtuals_all()
        devices = data['virtuals']
        return [devices[key]['id'] for key in devices.keys()]

    async def get_all_effect_ids(self):
        """
        Get the ids if all effects

        :return: List
        """
        schema = await self._api.ledfx_schema()
        return list(schema['effects'].keys())

    async def get_presets_for_effect(self, effect_id, preset_type: PresetType):
        """
        Get all presets of given type for the given effect

        :param effect_id: ID of the effect
        :param preset_type: preset type, default_presets or custom_presets
        :return: List
        """
        presets = await self._api.effect_get_presets(effect_id)
        if presets is None:
            return None
        return list(presets[preset_type.value].keys())

    async def get_all_presets_for_effect(self, effect_id):
        """
        Get all presets of for the given effect

        :param effect_id: ID of the effect
        :return: List of all preset ids
        """
        presets = await self._api.effect_get_presets(effect_id)
        if presets['status'] == 'failed':
            raise ApiError(presets['reason'])
        default_presets = list(presets[PresetType.DEFAULT.value].keys())
        custom_presets = list(presets[PresetType.CUSTOM.value].keys())
        return default_presets + custom_presets

    async def set_preset(self, virtual_id, effect_id, preset_id):
        if preset_id not in self._preset_lookup.keys():
            raise ValueError("Invalid preset id")
        preset_type = self._preset_lookup[preset_id]
        data = {
            'category': preset_type.value,
            'effect_id': effect_id,
            'preset_id': preset_id
        }
        return await self._api.virtual_presets_set(virtual_id, data)


