# :autor: @full.stack.hero
# :url: https://github.com/full-stack-hero/snippet/blob/master/snippet/snippets/201903051448-fire.py
# Python Fire is a simple way to create a CLI in Python.
#
# You can call Fire on any Python object:
# functions, classes, modules, objects, dictionaries, lists, tuples, etc. They all work!
#
# Here's an example of calling Fire on a class.
# Check out: https://github.com/google/python-fire
import fire

class Calculator(object):
  """A simple calculator class."""

  def double(self, number):
    return 2 * number

if __name__ == '__main__':
  fire.Fire(Calculator)
