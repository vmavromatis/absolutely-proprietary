# Absolutely Proprietary
Proprietary package detector. Compares your installed packages against Parabola's package blacklist and then prints your Stallman Freedom Index.

# Quick install & run
`sudo pacman -S python && cd /tmp && git clone https://github.com/vmavromatis/absolutely-proprietary.git && cd absolutely-proprietary && python main.py`

Once done, you may run `less disgusting.txt` to view the detailed results. Explanation of terms:
- *nonfree*: This package is blatantly nonfree software.
- *semifree*: This package is mostly free, but contains some nonfree software.
- *uses-nonfree*: This package depends on, recommends, or otherwise inappropriately integrates with other nonfree software or services.

# Dependencies
* `python`


# Example output
```
-====================-
34 ABSOLUTELY PROPRIETARY PACKAGES INSTALLED
-====================-
Your GNU/Linux is infected with 34 proprietary packages out of 1504 total installed. Your Stallman Freedom Index is 97.74
The proprietary packages have been saved to disgusting.txt
```
