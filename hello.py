#!/usr/bin/env python3
from pygit2 import Repository, GIT_SORT_TIME
repo = Repository('.git')

print("""<html>
<body>
<p>Hello, Juyoung!<p/>""")

print("""
<p>Git log is:
<pre>""")

last = repo[repo.head.target]
for commit in repo.walk(last.id, GIT_SORT_TIME):
    print(commit.message)

print("""
</pre>
</p>
""")

print("""
</body>
</html>""")
