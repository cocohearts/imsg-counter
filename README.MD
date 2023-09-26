# How To Use

## Dependencies
- `pip install git+https://github.com/my-other-github-account/imessage_tools.git`
- Also requires terminal full disk access, as described [https://osxdaily.com/2018/10/09/fix-operation-not-permitted-terminal-error-macos/]
- `ipython`
## Setup
- Download a vcf contacts file from GContacts
- Paste the path for said contacts file into `path = ` on line 7
- Requires MacOS that is connected to iMessages
## Use
- In directory boot up `ipython` in terminal
- Enter `from imsg_counter import *`
- Fetch the last number messages to fetch as prompted
- Run `top(N)` to retrieve the N people with the most texts
- Four columns correspond to:
    1. Total texts
    2. Their texts
    3. Your texts
    4. Name

# Production Notes
- Spent around 2.5 hours developing
- Inspired by iMazing
