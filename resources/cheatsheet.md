# For logic from my for_basic.py

loop externo → pega ("Ana", [8.5, 7.0, 9.5, 6.0])
│
├── total = 0                        # zera pra cada aluno
│
├── loop interno → percorre [8.5, 7.0, 9.5, 6.0]
│   ├── total += 8.5  → total = 8.5
│   ├── total += 7.0  → total = 15.5
│   ├── total += 9.5  → total = 25.0
│   └── total += 6.0  → total = 31.0
│
├── average = 31.0 / 4 → 7.75
│
├── total_averages += 7.75           # acumula pra média geral
├── count += 1                       # conta alunos
│
├── print "Ana -> 7.75"
│
├── 7.75 > 0? sim → best_average = 7.75, best_name = "Ana"
│
├── 7.75 <= 5.9? não → não faz continue
└── aproved.append("Ana")            # Ana é aprovada

loop externo → pega ("Bruno", [...])
│
└── ... repete tudo do zero

