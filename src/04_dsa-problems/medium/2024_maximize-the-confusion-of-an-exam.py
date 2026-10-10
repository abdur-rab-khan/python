def max_consecutive_answer(answer_key: str, k: int):
    key_count = [0] * 2
    max_consecutive: int = 0

    left_idx = 0
    for right_idx, ans in enumerate(answer_key):
        key_count[0 if ans == "T" else 1] += 1
        max_freq = max(key_count[0], key_count[1])

        while (right_idx - left_idx + 1) - max_freq > k:
            key_count[0 if answer_key[left_idx] == "T" else 1] -= 1
            left_idx += 1

        max_consecutive = max(max_consecutive, (right_idx - left_idx) + 1)

    return max_consecutive


if __name__ == "__main__":
    print(max_consecutive_answer("TFFT", 1))
    print(max_consecutive_answer("TTFF", 2))
    print(max_consecutive_answer("TTFTTFTT", 1))
