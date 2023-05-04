Dart ist eine rein objektorientierte Sprache, da alle Objekte Instanzen von Klassen sind. Aber Dart erfordert nicht, dass der gesamte Code innerhalb einer Klasse definiert wird - es können Variablen, Konstanten und Funktionen auf oberster Ebene definieren, ähnlich wie in einer prozeduralen oder funktionalen Sprache.

*Es gibt ein interessantes Paket namens [**fpdart**](https://pub.dev/packages/fpdart), das funktionale Programmiereigenschaften in Dart ermöglicht.*

Dart ist eine Garbage-Collected-Sprache mit einer C-ähnlichen Syntax.

In Flutter sind Backend und Frontend sehr eng ineinander integriert. Hier werden die beiden Layers nicht voneinander separiert entwickelt (z. B. Android [**XML Dateien**][316]).

[<img src="https://upload.wikimedia.org/wikipedia/commons/c/c6/Dart_logo.png" width="20" /> **Einführung in Dart**](https://dart.dev/language)

# [**Datentypen**](https://dart.dev/language/built-in-types) und Datenstrukturen

Ein Guide zu [**lists, maps, sets und stacks**][218].

Dart code is [**type-safe**](https://dart.dev/language/type-system).

# [**Klassen**](https://dart.dev/language/classes) und mehr

Meistens wird  eine Klasse in Flutter als eine Erweiterung (`extends`) der Klasse `StatelessWidget` oder `StatefulWidget` definiert und die verschiedenen Backendfunktionen schreibt man direkt in einem der Properties des Widgets (`onPressed`, `onTap` usw.). Natürlich kann man allerdings ohnehin Klassen definieren, die verschiedene Funktionen beinhalten und die dann in anderen Klassen instanziert werden können.

Class: [**Classes Tutorial**][207]\
Mixin: [**What are mixins**][203], [**Mixins in Dart**][204]\
Hooks: [**flutter_hooks**][205]

[<img src="https://cdn-icons-png.flaticon.com/512/5968/5968885.png" height="20" /> **Exploring Dart Constructors**](https://medium.flutterdevs.com/exploring-dart-constructors-345398a0e4c5)

# Benannte und positionierte, optionale und erforderliche Parameter

Umschließe die benannten Parameter mit geschweiften Klammern `{ }`.

```dart
class User {
  User(this.name, this._id, {this.age = 24, this.height, required this.nationality});
  String name; // positioned, not optional
  int? _id; // nullable, not optional, private
  int age; // named, optional, initialized
  double? height; // named, optional, not initialized but also nullable
  // actually, initial value is null
  String nationality; // named, required
}

User user1 = User('Jonas', 01234, nationality: 'German');
User user2 = User('Vivienne', null, age: 34, nationality: 'French');
User user3 = User('Robert', 98765, nationality: 'English', age: 12, height: null);
```

Umschließe die optionalen Parameter mit eckigen Klammern `[ ]`.

```dart
class User {
  User(this.name, [this.age = 24, this.height]);
  String name; // positioned, not optional
  int age; // positioned, optional, non-nullable but initialized
  double? height; // positioned, optional, not initialized but nullable
}

List<User> users = [
  User('Jonas'),
  User('Vivienne', 34),
  User('Robert', 12, null),
  User('Sören', 52, 1.82),
];
```

[<img src="https://cdn-icons-png.flaticon.com/512/2111/2111628.png" width="20" /> **Quelle**][208]

# Code-Dokumentation und Möglichkeiten zum Kommentieren/Auskommentieren

[**Effective Dart: Documentation**][209]

Kommentare starten mit `//`. Alles nach dem `//` wird von Dart ignoriert.\
Alternativ kann man auch ganze Codeabschnitte auskommentieren, indem man sie mit `/* ... */` einschließen.

Zur Dokumentation von Klassen, Methoden oder Variablen: `///` vor der Klassen-, Methoden- oder Variablendeklaration.

Beispiel:

```dart
/// Title text transfer fade.
const Duration _kNavBarTitleFadeDuration = Duration(milliseconds: 150);

/// An iOS-styled navigation bar with iOS-11-style large titles using slivers.
///
/// The [CupertinoSliverNavigationBar] must be placed in a sliver group such
/// as the [CustomScrollView].
///
/// ** See code in examples/api/lib/cupertino/nav_bar/cupertino_sliver_nav_bar.0.dart **
/// {@end-tool}
///
/// See also:
///
///  * [CupertinoNavigationBar], an iOS navigation bar for use on non-scrolling
///    pages.
///  * [CustomScrollView], a ScrollView that creates custom scroll effects using slivers.
class CupertinoSliverNavigationBar extends StatefulWidget { ...
```

# [**Null safety**](https://dart.dev/null-safety/understanding-null-safety)

`Null` selbst ist nicht das Problem, die Erfahrung zeigt, dass Entwickler dazu neigen, sehr oft Null-Fehler einzuführen. Null-Fehler verursachen Abstürze.

[<img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="20" /> **Null safety in Dart**](https://youtu.be/iYhOU9AuaFs)

Datentypen in Dart sind standardmäßig *nicht-nullbar (non-nullable)*. Das bedeutet, dass man standardmäßig verpflichtet ist, einer Variablen beim Definieren einen Wert zuzuweisen, sie darf niemals `null` zugewiesen werden, es sei denn, man erlaubt es.

```dart
String s = "hello";
```

Schauen wir uns eine kompliziertere Situation an:

```dart
class User {
  User({required this.id, required this.name});

  int id;
  String name;
}

User user1;

print(user1.name);
```

In diesem Fall wird `user1` kein Wert zugewiesen, so dass sein Wert `null` wäre (ohne null-safety). Beim Zugriff auf `name` wird die App abstürzen.

Um dies zu vermeiden, unterstreicht der *Code Reviewer* `user1` und weist uns darauf hin, dass wir ihm einen Wert geben müssen.

Wenn man aus irgendeinem Grund eine neue Variable unbedingt mit keinem Wert definieren will, wir aber sicher sein können, dass die Variable beim ersten Lesen einen Wert hat, dann gibt es eine Abhilfe, indem wir die Variable mit dem Modifikator [`late`][214] definieren:

```dart
late User user1;

user1 = User( // variable gets value before reading it
  id: 0123,
  name: 'Moritz',
);

print(user1.name); // Moritz
```

Oder wir können auch die Variable nullable definieren, indem wir den null-aware Operator `?` verwenden.

```dart
User? user1; // this means, that user1 is nullable

// so it can contain null
print(user1); // null
user1 = null;
print(user1); // null

// but before accessing its value, it has to get a value other than null
user1 = User(
  id: 0123,
  name: 'Moritz',
);

print(user1!.name); // Moritz
```

Nicht `null` ist schlecht, sondern die Tatsache, dass `null` dort auftaucht, wo man es nicht erwartet, verursacht Probleme.\
Wir müssen diese Situation nur klug handhaben!\
Entweder mit dem Operator `!`, wenn die Variable an der Stelle, an der man sie verwenden will, sicher nicht mehr `null` enthält:

```dart
String? s;
s = "hello"; // variable gets value before reading it
print(s!); // ! means: trust me, s has a value other than null
```

Oder durch die Implementierung verschiedener Aktionen, wenn der Wert der Variablen `null` ist oder nicht:

```dart
print(s ?? "hello"); // print s, but if s is null, then print "hello"

if (s != null) {
  action_if_s_is_not_null();
} else {
  action_if_s_is_null();
}
```

Je nach Situation gibt es also verschiedene Möglichkeiten, eine non-nullable Variable durch eine nullable zu ersetzen:

```dart
int? aNullableInt;
int aNonNullableInt = 5;

aNonNullableInt = aNullableInt!; // if you are sure, that aNullableInt is not null anymore at this point

aNonNullableInt = aNullableInt ?? 0;

aNullableInt != null ? aNonNullableInt = aNullableInt! : aNonNullableInt = 0; // ternary operator syntax

if (aNullableInt != null) aNonNullableInt = aNullableInt;

// the bug finder recognizes most of the time, that aNullableInt cannot be null because it was checked in the if statement.
// In some cases, especially if this logic is more complicated, the bug finder may not be so bright.
// Then just use the ! operator

// like here:

if (aNullableInt != null) aNonNullableInt = aNullableInt!;

// if using the ! operator is redundant, the bug finder warns you if the Flutter plugin is installed in either IntelliJ / Android Studio or VS Code
// for example
var someOtherVariable = aNonNullableInt!;
// or
if (aNonNullableInt != null)
```

Für weitere Informationen über *Sound null-safety in Flutter* kannst du entweder die [**Dart Seiten**][215] oder die [**Flutter Seiten**][216] lesen.

# Asynchrone Programmierung

[<img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="20" /> **Isolates and Event Loops**](https://youtu.be/vl_AaCgudcY)\
[<img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="20" /> **Futures**](https://youtu.be/OTS-ap9_aXc)\
[<img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="20" /> **Streams**](https://youtu.be/nQBpOIHE4eE)\
[<img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="20" /> **Async/Await**](https://youtu.be/SmTCmDMi4BY)\
[<img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="20" /> **Generators**](https://youtu.be/TF-TBsgIErY)

---

[*<< Vorherige Seite*](my-first-flutter-app) | [*Nächste Seite >>*](miscellaneous)

[203]: https://medium.com/flutter-community/dart-what-are-mixins-3a72344011f3 "Dart: What are mixins? It's a kind of magic"
[204]: https://medium.com/flutterdevs/mixins-in-dart-how-to-use-it-90d078e722d3 "Mixins in Dart: How to use it"
[205]: https://pub.dev/packages/flutter_hooks "flutter_hooks package"
[206]: https://dart.dev/guides/language/language-tour "A tour of the Dart language"
[207]: https://www.tutorialspoint.com/dart_programming/dart_programming_classes.htm "Dart Programming - Classes"
[208]: https://stackoverflow.com/a/55769496/15904893 "Constructor Optional Params"
[209]: https://dart.dev/guides/language/effective-dart/documentation "Effective Dart: Documentation"
[210]: https://github.com/pauldemarco/flutter_blue/issues/662#issuecomment-741710564 "I/flutter (13169): Error starting scan. #662"
[211]: https://flutter.dev/docs/deployment/android#shrinking-your-code-with-r8 "Shrinking your code with R8"
[212]: https://developer.android.com/studio/build/shrink-code "Shrink, obfuscate, and optimize your app"
[214]: https://dart.dev/null-safety/understanding-null-safety#late-variables "Understanding null safety"
[215]: https://dart.dev/null-safety "Sound null safety | Dart"
[216]: https://flutter.dev/docs/null-safety "Flutter | Null safety in Flutter"
[218]: https://blog.logrocket.com/dart-flutter-data-structures-comprehensive-guide/ "Dart and Flutter data structures: A comprehensive guide"
[316]: https://developer.android.com/guide/topics/ui/declaring-layout "Layouts"
[317]: https://pub.dev/packages/flutter_launcher_icons
[318]: https://pub.dev/packages/flutter_native_splash