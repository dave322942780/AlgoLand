# https://leetcode.com/problems/text-justification/description/

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        word_queue = []
        line_char_count = 0
        res = []

        def join_words(word_queue, sentence_count):
            if len(word_queue) == 1:
                return word_queue[0] + (" " * (maxWidth - len(word_queue[0])))
            overflow_spaces = maxWidth - sentence_count
            space_count = (len(word_queue) - 1)
            overflow = overflow_spaces % space_count
            avg_spaces = overflow_spaces / space_count
            average_spaces_str = " " * avg_spaces
            overflow_spaces_str = average_spaces_str + " "
            for i in range(1, len(word_queue)):
                spaces = overflow_spaces_str if overflow > 0 else average_spaces_str
                word_queue[i] = spaces + word_queue[i]
                overflow -= 1
            return "".join(word_queue)

        for idx, word in enumerate(words):
            if len(res) == 0 and not word_queue:
                line_char_count = len(word)
                word_queue.append(word)
            else:
                new_count = line_char_count + len(word) + 1
                if new_count <= maxWidth:
                    line_char_count = new_count
                    word_queue.append(' ' + word)
                else:
                    res.append(join_words(word_queue, line_char_count))

                    word_queue = [word]
                    line_char_count = len(word)
        if word_queue:
            res.append(join_words([''.join(word_queue)], line_char_count))
        return res