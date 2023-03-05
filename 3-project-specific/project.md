# Requirements

- SCAN: list available BI-Vitals nearby
- SELECT: highlight BI-Vitals
- START: connect to highlighted BI-Vitals and start measurement
- MONITOR: show status of running measurement during research
- END: connect to BI-Vitals and stop measurement

### SCAN

```dart
final FlutterBluePlus flutterBlue = FlutterBluePlus.instance;
flutterBlue.startScan();
flutterBlue.stopScan();
```

`/lib/src/pages/src/settings_methods.dart`

### SELECT

### START

Iterate through selected devices in a `for` loop.
1. Try to connect to one BI-Vital.
   - `/lib/...`
   - Take a look at the [**retry**](https://pub.dev/packages/retry) package.

    ```dart
    FlutterBlue().connect();
    ```

2. Write `start measurement` UUID.
   - `/lib/src/pages/ble_uuid.dart`

    ```dart
    characteristic.write();
    ```

3. Disconnect

Error management: what should happen if either **connect**, **write** or **disconnect** fail.

### MONITOR

### END

Similar to [**START**](#start).