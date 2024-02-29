# Setup Steps

```
sudo esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
sudo esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 /path/to/ESP32_GENERIC-20240222-v1.22.2.bin 
```

```
sudo rshell -p /dev/ttyUSB0
```

```
sudo picocom -b 115200 /dev/ttyUSB0
```
