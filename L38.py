class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        # Split the string into words
        words = self.text.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join the words back into a string
        return ' '.join(reversed_words)


# Example usage
text = "Hello world this is Python"
reverser = StringReverser(text)
print(reverser.reverse_words())
