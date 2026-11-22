"""Static integrity checks of the published Markdown article and repository.

Checks formal coverage and traceability, NOT objective scientific truth and NOT
verbatim fidelity of the unavailable raw voice transcript.
"""
from pathlib import Path
import re
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[1]
paper = (ROOT / 'paper.md').read_text(encoding='utf-8')
readme = (ROOT / 'README.md').read_text(encoding='utf-8')
audit = (ROOT / 'AUDIT.md').read_text(encoding='utf-8')
source_ai = (ROOT / 'sources/AI_statement_2026-11-22_verbatim.md').read_text(encoding='utf-8')
source_voice = (ROOT / 'sources/voice-archive-register.md').read_text(encoding='utf-8')
refs = (ROOT / 'references.md').read_text(encoding='utf-8')
math = (ROOT / 'mathematical-appendix.md').read_text(encoding='utf-8')

checks = []

def check(name, ok, detail=''):
    checks.append((name, bool(ok), detail))

chapters = [int(x) for x in re.findall(r'^## (\d+)\.', paper, flags=re.M)]
check('27 ordered paper chapters', chapters == list(range(1, 28)), str(chapters))
check('two properly marked authorial corpora', all(x in paper for x in ['# Parte I.', '# Parte II.', '2 novembre 2026', '22 novembre 2026']))
check('all 10 voice indices in register', all(f'V{i:02d}' in source_voice for i in range(1, 11)))
check('missing source explicitly declared', all(t in paper and t in source_voice for t in ['V09', '2:37']))
check('raw voice transcript absence disclosed', 'non contiene una trascrizione letterale' in (ROOT/'sources/VOICE_README.md').read_text(encoding='utf-8'))
check('verbatim author AI source preserved', len(source_ai.split()) > 1400 and 'Metti tutto insieme' in source_ai and 'cinquant' in source_ai)
check('original AI author position covered', all(x in paper for x in ['ottimista', 'concorrenza', 'reddito universale', 'Elon Musk', 'giovani', 'Svizzera', '1.000', '100 euro', 'qualità', 'breakthrough']))
check('historical contexts included', all(x in paper for x in ['agricoltura', 'Keynes', 'luddist', 'treno', 'automobile']))
check('voice completeness detailed', all(x in audit for x in ['35 voci', '37 voci']))
check('outside evidence cited', all(f'R{i:02d}' in refs for i in range(1, 15)))
check('mathematical distinction of cost and price', all(x in math for x in ['90%', '€310', 'elasticità', 'reddito disponibile reale']))
check('disclaimer of demonstration', all(x in paper.lower() for x in ['non è una', 'non implica', 'non è', 'illus']))
check('no old placeholder unupdated', not any(x in paper for x in ['non è ancora stato fornito', 'non ancora consegnata', 'L’intera teoria sull’intelligenza artificiale è esclusa']))
check('full original AI preserved separately', len(source_ai) > 10000 and 'enrichment e enlargement' in source_ai)
check('theoretical mechanisms include limitations', all(x in paper for x in ['elasticità', 'concentrazione', 'nuova domanda', 'prezzi reali', 'competenz']))
check('government 6 examples', all(f'### 22.{i} ' in paper for i in range(1, 7)))
check('three explicit AI scenarios', all(f'### Scenario {x}' in paper for x in 'ABC'))
check('migration percentages preserved', all(x in paper+source_voice for x in ['3%', '5%', '10%', '15%', '20%', '90–95%', '99%']))
check('research policy caveats', all(x in paper.lower() for x in ['non dimostra', 'non equivale', 'non è una', 'non si attribuiscono']))

for path in [ROOT/'README.md', ROOT/'paper.md', ROOT/'AUDIT.md', ROOT/'mathematical-appendix.md']:
    check('UTF-8 text ' + path.name, '\ufffd' not in path.read_text(encoding='utf-8'))

# Check local Markdown links in README (ignore http links).
missing=[]
for path in re.findall(r'\]\(([^)]+)\)', readme):
    if not path.startswith(('http:', 'https:', '#', 'mailto:')):
        if not (ROOT/path).exists(): missing.append(path)
check('README local links resolve', not missing, repr(missing))

csvfile = ROOT/'outputs/illustrative_scenarios.csv'
with csvfile.open(encoding='utf-8',newline='') as f:
    rows=list(csv.DictReader(f))
check('7 reproducible cases',len(rows)==7)
check('all cases marked synthetic',all(r['scenario_type']=='ILLUSTRATIVE_NOT_ESTIMATED' for r in rows))
check('example 100 EUR below full cost',all(r['price_below_cost']=='True' for r in rows if float(r['price_1_EUR'])==100))
check('sensitivity produces revenue both up and down',any(float(r['revenue_ratio'])>1 for r in rows) and any(float(r['revenue_ratio'])<1 for r in rows))

# Strong lexical spot-check for users' 22 Nov AI monologue.
for name, phrases in {
    'historical progress': ['contadini', 'treni', 'cavalli'],
    'human oversight': ['macchina', 'persona'],
    'entry-level': ['giovani', 'esperienza'],
    'competitive price': ['margini', 'prezzi', 'concorrenza'],
    'quality ladder': ['qualità media', 'qualità alta', 'qualità bassa'],
    'industrial structure': ['programmatore', 'consulente', 'auto'],
    'human capital': ['specializzati', 'remunerativi', 'tecnici'],
    'real vs nominal': ['termini reali', 'nominali'],
    'transfer policy': ['stipendio universale', 'Elon Musk', 'Stato'],
    'continuous monitoring': ['alla cieca', 'graduale', 'breakthrough'],
    'horizontal vertical': ['orizzontale', 'verticale', 'enrichment', 'enlargement'],
}.items():
    check('AI original spot-check: '+name,all(s.lower() in source_ai.lower() for s in phrases))

passed=sum(ok for _,ok,_ in checks)
print(f'AUDIT: {passed}/{len(checks)} PASS')
for name,ok,detail in checks:
    print(('PASS' if ok else 'FAIL')+' | '+name+((' | '+detail) if detail and not ok else ''))
print('PAPER:',len(paper.split()),'words;',len(paper),'characters; SHA256',hashlib.sha256(paper.encode('utf-8')).hexdigest())
if passed!=len(checks):
    raise SystemExit(1)
