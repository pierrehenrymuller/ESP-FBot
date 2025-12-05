#pragma once

#include "esphome/core/component.h"
#include "esphome/components/switch/switch.h"
#include "../fossibot.h"

#ifdef USE_ESP32

namespace esphome {
namespace fossibot {

class FossibotSwitch : public switch_::Switch, public Component {
 public:
  void setup() override;
  void dump_config() override;
  
  void set_parent(Fossibot *parent) { this->parent_ = parent; }
  void set_switch_type(const std::string &type) { this->switch_type_ = type; }
  
 protected:
  void write_state(bool state) override;
  
  Fossibot *parent_{nullptr};
  std::string switch_type_;
};

}  // namespace fossibot
}  // namespace esphome

#endif  // USE_ESP32
