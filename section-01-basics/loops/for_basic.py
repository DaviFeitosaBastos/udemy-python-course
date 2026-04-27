# for i in range(0, 11):
   # print(i)

# numbers = [3, 7, 2, 8, 1, 4, 9, 6]

# for i in numbers:
#     if i % 2 == 0:
#         print(i)

# values = [10, 5, 3, 8, 2]

# result = 0

# for i in values:
#     result += i

# print(result)

# names = ["ana", "bruno", "eva"]

# for item in names:
#     print(f"{item.upper()} have {len(item)} letters")

# fruits = ["apple", "banana", "grape", "mango"]

# for i, x in enumerate(fruits):
#     print(f"{i} - {x}")

students = [
    ("Ana", [8.5, 7.0, 9.5, 6.0]),
    ("Bruno", [5.0, 6.5, 4.0, 7.0]),
    ("Carlos", [10.0, 9.0, 8.5, 9.5]),
    ("Diana", [3.0, 4.5, 5.0, 2.5]),
    ("Eva", [7.0, 8.0, 7.5, 6.5]),
]

aproved = []
best_name = ""
best_average = 0
total_averages = 0
count = 0

print("=== Notas da Turma ===")

for name, grades in students:
    total = 0

    for grade in grades:
        total += grade

    average = total / len(grades)

    total_averages += average
    count += 1

    print(f"{name} -> {average:.2f}")

    if average > best_average:
        best_average = average
        best_name = name

    if average <= 5.9:   
        continue 
    aproved.append(name)
    
     

print("\n=== Alunos aprovados ===")

print(", ".join(aproved))

print(f"\n=== O melhor aluno foi ===")
print(f"{best_name} com {best_average:.2f}")

print(f"\n=== Média da turma ===")
print(f"{total_averages / count:.2f}")