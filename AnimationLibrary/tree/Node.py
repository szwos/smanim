"""based on https://github.com/guotsuan/pyTree/"""
import uuid

# TODO: pretty much everything that will be implemented here after re implementing tree class should be delegated to some more container specific (Node) class (so thatDrawableObject, that will be used in e.g. rendering won't have for example update_fpointer() method available, which is very tree-container specific)

class Node(object):

    # TODO: i much dislike this flag-like logic
    (ADD, DELETE, INSERT) = range(3)
    def __init__(self, expanded= True):
        #self.tag removed
        #self._identifier -> self._uuid
        self._uuid = uuid.UUID()
        self.expanded = expanded
        #self._bpointer -> self._back_pointer
        self._back_pointer = None
        #self._fpointer -> self._front_pointer
        self._front_pointer = []


    @property
    def uuid(self):
        return self._uuid

    @property
    def back_pointer(self):
        return self._back_pointer

    @back_pointer.setter
    def back_pointer(self, value):
        if value is not None:
            self._back_pointer = value

    @property
    def front_pointer(self):
        return self._front_pointer

    @front_pointer.setter
    def front_pointer(self, value):
        if value is not None and isinstance(value, list):
            self.front_pointer = value

    def update_front_pointer(self, identifier, mode=ADD):
        if mode is self.ADD:
            self._front_pointer.append(identifier)
        elif mode is self.DELETE:
            self._front_pointer.remove(identifier)
        elif mode is self.INSERT:
            self._front_pointer = [identifier] # weird one, i don't get it