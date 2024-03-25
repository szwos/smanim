import PIL
from AnimationLibrary import Canvas, Point, Rect, Animation, Color, Serializer, Path
import copy


# TODO: easing functions dla interpolacji
# RECT_HEIGHT = 30
# RECT_BASE_WIDTH = 40
# RECT_WIDTH_MULTIPLIER = 1.1
# STARTING_POS = 50
# DISTANCE_BETWEEN = 10

canvas = Canvas(100, 100)
print(canvas.get_width())

# rt4 = anim.Rect(anim.Point(STARTING_POS, canvas.get_height() - RECT_HEIGHT),
# anim.Point(RECT_BASE_WIDTH * 4 * RECT_WIDTH_MULTIPLIER, RECT_HEIGHT))
rect = Rect(Point(0, 0), Point(40, 40))


def f(t):
    return Point(t + 50, t + 50)


animation = Animation(20, canvas, Color(25, 25, 100))

path = Path(20)
path.add(Point(0, 0))
path.add(Point(50, 20))

animation.add(rect, path.asTimeFunction)
animation.add(copy.copy(rect), f)

#TODO: nie działa, wyswietla sie tylko pierwsza klatka,
# cos jest zle z interpolacja,
# lub zle z tym jak interpolacja jest wykorzystywana (konkretnie jak funkcja czasu Path'a jest wykrozystywana)
# lub zle z przepisywaniem koordow z interpolacji na pozycje recta


# for frame in animation.getFrames():
#     frame.img.show()


Serializer.save("test.gif", animation)








# tworzysz animacje
# do animacji dodajesz Prymityw jako key oraz lambdę, będącą funkcją Tranforma od czasu dla tego prymitywu
# narazie tą lambde zdefinuj na sztywno, potem stworzysz narzędzie, które pozwala w prosty sposób kreować taką lambdę (nie mam pojęcia w jaki sposób)
# w kazdej klatce animacji forach key w dikcie narysuj to co zwraca key.Draw przeskalowane o dikt[key].Transform


# co tu ma być:
# użytkownik konstruuje sobie wieze hanoi z kwadratow
# uzytkownik definiuje algorytm rozwiazywania wiezy hanoi
# pod czas wykonywania funkcji swap w wiezy hanoi wywolywana jest animacja: jej algorytm:
#   wez jako argumenty klocek A i stos K.
#   jezeli Klocek A.wielkosc > stos K.peak().wielkosc throw exception
#   else utworz sciezke:
#       klocek A tyle w gore az osiagnie wysokosc np 300
#       klocek A tyle w osi x az osiagnie x stosu
#       klocek A tyle w dol az osiagnie wierczh stosu
# uzytkownik definiuje animacje
# uzytkownik uruchamia algorytm hanoi, co dodaje wszystkie sciezki do kolejki animacji
# uzytkownik uruchamia render animacji
# animacja bierze parametry startowe wszystkich obiektow z ich definicji, a nastepnie z kazda kolejna ramka
# zmienia ich wartosci zgodnie ze sciezkami jakie sa przypisane do animacji

# wytyczne sciezek:
# kazdy obiekt moze byc przekazany do animacji tylko poprzez umieszczenie go w sciezce
# (domyslne argumenty beda takie, ze sciazka po prostu nie bedzie opisywala zadnego ruchu)
# animacja dostaje przez referencje obiekt do narysowania ze sciezki a potem na tym obiekcie wywoluje jakies
# draw, ktore zwraca array Colorów, oraz koordynaty, ktore zostana wklejone do finalnego obrazu
# (dzieki temu nie wazne jak skomplikowany bylby ksztalt do narysowania, bedzie on uniformalnie przetwarzany przez
# Animacje - to pozwoli na nieskonczona wolnosc w definiowaniu ksztaltow oraz ich zachowan)
