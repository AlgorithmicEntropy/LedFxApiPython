import os

from LedFxAPI.ledfx_api import LedFxApi

my_api = LedFxApi('192.168.178.27', '8888')

effects = my_api.helper.get_all_effect_ids()

i = 0
for effect in effects:
    print(f"{i}: {effect}")
    i -= - 1

number = input("Enter number: ")
os.system('cls' if os.name == 'nt' else 'clear')

effect = effects[int(number)]
presets = my_api.helper.get_all_presets_for_effect(effect)

i = 0
for pres in presets:
    print(f"{i}: {pres}")
    i -= - 1

number = input("Enter number: ")
os.system('cls' if os.name == 'nt' else 'clear')

preset = presets[int(number)]
res = my_api.helper.set_preset('wled', effect, preset)
print(res)
