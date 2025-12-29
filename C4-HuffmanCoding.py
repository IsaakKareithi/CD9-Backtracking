import heapq

class node:
    
    def __init__(self, freq, symbol, left=None, right=None):
        #Frequency of symbol
        self.freq = freq

        # symbol name(character)
        self.symbol = symbol

        # node left and right of current node
        self.left = left
        self.right = right

        #Tree direction(0/1)
        self.huff = ' '

        def __lt__(self, nxt):
            return self.freq < nxt.freq
    
# Utility function to print huffman codes
# for all symbols in the newly creates Huffman Trees
def printNodes(node, val=' '):
        # Huffman code for current node
        newVal = val + str(node.huff)

        # if node is not an edge node,
        # then traverse inside it
        if (node.left):
            printNodes(node.left, newVal)
        if (node.right):
            printNodes(node.right, newVal)

        # if node is an edge node,
        #display the huffman code
        if (not node.left and not node.right):
            print(f"{node.symbol} --> {newVal}")
        
# Characters for huffman code
chars = ['a','b','c','d','e','f']

# frequency of characters
freq = [5, 9, 12, 13, 16, 45]

# List containing unused nodes
nodes = []

# converting characters an frequencies 
# into huffman tree nodes
for x in range(len(chars)):
    heapq.heappush(nodes, node(freq[x], chars[x]))

while len(nodes) > 1:

    # Sort all nodes in ascending order
    # based on their frequencies
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    # assign directional values to these nodes
    left.huff = 0
    right.huff = 1

    # combine the 2 smallest nodes to create
    # new nodes as their parent
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

    heapq.heappush(nodes, newNode)

# huffman tree is ready!
printNodes(nodes[0])