#!/usr/bin/env python3
import sys
from datetime import datetime

def usage():
    print("Usage: python lp.py <lower> <upper> <current>")
    sys.exit(1)

if len(sys.argv) != 4:
    usage()

lo, hi, cur = map(float, sys.argv[1:4])
if lo >= hi:
    sys.exit("lower must be < upper")

width = hi - lo
mid = (hi + lo) / 2
dist = abs(cur - mid) / (width / 2)
share = max(0.0, 1.0 - min(1.0, dist))  # toy curve

print(f"lp-range-toy — {datetime.utcnow().isoformat()}Z")
print(f"range=({lo},{hi}) current={cur}")
print(f"toy_share_at_current={share:.4f}")
