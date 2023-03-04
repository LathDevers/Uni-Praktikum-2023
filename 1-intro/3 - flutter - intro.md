[**Flutter**][016] ist ein Open-Source Cross-Platform Software Development Kit (SDK), das die Programmiersprache [**Dart**][001] verwendet. 

> <details>
> <summary>Dart</summary>
> Dart is a "pure" object-oriented language in that all objects are instances of classes. But Dart does not require all code to be defined inside a class - you can define top-level variables, constants, and functions like you can in a procedural or functional language.<br><i>There's an interesting package, called <b><a href="https://pub.dev/packages/fpdart">fpdart</a></b>, that enables functional programming properties in Dart.</i><br><br>Dart is a garbage-collected language with C-like syntax.
> </details>

Da sowohl Flutter als auch Dart von Google betreut und gesponsert wird, sind beide weltweit benutzt und sehr gründlich dokumentiert. Der Basis Code ist ohne größere Anpassungen auf **Android**, **iOS**, **Web**, **Windows**, **macOS** und **Linux** mit nativ-naher Performanz lauffähig, weil Dart den Code zur nativen Maschinencode (Kotlin, Swift usw.) auf Mobile und Desktop, sowie zu JavaScript auf dem Web kompiliert.

Flutter kann Cross-Platform funktionieren, weil es ein leeres Canvas vom jeweiligen OS zur Verfügung gestellt bekommt und es zeichnet die Grafikelemente ([**Flutter widget index**][002]) darauf, so hat Flutter die vollste Kontrolle über jeden einzelnen Pixel.

[<img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="20" /> **Life of a Widget**][014]

|<b>Widget Tree</b>|<b>Row widget</b>|<b>Column widget</b>|
| :---: | :---: | :---: |
| <img src="https://github.com/LathDevers/flutter-training/raw/master/src/sample-flutter-layout.png" alt="Diagram of the widget tree" width="500" /> | <img src="https://github.com/LathDevers/flutter-training/raw/master/src/row-diagram.png" alt="Aligning widget - Row" /> | <img src="https://github.com/LathDevers/flutter-training/raw/master/src/column-diagram.png" alt="Aligning widget - Column" /> |

