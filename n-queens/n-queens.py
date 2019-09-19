def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield state + (pos,)
            else:
                for answer in queens(num, state + (pos,)):
                    yield answer


def my_print(answer):
    def line(pos, length=len(answer)):
        return ' .' * pos + ' Q' + ' .' * (length - pos - 1)
    for pos in answer:
        print(line(pos))


n = int(input('N: '))
print()
for answer in queens(n):
    my_print(answer)
    print()
