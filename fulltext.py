import os, time, fulltext
from sphinx_app.index import MyIndex

# Add a document to the index.
path = 'resume.doc'
st = os.stat(path)
MyIndex.objects.create(
    name = path,
    content = fulltext.get(path, ''),
    size = st.st_size,
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(st.st_mtime)),
)

# Update a document in the index
doc = MyIndex.objects.get(pk=1)
doc.content = fulltext.get(path, '')
doc.size = st.st_size
doc.date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(st.st_mtime))
doc.save()