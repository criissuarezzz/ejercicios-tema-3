import polinomio.polinomio as polinomio
import unittest
import sarrus.sarrus as sarrus
import torrehanoi

class testdatabase(unittest.TestCase):
    def test_polinomio(self):
        pol1 = polinomio.Polinomio()
        pol2 = polinomio.Polinomio()
        polinomio.Polinomio.agregar_termino(pol1, 2, 3)
        polinomio.Polinomio.agregar_termino(pol1, 1, 2)
        polinomio.Polinomio.agregar_termino(pol1, 0, 1)
        polinomio.Polinomio.agregar_termino(pol2, 2, 1)
        polinomio.Polinomio.agregar_termino(pol2, 1, 1)
        polinomio.Polinomio.agregar_termino(pol2, 0, 1)
        pol3 = polinomio.Polinomio.sumar_polinomios(pol1, pol2)
        pol4 = polinomio.Polinomio.restar_polinomios(pol1, pol2)
        pol5 = polinomio.Polinomio.multiplicar_polinomios(pol1, pol2)
        pol6, pol7 = polinomio.Polinomio.dividir_polinomios(pol1, pol2)
        self.assertEqual(polinomio.Polinomio.evaluar_polinomio(pol3, 1), 7)
        self.assertEqual(polinomio.Polinomio.evaluar_polinomio(pol4, 1), 1)
        self.assertEqual(polinomio.Polinomio.evaluar_polinomio(pol5, 1), 6)
        self.assertEqual(polinomio.Polinomio.evaluar_polinomio(pol6, 1), 3)
        self.assertEqual(polinomio.Polinomio.evaluar_polinomio(pol7, 1), 0)
    def test_sarrus(self):
        matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(sarrus.Sarrus.calcular_determinante(matriz), 0)
    def test_torrehanoi(self):
        torrehanoi.TorreHanoi.resolver_torrehanoi(3, 1, 2, 3)

if __name__ == '__main__':
    unittest.main()

