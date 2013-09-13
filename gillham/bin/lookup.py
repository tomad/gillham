#!/usr/bin/env python

import json

from gillham import dump_code
from chap3 import read_ch3_appendix


def main():
    """ Generate a lookup table from the gillham decoder implementation,
    testing that it's output matches that given in the Annex-10 Chapter 3
    appendix. """
    ch3_alts = read_ch3_appendix()
    gillham_alts = dump_code()

    assert len(ch3_alts) == len(gillham_alts)
    assert all(a == b for (a, b) in zip(ch3_alts, gillham_alts))

    print(json.dumps(gillham_alts, indent=4))

if __name__ == '__main__':
    main()
