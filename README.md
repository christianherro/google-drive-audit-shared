google-drive-list-shared
========================

So there I was, not wanting to pay for G Suite Business or Enterprise, knowing zero Python, but hoping I could audit my shared files and find what had been shared outside my company.

Starting with @jameswthorne's blog post and script, I hacked around with the google drive API for far too long, and added a pretty print helper on @hayify's blog to do all the JSON things.

The output is still pretty ugly, but you can grep -v through it to remove known domains. 

Supporting files for blog post: [Find All Shared Files in Google Drive with a Python Script](https://thornelabs.net/2018/01/03/find-all-shared-files-in-google-drive-with-a-python-script.html).
