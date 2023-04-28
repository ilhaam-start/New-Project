class GrammarStats:
    def __init__(self):
        self.text_checked = 0
        self.checks_passed = 0

    def check(self, text):
        if text == "":
            raise Exception("There is no text, cannot check grammar.")
        self.text_checked += 1
        if text[0].isupper() and text[-1] in ".!?":
            self.checks_passed += 1
            return True
        else:
            return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.text_checked == 0:
            return 0
        else:
            return int((self.checks_passed / self.text_checked) * 100)