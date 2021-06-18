# Trie
<!-- GFM-TOC -->
* [Leetcode Trie](#Trie)
    * [1. Introduction to Trie](#1-Introduction-to-Trie)
       * [1.1 How to represent a Trie](#11-How-to-represent-a-Trie)
       * [1.2 Insertion in Trie](#12-Insertion-in-Trie)
       * [1.3 Search in Trie](#13-Search-in-Trie)
       * [1.4 Complexity Analysis](#14-Complexity-Analysis)
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
In the example, the value we mark in each node is the string the node represents. For instance, we start from the root node and choose the second path 'b', then choose the first child 'a', and choose child 'd', finally we arrived at the node "bad". The value of the node is exactly formed by the letters in the path from the root to the node sequentially.\
It is worth noting that the root node is associated with the empty string.\
One important property of Trie is that all the descendants of a node have a common prefix of the string associated with that node. That's why Trie is also called prefix tree.\

## 1.1 How to represent a Trie
### Array
We can use an array to store children nodes. It is really fast to visit a child node. But as not all children nodes are needed, there might be some waste of space.\
```
/ change this value to adapt to different cases
#define N 26

struct TrieNode {
    TrieNode* children[N];
    
    // you might need some extra values according to different cases
};

/** Usage:
 *  Initialization: TrieNode root = new TrieNode();
 *  Return a specific child node with char c: (root->children)[c - 'a']
 */
```
### Hashmap
We can also declare a hashmap in each node. The key of the hashmap are characters and the value is the corresponding child node.\
It is even easier to visit a specific child directly by the corresponding character. But it might be a little slower than using an array.
```
struct TrieNode {
    unordered_map<char, TrieNode*> children;
    
    // you might need some extra values according to different cases
};

/** Usage:
 *  Initialization: TrieNode root = new TrieNode();
 *  Return a specific child node with char c: (root->children)[c]
 */
```

## 1.2 Insertion in Trie
When we insert a target value into a Trie, we will also decide which path to go depending on the target value we insert.\
To be more specific, if we insert a string S into Trie, we start with the root node. We will choose a child or add a new child node depending on S\[0\], the first character in S. Then we go down to the second node and we will make a choice according to S\[1\]. Then we go down to the third node, so on and so for. Finally, we traverse all characters in S sequentially and reach the end. The end node will be the node which represents the string S.\
Let's summarize the strategy using pseudo-code:
```
Initialize: cur = root
for each char c in target string S:
     if cur does not have a child c:
         cur.children[c] = new Trie node
     cur = cur.children[c]
cur is the node which represents the string S
```
Usually, you will need to build the trie by yourself. Building a trie is actually to call the insertion function several times. But remember to initialize a root node before you insert the strings.\

## 1.3 Search in Trie
Searching for a key in a trie has only O(m) time complexity, where m is the key length.
### Search Prefix
Since all the descendants of a node have a common prefix of the string associated with that node, it should be easy to search if there are any words in the trie that starts with the given prefix.\
Similarly, we can go down the tree depending on the given prefix. Once we can not find the child node we want, search fails. Otherwise, search succeeds.\
Let's summarize the strategy using pseudo-code:
```
Initialize: cur = root
for each char c in target string S:
  if cur does not have a child c:
    search fails
  cur = cur.children[c]
search successes
```

### Search Word
You might also want to know how to search for a specific word rather than a prefix. We can treat this word as a prefix and search in the same way we mentioned above.
1. If search fails which means that no words start with the target word, the target word is definitely not in the Trie.
2. If search succeeds, we need to check if the target word is only a prefix of words in Trie or it is exactly a word. To solve this problem, you might want to modify the node structure a little bit.

Hint: A boolean flag in each node might work.


## 1.4 Complexity Analysis
**Time complexity:** O(m), where m is the key length.\
In each iteration of the algorithm, we either examine or create a node in the trie till we reach the end of the key. This takes only mm operations.\

**Space complexity:** O(m).\
In the worst case newly inserted key doesn't share a prefix with the the keys already inserted in the trie. We have to add mm new nodes, which takes us O(m)O(m) space.



















