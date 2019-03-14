# items = [4, 6, 2, 2, 6, 4, 4, 4]
items = ['bob', 'bob', 'carl', 'alex', 'bob']

cnt = {}
for item in items:
    if(item in cnt):
        cnt[item] += 1
    else:
        cnt[item] = 1
print(cnt)

num = len(cnt)
lst = []

sorted_k = (sorted(cnt, key=lambda k: cnt[k], reverse=True))

for k in sorted_k:
    for i in range(0, cnt[k]):
        lst.append(k)
print(lst)

# for i in range(0, num):
#     max = -1
#     prt = None
#     for key in cnt.keys():
#         if(cnt[key] > max):
#             max = cnt[key]
#             prt = key
#     for j in range(0, max):
#         lst.append(prt)
#     cnt.pop(prt)
# print(lst)

# print(sorted(items, key=lambda x: (-items.count(x), items.index(x))))   # Default is asc
# key: 비교 기준
# count: 리스트에 포함된 요소 x의 개수 세기
# index: x의 위치값을 리턴한다.
# 이 익명 함수는 인자 x를 전달 받아서 tuple(수정할 수 없는 list)을 return한다.