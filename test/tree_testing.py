from AnimationLibrary.tree.Tree import Tree
from AnimationLibrary.tree.Node import Node

# Do czego będzie potrzebne drzewo w projekcie:
# Pod czas renderowania warto skorzystać z drzewa, żeby zamiast jebać się z rekursją (jak masz np, że w Gridzie jest Canvas i Circle i Grid2 i w Grid2 też coś etc.)
# to po prostu iterować sobie elegancko po drzewku i w odpowiedniej kolejności wywoływać rasteryzacje i wklejać tąrasteryzacje na ekran,
# pozycja wtedy to suma pozycji wszystkich poprzednich elementów w drzewie + pozycja aktualnego (czy coś xD)
#DONE   -   DrawableObject musi trzymać pozycję
#       DrawableTree musi mieć jakąś metode, która zwraca sumę pozycji każdego DrawableObject od roota do podanego DrawableObject (wystarczy iterować parent po praencie aż do roota)
#BARDZO TRUDNOE, TO DO LATER   -   DrawableTree musi mieć jakąś metodę iteracji, odpowiednią na potrzeby renderowania (kolejność zwracanych obiektów musi być zgodna z algoprytmem malarza)
#       -   Jednak musi pozwalać na maskowanie (idk jak, nad tym sie trzeba zastanowić, może prościej narazie to opluć i poprawić później)
#       -   Też warto by było udostępnić jakąś zmienną typu LayerMask, albo DrawLayer, tak, żeby kolejność rysowania mogła być modyfikowana przez użytkownika (co ma być nad czym)
#           Najprościejsza implementacja, to np. Jest n=10 poziomów DrawLayer, za każdym n-poziomem drzewo jest iterowane w całości, ale rysowane są tylko obiekty z
#           z odpowiednim(n-tym) DrawLayer (to sprawia, że renderowanie będzie trwać n razy dłużej :/ )

# żeby grupować rzeczy tak ogółem, warto będzie umożliwić dodanie obiektu po prostu jako dziecko innego obiektu, tak żeby ich pozycje były ze sobą "sprzężone"
# potem też fajnie by było umożliwić dynamiczne rozłączanie i łączenie takich obiektów (ale to juz może być ciutke przejebane XD)
#DONE, ALE DODANIE EVENTU JEST TO CONSIDER   -   w DrawableObject jakiś sposób na określenie parenta w konstruktorze, i w DrawableTree obsłużenie tego (event??)
#       jako dodanie nowego childa z jakimśtam parentem (dodanie w odpowiedni sposob do kontenera basically, z perspektywy konstruktora DrawableObject
#       ta operacja ma być trywialna, w DrawableTree może być to już jakaś metoda, która robi skomplikowane rzeczy,
#       ale jej parametry muszą być mało wymagające bo sąwywoływane w DrawableObject())

# przy mieszaniu kolorow, teraz będzie można określić kolor końcowy jako wypadkową wszystkich kolorów po drodze aż do ROOT DrawableObjecta na określonej pozycji
# (to brzmi troche bardzo rastrowo, upewnij się, że jeśli DrawableObjecty faktycznie będą wektorami tak jak ma być, to to będzie działało tak jak tu jest opisane bo nie ejstem coś pewny)
#DONE   - możliwość otrzymania kolorów wszystkich DrawableObjectów po drodze  na danym pixelu (narazie zrealizuje to przekazując wszystkie DrawableObjecty aż do ROOt'a)

# Warto by było udostępnić użytkownikowi możliwość pobrania parenta aktualnego obiektu (np użytkownik chce zaskryptować funkcjonalność, że jeżeli dany element w gridzie otrzyma sygnał,
# to cały grid powinien zmienić swoje tło na niebieskie (to sie da zrobić inaczej, np z perspektywy użytkownika tworząc manager obiektów w gridzie czy coś, ale no z takim drzewem
# jest prościej i po to ono zostało dodane))
#DONE (parent property)  -   getParent() albo coś w DrawableObject (i np takie Circle to odziedziczy (lub bedzie miało dostepne przez kompozycje jeszcze idk))

# Skoro już mowa o skryptowaniu Drawable objectów, to warto by było wgl umożliwić użytkownikowi przegladanie drzewa
#DONE   -   getChildren()
#SKIP   -   getSubTree()??? - może być przydatne w celu iterowania po wszystkich childrenach danego obiektu - zaimplementuje to jak okaże się potrzebne
#SKIP   -   getSiblings()??? - bez sensu, co za problem sb wywołać getchildren z obj.parent zamiast obj i dostać siblingsów, potem wykluczyć if child != obj


class DrawableTree():
    def __init__(self):
        self._tree = Tree() # todo: create a method for walking the tree and set this to private

    def add(self, obj: 'DrawableObject', parent=None):
        self._tree.add_node(obj, parent)

    def sum_pos_of_ancestors_and_self(self, obj: 'DrawableObject'):
        if obj is None:
            return 0

        return obj.position + self.sum_pos_of_ancestors_and_self(obj.parent)

    def all_ancestors_and_self(self, obj: 'DrawableObject'):
        if obj is None:
            return []

        return [obj] + self.all_ancestors_and_self(obj.parent)

    def children(self, obj: 'DrawableObject'):
        for child_id in obj.front_pointer:
            yield self._tree.get_node(child_id)

class DrawableObject(Node): #TODO: some kind of encapsulation, to not let library users use Node methods (they should use them via DrawableObject's api),

        def __init__(self, position, animation: 'Animation', parent: 'DrawableObject' = None):
            super().__init__()
            #self.parent = parent TODO: should this ref be kept or no?
            #self.path = path # will be used in rendering
            self.position = position
            self.parent = parent

            if animation is None:
                raise ValueError("TODO: add short and concise error message, saying that animation cannot be None idk")

            animation.add(self, parent)





class Circle(DrawableObject):
    def __init__(self, animation: 'Animation', r: float, position: int = 0, parent: DrawableObject = None):
        super().__init__(position, animation, parent)
        self.radius = r
        #self.position = position # will be stored in super class

    def rasterize(self):
        pixels = []

        #rasterization fills pixels array
        pixels.append(1)
        pixels.append(2)
        pixels.append(3)

        return pixels

    def __repr__(self):
        return f"(Circle, radius: {self.radius}, position: {self.position})"
class Animation():
    def __init__(self):

        #self.objects = {} this will become tree now
        self.objects = DrawableTree()

    def add(self, obj: DrawableObject, parent: DrawableObject = None):
        self.objects.add(obj, parent)

    #this is a simplification method, it should access whatever actual rendering process would access, to prove that it works
    def render(self):

        # TODO: walking the tree?

        for obj in self.objects._tree.nodes.values(): # if i'd had walking method in DrawableTree, it's return type would be DrawableObject and i would have typehints
            print(f"pixels: {obj.rasterize()}, position: {obj.position}, sum pos of ancestors: {self.objects.sum_pos_of_ancestors_and_self(obj)}")




anim = Animation()

circle = Circle(anim, 2, 1)
circle_child = Circle(anim, 3.14, 2, circle)
circle_sibling = Circle(anim, 3.14, 5, circle)
circle_grand_child = Circle(anim, 6.28, 69, circle_child)


anim.render()

print(anim.objects.all_ancestors_and_self(circle_grand_child))

for obj in anim.objects.all_ancestors_and_self(circle_grand_child):
    print(obj.rasterize()[2])  # will be obj.rasterize()[2].color[pos_x][pox_y] instead


for obj in anim.objects.children(circle):
    print(obj)

