# Requirements

- SCAN: list available BI-Vitals nearby
- SELECT: highlight BI-Vitals
- START: connect to highlighted BI-Vitals and start measurement
- MONITOR
  - status of running measurement during research
  - battery level
  - *LED settings*
  - free storage
- END: connect to BI-Vitals and stop measurement
- LABEL: send text that will be saved in the measurement file
- management (single and all)
  - FORMAT internal storage
  - REBOOT and SHUTDOWN
  - LED actions

## SCAN

```dart
final FlutterBluePlus flutterBlue = FlutterBluePlus.instance;
flutterBlue.startScan();
flutterBlue.stopScan();
```

`/lib/src/pages/src/settings_methods.dart`

## START

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

## LED actions

`uint8`

LSB: `B` | `G` | `R` (no PWM)

---

[*<< Vorherige Seite*](my-first-flutter-app) | [*Nächste Seite >>*](miscellaneous)