class Checking:
    def __init__(self) -> None:
        self.headers = {"User-Agent": ua.random}

    # Check word
    def check_word(self) -> bool:
        if (
            not words.word.startswith(str(words.last_letter))
            and len(words.word_list) > 0
        ):
            print("Слово начинается с не правильной буквы!")
            return False

        last_word = str(self.word_list[-1])
        self.last_letter = (
            last_word[-2]
            if last_word.endswith(("ь", "ы", "ъ"))
            else last_word[-1]
        )

        self.word = input(
            f"{name}, слово на букву '{self.last_letter}': \n"
        ).lower()
        \
