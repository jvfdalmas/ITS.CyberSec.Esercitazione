### Lezione 8 - Ripasso (bonus)

"""1. Completion requirements

    The Number of Beautiful Subsets: write a function with an array nums of positive integers and a positive integer k given as inputs. A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k. Return the number of non-empty beautiful subsets of the array nums. A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

    Example 1:
    Input: nums = [2,4,6], k = 2
    Output: 4

    Example 2:
    Input: nums = [1], k = 1
    Output: 1 """

print("Soluzione - Question 1:")


# -------------------------------------------------------------------------------------------------------------------------------
print("\n")


"""2. Combinations: given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n]. You may return the answer in any order.

    Example 1:
    Input: n = 4, k = 2
    Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    Example 2:
    Input: n = 1, k = 1
    Output: [[1]]"""

print("Soluzione - Question 2:")

def combinations(n: int, k: int) -> list[list[int]]:
    arr: list = [0] * k
    result: list = []
    
    if k == 1:
        for num in range(1,n+1):
             result.append([num])
        return result
    
    if k > 2:
        for num in range(1,n+1):
            arr = [num] + combinations(n, k-1)
            if (arr not in result) and (arr[::-1] not in result) and (len(set(arr)) == len(arr)):
                arr.sort()
                result.append(arr[:])
        return result
    
    else:
        for num in range(1,n+1):
            arr[0] = num
            for num_p2 in range(1,n+1):
                if arr[0] != num_p2:
                    arr[1] = num_p2
                    return arr[:]
                else:
                    arr[1] = 0


print(combinations(4, 2)) # [[1,2]]
print(combinations(1, 1)) # [[1]]
print(combinations(2, 1)) # [[1],[2]]
print(combinations(3,3)) # [[1,2,3]]

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")


"""3. Generate Parentheses: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:
    Input: n = 1
    Output: ["()"]"""

print("Soluzione - Question 3:")





# -------------------------------------------------------------------------------------------------------------------------------
print("\n")