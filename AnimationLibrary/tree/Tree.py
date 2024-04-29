"""
based on https://github.com/guotsuan/pyTree/ - implemented for python 2.7
code ported to python 3, docs copied as is
"""

import uuid
from collections import deque

from AnimationLibrary.tree.Node import Node

class MultipleRootError(Exception):
    pass

class DuplicatedNodeIdError(Exception):
    pass

#name changes from https://github.com/guotsuan/pyTree/ (bo zapomne i sie pogubie xd)
# nid -> node_id

# TODO: rename to DrawableObjectTree, bcs this tree itself is not Drawable and it sounds like it
class Tree():

    (ROOT, DEPTH, WIDTH) = range(3) # TODO: i don't like this, seems elegant but also kind of weird

    def __init__(self):
        self.nodes = {}
        self.root = None

    def add_node(self, node: Node, parent=None):
        """
        Add a new node to tree.
        The 'node' parameter refers to an instance of Class::Node
        """
        if node.uuid in self.nodes:
            raise DuplicatedNodeIdError(f"Can't create node with ID {node.uuid}")

        if parent is None:
            if self.root is not None:
                raise MultipleRootError
            else:
                self.root = node.uuid

        self.nodes.update({node.uuid: node})
        self._update_front_pointer(parent, node.uuid, Node.ADD)
        node.back_pointer = parent

    def create_node(self, parent=None):
        """
        Create a child node for the node indicated by the 'parent' parameter
        """
        node = Node()
        self.add_node(node, parent)
        return node

    def expand_tree(self, node_id=None, mode=DEPTH, filter=None, key=None, reverse=False):
        """
        Python generator. Loosly based on an algorithm from 'Essential LISP' by
        John R. Anderson, Albert T. Corbett, and Brian J. Reiser, page 239-241
        UPDATE: the @filter function is perform on Node object.
        UPDATE: the @cmp @key @reverse is present to sort node at each level.
        UPDATE: it
        """
        node_id = self.root if (node_id is None) else uuid.uuid1()
        filter = (lambda x: True) if (filter is None) else filter

        if filter(self[node_id]):
            yield node_id
            queue = [self[i] for i in self[node_id]._front_pointer if filter(self[i])]
            queue.sort(key=key, reverse=reverse)
            while queue:
                yield queue[0].uuid
                expansion = [self[i] for i in queue[0]._front_pointer if filter(self[i])]
                expansion.sort(key=key, reverse=reverse)
                if mode is self.DEPTH:
                    queue = expansion + queue[1:]
                elif mode is self.WIDTH:
                    queue = queue[1:] + expansion

    def get_node(self, node_id):
        """
        Return the node with nid.
        None returned if nid not exists.
        """
        if node_id is not None:
            try:
                node = self.nodes[node_id] # TODO isn't self[node_id] the same? check under debug and change for cohesion
            except KeyError:
                node = None
            return node

    # TODO: why is this called is_branch() instead of get_front_pointer()?
    def is_branch(self, node_id):
        """
        Return the following nodes of nid.
        Empty list returned if nid not exists
        """
        if node_id is not None:
            try:
                front_pointer = self[node_id]._front_pointer
            except KeyError:
                front_pointer = []
            return front_pointer

    def move_node(self, source, destination):
        """
        Move a node indicated by the 'source' parameter to the parent node
        indicated by the 'dest' parameter
        """
        parent = self[source].back_pointer
        self._update_front_pointer(parent, source, Node.DELETE)
        self._update_front_pointer(destination, source, Node.ADD)
        self._update_back_pointer(source, destination)


    def paste(self, node_id, new_tree: 'Tree'):
        """
        Paste a new tree to the original one by linking the root
        of new tree to nid.
        """
        assert isinstance(new_tree, Tree)

        if node_id is None:
            raise OSError("First parameter can't be None")

        set_joint = set(new_tree.nodes) & set(self.nodes)
        if set_joint:
            raise ValueError(f'Duplicated nodes {list(set_joint)} exists.')

        new_tree[new_tree.root].back_pointer = node_id
        self._update_front_pointer(node_id, new_tree.root, Node.ADD)
        self.nodes.update(new_tree.nodes)

    def remove_node(self, identifier):
        """
        Remove a node indicated by 'identifier'. All the successors are removed, too.
        """
        if identifier is None:
            return

        parent = self[identifier].back_pointer
        remove = []
        for id in self.expand_tree(identifier):
            #comment from pyTree
            # TODO: implementing this function as a recursive function:
            #       check if node has children
            #       true -> run remove_node with child_id
            #       no -> delete node
            remove.append(id)

            for id in remove:
                del(self.nodes[id])

            self._update_front_pointer(parent, identifier, Node.DELETE)

    def rsearch(self, node_id, filter=None):
        """
        Search the tree from nid to the root along links reversedly.
        """
        if node_id is None:
            return
        filter = (lambda x: True) if (filter is None) else filter

        current = node_id
        while current is not None:
            if filter(self[current]):
                yield current
            current = self[current].back_pointer

    def to_string(self, node_id=None, level=ROOT, filter=None, key=None, reverse=False, result: str = "") -> str:
        """
        UPDATE(szwos): string of tree is now generated in to_string() and used in save2file() and show()
        """

        leading = ''
        lasting = '|___'

        node_id = self.root if (node_id is None) else node_id
        label = f"{self[node_id].uuid}"
        filter = (lambda x: True) if (filter is None) else filter

        if level == self.ROOT:
            return f"{label}\n"
        else:
            if level <= 1:
                leading += ('|' + ' ' * 4) * (level - 1)
            else:
                leading += ('|' + ' ' * 4) + (' ' * 5 * (level - 2))
            result = f"{result}{leading}{lasting}{label}\n"

        if filter(self[node_id]) and self[node_id].expanded:
            queue = [self[i] for i in self[node_id].front_pointer if filter([self[i]])]
            key = (lambda x: x) if (key is None) else key
            queue.sort(key=key, reverse=reverse)
            level += 1
            for element in queue:
                return self.to_string(element.uuid, level, filter, key, reverse, result)



    def save2file(self, filename, node_id=None, level=ROOT, filter=None, key=None, reverse=False):
        """
        Update 20/05/13: Save tree into file for offline analysis
        """
        open(filename, 'w').write(self.to_string(node_id, level, filter, key, reverse))

    def show(self, node_id=None, level=ROOT, filter=None, key=None, reverse=False):
        """
        Another implementation of printing tree using Stack
        Print tree structure in hierarchy style.
        For example:
            Root
            |___ C01
            |	 |___ C11
            |		  |___ C111
            |		  |___ C112
            |___ C02
            |___ C03
            |	 |___ C31
        A more elegant way to achieve this function using Stack structure,
        for constructing the Nodes Stack push and pop nodes with additional level info.
        UPDATE: the @cmp @key @reverse is present to sort node at each level.
        """
        print(self.to_string(node_id, level, filter, key, reverse))

    def subtree(self, node_id):
        st = Tree()
        if node_id is None:
            return st
        st.root = node_id
        for node_n in self.expand_tree(node_id):
            st.nodes.update({self[node_n].uuid: self[node_n]})
        return st

    #TODO: better name
    #TODO: typehint root to UUID object
    def traverse(self, root = None):

        if root == None:
            root = self.root

        stack = deque([])
        preorder = []
        preorder.append(self.root)
        stack.append(root)

        while len(stack) > 0:

            were_all_child_nodes_visited = 0

            if len(stack[len(stack) - 1].front_pointer) == 0:
                x = stack.pop()
            else:
                parent = stack[len(stack) - 1]

            for i in range(0, len(parent.front_pointer)):
                if parent.front_pointer[i] not in preorder:
                    were_all_child_nodes_visited = 1

                    children = []
                    for child_uuid in parent.front_pointer:
                        children.append(self[child_uuid])

                    stack.append(children[i])
                    preorder.append(children[i].uuid)

                    break

            if were_all_child_nodes_visited == 0:
                stack.pop()

        return preorder

    def __contains__(self, uuid):
        return [node.uuid for node in self.nodes if node.uuid is uuid]

    def __getitem__(self, key) -> Node:
        return self.nodes[key]

    def __len__(self):
        return len(self.nodes)

    def __setitem__(self, key, item):
        self.nodes.update({key: item})

    def _update_back_pointer(self, node_id, identifier):
        self[node_id].back_pointer = identifier

    def _update_front_pointer(self, owner_id, target_id, mode):
        if owner_id is None:
            return
        else:
            self[owner_id.uuid].update_front_pointer(target_id, mode)
