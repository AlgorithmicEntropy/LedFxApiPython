"""Basic example showcasing how to set effects"""
import asyncio

from LedFxAPI import *


async def main():
    ledfx = LedFx('192.168.178.27', '8888')  # new api object
    await ledfx.helper.load_helpers()  # init helpers, e.g build preset table

    virtuals = await ledfx.helper.get_all_virtuals()  # get all virtuals defined in ledfx
    effects = await ledfx.helper.get_all_effect_ids()  # get all possible effects

    for i in range(len(virtuals)):
        print(f"{i} {virtuals[i]}")
    my_virt_idx = input("Select virtual to control: ")
    my_virt = virtuals[int(my_virt_idx)]

    for i in range(len(effects)):
        print(f"{i} {effects[i]}")
    my_effect_idx = input("Select effect: ")
    my_effect = effects[int(my_effect_idx)]

    presets = await ledfx.helper.get_all_presets_for_effect(my_effect)

    for i in range(len(presets)):
        print(f"{i} {presets[i]}")
    my_preset_idx = input("Select preset, empty for default: ")
    if not my_preset_idx:
        my_preset = 'reset'
    else:
        my_preset = presets[int(my_preset_idx)]

    await ledfx.helper.set_preset(my_virt, my_effect, my_preset)


if __name__ == '__main__':
    asyncio.run(main())
