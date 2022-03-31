import api

my_api = api.API('192.168.178.27', '8888')

config = my_api.ledfx_schema()

effects = list(config['effects'].keys())

for effect in effects:
    print(effect)

number = input("Enter number: ")
effect = effects[number]

my_api.devices_