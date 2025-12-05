import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import switch
from esphome.const import CONF_ID, CONF_ICON
from .. import fossibot_ns, Fossibot, CONF_FOSSIBOT_ID

DEPENDENCIES = ["fossibot"]

CONF_USB = "usb"
CONF_DC = "dc"
CONF_AC = "ac"
CONF_LIGHT = "light"

FossibotSwitch = fossibot_ns.class_("FossibotSwitch", switch.Switch, cg.Component)

SWITCH_TYPES = {
    CONF_USB: "usb",
    CONF_DC: "dc",
    CONF_AC: "ac",
    CONF_LIGHT: "light",
}

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_FOSSIBOT_ID): cv.use_id(Fossibot),
        cv.Optional(CONF_USB): switch.switch_schema(
            FossibotSwitch,
            icon="mdi:usb-port",
        ),
        cv.Optional(CONF_DC): switch.switch_schema(
            FossibotSwitch,
            icon="mdi:power-socket-de",
        ),
        cv.Optional(CONF_AC): switch.switch_schema(
            FossibotSwitch,
            icon="mdi:power-plug",
        ),
        cv.Optional(CONF_LIGHT): switch.switch_schema(
            FossibotSwitch,
            icon="mdi:lightbulb",
        ),
    }
)

async def to_code(config):
    parent = await cg.get_variable(config[CONF_FOSSIBOT_ID])
    
    for key, switch_type in SWITCH_TYPES.items():
        if key in config:
            var = await switch.new_switch(config[key])
            await cg.register_component(var, config[key])
            cg.add(var.set_parent(parent))
            cg.add(var.set_switch_type(switch_type))
