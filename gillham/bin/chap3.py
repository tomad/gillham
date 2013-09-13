#!/usr/bin/env python

import re
import fileinput


def fix_alt(alt):
    """ Fix oddities in pdftotext output;;

        '1 000' -> '1000'
        'B950' -> '-950'
    """
    return alt.replace(' ', '').replace('B', '-')


def read_ch3_appendix(ch3_appendix=None):
    """
      Extract pressure-altitude code from appendix

      $ pdftotext -layout -f 109 -l 137 an10_V4_cons.pdf ch3_appendix.txt

      Outputs list of  tuples (lower, upper, bits)

      Where bits have bit positions (D1 added):

          D1 D2 D4 A1 A2 A4 B1 B2 B4 C1 C2 C4
    """

    alt = re.compile('^\s*(B?\d+(?:\ \d+)?)\s+to\s+(B?\d+(?:\ \d+)?)(.*)$')
    bit = re.compile('\s+([01])')

    alts = []

    for line in fileinput.input(files=ch3_appendix):
        alt_match = alt.match(line)

        if not alt_match:
            continue

        lower, upper, bits = alt_match.groups()

        lower = int(fix_alt(lower))
        upper = int(fix_alt(upper))

        bits = bit.findall(bits)
        assert len(bits) == 11

        # append add D1 bit
        bits = '0b0' + ''.join(bits)

        alts.append((lower, upper, bits))

    # 100 ft increments between 126750 and -950
    # one 50 ft increment between -950 and -1000
    assert len(alts) == ((126750 - -950) / 100) + 1

    return alts


def main():
    alts = read_ch3_appendix()
    for lower, upper, bits in alts:
        median = int((((upper - lower) / 2) + lower))
        print('{0:>10} to {1:>10} ({2}): {3}'.format(
            lower,
            upper,
            median,
            bits,
            width=40))

if __name__ == '__main__':
    main()
