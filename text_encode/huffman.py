"""
Huffman coding is commonly used for lossless data compression.
The code length is related to how frequently characters are used. Most frequent characters have the
smallest codes and longer codes for least frequent characters.
Huffman codes are of variable-length, and prefix-free. Any prefix-free binary code can be
visualized as a binary tree with the encoded characters stored at the leaves.
Huffman coding tree or Huffman tree is a full binary tree in which each leaf of the tree
corresponds to a letter in the given alphabet.
"""

import heapq
from collections import Counter, namedtuple

Leaf = namedtuple("Leaf", ["freq", "char"])


class Node:
    """
    Represents a graph node, that will store pairs of characters/Nodes when finding
    two rarest(by frequency) ones.
    """

    def __init__(self, freq, left, right):
        """
        :param in freq: Number, that represents character frequency.
        :param left: Character or another Node instance.
        :param right: Character or another Node instance.
        """
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq <= other.freq

    def __gt__(self, other):
        return self.freq >= other.freq

    def __repr__(self):
        return f"Node(left='{self.left}', right='{self.right}')"


def find_all_leaves(tree, path=""):
    """
    Helper function to recursively traverse graph tree and remember path to the characters.

    :param tree: Huffman binary tree of characters or on of its sub-nodes(leaves).
    :param path: Represents path to the character - it's a sequence of "0"s and "1"s.

    :returns: Tuple of two elements - character and its corresponding code.
    """
    if isinstance(tree, Node):
        yield from find_all_leaves(tree.left, path + "0")
        yield from find_all_leaves(tree.right, path + "1")
    else:
        yield tree, path


def huffman_encode(string):
    """
    Main function to encode provided string using Huffman algorithm.

    :param str string: Any string to encode.

    :returns: Tuple of two elements - encoded string and table for encoding a source symbol.
    """
    chars_frequency = [Leaf(fr, ch) for ch, fr in Counter(string).items()]
    heapq.heapify(chars_frequency)

    while len(chars_frequency) > 1:
        min_elem = heapq.heappop(chars_frequency)
        before_min_elem = heapq.heappop(chars_frequency)
        heapq.heappush(
            chars_frequency,
            Node(
                freq=before_min_elem.freq + min_elem.freq,
                left=before_min_elem,
                right=min_elem,
            ),
        )
    tree = chars_frequency[0]
    chars_table = {leaf.char: path for leaf, path in find_all_leaves(tree)}
    return " ".join(chars_table[c] for c in string), chars_table


# Testing
if __name__ == "__main__":
    string_to_encode = input("Enter string to encode: ")
    encoded_string, chars_table = huffman_encode(string_to_encode)
    print("Encoded string using Huffman algorithm:", encoded_string)
    print(
        "Original string:",
        "".join({v: k for k, v in chars_table.items()}[c] for c in encoded_string.split()),
    )
