# Trie
<!-- GFM-TOC -->
* [Leetcode Trie](#Trie)
    * [1. Introduction to Trie](#1-Introduction-to-Trie)
<!-- GFM-TOC -->


# 1. Introduction to Trie
A Trie is a special form of a Nary tree. Typically, a trie is used to store strings. Each Trie node represents a string (a prefix). Each node might have several children nodes while the paths to different children nodes represent different characters. And the strings the child nodes represent will be the origin string represented by the node itself plus the character on the path.\
```
                      [ ]
             /         |         \    
            a          b          s
            |       /     \       |
            m      a       e      o
                   |
                   d
```


