from LedFxAPI.rest_client import RESTClient


class RawAPI:

    def __init__(self, host, port, ssl=False):
        self._client = RESTClient(host, port, '/api/', ssl)

    # method order follows api spec
    # general section

    async def ledfx_info(self):
        """
        Returns basic information about the LedFx instance as JSON

        :return: dict
        """
        return await self._client.get('info')

    async def ledfx_config(self):
        """
        Returns the current configuration for LedFx as JSON

        :return: dict
        """
        return await self._client.get('config')

    async def ledfx_schema(self):
        """
        Returns all LedFx schemas for devices, effects, and integrations as JSON

        :return: dict
        """
        return await self._client.get('schema')

    async def ledfx_schema_devices(self):
        """
        Returns all the devices registered with LedFx

        :return: dict
        """
        return await self._client.get('schema/device')

    async def ledfx_schema_effect(self):
        """
        Returns all the valid schemas for an LedFx effect

        :return: dict
        """
        return await self._client.get('schema/effect')

    async def ledfx_schema_integration(self):
        """
        Returns all the integrations registered with LedFx

        :return: dict
        """
        return await self._client.get('schema/integration')

    async def ledfx_log(self):
        """
        Not yet implemented

        :return: NotImplementedError
        """
        raise NotImplementedError('Endpoint available in upcoming version')

    # devices

    async def devices_all_config(self):
        """
        Get configuration of all devices

        :return: dict
        """
        return await self._client.get('devices')

    async def devices_add(self, config):
        """
        Adds a new device to LedFx based on the provided JSON configuration

        :param config: device config as JSON
        :return: status as dict
        """
        return await self._client.post('devices', data=config)

    async def devices_config_by_id(self, device_id: str):
        """
        Returns information about the device

        :param device_id: ID of the device
        :return: dict
        """
        return await self._client.get(f"devices/{device_id}")

    async def devices_modify_by_id(self, device_id: str, config):
        """
        Modifies the information pertaining to the device and returns the new device as JSON

        :param device_id: ID of the device
        :param config: device config as JSON
        :return: new device config as dict
        """
        return await self._client.put(f"devices/{device_id}", data=config)

    async def devices_delete_by_id(self, device_id: str):
        """
        Deletes a device with the matching device_id

        :param device_id: ID of the device
        :return: status as dict
        """
        return await self._client.delete(f"devices/{device_id}")

    # effects

    async def effects_get_current(self):
        """
        Returns all the effects currently created in LedFx as JSON

        :return: dict
        """
        return await self._client.get('effects')

    async def effects_new(self, config):
        """
        Not yet implemented

        :param config:
        :return: NotImplementedError
        """
        raise NotImplementedError

    async def effects_by_id(self, effect_id: str):
        """
        Returns information about the effect

        :param effect_id: Id of the effect
        :return: dict
        """
        return await self._client.get(f"effects/{effect_id}")

    async def effects_modify(self, effect_id: str, config):
        """
        Not yet implemented

        :param effect_id: Id of the effect
        :param config:
        :return: NotImplementedError
        """
        raise NotImplementedError

    async def effects_delete(self, effect_id: str):
        """
        Not yet implemented

        :param effect_id: Id if the effect
        :return: NotImplementedError
        """
        raise NotImplementedError

    # device effects

    async def device_get_effect(self, device_id: str):
        """
        Returns the active effect config of a device

        :param device_id: Id if the device
        :return: dict
        """
        return await self._client.get(f"devices/{device_id}/effects")

    async def device_update_effect(self, device_id: str, effect_config='RANDOMIZE'):
        """
        Update the active effect config of a device based on the provided JSON configuration.
        If config given is “RANDOMIZE”, the active effect config will be automatically generated to random values

        :param device_id:
        :param effect_config: dict
        :return: dict
        """
        return await self._client.put(f"devices/{device_id}/effects", data=effect_config)

    async def device_set_new_effect(self, device_id: str, effect_config):
        """
        Set the device to a new effect based on the provided JSON configuration

        :param device_id:
        :param effect_config:
        :return: dict
        """
        return await self._client.post(f"devices/{device_id}/effects", data=effect_config)

    async def device_delete_effect(self, device_id: str):
        """
        Clear the active effect of a device

        :param device_id:
        :return: dict
        """
        return await self._client.delete(f"devices/{device_id}/effects")

    # device presets

    async def device_get_presets(self, device_id: str):
        """
        Get preset effect configs for active effect of a device

        :param device_id: Id of the device
        :return: dict
        """
        return await self._client.get(f"devices/{device_id}/presets")

    async def device_set_preset(self, device_id: str, preset):
        """
        Set active effect config of device to a preset

        :param device_id: Id of the device
        :param preset: dict
        :return: dict
        """
        return await self._client.put(f"devices/{device_id}/presets", data=preset)

    async def device_save_as_preset(self, device_id: str, preset_config):
        """
        Save configuration of device’s active effect as a custom preset for that effect

        :param device_id: Id of the device
        :param preset_config: JSON
        :return: dict
        """
        return await self._client.post(f"devices/{device_id}/presets", data=preset_config)

    async def device_clear_effect(self, device_id: str):
        """
        Clear effect of a device

        :param device_id: Id of the device
        :return: status as dict
        """
        return await self._client.delete(f"devices/{device_id}/presets")

    # effect presets

    async def effect_get_presets(self, effect_id: str):
        """
        Get all presets for an effect

        :param effect_id: Id of the effect
        :return: dict
        """
        return await self._client.get(f"effects/{effect_id}/presets")

    async def effect_rename_preset(self, effect_id: str, preset_config):
        """
        Rename a preset

        :param effect_id: Id of the effect
        :param preset_config: dict
        :return: dict
        """
        return await self._client.put(f"effects/{effect_id}/presets", data=preset_config)

    async def effect_delete_preset(self, effect_id: str, preset_config):
        """
        Delete a preset

        :param effect_id: Id of the effect
        :param preset_config: dict
        :return: dict
        """
        return await self._client.delete(f"effects/{effect_id}/presets", data=preset_config)

    # scenes

    async def scenes_get_all(self):
        """
        Get all saved scenes

        :return: dict
        """
        return await self._client.get('scenes')

    async def scenes_set(self, scene_config):
        """
        Set effects and configs of all devices to those specified in a scene

        :param scene_config: dict
        :return:
        """
        return self._client.put('scenes', data=scene_config)

    async def scenes_save_current_config_as_scene(self, scene_config):
        """
        Save effect configuration of devices as a scene

        :param scene_config: dict
        :return:
        """
        return await self._client.post('scenes', data=scene_config)

    async def scenes_delete_scene(self, scene_config):
        """
        Delete a scene

        :param scene_config: dict
        :return: dict
        """
        return await self._client.delete('scenes', data=scene_config)

    # virtuals

    async def virtuals_all(self):
        """
        Get all virtuals from the instance

        :return: dict
        """
        return await self._client.get('virtuals')

    async def virtuals_pause_unpause_all(self):
        """
        Pauses all virtuals or resumes when paused

        :return:
        """
        return await self._client.put('virtuals')

    async def virtuals_add(self, config):
        """
        Add a new virtual with the supplied config

        :param config: dict
        :return: dict
        """
        return await self._client.post('virtuals', data=config)

    # virtual config

    async def virtual_get_config(self, virtual_id):
        """
        Get configuration of a virtual

        :param virtual_id: Id of the virtual
        :return:
        """
        return await self._client.get(f"virtuals/{virtual_id}")

    async def virtual_pause_unpause(self, virtual_id, is_active: bool):
        """
        Pauses or unpauses a virtual

        :param virtual_id: Id of the virtual
        :param is_active:
        :return:
        """
        return await self._client.put(f"virtuals/{virtual_id}", {'active': is_active})

    # virtuals effects

    async def virtual_effect_active(self, virtual_id: str):
        """
        Active effect config

        :param virtual_id: Id of the virtual
        :return:
        """
        return await self._client.get(f"virtuals/{virtual_id}/effects")

    async def virtual_effect_update(self, virtual_id, config):
        """
        TODO add desc

        :param virtual_id:
        :param config:
        :return:
        """
        return await self._client.put(f"virtuals/{virtual_id}/effects", data=config)

    async def virtual_effect_set(self, virtual_id, config):
        """
        TODO add desc

        :param virtual_id:
        :param config:
        :return:
        """
        return await self._client.post(f"virtuals/{virtual_id}/effects", config)

    # virtual presets

    async def virtual_presets_active(self, virtual_id):
        """
        TODO add desc

        :param virtual_id:
        :return:
        """
        return await self._client.get(f"virtuals/{virtual_id}/presets")

    async def virtual_presets_set(self, virtual_id, config):
        """
        TODO add desc

        :param virtual_id:
        :param config:
        :return:
        """
        return await self._client.put(f"virtuals/{virtual_id}/presets", data=config)
