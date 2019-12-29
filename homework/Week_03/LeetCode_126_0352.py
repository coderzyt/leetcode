from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or len(wordList) == 0:
            return 0
        if endWord not in wordList:
            return 0
