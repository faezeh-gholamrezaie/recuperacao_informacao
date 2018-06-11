import unicodedata

""" Normalise (normalize) unicode data in Python to remove umlauts, accents etc. """

data = u'naïve café'
normal = unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')
print normal
