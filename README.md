# Exoop

Portable for your scoop apps.

## Installation

```powershell
git clone https://github.com/AnyThund/exoop.git
cd exoop
python setup.py install
```

## Usage

```shell
$ exoop
```

This command will export installed apps default on your Desktop, named apps.txt. The same function as `scoop export > apps.txt`.

```shell
$ exoop -h
```

Show help.

```shell
$ exoop -z
```

Export all installed apps' installation packages into 'apps.zip' default on your Desktop.

```shell
$ exoop -n name
```

Rename output file name to `name.txt`.

```shell
$ exoop -d path
```

Choose another path your file export to.