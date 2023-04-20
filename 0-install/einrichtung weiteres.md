# Android Studio auf Windows löschen

1. Run the Android Studio uninstaller
   - Open the **Control Panel** and under **Programs**, select **Uninstall a Program**. After that, click on "Android Studio" and press **Uninstall**. If you have multiple versions, uninstall them as well.
2. Remove the Android Studio files
   - To delete any remains of Android Studio setting files, in File Explorer, go to your user folder (`%USERPROFILE%`), and delete `.android`, `.AndroidStudio` and any analogous directories with versions on the end, i.e. `.AndroidStudio1.2`, as well as `.gradle` and `.m2` if they exist.
   - Then go to `%APPDATA%` and delete the `JetBrains` directory.
   - Finally, go to `C:\Program Files` and delete the `Android` directory.
3. Remove SDK
   - To delete any remains of the SDK, go to `%LOCALAPPDATA%` and delete the `Android` directory.
4. Delete Android Studio projects
   - Android Studio creates projects in a folder `%USERPROFILE%\AndroidStudioProjects`, which you may want to delete.

# VS Code Tipps

### Shortcuts
>
> **Quick Fix**: Windows`Strg + .`, Mac`CMD + .`

### Edit your `settings.json`
>
> Open the `settings.json` and add the file nesting patterns:
>
> > To do so, in VS Code type into the Command Palette (`Strg + P` or `CMD + P`) `>settings`, then choose `Preferences: Open Settings (JSON)`
> >
> > or
> >
> > - **Windows** `%APPDATA%\Code\User\settings.json`
> > - **macOS** `$HOME/Library/Application\ Support/Code/User/settings.json` or `$HOME/Users/<username>/Library/Application\ Support/Code/User/settings.json`
> > - **Linux** `$HOME/.config/Code/User/settings.json`
>

> ```dart
> {
>     "workbench.colorTheme": "Default Dark+",
>     "workbench.startupEditor": "none",
>     "dart.hotReloadOnSave": "all", // Triggers Hot Reload on save
>     "dart.flutterHotReloadOnSave": "all", // Triggers Hot Reload on save
>     "dart.previewFlutterUiGuides": true // enable Widget child-parent connection lines
>     "dart.lineLength": 200, // maximum characters in a line, otherwise use word wrap
>     // don't forget to also set ruler below
>     "[dart]": {
>         "editor.formatOnSave": true, // Code formatting on save
>         "editor.formatOnType": true,
>         "editor.rulers": [
>             200
>         ],
>         "editor.selectionHighlight": false,
>         "editor.suggest.snippetsPreventQuickSuggestions": false,
>         "editor.suggestSelection": "first",
>         "editor.tabCompletion": "onlySnippets",
>         "editor.wordBasedSuggestions": false,
>         "editor.codeActionsOnSave": {
>             "source.fixAll": true // To correct every warning automatically on save.
>         },
>         "editor.bracketPairColorization.enabled": true, // Bracked Pair Colorization
>     },
>     // To fold files inside your Pubspec.yaml like on the image below.
>     "explorer.fileNesting.enabled": true,
>     "explorer.fileNesting.expand": false,
>     "explorer.fileNesting.patterns": {
>         "pubspec.yaml": ".packages, .metadata, pubspec.lock, analysis_options.yaml",
>     },
> }
> ```
> <img
> src="https://gitlab.ub.uni-bielefeld.de/bi-vital/bi-vital-flutter-app/-/raw/main/docs/media/vs-code-fileNesting.png"
> alt="File nesting"
> width="40%"
> />
>
> To enable **font ligatures**:
> 1. **Download** [**Cascadia Code**][202] (or another font that supports ligatures) as a `.zip` and **install** it on your machine.
> 2. Add these lines to your VS Code `settings.json` file:
> ```dart
>     "editor.fontFamily": "'Cascadia Code', Consolas, 'Courier New', monospace",
>     "editor.fontSize": 14,
>     "editor.fontLigatures": true,
> ```
> 3. Add the following also to the `"[dart]"` section in your `settings.json`
> ```dart
>         "editor.fontLigatures": true,
> ```

### Useful extensions
>
> Flutter Intl\
> Flutter Color\
> Error Lens\
> Better Comments\
> Material Icon Theme\
> *Java management extensions*

For more: see [**this article**][201].

# Deploy to iOS devices [:link:](https://docs.flutter.dev/get-started/install/macos#deploy-to-ios-devices)

:warning: For this, you'll need a Mac.

1. The **first time** you use an attached physical device for iOS development, you need to **trust** both your Mac and the Development Certificate on that device.

   ![](https://docs.flutter.dev/assets/images/docs/setup/trust-computer.png)

2. On iOS 16 and higher you must also **enable [Developer Mode](https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device)**.
   - Open the Flutter project's `ios` folder in **Xcode** and try to run the app on the connected device (⌘ + R).
   - Go to **Settings** > **Privacy & Security** on the iOS device. Scroll down and toggle the *Developer Mode* switch.

     ![](https://images.tenorshare.com/topics/ios-16/turn-on-developer-mode-iphone.webp?w=394&h=425)

   - **Restart** the iOS device.

     ![](https://images.tenorshare.com/topics/ios-16/developer-mode-restart.webp?w=196&h=425)

   - After the phone boots up, tap “Turn On” on the pop up, then enter your device passcode to confirm.

     ![](https://images.tenorshare.com/topics/ios-16/successfully-turn-on-developer-mode.webp?w=387&h=425)

![](https://docs.flutter.dev/assets/images/docs/setup/xcode-account.png)

> Development and testing are supported for any Apple ID. Enrolling in the Apple Developer Program is required to distribute your app to the App Store.
>
> For the installation, a provisioning profile is used. [**Free provisioning**](https://steemit.com/xcode/@ktsteemit/xcode-free-provisioning) includes building at the same time only on 3 devices, and expires in 1 week. (This means that an app installed on the device will become unavailable after 6 days, cannot be opened, and will need *re-provisioning*.)
>
> <img src="https://gitlab.ub.uni-bielefeld.de/bi-vital/bi-vital-flutter-app/-/raw/main/docs/media/ios-provisioning.png" width="500"/>
>
>*The paid developer program increases this time limit to 1 year. But only with a paid dev account can you publish an app to the AppStore. (In which case, the app obviously stays on the device indefinitely.)*

3. When you try to run the app from Xcode again, you'll get an error message on your iPhone.

   <img src="https://i.stack.imgur.com/mVyQi.jpg" width="400">

   - Go to **Settings** > **General** > **VPN & Device Management**, where a new entry should've appeared. **Trust** it.

     ![](https://www.lifewire.com/thmb/57JE386sSmyzGXAL_tZNYNYmgSU=/750x0/filters:no_upscale():max_bytes(150000):strip_icc()/002-trust-an-app-on-iphone-4177822-e2bf429599944eb48e692a0c76e1c26d.jpg)

---

[*<< Vorherige Seite*](set-up-flutter-sdk) | [🏠](home)

[201]: https://codewithandrea.com/articles/vscode-shortcuts-extensions-settings-flutter-development/#1-quick-fix "VSCode Shortcuts, Extensions & Settings for Flutter Development"
[202]: https://github.com/microsoft/cascadia-code/wiki/Installing-Cascadia-Code "Installing Cascadia Code"