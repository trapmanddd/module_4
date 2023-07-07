## Решение задачи за O(N**2)

# def strcounter(s):
#     for lit in s:
#         counter = 0
#         for sub_lit in s:
#             if lit == sub_lit:
#                 counter +=1
#         print(lit, counter)
#
# strcounter('aabbbbcd')

## Решение задачи за O(N*M)

# str = 'asdfghjkadsf'
# print(list(str))
# print(set(str))

# def strcounter(s):
#     for lit in set(s):
#         counter = 0
#         for sub_lit in s:
#             if lit == sub_lit:
#                 counter +=1
#         print(lit, counter)
#
# strcounter('kjasghdashdd')

# Решение задачи за O(N)

def strcounter(s):
    lits_counter = {}
    for lit in s:
        lits_counter[lit] = lits_counter.get(lit, 0) + 1
    for lits, counter in lits_counter.items():
        print(lits, counter)

strcounter('aasssssdffffg')

