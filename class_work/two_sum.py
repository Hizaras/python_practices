def two_sum(arr: list, target: int) -> list:
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return [-1, -1]


# print(two_sum(3))

# def balance_pair(brackets: str) -> bool:
#     # if brackets.strip() = "" or len(brackets) % 2 == 1:
#     if not brackets or len(brackets) % 2 == 1:
#         return False


# print(balance_pair("[]"))


