# 파일 읽는 부분
with open("ik.txt", "r") as f:
    data = f.read()

# 각 줄마다 자르기
n = data.split("\n")

result = []

#출력을 원하는 단어입력
word = ""

#x와 y 시작점 설정
for y in range(len(n)):
    for x in range(len(n[0])):
        # n이  있는 위치 찾기
        if len(word) > 0 and n[y][x] == word[0]:
            # 오른쪽 가로
            check = True
            if x + len(word) - 1 < len(n[0]):
                for b in range(len(word)):
                    if n[y][x + b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            # 왼쪽 가로
            check = True
            if x - len(word) + 1 >= 0:
                for b in range(len(word)):
                    if n[y][x - b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            # 아래로 내려가는 세로
            check = True
            if y + len(word) - 1 < len(n):
                for b in range(len(word)):
                    if n[y + b][x] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            # 위로 올라가는 세로
            check = True
            if y - len(word) + 1 >= 0:
                for b in range(len(word)):
                    if n[y - b][x] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])
                    check = True
            #오른쪽 위 대각선
            check = True
            if x + len(word) - 1 < len(n[0]) and  y - len(word) + 1 >= 0:
                for b in range(len(word)):
                    if n[y - b][x + b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])
            #왼쪽 위 대각선
            check = True
            if x - len(word) + 1 >= 0 and y - len(word) + 1 >= 0:
                for b in range(len(word)):
                    if n[y - b][x - b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])
            #오른쪽 아래 대각선
            check = True
            if x + len(word) - 1 < len(n[0]) and  y + len(word) - 1 < len(n):
                for b in range(len(word)):
                    if n[y + b][x - b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])
            #왼쪽 아래 대각선
            check = True
            if x - len(word) + 1 >= 0 and  y + len(word) - 1 < len(n):
                for b in range(len(word)):
                    if n[y - b][x - b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

print(result)
