cd ~/cpp_sensors
cat > main.cpp << 'EOF'
#include "sensors.hpp"
#include <chrono>
#include <fstream>
#include <iostream>
#include <string>
#include <thread>
#include <sstream>

// getMemoryKb(), benchmark<>() helper...

int main() {
  std::ofstream out("cpp_sensor_bench.csv");
  out << "sensor,iterations,time_ns,mem_kb\n";
  // servo, LED, usb_cache, volatile_usb, RF, wifi_scan, button, pot benchmarks...
  return 0;
}
EOF

