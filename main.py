def main():
    print("Enter scores separated by spaces:")
    user_input = input().strip()

    scores = list(map(float, user_input.split()))

    total = sum(scores)
    average = total / len(scores)
    max_score = max(scores)
    min_score = min(scores)

    print(f"Sum of scores: {total}")
    print(f"Average of scores: {average:.2f}")
    print(f"Maximum score: {max_score}")
    print(f"Minimum score: {min_score}")

if __name__ == "__main__":
    main()
