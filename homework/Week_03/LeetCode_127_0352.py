from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or len(wordList) == 0:
            return 0
        if endWord not in wordList or not beginWord or not endWord:
            return 0
        length = len(beginWord)
        dict = defaultdict(list)
        for word in wordList:
            for i in range(length):
                dict[word[:i] + "*" + word[i+1:]].append(word)
        queue = [(beginWord, 1)]
        visitedWords = {beginWord: True}
        while queue:
            currentWord, level = queue.pop()
            for i in range(length):
                nextWord = currentWord[:i] + "*" + currentWord[i+1:]
                for word in dict[nextWord]:
                    if word == endWord:
                        return level + 1
                    if word not in visitedWords:
                        visitedWords[word] = True
                        queue.append((word, level + 1))

                dict[currentWord] == []
        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.ladderLength("hit", "cog", ["hit","hot","dot","dog","lot","log"]))

