# Absolutely Proprietary
Proprietary package detector. Compares your installed packages against Parabola's package blacklist and then prints your Stallman Freedom Index.

*Update - I thought it's better to remove all the ascii stuff so there are no external libs. Thanks for the PRs!*

# Quick install & run
`curl -o - https://raw.githubusercontent.com/vmavromatis/absolutely-proprietary/master/run.sh | sh`

Once done, you may run `less disgusting.txt` to view the detailed results. Explanation of terms:
- *nonfree*: This package is blatantly nonfree software.
- *semifree*: This package is mostly free, but contains some nonfree software.
- *uses-nonfree*: This package depends on, recommends, or otherwise inappropriately integrates with other nonfree software or services.

# Output
```
-====================-
34 ABSOLUTELY PROPRIETARY PACKAGES INSTALLED
-====================-
Your GNU/Linux is infected with 34 proprietary packages out of 1504 total installed. Your Stallman Freedom Index is 97.74
The proprietary packages have been saved to disgusting.txt
```
