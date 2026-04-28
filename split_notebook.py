import json
import sys

with open(sys.argv[1], 'r') as f:
    nb = json.load(f)

part_a_idx = None
part_b_idx = None

for i, cell in enumerate(nb['cells']):
    source = ''.join(cell['source'])
    if '# Part A: Similarity and Anomalies' in source and part_a_idx is None:
        part_a_idx = i
    if '# Part B: Research Question' in source and part_b_idx is None:
        part_b_idx = i

print(f"Part A starts at cell {part_a_idx}, Part B starts at cell {part_b_idx}")
print(f"Preprocessing: cells 0-{part_a_idx - 1} ({part_a_idx} cells)")
print(f"Part A: cells {part_a_idx}-{part_b_idx - 1} ({part_b_idx - part_a_idx} cells)")
print(f"Part B: cells {part_b_idx}-{len(nb['cells']) - 1} ({len(nb['cells']) - part_b_idx} cells)")

for label, start, end in [('preprocessing', 0, part_a_idx),
                           ('part_a', part_a_idx, part_b_idx),
                           ('part_b', part_b_idx, len(nb['cells']))]:
    chunk = dict(nb)
    chunk['cells'] = nb['cells'][start:end]
    outpath = f"{label}.ipynb"
    with open(outpath, 'w') as f:
        json.dump(chunk, f, indent=1)
    print(f"Wrote {outpath}")