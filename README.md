google-drive-list-shared
========================

So there I was, not wanting to pay for G Suite Business or Enterprise, knowing zero Python, but hoping I could audit my shared files and find what had been shared outside my company.

Starting with @jameswthorne's blog post and script, I hacked around with the google drive API for far too long, and added a helper class found on @hayify's blog to do make life easier and added a pretty print for all the JSON things. And here we are today.

---

Parsing through the output can be fairly easily made into a usable list by:

```shell
sed -i "s/owners': \[{'emailAddress/OwnersEmailAddress/g" filename_1
egrep -v "'emailAddress': '([[:alnum:]_.-]+@yourdomaingoeshere.com)'" filename_1 | grep -B 2 "'emailAddress'" > filename_2
```

---

@jameswthorne's original post that got me here:
[Find All Shared Files in Google Drive with a Python Script](https://thornelabs.net/2018/01/03/find-all-shared-files-in-google-drive-with-a-python-script.html).
@hayify's helper class:
[Handling complex nested dicts in Python](https://www.haykranen.nl/2016/02/13/handling-complex-nested-dicts-in-python/)
