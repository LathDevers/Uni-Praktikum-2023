In this guide, we will
1. first [**generate an SSH key for GitHub**](#generate-a-new-ssh-key-for-github) and [**register it in our GitHub account**](add-the-ssh-key-to-your-github-account) then
2. [**generate another SSH key for GitLab**](generate-a-new-ssh-key-for-gitlab) and [**register it in our GitLab account**](add-the-public-ssh-key-to-your-gitlab-account) and finally
3. [**set up a config file**](set-up-an-ssh-config-file) that will manage which SSH key to use in different scenarios.

[<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/2048px-Octicons-mark-github.svg.png" width="15"/> **Source**](https://gist.github.com/marcoandre1/4b0fbca83104e08d3e729a25a0cba4eb)

I recently had to manage two ssh keys (one for Github and one for GitLab).

The first question you can ask yourself is [**can you have the same ssh key for both GitHub and GitLab**](https://stackoverflow.com/questions/56285972/can-you-and-is-it-advisable-to-use-the-same-ssh-key-for-github-and-gitlab-gitbuc)? The answer is *yes* [**but it is not advisable**](https://stackoverflow.com/a/56285988).

The **best answer** is that you should set one ssh key for Github and another one for GitLab. First, you should [**check for existing ssh-keys on your system**](https://docs.github.com/en/github/authenticating-to-github/checking-for-existing-ssh-keys):

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

> 🔎 You can simply delete these files if you want to remove the keys. No additional step is required.

## [**Generate a new SSH key for GitHub**](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)

If you don't have an existing public and private key pair or don't wish to use any that are available to connect to GitHub, then **generate a new SSH key**:

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

If your SSH public key file has a different name than the example code, modify the filename to match your current setup. When copying your key, don't add any new lines or whitespace.

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

## [**Generate a new SSH key for GitLab**](https://docs.gitlab.com/ee/ssh/)

```bash
$ ssh-keygen -f ~/.ssh/id_ed25519_lab -t ed25519 -C "max.mustermann@uni-bielefeld.de"
# User your GitLab email address
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
7. Optional. In the **Expires at** box, select an expiration date. ([Introduced in GitLab 12.9.](https://gitlab.com/gitlab-org/gitlab/-/issues/36243)) The expiration date is informational only and does not prevent you from using the key. However, administrators can view expiration dates and use them for guidance when [**deleting keys**](https://docs.gitlab.com/ee/user/admin_area/credentials_inventory.html#delete-a-users-ssh-key).
8. Select **Add key**.

## [**Set up an SSH config-file**](https://stackoverflow.com/a/56536275)

**Generally, in Windows machines, the SSH config file is stored in the following location:** `/c/Users/PC_USER_NAME/.ssh/`

Just follow the steps below (if you're using Git Bash):

1. Go to the .ssh directory `/c/Users/PC_USER_NAME/.ssh/`, click the right mouse button, and choose "Git Bash Here" or open a terminal at this location.
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

---

[*<< Vorherige Seite*](introduction-to-git) | [*Nächste Seite >>*](set-up-flutter-sdk)