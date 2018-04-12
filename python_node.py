# -*- coding:utf-8 -*-
# Minimal graph specification
import random
from itertools import combinations

class Node:
    def __init__(self, children=None):
        # 'children' is a dictionary that associates each child
        # to the influence on that child.
        # children = {Node(): 1.1, Node(): 2.2}
        if children is None: children = {}
        self.children = children

    def addchild(self, child):
        self.children.add(child)

    def removechild(self, child):
        self.children.remove(child)

    @property
    def descent(self):
        # Returns a set containing the descent of the node
        # (including the node itself).
        if not self.children: return set()
        descendents = set(self.children)
        for child in self.children:
            descendents.update(child.descent)
        return descendents



class Network:
    def __init__(self, nodes=None):
        self.layers = []
        self.relayer(nodes)

    def relayer(self, nodes=None, regenerate=False):
        if regenerate:
            set([node for node in nodeset for nodeset in self.layers])
        elif nodes is None: nodes = set()
        # Identify the nodes of the top layers from the provided
        # set of nodes.
        son_of_a_bitch = set()
        for node in nodes:
            son_of_a_bitch.update(node.descent)
        current_layer = nodes.difference(son_of_a_bitch)
        # Put the nodes in the appropriate layers.
        while current_layer:
            self.layers.append(current_layer)
            next_layer = set()
            for node in current_layer:
                for child in node.children:
                    next_layer.add(child)
            current_layer = next_layer
        # Cleaning the layers. Nodes can be present on several layers
        # Keep only the lowest appearance of a Node. For this we use
        # the 'difference_update' from the set object, and the
        # 'combination' iterator, which will yield the layers in the
        # order we need them (after reversing).
        for lower_layer, higher_layer in combinations(reversed(self.layers), 2):
            higher_layer.difference_update(lower_layer)

    def fitness(self):
        return None


    # If executed rather than imported we need to pass the arguments.
if __name__ == '__main__':
    x = Node()
    y = Node(set([x]))
    N = Network(set([x,y]))
    print N.layers

