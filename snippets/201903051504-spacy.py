# :autor: @full.stack.hero
# :url: https://github.com/full-stack-hero/snippet/blob/master/snippet/snippets/201903051504-spacy.py
# spaCy is an open-source software library for advanced Natural Language Processing.
# spaCy excels at large-scale information extraction tasks. It's written from the ground up in carefully memory-managed Cython.
#
# The library respects your time, and tries to avoid wasting it. It's easy to install, and its API is simple and productive.
import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)
