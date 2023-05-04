# Aufbau des Projektes

```dart
📦 bivital_flutterapp
├───android
├───assets
│   └───modules // upload module cover images here
└───lib
    ├───l10n // language files
    ├───modules
    │   ├───plot // Data plotter module
    │   ├───soniccoach
    │   └───template // This folder you can copy, paste and rename to start your own module
    └───src // source files for the entire app
        ├───moduleslist
        │   └───src
        │           📜 moduleslist.dart // This list will be displayed in the Gallery
        ├───pages // Here are all of the activities except the modules
        └───services // BLE, map and location, logging, music and theming services
            📜 adaptive-widgets.dart // General platform adaptive widgets
            📜 line_chart_widget.dart // A useful widget for general purpose plotting
        📜 main.dart
    📜 pubspec.yaml
```

# Galeriebild

Idealerweise 3:2 und eher dunkel.

[<img src="https://upload.wikimedia.org/wikipedia/commons/3/33/Figma-logo.svg" width="12" /> **Figma**](http://figma.com/)

# Internationalisierung

Folgende Abkürzungen sind gängig:
- **l10n** *auf eng.* **l**ocalizatio**n** (10 Buchstaben zwischen "l" und "n")
- **i18n** *auf eng.* **i**nternationalizatio**n** (18 Buchstaben zwischen "i" und "n")
- manchmal auch **g11n** *auf eng.* **g**lobalizatio**n** (11 Buchstaben zwischen "g" und "n")
Die einzelnen Ausdrücke haben zwar leicht verschiedene Bedeutungen, können aber mehr oder weniger als Synonyme verwendet werden. [**Hier**](https://bpcs.com/blog/acronyms-every-company-should-know-when-going-global) ist eine gute Beschreibung.

Bearbeite die `lib/l10n/app_en.arb` und `lib/l10n/app_de.arb` Dateien.

```dart
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

AppLocalizations.of(context)!.word;
```

# Ein neues Package zum Projekt hinzufügen

- [**Using packages**](https://flutter.dev/docs/development/packages-and-plugins/using-packages "Flutter - Using Packages"); Packages durchstöbern geht auf [**pub.dev**](https://pub.dev) oder auch auf [**Flutter Gems**](https://fluttergems.dev/ "Flutter Gems - A Curated List of Dart & Flutter packages").
- Offizielle, regelmäßig aktualisierte [**Google.dev packages**](https://pub.dev/publishers/google.dev/packages "Packages of publisher google.dev"). Wenn möglich, benutze diese Packages.

Um das Beispielpackage, `css_colors`, zur App hinzufügen:

1. Depend on it.
   - In der `pubspec.yaml` Datei, die sich im Anwendungsordner befindet, ist `css_colors:` unter `dependencies` einzutragen.
2. Installation.
   - Führen Sie `flutter pub get` im Terminal aus ODER klicken Sie auf Pub get im Reiter am oberen Rand von `pubspec.yaml`.
3. Import.
   - Eine entsprechende `import`-Anweisung am Anfang des Dart Codes hinzufügen.
4. App stoppen und neustarten, wenn nötig.
   - Im Falle eines Plugins (d. h. ein Package, das plattformspezifischen Code enthält), mag Hot Reload und Hot Restart nicht ausreichend sein. Die App muss evtl. vollständig neugestartet werden, um Fehler wie "MissingPluginException" bei der Verwendung des Plugins zu vermeiden.

Der **Installations*****tab***, der auf jeder Paketseite auf [**pub.dev**](https://pub.dev "The official package repository for Dart and Flutter apps.") zu finden ist, ist eine praktische Referenz für diese Schritte.

![](https://gitlab.ub.uni-bielefeld.de/biomechatronik-praktikum-23/flutter-training/-/raw/master/src/Screen%20Recording%202022-09-06%20at%2009.27.22.gif)

Ein vollständiges Beispiel ist im [**css_colors example**](https://docs.flutter.dev/development/packages-and-plugins/using-packages#css-example "Example: Using the css_colors package") zu finden.

#### Bei der Suche nach einem Package sollte ihr folgende Punkte beachten:

- wann es veröffentlicht bzw. das letzte Mal aktualisiert wurde
- ob es `null safety` unterstützt
- welche Plattformen unterstützt werden
- Metriken wie `Likes` und `Popularity` sind ebenfalls hilfreich

![](https://github.com/LathDevers/flutter-training/blob/master/src/Screenshot%202022-09-06%20at%2009.18.21.png)

# Adaptives Design in Flutter

Manche offiziellen Widgets kommen mit dem prädefinierten Constructor `adaptive`, so returnt dieses Widget dann auf Android ein Widget mit dem ***Material Design*** und auf iOS ein mit dem ***Cupertino Design***. (siehe z. B. [**Switch.adaptive**](https://api.flutter.dev/flutter/material/Switch/Switch.adaptive.html "Switch.adaptive constructor"))

Es gibt sogar mehrere Plugins (siehe [**pub.dev**](pub.dev)), die weiteren adaptiven Widgets verfügbar machen. Und du kannst auch einfach `AdaptiveWidget` in diesem Projekt benutzen, definiert in `lib\src\adaptive_widgets.dart`.

| Platform | Links |
| ------ | ------ |
| <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Android_logo_2019_%28stacked%29.svg/2346px-Android_logo_2019_%28stacked%29.svg.png" height="55" /> | [**Material Design guidelines**](https://developer.android.com/design "Design for Android")<br>[**Material Design 3**](https://m3.material.io "Meet Material Design 3")<br>[**Material Design for large screens**](https://material.io/blog/material-design-for-large-screens "Material Design for large screens") |
| <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Apple_logo_grey.svg/1724px-Apple_logo_grey.svg.png" height="60" /> | [**macOS und iOS UI guidelines**](https://developer.apple.com/design/human-interface-guidelines/ "Apple Developer Human Interface Guidelines")<br>[**iOS-style widgets**](https://flutter.dev/docs/development/ui/widgets/cupertino "Cupertino widgets")<br>[**Automatische Anpassungen provided by Flutter auf Android und iOS**](https://flutter.dev/docs/resources/platform-adaptations "Platform-specific behaviors and adaptations")<br>[**macos_ui package**](https://pub.dev/packages/macos_ui "Flutter MacOS UI package") |
| <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Windows_logo_-_2021.svg/768px-Windows_logo_-_2021.svg.png" height="45" /> | [**Microsoft Fluent Design**](https://www.microsoft.com/design/fluent/#/windows "Microsoft Fluent Design") |
| <img src="https://seeklogo.com/images/T/tux-logo-AA06C623EC-seeklogo.com.png" height="55" /> | [**Ubuntu's official theme: Yaru**](https://github.com/ubuntu/yaru "Ubuntu Yaru theme suite")<br>[**Find UI packages from Canonical on pub.dev**](https://pub.dev/publishers/canonical.com/packages "Packages of publisher canonical.com") |

---

[*<< Vorherige Seite*](backend) | [*Nächste Seite >>*](project-management)