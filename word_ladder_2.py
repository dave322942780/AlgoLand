class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        pre_process = {}
        for word in wordList + [beginWord, endWord]:
            for i in range(len(word)):
                word_pre = word[:i] + '_' + word[i + 1:]
                pre_process.setdefault(word_pre, set())
                pre_process[word_pre].add(word)
        res = []
        visited = {hash(beginWord)}
        bst1 = [[beginWord]]
        bst2 = []
        while not res:
            while bst1:
                path = bst1.pop()
                cur_ending_word = path[-1]
                for i in range(len(cur_ending_word)):
                    word_pre = cur_ending_word[:i] + '_' + cur_ending_word[i + 1:]
                    for adj in pre_process[word_pre]:
                        if hash(adj) not in visited:
                            new_path = path + [adj]
                            if adj == endWord:
                                res.append(new_path)
                            else:
                                visited.add(hash(adj))
                                bst2.append(new_path)
            bst1,bst2 = bst2, bst1
        return res
