import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()

    def test_dever_adiciona_dois_numeros(self):
        # Teste de adição de números positivos
        self.assertEqual(self.calculadora.adicao(5, 3), 8)
        # Teste de adição de números negativos
        self.assertEqual(self.calculadora.adicao(-2, 2), 0)
        # Teste de adição com um número zero
        self.assertEqual(self.calculadora.adicao(0, 0), 0)
        # Teste de adição de número positivo e negativo
        self.assertEqual(self.calculadora.adicao(5, -3), 2)

    def test_subtracao(self):
        # Teste de subtração de números positivos
        self.assertEqual(self.calculadora.subtracao(5, 3), 2)
        # Teste de subtração de números negativos
        self.assertEqual(self.calculadora.subtracao(-2, -3), 1)
        # Teste de subtração com um número zero
        self.assertEqual(self.calculadora.subtracao(0, 0), 0)
        # Teste de subtração de número negativo de número positivo
        self.assertEqual(self.calculadora.subtracao(5, -3), 8)

    def test_multiplicacao(self):
        # Teste de multiplicação de números positivos
        self.assertEqual(self.calculadora.multiplicacao(5, 3), 15)
        # Teste de multiplicação de números negativos
        self.assertEqual(self.calculadora.multiplicacao(-2, -3), 6)
        # Teste de multiplicação por zero
        self.assertEqual(self.calculadora.multiplicacao(5, 0), 0)
        # Teste de multiplicação por um
        self.assertEqual(self.calculadora.multiplicacao(5, 1), 5)

    def test_divisao(self):
        # Teste de divisão de números positivos
        self.assertEqual(self.calculadora.divisao(6, 3), 2)
        # Teste de divisão de números negativos
        self.assertEqual(self.calculadora.divisao(-6, -3), 2)
        # Teste de divisão por zero
        self.assertEqual(self.calculadora.divisao(5, 0), "ERRO: Não é possível dividir por zero.")
        # Teste de divisão de zero por número positivo
        self.assertEqual(self.calculadora.divisao(0, 5), 0)
        # Teste de divisão de número positivo por zero
        self.assertEqual(self.calculadora.divisao(5, 0), "ERRO: Não é possível dividir por zero.")
        # Teste de precisão em divisão de números reais
        self.assertAlmostEqual(self.calculadora.divisao(1, 3), 0.3333333333333333)

    def test_calcular(self):
        # Teste de adição
        self.assertEqual(self.calculadora.calcular("+", 5, 3), 8)
        # Teste de subtração
        self.assertEqual(self.calculadora.calcular("-", 5, 3), 2)
        # Teste de multiplicação
        self.assertEqual(self.calculadora.calcular("*", 5, 3), 15)
        # Teste de divisão
        self.assertEqual(self.calculadora.calcular("/", 6, 3), 2)
        # Teste de divisão por zero
        self.assertEqual(self.calculadora.calcular("/", 5, 0), "ERRO: Não é possível dividir por zero.")
        # Teste de operação inválida
        self.assertEqual(self.calculadora.calcular("?", 5, 3), "ERRO: Operação inválida. Por favor, escolha +, -, * ou /.")
        # Teste de entrada inválida
        self.assertEqual(self.calculadora.calcular("+", "a", 3), "ERRO: Entrada inválida. Certifique-se de digitar números válidos.")

if __name__ == '__main__':
    unittest.main()