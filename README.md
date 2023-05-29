<h1 align="center">httpanalyzer</h1>

<p align="center">
<a href="https://www.python.org/"><img alt="Language" src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python"></a>
<a href="https://mit-license.org/"><img alt="License" src="https://img.shields.io/pypi/l/phishing-baiter?color=blueviolet&style=for-the-badge"></a>
<a href="https://pypi.org/project/phishing-baiter/"><img alt="Version" src="https://img.shields.io/pypi/v/phishing-baiter?label=version&logo=pypi&style=for-the-badge"></a>
<a href="https://github.com/MartinMerkli/phishing-baiter"><img alt="Stars" src="https://img.shields.io/github/stars/martinmerkli/phishing-baiter?color=lightgrey&logo=github&style=for-the-badge"></a>
<a href="https://github.com/MartinMerkli/phishing-baiter/commits/main"><img alt="Commit Activity" src="https://img.shields.io/github/commit-activity/m/martinmerkli/phishing-baiter?color=green&style=for-the-badge"></a>
</p>

phishing-baiter is a tool to flush phishing websites with fake, although good-looking, personal data.

## License

This project is licensed under the MIT-license. See LICENSE.txt for more information.

## Installing

Make sure pip3 is installed and up to date before executing this command.

```
pip3 install phishing-baiter
```

## Usage

Import the library:

```
import phishing_baiter
```

In a loop, create a new fake identity:

```
identity = phishing_baiter.FakeIdentity()
```

You can now get and send the fake data to the phishing site (on your own risk). Data is only generated if it is actually used.

```
print(f"{identity.name()} {identity.e_mail()} {identity.password()}")
```
