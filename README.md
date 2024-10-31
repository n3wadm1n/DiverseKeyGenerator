# DiverseKeyGenerator

The DiverseKeyGenerator is an innovative tool designed to create strong and secure passwords, utilizing a wide range of characters from different languages and cultures. Supporting Latin, Japanese, Chinese, Korean, and Russian characters, the tool ensures that your passwords not only meet the highest security standards but also reflect the diversity of the modern world.

## Features:
### Character Variety:
Generates passwords using letters, numbers, and symbols from multiple alphabets, ensuring maximum security.
### Advanced Customization:
Allows users to choose the length and types of characters they want, tailoring the password generation to their specific needs.
### User-Friendly Interface:
The tool is easy to use, with a clear interface that makes the password generation process quick and efficient.
### Enhanced Security:
The passwords are created with robust algorithms that provide high resistance to cyber attacks, keeping your personal information safe.

```
usage: diversekeygenerator.py [-h] [--ma MA] [--mi MI] [--nu NU] [--es ES] [--ra RA]

Strong and complex password generator.

options:
  -h, --help  show this help message and exit
  --ma MA     Number of uppercase letters in the password
  --mi MI     Number of lowercase letters in the password
  --nu NU     Number of digits in the password
  --es ES     Number of special characters in the password
  --ra RA     Generate a password with a random distribution of characters with the specified total length
```

Examples:

```
python3 diversekeygenerator.py --ra 19

Generated password:
 ムウごaý+Ыむeぅく²8いaХソぅF
```

```
python3 diversekeygenerator.py --ma 6 --mi 5 --nu 10 --es 8

Generated password:
 Э=8rhO37Т0YSДMZUq63kc10{ôë5Ж8

```
