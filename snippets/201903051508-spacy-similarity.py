# :autor: @full.stack.hero
# :url: https://github.com/full-stack-hero/snippet/blob/master/snippet/snippets/201903051508-spacy-similarity.py
# spaCy is able to compare two objects, and make a prediction of how similar they are. Predicting similarity is
# useful for building recommendation systems or flagging duplicates.
#
# For example, you can suggest a user content that's similar to what they're currently looking at, or label a
# support ticket as a duplicate if it's very similar to an already existing one.
#
# Download the model "en_core_web_md" to try this example
# python -m spacy download en_core_web_md
import spacy

nlp = spacy.load('en_core_web_md')
tokens = nlp(u'dog cat banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
