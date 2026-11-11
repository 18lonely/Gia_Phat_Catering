"""Arithmetic examples for confirmed accounting intent; not a tax or backend test."""
from decimal import Decimal as D

# Example tax rate only, not actual configured tax.
gross_from_exclusive=D('100000')*(1+D('8')/100)
gross_inclusive=D('108000')
assert gross_from_exclusive==gross_inclusive==D('108000')
assert D('70')/1000*gross_from_exclusive==D('7560')
assert D('70')/1000*D('100000')==D('7000')
original_due=D('100')*D('40000')
# Percentage base below is a proposed fixture, still awaiting business confirmation.
percent_separate=original_due*D('5')/100
fixed_separate=D('100')*D('2000')
assert percent_separate==fixed_separate==D('200000')
assert original_due==D('4000000')
assert original_due!=original_due-fixed_separate
print('PASS: 3 purchase-cost examples; 2 separate-discount examples keep order amount due at 4000000. Percent base is hypothetical. Backend tests executed: 0.')
