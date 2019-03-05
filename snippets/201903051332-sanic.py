# :autor: @full.stack.hero
# :url: https://github.com/full-stack-hero/snippet/blob/master/snippet/snippets/201903051332-sanic.py
# Sanic is a Python web server and web framework that's
# written to go fast. It allows the usage of the async/await
# syntax added in Python 3.5, which makes your code non-blocking
# and speedy.
#
# The goal of the project is to provide a simple way to get
# up and running a highly performant HTTP server that is easy
# to build, to expand, and ultimately to scale.
from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