[*Source*](https://docs.flutter.dev/development/ui/layout)

Die App kann in der Entwicklungsphase schnell mit [**Stateful Hot Reload**][003] aktualisiert werden, so dass der aktuelle App Zustand und die User Daten bewahrt werden. Wenn die Änderungen den Widget-tree oder den Appzustand zu sehr beeinflussen, kann man statt Hot Reload das **Hot Restart** benutzen, das zwar ein bisschen länger dauert, weil es die Änderungen einlädt, die App neustartet und den Zustand resettet, es ist doch schneller, als ein kompletter Neustart.

[<img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="20" /> **Hot reload**](https://youtu.be/sgPQklGe2K8)

[**Flutter 2.0.0**][004] wurde in *März 2021* veröffentlicht und hat u. a. die folgenden Updates gebracht:
 - [**sound null safety**][005],
 - Appkompatibilität mit Web, Windows, macOS und Linux,
 - [**Unterstützung für Foldable Geräte**][006].

#### Ein paar weitere hilfsreiche Links:
- für die ersten Schritte im Flutter: [**Intro to Flutter**][108]
- [**Using packages**][109]; Packages durchstöbern geht auf [**pub.dev**](pub.dev) oder auch [**hier**](https://fluttergems.dev/ "Flutter Gems - A Curated List of Dart & Flutter packages").
- Eine ausführliche Beschreibung für Flutter findest du auf der GitHub Seite von Tomic Riedel, [**hier**][015].
- [**Flutter Cookbook**](https://docs.flutter.dev/cookbook)
- Schaue dich auch Andrea Bizzottos [**"Flutter tips & tricks" GitHub Repo**][017] an.
- [**Kindacode**](www.kindacode.com)

Hier ist eine [**Liste**][018] von Unternehmen, die Flutter verwenden.

Seht euch diesen detaillierten [**Vergleich**][019] zwischen der plattformübergreifenden und der nativen App-Entwicklung an, zusammen mit den jeweiligen Vor- und Nachteilen.

Letzendlich ist es zu erwähnen, dass hinter Flutter eine immens große [**Community**][112] steht. 2022 war [**Flutter**][115] das [**drittgrößte**][110] Open-Source Projekt, gemessen an der Zahl der Mitwirkenden. Die Community von FlutterDevs kommuniziert hauptsächlich über [**Discord**][111] *(51680 Mitglieder - Feb. 2023)*, [**Stack Overflow**][113] *(155,446 Fragen - bis zu Feb. 2023)* und [**Reddit**][114] *(104k Flutter Devs - Feb. 2023)*.

<a href="https://docs.flutter.dev/dash">
  <img
    src="https://github.com/LathDevers/flutter-training/raw/master/src/Dashatars.png"
    alt="Flutter's Mascot: Dash"
  />
</a>

[001]: https://dart.dev/ "Homepage of Dart"
[002]: https://flutter.dev/docs/reference/widgets "Flutter's widget index"
[003]: https://flutter.dev/docs/development/tools/hot-reload "Hot Reload documentation"
[004]: https://flutter.dev/docs/development/tools/sdk/release-notes/release-notes-2.0.0 "Flutter 2.0.0 release notes"
[005]: https://dart.dev/null-safety "Null safety in Flutter documentation"
[006]: https://docs.microsoft.com/de-de/dual-screen/flutter/twopane-widget "Microsoft's documentation about the FlutterTwoPane-widget"
[014]: https://www.youtube.com/watch?v=cyFM2emjbQ8 "Life of a Widget?! | Decoding Flutter - Youtube"
[015]: https://github.com/Tomic-Riedel/Flutter-Roadmap "Tomic-Riedel/Flutter-Roadmap"
[016]: https://flutter.dev "Flutter - Build apps for any screen"
[017]: https://github.com/bizz84/flutter-tips-and-tricks "biz84/flutter-tips-and-tricks"
[018]: https://flutter.dev/showcase "Showcase - Flutter apps in production"
[019]: https://www.christianfindlay.com/blog/cross-platform-vs-native
[108]: https://developers.google.com/learn/pathways/intro-to-flutter?hl=en "Intro to Flutter"
[109]: https://flutter.dev/docs/development/packages-and-plugins/using-packages "Flutter - Using Packages"
[110]: https://octoverse.github.com/2022/state-of-open-source "GitHub Octoverse - State of Open Source"
[111]: https://discord.com/invite/N7Yshp4 "Invitation to join Discord Server"
[112]: https://flutter.dev/community "Flutter Community"
[113]: https://stackoverflow.com/tags/flutter "Newest 'Flutter' Questions - Stack Overflow"
[114]: https://www.reddit.com/r/FlutterDev/ "FlutterDev - Reddit"
[115]: https://github.com/flutter/flutter "GitHub - Flutter"

# Basic tutorial

[<img src="https://upload.wikimedia.org/wikipedia/commons/c/c6/Dart_logo.png" width="20" /> **DartPad**](https://www.dartpad.dev)

```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData.dark(),
      debugShowCheckedModeBanner: false,
      home: MyWidget(),
    );
  }
}
```

### StatelessWidget

### StatefulWidget

## Entwurf eines neuen Moduls

Um ein neues Modul zu schaffen, ist einfach der `template` Ordner unter `lib\modules\` zu kopieren und umbenennen. Die Dateien und deren Imports sind auch anzupassen. Es ist noch wichtig, die "äußerste" Klasse: `TempMyModulePage` umzubenennen.

> :key: Jetzt, dass das neue Modul existiert und funktionsfähig ist, ist es nur noch in der Galerie zu definieren.

Dafür ist das letzte Element in der Liste in der `lib\src\moduleslist\src\moduleslist.dart` Datei in der `Data` Klasse zu kopieren, zum Ende hinzufügen  und die Properties anzupassen:
 - *image*: ein hübsches Bild, möglichst mit hoher Auflösung und möglichst im Format 3:2. Dieses Bild wird als Hintergrund auf der Karte in der Galerie verwendet. Diese Datei solltet ihr in `assets\modules` hochladen und in der `pubspec.yaml` zu den Assets hinzufügen.
 - *name*: die Benennung des Projekts
 - *description*: eine kurze Beschreibung. Der Name und die Beschreibung werden auf der Galeriekarte angezeigt.
 - *myClass*: Hier ist der neue Klassenname anzugeben. So weiß die App, welche Klasse zu öffnen, wenn diese Karte gedrückt wird.

## Flutter --> Flutter intro

## Hot reload, Hot restart

# Hilfsreiche Links

[**Dart cheatsheet**](https://dart.dev/codelabs/dart-cheatsheet "Dart cheatsheet")\
[**Intro to Flutter**](https://developers.google.com/learn/pathways/intro-to-flutter?hl=en "Intro to Flutter")\
Offizielle, regelmäßig aktualisierte [**Google.dev packages**](https://pub.dev/publishers/google.dev/packages "Packages of publisher google.dev"). Wenn möglich, benutze diese Packages\
[**Flutter YouTube page**](https://www.youtube.com/c/flutterdev "Flutter YouTube page")\
[**Flutter codelabs page**](https://flutter.dev/docs/codelabs "Flutter codelabs page")

---

[*<< Vorherige Seite*](set-up-flutter-sdk) | [*Nächste Seite >>*](miscellaneous)