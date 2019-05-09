from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    # TODO
    # take string inputs a and b
    # split each string into lines
    # compute a list of all lines that appear in both a and b
    # return the list
    return list(set(a.split("\n")).intersection(set(b.split("\n"))))


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    # take string inputs a and b
    # split each string into sentences
    # to split use Natural Language ToolKit sent_tokenize
    # compute a list of all sentences that appear in both a and b
    # return the list
    return list(set(sent_tokenize(a)).intersection(set(sent_tokenize(b))))


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    # take string inputs a, b and substring length n
    # split each string into substrings of length n
    suba = set(a[i:n+i] for i in range(len(a) - 1))
    subb = set(b[i:n+i] for i in range(len(b) - 1))
    # compute a list of all substrings that appear in both a and b
    # return the list
    return list(suba.intersection(subb))