#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/2 10:46
# @File     : BubbleSortCode.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class TrieNode:
    def __init__(self):
        self.end = 0
        self.path = 0
        self.next_node = {}


class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if word is None:
            return
        node = self.root
        for char in word:
            index = ord(char) - ord("a")
            if not (index in node.next_node):
                node.next_node[index] = TrieNode()
            node = node.next_node.get(index)
            node.path += 1
        node.end += 1

    def search(self, word):
        if word is None:
            return 0
        node = self.root
        for char in word:
            index = ord(char) - ord("a")
            if not (index in node.next_node):
                return 0
            node = node.next_node.get(index)
        return node.end

    def delete(self, word):
        if self.search(word):
            node = self.root
            for char in word:
                index = ord(char) - ord("a")
                if node.next_node[index].path - 1 == 0:
                    node.next_node[index].path -= 1
                    node.next_node[index] = None
                    return
                node = node.next_node.get(index)
            node.end -= 1

    def prefix_number(self, pre):
        if pre is None:
            return 0
        node = self.root
        for char in pre:
            index = ord(char) - ord("a")
            if not (index in node.next_node):
                return 0
            node = node.next_node.get(index)
        return node.path


if __name__ == '__main__':
    trie_tree = TrieTree()
    print(trie_tree.search("alex"))
    trie_tree.insert("alex")
    print(trie_tree.search("alex"))
    trie_tree.delete("alex")
    print(trie_tree.search("alex"))
