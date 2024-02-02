See [`hw1.py`](hw1.py). Sample invocation:

    ./hw1.py horoscopes-1.tsv kjv.tsv

Using horoscopes as the numerator in the ratio and the KJV as the denominator,
the ten words with the lowest log-odds ratios (i.e., which are most
characteristic of the KJV) are:

| lord | -8.3883 |
| unto | -7.4430 |
| ye | -7.2658 |
| father | -7.1277 |
| thee | -6.9987 |
| men | -6.9507 |
| holy | -6.6125 |
| o | -6.4662 |
| king | -6.4653 |
| fathers | -6.4524 |

(I note that *father* and *fathers* are inflectional variants of the same lemma.
Had I lemmatized or stemmed the data before building the frequency
distributions, this term might have an even more extreme score.)

And the ten words with the highest log-odds ratios (i.e., which are most
characteristic of the horoscopes) are:

| action | 6.4896 |
| everything | 6.4900 |
| feeling | 6.5184 |
| fact | 6.7074 |
| trying | 6.7493 |
| usual | 6.8518 |
| attention | 7.0517 |
| everyone | 7.3775 |
| comes | 7.5819 |
| around | 7.8220 |

(I do not generally provide solutions for the stretch goals.)
