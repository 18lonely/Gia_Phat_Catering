"""Verify synthetic arithmetic, not the production engine or accountant acceptance."""
from pathlib import Path
from decimal import Decimal as D, ROUND_HALF_UP, ROUND_CEILING, localcontext
import json
B=Path(__file__).resolve().parents[1]
data=json.loads((B/'test/fixtures/synthetic-cost.json').read_text(encoding='utf-8'))
assert data['status']=='SYNTHETIC_NOT_ACCOUNTANT_APPROVED'
assert len(data['dishes'])==len(data['days'])==10
with localcontext() as ctx:
    ctx.prec=40
    for dish in data['dishes']:
        total=D(0)
        for r in dish['lines']:
            if not r['includeInCost']:continue
            q,p,f,h=map(D,[r['qty'],r['priceVnd'],r['conversionFactor'],r['wastePct']])
            assert f>0 and p>0 and 0<=h<100
            if dish['applyWaste']:q/=1-h/100
            total+=q*p/f
        assert total==D(dish['expectedExactCost']),(dish['id'],total)
    for day in data['days']:
        mains=list(map(D,day['mainCosts']))
        a={'DAT_NHAT':max(mains),'BINH_QUAN':sum(mains)/len(mains),'MAC_DINH':mains[day['defaultIndex']]}[day['method']]*day['mainPick']
        cost=a+D(day['otherCost'])+D(day['allowance'])
        revenue=D(day['mealPrice'])/(1+D(day['vatPct'])/100)
        pct=(cost/revenue*100).quantize(D('.01'),rounding=ROUND_HALF_UP)
        result='DAT' if pct<=D(day['thresholdPct']) else 'KHONG_DAT'
        assert (cost,pct,result)==(D(day['expectedCost']),D(day['expectedPct']),day['expectedResult']),(day['id'],cost,pct,result)
    # Independent scalar anchors for estimate rounding and waste applied once.
    assert (D(1001)/1000).quantize(D('.01'),rounding=ROUND_CEILING)==D('1.01')
    assert (D(70)*10/(1-D('.20'))/1000).quantize(D('.01'),rounding=ROUND_CEILING)*120000==D('105600')
    assert D('1.2').quantize(D(1),rounding=ROUND_HALF_UP)==D(1)
register=json.loads((B/'review/decision-register.json').read_text(encoding='utf-8'))
assert len({r['id'] for r in register})==len(register)
assert all(r['status'] in ('OPEN','PARTIALLY_CONFIRMED') and r['decision'] is None and r['approvedBy'] is None for r in register)
print(f'PASS: 10 synthetic dish calculations, 10 synthetic day calculations, 3 rounding anchors; {len(register)} review items retain unresolved details. Production/accountant tests executed: 0.')
