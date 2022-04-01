from rest_client import RESTClient


class API:

    def __init__(self, host, port, https=False):
        self._client = RESTClient(host, port, '/api/', https)

    # method order follows api spec
    # general section

    def ledfx_info(self):
        """
        Returns basic information about the LedFx instance as JSON

        :return: JSON obj
        """
        return self._client.get('info')

    def ledfx_config(self):
        """
        Returns the current configuration for LedFx as JSON

        :return: JSON obj
        """
        return self._client.get('config')

    def ledfx_schema(self):
        """
        Returns all LedFx schemas for devices, effects, and integrations as JSON

        :return: JSON obj
        """
        return self._client.get('schema')

    def ledfx_schema_devices(self):
        """
        Returns all the devices registered with LedFx

        :return: JSON obj
        """
        return self._client.get('schema/device')

    def ledfx_schema_effect(self):
        """
        Returns all the valid schemas for an LedFx effect

        :return: JSON obj
        """
        return self._client.get('schema/effect')

    def ledfx_schema_integration(self):
        """
        Returns all the integrations registered with LedFx

        :return: JSON obj
        """
        return self._client.get('schema/integration')

    def ledfx_log(self):
        """
        Not yet implemented

        :return: NotImplementedError
        """
        raise NotImplementedError('Endpoint available in upcoming version')

    # devices

    def devices_all_config(self):
        """
        Get configuration of all devices

        :return: JSON obj
        """
        return self._client.get('devices')

    def devices_add(self, config):
        """
        Adds a new device to LedFx based on the provided JSON configuration

        :param config: device config as JSON
        :return: status as JSON obj
        """
        return self._client.post('devices', data=config)

    def devices_config_by_id(self, device_id: str):
        """
        Returns information about the device

        :param device_id: ID of the device
        :return: JSON obj
        """
        return self._client.get(f"devices/{device_id}")

    def devices_modify_by_id(self, device_id: str, config):
        """
        Modifies the information pertaining to the device and returns the new device as JSON

        :param device_id: ID of the device
        :param config: device config as JSON
        :return: new device config as JSON obj
        """
        return self._client.put(f"devices/{device_id}", data=config)

    def devices_delete_by_id(self, device_id: str):
        """
        Deletes a device with the matching device_id

        :param device_id: ID of the device
        :return: status as JSON obj
        """
        return self._client.delete(f"devices/{device_id}")

    # effects

    def effects_get_current(self):
        """
        Returns all the effects currently created in LedFx as JSON

        :return: JSON obj
        """
        return self._client.get('effects')

    def effects_new(self, config):
        """
        Not yet implemented

        :param config:
        :return: NotImplementedError
        """
        raise NotImplementedError

    def effects_by_id(self, effect_id: str):
        """
        Returns information about the effect

        :param effect_id: Id of the effect
        :return: JSON obj
        """
        return self._client.get(f"effects/{effect_id}")

    def effects_modify(self, effect_id: str, config):
        """
        Not yet implemented

        :param effect_id: Id of the effect
        :param config:
        :return: NotImplementedError
        """
        raise NotImplementedError

    def effects_delete(self, effect_id: str):
        """
        Not yet implemented

        :param effect_id: Id if the effect
        :return: NotImplementedError
        """
        raise NotImplementedError

    # device effects

    def device_get_effect(self, device_id: str):
        """
        Returns the active effect config of a device

        :param device_id: Id if the device
        :return: JSON obj
        """
        return self._client.get(f"devices/{device_id}/effects")

    def device_update_effect(self, device_id: str, effect_config='RANDOMIZE'):
        """
        Update the active effect config of a device based on the provided JSON configuration.
        If config given is “RANDOMIZE”, the active effect config will be automatically generated to random values

        :param device_id:
        :param effect_config: JSON obj
        :return: JSON obj
        """
        return self._client.put(f"devices/{device_id}/effects", data=effect_config)

    def device_set_new_effect(self, device_id: str, effect_config):
        """
        Set the device to a new effect based on the provided JSON configuration

        :param device_id:
        :param effect_config:
        :return: JSON obj
        """
        return self._client.post(f"devices/{device_id}/effects", data=effect_config)

    def device_delete_effect(self, device_id: str):
        """
        Clear the active effect of a device

        :param device_id:
        :return: JSON obj
        """
        return self._client.delete(f"devices/{device_id}/effects")

    # device presets

    def device_get_presets(self, device_id: str):
        """
        Get preset effect configs for active effect of a device

        :param device_id: Id of the device
        :return: JSON obj
        """
        return self._client.get(f"devices/{device_id}/presets")

    def device_set_preset(self, device_id: str, preset):
        """
        Set active effect config of device to a preset

        :param device_id: Id of the device
        :param preset: JSON obj
        :return: JSON obj
        """
        return self._client.put(f"devices/{device_id}/presets", data=preset)

    def device_save_as_preset(self, device_id: str, preset_config):
        """
        Save configuration of device’s active effect as a custom preset for that effect

        :param device_id: Id of the device
        :param preset_config: JSON
        :return: JSON obj
        """
        return self._client.post(f"devices/{device_id}/presets", data=preset_config)

    def device_clear_effect(self, device_id: str):
        """
        Clear effect of a device

        :param device_id: Id of the device
        :return: status as JSON obj
        """
        return self._client.delete(f"devices/{device_id}/presets")

    # effect presets

    def effect_get_presets(self, effect_id: str):
        """
        Get all presets for an effect

        :param effect_id: Id of the effect
        :return: JSON obj
        """
        return self._client.get(f"effects/{effect_id}/presets")

    def effect_rename_preset(self, effect_id: str, preset_config):
        """
        Rename a preset

        :param effect_id: Id of the effect
        :param preset_config: JSON obj
        :return: JSON obj
        """
        return self._client.put(f"effects/{effect_id}/presets", data=preset_config)

    def effect_delete_preset(self, effect_id: str, preset_config):
        """
        Delete a preset

        :param effect_id: Id of the effect
        :param preset_config: JSON obj
        :return: JSON obj
        """
        return self._client.delete(f"effects/{effect_id}/presets", data=preset_config)

    # scenes

    def scenes_get_all(self):
        """
        Get all saved scenes

        :return: JSON obj
        """
        return self._client.get('scenes')

    def scenes_set(self, scene_config):
        """
        Set effects and configs of all devices to those specified in a scene

        :param scene_config: JSON obj
        :return: JSON obj
        """
        return self._client.put('scenes', data=scene_config)

    def scenes_save_current_config_as_scene(self, scene_config):
        """
        Save effect configuration of devices as a scene

        :param scene_config: JSON obj
        :return: JSON obj
        """
        return self._client.post('scenes', data=scene_config)

    def scenes_delete_scene(self, scene_config):
        """
        Delete a scene
        :param scene_config: JSON obj
        :return: JSON obj
        """
        return self._client.delete('scenes', data=scene_config)

    # virtuals

    def virtuals_all(self):
        return self._client.get('virtuals')

    def virtuals_pause_all(self):
        return self._client.put('virtuals')

    def virtuals_add(self, config):
        return self._client.post('virtuals', data=config)

    # virtuals effects

    def virtual_effect_active(self, virtual_id):
        return self._client.get(f"virtuals/{virtual_id}/effects")

    def virtual_effect_update(self, virtual_id, config):
        return self._client.put(f"virtuals/{virtual_id}/effects", data=config)

    def virtual_effect_set(self, virtual_id, config):
        return self._client.post(f"virtuals/{virtual_id}/effects", config)

    # virtual presets

    def virtual_presets_active(self, virtual_id):
        return self._client.get(f"virtuals/{virtual_id}/presets")

    def virtual_presets_set(self, virtual_id, config):
        return self._client.put(f"virtuals/{virtual_id}/presets", data=config)
