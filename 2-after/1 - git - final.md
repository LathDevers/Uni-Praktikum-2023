[**Git**](https://git-scm.com/) ist ein kostenloses und open-source Versionsverwaltungsprogramm, das unter Softwareentwicklern sehr beliebt und weit verbreitet ist.\
In seiner Grundfunktion tut **Git** nichts weiter, als Dateien, die ihr im "gebt",
zu verwalten, und die Änderungen zwischen verschiedenen Versionen zu registrieren.

Vorteile sind u. a.:

- In der Versionsgeschichte ist klar zu erkennen, was wann getan wurde.
- Sollte eine Version einmal nicht mehr funktionieren, könnt ihr einfach zum letzten funktionierenden Stand zurückkehren.
- Man kann gezielt einzelne Änderungen an einzelnen Dateien zurückverfolgen.

Und noch viele mehr.

> <img align="left" src="https://gitlab.ub.uni-bielefeld.de/biomechatronik-praktikum-23/control-app/raw/main/docs/wiki-src/SCR-20230302-pzrj.jpeg" width="10%"/> Eine sehr ausführliche Einführung in die Arbeit mit Git bietet das kostenlose E-book [**Pro Git**](https://git-scm.com/book/en/v2) von Scott Chacon!
> <br clear="left"/>
>
> Es gibt darüber hinaus auch viele [**Cheat Sheets**](https://education.github.com/git-cheat-sheet-education.pdf).

<img
src="https://gitlab.ub.uni-bielefeld.de/biomechatronik-praktikum-23/control-app/raw/main/docs/wiki-src/20220802_165310.jpg"
min-width="100"
width="50%"
/>

## Gitlab

Wir verwenden Git im Zusammenhang mit einem Git Server. Der Server ist in unserem Fall der Gitlab Server der Uni Bielefeld.
Für euch ist es nur wichtig zu wissen, dass euer lokales Projekt immer eine **vollständige** Kopie des Projektes auf der Serverseite ist. Ihr verfügt also immer über alle Daten und Dateien.

**Git kommuniziert nicht automatisch mit dem Server**. Wenn es also neue Änderungen bei euch gibt, oder auf dem Server, dann müsst ihr Git erst darauf hinweisen. (`git pull`, `git push` etc.)

| git | Github | GitLab |
| :-: | :-: | :-: |
| <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/640px-Git-logo.svg.png" width="100"/> | &nbsp;&nbsp;&nbsp;<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="80"/>&nbsp;&nbsp;&nbsp; | <img src="https://about.gitlab.com/images/press/logo/png/gitlab-logo-500.png" width="100"/> |

## Installation

Für Informationen zur Installation sollte die [**git Webseite**](https://git-scm.com/) zu Rate gezogen werden.

![](https://gitlab.ub.uni-bielefeld.de/biomechatronik-praktikum-23/control-app/raw/main/docs/wiki-src/SCR-20230302-pkbk-2.png)

![](https://gitlab.ub.uni-bielefeld.de/biomechatronik-praktikum-23/control-app/raw/main/docs/wiki-src/SCR-20230302-popq.png)

> Es gibt natürlich eine Vielzahl an grafischen Tools und Helferlein, die sich gegenseitig mit Features für den Anwender übertrumpfen. Wenn ihr mit Git vertraut seid, könnt ihr gerne auch mit solchen Tools arbeiten.
>
> Android Studio verfügt allerdings über eine eingebaute UI für Git.

<img
src="https://gitlab.ub.uni-bielefeld.de/biomechatronik-praktikum-23/control-app/raw/main/docs/wiki-src/Screenshot 2023-03-03 at 08.21.14.png"
/>

## Vor der ersten Verwendung

Bevor es los geht, müsst ihr Git mitteilen, wie ihr heißt. Das ist wichtig, um nachzuverfolgen, wer welche Änderungen eingebracht hat. Öffnet dazu die Git Konsole:

```bash
git config --global user.name "Euer Name"
git config --global user.email "euer.name@uni-bielefeld.de"
```

# Managing SSH keys for Github and Gitlab

[<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/2048px-Octicons-mark-github.svg.png" width="15"/> **Source**](https://gist.github.com/marcoandre1/4b0fbca83104e08d3e729a25a0cba4eb)

I recently had to manage two ssh keys (one for Github and one for Gitlab).

The first question you can ask yourself is [**can you have the same ssh key for both Github and Gitlab**](https://stackoverflow.com/questions/56285972/can-you-and-is-it-advisable-to-use-the-same-ssh-key-for-github-and-gitlab-gitbuc)? The answer is *yes* [**but it is not advisable**](https://stackoverflow.com/a/56285988).

The **best answer** is that you should set one ssh key for Github and another one for Gitlab. First, you should [**check for existing ssh-keys on your system**](https://docs.github.com/en/github/authenticating-to-github/checking-for-existing-ssh-keys):

```bash
$ ls -al ~/.ssh
# Lists the files in your .ssh directory, if they exist
```

3. Check the directory listing to see if you already have a public SSH key. By default, the filenames of the public keys are one of the following:

```console
id_rsa.pub
id_ecdsa.pub
id_ed25519.pub
```

> 🔎 You can simply delete these files, if you want to remove the keys. No additional step is required.

If you don't have an existing public and private key pair, or don't wish to use any that are available to connect to GitHub, then [**generate a new SSH key**](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent):

```bash
$ ssh-keygen -f ~/.ssh/id_ed25519_hub -t ed25519 -C "your_email@example.com"
# Use your GitHub email address
```

> 🔎 If you are using a legacy system that doesn't support the Ed25519 algorithm, use: 
> 
> `$ ssh-keygen -f ~/.ssh/id_rsa_hub -t rsa -b 4096 -C "your_email@example.com"`

This creates a new ssh key, using the provided email as a label. 

```bash
> Generating public/private ed25519 key pair.
```

### [**Add your SSH key to the ssh-agent**](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)

1. Ensure the ssh-agent is running. You can use the "Auto-launching the ssh-agent" instructions in "[**Working with SSH key passphrases**](https://docs.github.com/en/github/authenticating-to-github/working-with-ssh-key-passphrases)", or start it manually:

```bash
# start the ssh-agent in the background
$ eval `ssh-agent -s`
> Agent pid 59566
```

2. Add your SSH private key to the ssh-agent. If you created your key with a different name, or if you are adding an existing key that has a different name, replace *id_ed25519_hub* in the command with the name of your private key file.

```bash
$ ssh-add ~/.ssh/id_ed25519_hub
```

### [**Add the SSH key to your GitHub account**](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)

1. Copy the SSH public key to your clipboard.

If your SSH public key file has a different name than the example code, modify the filename to match your current setup. When copying your key, don't add any newlines or whitespace.

```bash
$ clip < ~/.ssh/id_ed25519_hub.pub
# Copies the contents of the id_ed25519_hub.pub file to your clipboard
```

> 🔎  If `clip` isn't working, you can locate the hidden `.ssh` folder, open the file in your favorite text editor, and copy it to your clipboard.

2. In the upper-right corner of any page, click your profile photo, then click **Settings**. 
3. In the user settings sidebar, click **SSH and GPG keys**. 
4. Click **New SSH key** or **Add SSH key**. 
5. In the "Title" field, add a descriptive label for the new key.
6. Paste your key into the "Key" field. 
7. Click **Add SSH key**. 
8. If prompted, confirm your GitHub password. 

## [**Generate a new SSH key for Gitlab**](https://docs.gitlab.com/ee/ssh/)

```bash
$ ssh-keygen -f ~/.ssh/id_ed25519_lab -t ed25519 -C "max.mustermann@uni-bielefeld.de"
# User your Gitlab email address
```

### [**Add your SSH key to the ssh-agent**](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)

1. Ensure the ssh-agent is running. You can use the "Auto-launching the ssh-agent" instructions in "[**Working with SSH key passphrases**](https://docs.github.com/en/github/authenticating-to-github/working-with-ssh-key-passphrases)", or start it manually:

```bash
# start the ssh-agent in the background
$ eval `ssh-agent -s`
> Agent pid 59566
```

2. Add your SSH private key to the ssh-agent. If you created your key with a different name, or if you are adding an existing key that has a different name, replace _id_ed25519_lab_ in the command with the name of your private key file.

```bash
$ ssh-add ~/.ssh/id_ed25519_lab
```

### [**Add the public SSH key to your GitLab account**](https://docs.gitlab.com/ee/ssh/#add-an-ssh-key-to-your-gitlab-account)

To use SSH with GitLab, copy your public key to your GitLab account.

1. Copy the contents of your public key file. You can do this manually or use a script. For example, to copy an ED25519 key to the clipboard: 

```bash
cat ~/.ssh/id_ed25519_lab.pub | clip
```

1. Sign in to GitLab.
2. In the top right corner, select your avatar.
3. Select **Settings**.
4. From the left sidebar, select **SSH Keys**.
5. In the **Key** box, paste the contents of your public key. If you manually copied the key, make sure you copy the entire key, which starts with `ssh-ed25519` or `ssh-rsa`, and may end with a comment.
6. In the **Title** text box, type a description, like _Work Laptop_ or _Home Workstation_.
7. Optional. In the **Expires at** box, select an expiration date. ([Introduced in GitLab 12.9.](https://gitlab.com/gitlab-org/gitlab/-/issues/36243)) The expiration date is informational only, and does not prevent you from using the key. However, administrators can view expiration dates and use them for guidance when [**deleting keys**](https://docs.gitlab.com/ee/user/admin_area/credentials_inventory.html#delete-a-users-ssh-key).
8. Select **Add key**.

## [**Set up an SSH config-file**](https://stackoverflow.com/a/56536275)

**Generally, in Windows machine, the SSH config file stored in the following location:** `/c/Users/PC_USER_NAME/.ssh/`

Just follow the steps in below (if you're using the Git Bash):

1. Go to the .ssh directory `/c/Users/PC_USER_NAME/.ssh/`, click right mouse button and choose "Git Bash Here" or open a terminal at this location.
2. Create a file named "config" with the following command:

```bash
$ touch config
```

3. Now open the config file with the command (you can use any text editor as well):

```bash
$ nano config
```

4. Now write the following lines inside the config file:

Let's assume you've created two files named `id_ed25519_hub` for Github and `id_ed25519_lab` for GitLab.

```
# GITHUB
Host github.com
   HostName github.com
   PreferredAuthentications publickey
   IdentityFile ~/.ssh/id_ed25519_hub

# GITLAB
Host gitlab.com
   HostName gitlab.com
   PreferredAuthentications publickey
   IdentityFile ~/.ssh/id_ed25519_lab
```

> 🔎 [**How to edit files in a terminal with nano?**](https://askubuntu.com/questions/54221/how-to-edit-files-in-a-terminal-with-nano)

## Das Repository klonen

Um mit an dem Projekt zu arbeiten, müsst ihr zunächst das repository klonen. 
Dazu findet ihr auf der [**Startseite des Projekts**](https://gitlab.ub.uni-bielefeld.de/biomechatronik-praktikum-23/control-app) den blauen Button "Clone" und könnt das repository mit SSH oder HTTPS klonen.

> Falls ihr SSH nicht kennt, könnt ihr mit dem folgenden Befehl das Projekt mit HTTPS klonen.
>
> ```bash
> git clone https://gitlab.ub.uni-bielefeld.de/biomechatronik-praktikum-23/control-app.git
> ```

Anschließend müsst ihr euer Git-Passwort und -Benutzernamen eingeben.

> ❓ Falls ihr das Passwort oder den Benutzernamen zum Klonen falsch eingegeben habt, müssen diese manuell auf dem Rechner geändert werden, da git Bash euch nicht erneut danach fragt.
>
> Dazu geht ihr unter **Systemsteuerung** > **Benutzerkonten** > **Anmeldeinformationsverwaltung** auf **Windows-Anmeldeinformationen** und seht dann unter **generische Anmeldeinformationen** eine Zeile mit git. Dort drückt ihr auf den Pfeil rechts in der Zeile und dann auf **Bearbeiten***". So könnt ihr das richtige Passwort und den Benutzernamen eingeben. 
Daraufhin könnt ihr das repository dann klonen mit:
>
> ```bash
> git clone https://gitlab.ub.uni-bielefeld.de/biomechatronik-praktikum-23/control-app.git
> ```

## Arbeiten mit Branches

Git arbeitet mit dem Konzept von "branches". Branches kann man sich als isolierte Arbeitsumgebungen vorstellen, die bestimmte Versionen bestimmter Dateien beherbergen. Der "Haupt"-branch eines Projektes heißt üblicherweise *master*. Dort befindet sich in der Regel die neueste, stabile Version eines Projektes.

Wenn ihr mit Git arbeitet, empfiehlt es sich, Arbeiten **niemals** direkt im Master-branch durchzuführen. Stattdessen eröffnet ihr einen neuen Branch, der vom Master "abzweigt", und führt eure Änderungen dort durch. Spätestens, wenn ihr mit mehreren Leuten an einem Projekt arbeitet, ist das unabdingbar.

Andernfalls kann es auch schnell einmal passieren, dass ihr nur "eine kleine Änderung" einschiebt, und euer Projekt anschließend nicht mehr funtioniert.
Also vermeidet das, bitte.

Branches erstellt ihr im Projekt über die Gitlab Weboberfläche, nachdem ihr ein Issue zu einem konkreten Anliegen erstellt habt.

> Ein Branch ist immer die Grundlage für eure Beiträge zum Projekt!
> Arbeitet niemals im master-Branch!

Innerhalb des Issues habt ihr dann einen Knopf, der euch anbietet, ein "Merge-Request" zu erstellen. Für dieses Merge-Request wird dann ein eigener Branch erstellt, auf dem ihr Änderungen beitragt, die **mit dem zugehörigen Issue zu tun haben**.
Sollte eine Änderung thematisch nicht zu eurem aktuellen Issue passen, dann erzeugt ein neues Issue/einen neuen Branch. Das macht die Rückverfolgung der Änderungen einfacher.

## Git Befehle

Um euch die neuesten "Infos" vom Server zu holen, verwendet ihr

```bash
git fetch origin
```

In der Ausgabe seht ihr dann ggf., dass es neue Branches gibt.
Wollt ihr euer lokales Projekt auf den Stand bringen, den der Git Server im
Moment hat, verwendet ihr

```bash
git pull origin
```

Es ist generell eine gute Idee, `git pull` wenigstens auf dem Master branch
regelmäßig auszuführen, wenn ihr mit den Matlab Codes selbst arbeiten wollt.
Wenn ihr zu zweit (oder mit noch mehr Leuten) auf einem Branch arbeitet, solltet
ihr das auch tun, da ihr sonst ggf. die Änderungen nicht bekommt, die eure Kollegen
erstellt haben.

Eine Liste aller verfügbaren Branches liefert euch:

```bash
git branch --all
```

Eine Liste der Branches auf eurem Rechner:

```bash
git branch
```

Eine Liste der Branches auf dem remote Server liefert:

```bash
git branch --remote
```

Hier tauchen dann z.B. auch die branches auf, die ihr über die Gitlab Oberfläche
erstellt habt. Um auf einen dieser branches zu wechseln verwendet ihr:

```bash
git checkout <Name des Branches>
```

Und jetzt könnt ihr Anfangen, eure Änderungen in das Projekt einzubringen.
Achtet darauf, dass ihr auf dem richtigen Branch arbeitet. Das ist umso wichtiger,
wenn ihr an mehreren Issues zeitgleich arbeiten wollt.

Der Befehl

```bash
git status
```

sagt euch, was sich in eurer lokalen Version des Projekts verändert hat.
Habt ihr zum Beispiel eine Datei bearbeitet, oder neu erzeugt, sind diese
in Git farblich rot hinterlegt.
Wollt ihr eure Änderungen in das Projekt mit aufnehmen, verwendet ihr

```bash
git add <Name der Datei>
```

Ihr könnt auf diese Weise mehrere Dateien markieren. In `git status` sind diese
dann grün hinterlegt. Um die Änderungen in die Versinsverwaltung zu schreiben
(also in die "Geschichte" des Projektes aufzunehmen), verwendet ihr dann

```bash
git commit
```

Wenn ihr den Befehl ausführt, öffnet sich (irgend-) ein Texteditor.
Hier gebt ihr eine Nachricht ein, die eure Änderung möglichst präzise
beschreibt. Auch das hilft dabei, nachzuvollziehen, was genau im Projekt
passiert ist.

> Achtet darauf, in sich schlüssige Änderungen als "commits" beizutragen.
> Sollte eure Änderung 4 verschiedene Dateien umschließen oder sehr, sehr viele
> Zeilen Code, spaltet euren Commit bitte in kleinere Änderungen auf.
> Es sollte niemals passieren, dass auch umfangreiche Issues in nur einem
> commit bearbeitet werden - Sollte hier ein Fehler auftreten ist die
> Rückverfolgung erheblich schwieriger.

Solltet ihr zwischenzeitlich vergessen haben, was genau ihr an einer Datei getan
habt, könnt ihr das mit

```bash
git diff <Name der Datei>
```

in Erfahrung bringen. Sofern die Datei bereits mit "git add" in das Projekt
aufgenommen wurde, lautet der Befehl stattdessen

```bash
git diff --cached <Name der Datei>
```

Wenn ihr euren aktualisierten Projektstand auf dem Server speichern wollt,
verwendet ihr den Befehl

```bash
git push origin
```

Beachtet, dass nur Änderungen, die ihr als "commits" in die Projekthistorie
aufgenommen habt, auf dem Server landen.

Wenn ihr der Meinung seid, dass ihr ein Issue vollständig bearbeitet habt und
das Problem behoben wurde, öffnet ihr die Gitlab Weboberfläche und navigiert
zu eurem Merge-Request. Dort drückt ihr auf den Knopf "Resolve VIP Status", und
folgt dann den Anweisungen in Gitlab.

---

[🏠](home) | [*Nächste Seite >>*](set-up-flutter-sdk)