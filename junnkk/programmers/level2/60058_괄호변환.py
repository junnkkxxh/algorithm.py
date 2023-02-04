def is_correct_str(str):
    stack = []
    for s in str:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True if not stack else False


def seperate_balanced_str(str):
    u = ''
    cnt1 = 0
    cnt2 = 0
    for s in str:
        if s == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        u += s
        if cnt1 != 0 and cnt1 == cnt2:
            break
    v = str[len(u):]
    return (u, v)


def make_correct_str(str):
    if len(str) == 0 or is_correct_str(str):
        return str

    u, v = seperate_balanced_str(str)

    if is_correct_str(u):
        v = make_correct_str(v)
        return u+v
    else:
        temp = "("+make_correct_str(v)+")"
        new_u = ''
        for i in range(1, len(u)-1):
            if u[i] == "(":
                new_u += ")"
            else:
                new_u += "("
        return temp+new_u


def solution(p):
    return make_correct_str(p)
