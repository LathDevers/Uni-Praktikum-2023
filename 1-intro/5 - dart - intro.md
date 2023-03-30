In Flutter sind Backend und Frontend sehr eng ineinander integriert. Hier werden die beiden Layers nicht voneinander separiert entwickelt (z. B. Android [**XML Dateien**][316]).

# Datentypen und Datenstrukturen

Ein Guide zu [**lists, maps, sets und stacks**][218]

[<img src="https://upload.wikimedia.org/wikipedia/commons/c/c6/Dart_logo.png" width="20" /> **Einführung in Dart**](https://dart.dev/language)

# Klassen und mehr

Meistens wird  eine Klasse in Flutter als eine Erweiterung (`extends`) der Klasse `StatelessWidget` oder `StatefulWidget` definiert und die verschiedenen Backendfunktionen schreibt man direkt in einem der Properties des Widgets (`onPressed`, `onTap` usw.). Natürlich kann man allerdings ohnehin Klassen definieren, die verschiedene Funktionen beinhalten und die dann in anderen Klassen instanziert werden können.

[**Language Tour**][206]

Class: [**Classes Tutorial**][207]\
Mixin: [**What are mixins**][203], [**Mixins in Dart**][204]\
Hooks: [**flutter_hooks**][205]

# Named and positioned, optional and required parameters
[**Stackoverflow**][208] \
Wrap the named parameter with `{ }` curly braces.
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
Wrap the optional parameter with `[ ]` brackets.
```dart
class User {
  User(this.name, [this.age = 24, this.height]);
  String name; // positioned, not optional
  int age; // positioned, optional, non-nullable but initialized
  double? height; // positioned, optional, is not initialized but nullable
}

List<User> users = [
  User('Jonas'),
  User('Vivienne', 34),
  User('Robert', 12, null),
  User('Sören', 52, 1.82),
];
```

# Code documentation and commenting
[**Commenting rules**][209] \
Comment: `//` or `/* ... */` \
To write documentation classes, methods, or variables: `///` before the class-, method- or variable declaration

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

`null` itself is not the problem, experience shows that developers tend to introduce null-errors very often. Null-errors cause crashes.

[<img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="20" /> **Null safety in Dart**](https://youtu.be/iYhOU9AuaFs)

Types in Dart are *non-nullable* by default. This means, that by default you are bound to give value to a variable when defining it, it must never be assigned `null` unless you say it can.

```dart
String s = "hello";
```

Let's take a look at a more complicated situation:

```dart
class User {
  User({required this.id, required this.name});

  int id;
  String name;
}

User user1;

print(user1.name);
```

In this case, user1 is not given a value, so its value would be null (without null-safety). When accessing `name`, our application will crash.

To avoid this, the *code reviewer* will underline `user1` and will notify you, that you must give it a value.

If for some reason you absolutely don't want to define a new variable with a value, but you can assure, that the variable will have a value when it's first read, then there's a workaround to define the variable with the [`late`][214] modifier:

```dart
late User user1;

user1 = User( // variable gets value before reading it
  id: 0123,
  name: 'Moritz',
);

print(user1.name); // Moritz
```

Or you could define the variable nullable by using the `?` null-aware operator.

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

It is not `null` that is bad, it is having `null` go where you don’t expect it that causes problems.\
You only need to manage this situation wisely: by either using the `!` operator, if, in the place, you want to use this variable, it is not containing `null` anymore.

```dart
String? s;
s = "hello"; // variable gets value before reading it
print(s!); // ! means: trust me, s has a value other than null
```

Or implement different actions if the variable's value is `null` or not.

```dart
print(s ?? "hello"); // print s, but if s is null, then print "hello"

if (s != null) {
  action_if_s_is_not_null();
} else {
  action_if_s_is_null();
}
```

So depending on the situation, there are different possibilities to set a non-nullable variable with a nullable one:

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

For more information about *sound null safety in Flutter* you can either read the [**Dart pages**][215] or the [**Flutter pages**][216].

# Asynchronous Programming

[<img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="20" /> **Isolates and Event Loops**](https://youtu.be/vl_AaCgudcY)\
[<img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="20" /> **Futures**](https://youtu.be/OTS-ap9_aXc)\
[<img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="20" /> **Streams**](https://youtu.be/nQBpOIHE4eE)\
[<img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="20" /> **Async/Await**](https://youtu.be/SmTCmDMi4BY)\
[<img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="20" /> **Generators**](https://youtu.be/TF-TBsgIErY)

---

[*<< Vorherige Seite*](miscellaneous) | [🏠](home)

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