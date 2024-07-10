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

# my code
def combine(n: int, k: int) -> list[list[int]]: 
    result: list = []

    if k == 1:
        for nums in range(1,n+1):
            arr = [nums]
            result.append(arr[:])
    
    else:
        for nums in range(1,n+1):
            for lista in combine(n, k-1):
                arr = [nums] + lista
                if (len(arr) == len(set(arr))) and (sorted(arr) not in result):
                    result.append(arr)
    
    return result


# efficient code
def combine(n: int, k: int) -> list[list[int]]: 
    result = []  # This will hold all the combinations

    def backtrack(start: int, path: list[int]):
        # Base case: if the path has reached the desired length, add it to result
        if len(path) == k:
            result.append(path[:])  # Make a copy of the current path
            return
        
        # Try each number from 'start' to 'n'
        for i in range(start, n + 1):
            path.append(i)  # Add number to the current path
            backtrack(i + 1, path)  # Recursively build the next part of the combination
            path.pop()  # Remove the last number to try the next possible number (backtrack)

    backtrack(1, [])  # Start the backtracking process from number 1
    return result  # Return all found combinations


# Example usage
print(combine(3, 1))
print(combine(3, 2))
print(combine(4, 2)) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(combine(1, 1)) # [[1]]
print(combine(2, 1)) # [[1],[2]]
print(combine(3, 3)) # [[1,2,3]]

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")


"""3. Generate Parentheses: Given n pairs of parentheses, write a function to generate all combine of well-formed parentheses.

    Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:
    Input: n = 1
    Output: ["()"]"""

print("Soluzione - Question 3:")





# -------------------------------------------------------------------------------------------------------------------------------
print("\n")