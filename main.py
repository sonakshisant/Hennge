def solve(i):
    print(f"\n--- Test case {i + 1} ---")
    x = int(input("Enter x (how many numbers): "))
    yn = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    if len(ys) != x:
        return -1
    return sum(map(lambda y: y ** 4 * (y <= 0), yn))

def main():
    n = int(input("Enter number of test cases: "))
    results = list(map(solve, range(n)))
    print("\nResults:")
    print(*results, sep="\n")

main()