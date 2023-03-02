# Einrichtung der Flutter SDK

Die ausführliche, englischsprachige Dokumentation zur Einrichtung befindet sich auf der offiziellen Webseite:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://flutter.dev/docs/get-started/install/windows">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Windows_logo_-_2021.svg/768px-Windows_logo_-_2021.svg.png" height="45" />
</a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://flutter.dev/docs/get-started/install/macos">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Apple_logo_grey.svg/1724px-Apple_logo_grey.svg.png" height="50" />
</a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://flutter.dev/docs/get-started/install/linux">
    <img src="https://seeklogo.com/images/T/tux-logo-AA06C623EC-seeklogo.com.png" height="50" />
</a>

In dieser Anleitung wird die Installation **auf Windows** beschrieben.

## 1) Flutter SDK herunterladen

Clone die aktuelleste stabile release Version der Flutter SDK in einen gewünschten Installationsordner (z. B. `C:\Users\<your-user-name>\Documents`):

> ☢️ **WARNUNG** ☢️ Installiere Flutter nicht in einem Ordner wie `C:\Program Files\`, der erhöhte Rechte erfordert.

## 2) Den Pfad aktualisieren

- Tippe in die Start Suchleiste von Windows `env` ein und wähle **Edit environment variables for your account**.
- Überprüfe unter **User variables**, ob ein Entrag namens **Path** existiert.
  - Wenn der Eintrag existiert: füge den vollen Pfad zu `flutter\bin` mit dem `;` Trennzeichen nach existierenden Werten hinzu.
  - Wenn der Eintrag nicht existiert: erstelle eine neue Variable namens `Path` mit dem vollen Pfad zu `flutter\bin`.

> ❗️ Alle vorhandenen Konsolenfenster müssen geschlossen und wieder geöffnet werden, damit diese Änderungen wirksam werden.

# Android Studio installieren

![](src/android-studio.png)

Installiere [**Android Studio**][105] ⬇️.

> Anstatt Android Studio kann auch VS Code verwendet werden. Siehe [**Anleitung**][106].

**Nach der Installation:** Im **Welcome Fenster** wähle _Configure_ auf der linken Seite, dann _Plugins_ und lade das **Flutter** und das **Dart** Plugin herunter.

## `flutter doctor` ausführen

Führe in einem Konsolenfenster den folgenden Befehl aus, um zu sehen, ob es irgendwelche Plattformabhängigkeiten es gibt, welche noch zur Fertigstellung der Einrichtung benötigt werden:

```python
flutter doctor
```

> 🔍 Dieser Befehl überprüft deine Environment und gibt einen Bericht über den Zustand der Flutter Installation wieder. Checke die Ausgaben aufmerksam Schritt für Schritt (**Chrome** und **Visual Studio Errors** können **unbeachtet** gelassen werden).

* *Bei Fehler* `cmdline-tools component is missing`: Installiere das **Command Line Tool** unter Android Studio (Welcome screen: More Actions > SDK Manager > Reiter: SDK Tools > Android SDK Command-line Tools (latest))
* *Bei Fehler* `Android license status unknown`: Run `flutter doctor --android-licenses`

# Das BI-Vital Flutter Projekt

Im Welcome Screen von Android Studio auf **Open** drücken und den Ordner: `/bi-vital-flutter-app/bivital_flutterapp` aus dem geklonten Repo als Projekt hinzuzufügen.

> #### ❓ Flutter SDK Pfad angeben
> >
> > Manchmal kann es passieren, dass trotz der Eingabe des Flutter SDK Pfades in Windows, der Pfad nicht in Android Studio übernommen wird. Um dies zu checken bzw. zu beheben, gehe zu:
> >
> > File > Settings > Language & Frameworks > Flutter > SDK
> >
> > und setze den Pfad zum Flutter SDK Repo aus Schritt 2 (z. B., `C:\Users\<your-user-name>\Documents\flutter`).
> >

## 8) Android Gerät vorbereiten (nur für Debug Modus nötig)

1. **Entwickleroptionen** und **USB debugging** auf dem Gerät aktivieren.
   - Wenn das **Entwickleroptionen** Menü in den OS Einstellungen nicht zu finden ist, muss es vorher aktiviert werden. Dazu die Buildnummer (unter Telefoninfo, evtl Softwareinformationen) 7 Mal antippen. Siehe [**Dokumentation**][107].
2. Den [**Google USB Driver**][108] installieren in Android Studio.
3. Das Handy mit einem USB-Kabel am Computer anschließen. Wenn Sie auf Ihrem Gerät dazu aufgefordert werden, autorisieren Sie den Computer für den Zugriff auf das Gerät.

Stellt euch sicher, dass ihr den Projekt Orner in Android Studio öffnen könnt, und etwas ähnliches seht, wie hier:

![](src/Screenshot%202023-03-02%20at%2017.49.15.png)

[101]: https://flutter.dev/docs/get-started/install/windows "Flutter - Windows install"
[102]: https://flutter.dev/docs/get-started/install/macos "Flutter - macOS install"
[103]: https://flutter.dev/docs/get-started/install/linux "Flutter - Linux install"
[104]: https://snapcraft.io/flutter "Install Flutter on Linux | Snapcraft"
[105]: https://developer.android.com/studio "Download Android Studio"
[106]: https://docs.flutter.dev/development/tools/vs-code "Visual Studio Code setup"
[107]: https://developer.android.com/studio/debug/dev-options "Configure on-device developer options"
[108]: https://developer.android.com/studio/run/win-usb "Get the Google USB Driver"
[109]: https://flutter.dev/docs/deployment/android "Build and release an Android app"
[110]: https://play.google.com/store/apps/details?id=com.inkwired.droidinfo&pli=1 "Droid Hardware Info - Apps on Google Play"
[111]: https://pub.dev "The official package repository for Dart and Flutter apps."
[112]: https://docs.flutter.dev/development/packages-and-plugins/using-packages#css-example "Example: Using the css_colors package"
[113]: https://dart.dev/codelabs/dart-cheatsheet "Dart cheatsheet"
[114]: https://developers.google.com/learn/pathways/intro-to-flutter?hl=en "Intro to Flutter"
[115]: https://pub.dev/publishers/google.dev/packages "Packages of publisher google.dev"
[116]: https://flutter.dev/docs/development/ui/layout/adaptive-responsive "Creating responsive and adaptive apps"
[117]: https://www.youtube.com/c/flutterdev "Flutter YouTube page"
[118]: https://flutter.dev/docs/codelabs "Flutter codelabs page"
[119]: https://docs.flutter.dev/deployment/ios "Build and release an iOS app"