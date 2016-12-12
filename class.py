class TestTaking:
    def findMax(self, questions, guessed, actual):
        guessedfalse = questions - guessed
        actualfalse = questions - actual
        result1 = 0
        result2 = 0
        while guessed > 0 and actual > result1:
            result1 += 1
            guessed -= 1
        while guessedfalse > 0 and actualfalse > result2:
            result2 += 1
            guessedfalse -= 1

        return result1+result2
