class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        word_nums = self.preprocess(sentence, cols)
        word_count = 0
        for _ in xrange(rows):
            word_count += word_nums[word_count % len(sentence)]
        return word_count / len(sentence)

    # Preprocessing
    def preprocess(self, sentence, cols):
        word_nums = [0] * len(sentence)
        word_ptr, word_sum = 0, 0
        word_len = len(sentence[0])
        for i, word in enumerate(sentence):
            while (word_sum + word_len <= cols):
                word_sum += word_len
                word_ptr += 1
                word_len = len(sentence[word_ptr % len(sentence)]) + 1
            word_nums[i] = word_ptr - i
            word_sum -= (len(word) + 1)
        return word_nums