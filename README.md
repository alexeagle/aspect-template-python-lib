# Python library template for Bazel

This assumes you've started from https://github.com/bazel-starters/py

Then run this (replacing `mylib` with the folder you'd like to create):

```shell
copier copy gh:alexeagle/aspect-template-python-lib mylib
buildozer "add data //${_}:requirements" //requirements:requirements.all
```

Finally update the `requirements/all.in` file with a new `-r` line pointing to the new requirements.txt file.
