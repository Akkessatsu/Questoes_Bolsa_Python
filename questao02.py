import unittest


def verbing(s):
    lastletters = s[-3:]
    if lastletters == "ing":
        return s + "ly"
    elif s == "do":
        return s
    else:
        return s + "ing"


# Dado uma string, procurar a primeira ocorrência da substring 'not' e 'bad'
# Se 'bad' vier após o 'not'
# substituir todo o trecho "not ... bad" por 'good'
# Retorne a string resultante.
def not_bad(s):
    not_position = s.find('not')
    bad_position = s.find('bad')
    if bad_position > not_position:
        return s.replace(s[not_position: bad_position + 3], 'good')
    return s

# Considere dividir uma string em duas metades.
# Se o comprimento for par, a parte da frete (front) e a parte de trás (back) são do mesmo tamanho.
# Se o comprimento for ímpar, o caracter extra irá para a parte da frente.
#
# Dado 2 strings, 'a' e 'b', retornar um string na forma
# a front + b front + a back + b back
def front_back(a, b):
    rest_of_a = len(a) % 2
    rest_of_b = len(b) % 2
    a_mid_point = len(a)//2 + rest_of_a
    b_mid_point = len(b)//2 + rest_of_b
    
    a_front = a[0: a_mid_point]
    a_back = a[a_mid_point: len(a)]
    
    b_front = b[0: b_mid_point]
    b_back = b[b_mid_point: len(b)]
    
    return a_front + b_front + a_back + b_back

class MyTest(unittest.TestCase):

  def test_verbing(self):
    self.assertEqual(verbing('hail'), 'hailing')
    self.assertEqual(verbing('swiming'), 'swimingly')
    self.assertEqual(verbing('do'), 'do')

  def test_not_bad(self):
    self.assertEqual(not_bad('This movie is not so bad'), 'This movie is good')
    self.assertEqual(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot')
    self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")

  def test_front_back(self):
    self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
    self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
    self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  unittest.main()