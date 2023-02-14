def balance_pair(brackets: str) -> bool:
    if brackets.strip() == "" or len(brackets) % 2 == 1:
        return False

    stack = []
    for bracket in brackets:
        if bracket in "{[(":
            stack.append(bracket)
        elif bracket in "}])":
            peek = stack[-1]
            if peek == "{" and bracket == "}":
                stack.pop()
            if peek == "[" and bracket == "]":
                stack.pop()
            if peek == "(" and bracket == ")":
                stack.pop()

            else:
                return False
            return True


print(balance_pair("[]"))
