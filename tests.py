import unittest  # Importa a biblioteca unittest, usada para criar e rodar testes automatizados
from extrair_socios import extract_socios_cotas  # Importa a função que será testada

# Define a classe de teste que herda de unittest.TestCase
class TestExtractSociosCotas(unittest.TestCase):
    """
    Classe de teste para a função 'extract_socios_cotas'.
    Testa se a função extrai corretamente os nomes dos sócios e suas cotas
    a partir de um texto simulado que representa o contrato.
    """

    def test_extract_socios(self):
        """
        Testa se a função 'extract_socios_cotas' retorna corretamente
        os nomes dos sócios e as cotas a partir de um texto simulado.
        """
        # Texto de exemplo que simula o conteúdo de um contrato de partnership
        doc_content = """
        1. João Silva, portador do CPF 123.456.789-00, detentor de 20 cotas.
        2. Maria Souza, portadora do CPF 987.654.321-00, detentora de 15 cotas.
        """
        
        # Valor esperado: a lista de dicionários que a função deve retornar
        expected_output = [
            {"Sócio": "1. João Silva,", "Cotas": 20},  # Sócio 1 com 20 cotas
            {"Sócio": "2. Maria Souza,", "Cotas": 15}  # Sócio 2 com 15 cotas
        ]
        
        # Executa a função 'extract_socios_cotas' com o texto simulado
        result = extract_socios_cotas(doc_content)
        
        # Compara o resultado da função com o valor esperado
        # Se forem iguais, o teste passa; se forem diferentes, o teste falha
        self.assertEqual(result, expected_output)

# Executa os testes quando o arquivo é executado diretamente
if __name__ == '__main__':
    unittest.main()  # Roda os testes e exibe os resultados no terminal
