#!/usr/bin/env python
import sys
from urllib.request import Request, urlopen
request = Request(sys.argv[1])
request.get_method = lambda: 'HEAD'
print(urlopen(request).url)
