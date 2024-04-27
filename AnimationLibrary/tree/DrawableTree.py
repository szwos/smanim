from AnimationLibrary.tree.Tree import Tree
from AnimationLibrary.drawable.DrawableObject import DrawableObject

# TODO: tree walking algorithm
class DrawableTree:
    def __init__(self):
        self._tree = Tree()

    def add(self, obj: DrawableObject, parent = None):
        self._tree.add_node(obj, parent)

    def positions_to_root(self, obj: DrawableObject):
        if obj is None:
            return 0

        return obj.position + self.positions_to_root(obj.parent)

    def ancestors_to_root(self, obj: DrawableObject):
        if obj is None:
            return []

        return [obj] + self.ancestors_to_root(obj.parent)

    def children(self, obj: DrawableObject):
        for child_id in obj.front_pointer:
            yield self._tree.get_node(child_id)