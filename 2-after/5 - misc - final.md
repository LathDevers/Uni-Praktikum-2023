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

Um das Beispielpackage, `css_colors`, zur App hinzufügen:

1. Depend on it.
   - In der `pubspec.yaml` Datei, die sich im Anwendungsordner befindet, ist `css_colors:` unter `dependencies` einzutragen.
1. Installation.
   - Führen Sie `flutter pub get` im Terminal aus ODER klicken Sie auf Pub get im Reiter am oberen Rand von `pubspec.yaml`.
1. Import.
   - Eine entsprechende `import`-Anweisung am Anfang des Dart Codes hinzufügen.
1. App stoppen und neustarten, wenn nötig.
   - Im Falle eines Plugins (d. h. ein Package, das plattformspezifischen Code enthält), mag Hot Reload und Hot Restart nicht ausreichend sein. Die App muss evtl. vollständig neugestartet werden, um Fehler wie "MissingPluginException" bei der Verwendung des Plugins zu vermeiden.

Der **Installations*****tab***, der auf jeder Paketseite auf [**pub.dev**](https://pub.dev "The official package repository for Dart and Flutter apps.") zu finden ist, ist eine praktische Referenz für diese Schritte.

![](https://gitlab.ub.uni-bielefeld.de/biomechatronik-praktikum-23/flutter-training/raw/master/src/Screen%20Recording%202022-09-06%20at%2009.27.22.gif)

Ein vollständiges Beispiel ist im [**css_colors example**](https://docs.flutter.dev/development/packages-and-plugins/using-packages#css-example "Example: Using the css_colors package") zu finden.

#### Bei der Suche nach einem Package sollte ihr folgende Punkte beachten:

- wann es veröffentlicht bzw. das letzte Mal aktualisiert wurde
- ob es `null safety` unterstützt
- welche Plattformen unterstützt werden
- Metriken wie `Likes` und `Popularity` sind ebenfalls hilfreich

![](https://gitlab.ub.uni-bielefeld.de/biomechatronik-praktikum-23/flutter-training/raw/master/src/Screenshot%202022-09-06%20at%2009.18.21.png)

---

[*<< Vorherige Seite*](project-management) | [*Nächste Seite >>*](backend)