def generate_filename(question_title: str, file_ext=".cpp"):
    number_part, _, title_part = question_title.lower().partition(" ")

    question_number = number_part.rstrip(".")
    title_words = title_part.split()

    if not question_number.isdigit() or not title_words:
        raise ValueError(f"Expected '<number>. <title>, get: {question_title!r}")

    return question_number + "_" + "-".join(title_words) + file_ext


def main(bills: list[int]):
    fiveBills = tenBills = 0

    for bill in bills:
        if bill == 5:
            fiveBills += 1
        elif bill == 10:
            if fiveBills <= 0:
                return False
            tenBills += 1
            fiveBills -= 1
        elif bill == 20:
            if fiveBills >= 1 and tenBills >= 1:
                fiveBills -= 1
                tenBills -= 1
            elif fiveBills >= 3:
                fiveBills -= 3
            else:
                return False
    return True


if __name__ == "__main__":
    print("Is change possible: ", main([5, 5, 5, 10, 20]))
    print("Is change possible: ", main([5, 5, 10, 10, 20]))
    print("Is change possible: ", main([5, 5, 5, 5, 10, 5, 10, 10, 10, 20]))
