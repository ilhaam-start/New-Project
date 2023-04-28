class GrammarStats:
    def __init__(self):
        self.text_checked = 0 #Initialzed this
        self.checks_passed = 0 #Initialzed this

    def check(self, text):
        if text == "":
            raise Exception("There is no text, cannot check grammar.")
        self.text_checked += 1 #Adds one to the count of text checked
        if text[0].isupper() and text[-1] in ".!?":
            self.checks_passed += 1 #Adds one to the count of text which passed
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
            return int((self.checks_passed / self.text_checked) * 100) #multiply by 100 to turn into percentage