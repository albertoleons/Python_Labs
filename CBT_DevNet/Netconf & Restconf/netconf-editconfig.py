from ncclient import manager
from router_info import router

config_template = open("ios_config.xml").read()

netconf_config = config_template.format(
    interface_name="GigabitEthernet1", interface_desc="Alberto was here again")

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)
