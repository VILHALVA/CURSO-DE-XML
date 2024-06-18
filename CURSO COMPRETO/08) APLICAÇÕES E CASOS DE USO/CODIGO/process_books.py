import xml.etree.ElementTree as ET

# Função para calcular o preço total dos livros
def calculate_total_price(root):
    total_price = 0.0
    for book in root.findall('book'):
        price = float(book.find('price').text)
        total_price += price
    return total_price

# Função principal para processar o XML
def process_xml(input_file, output_file):
    # Parsing do arquivo XML de entrada
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Calcular o preço total dos livros
    total_price = calculate_total_price(root)

    # Criar novo elemento XML com os resultados
    results = ET.Element('results')
    total_price_elem = ET.SubElement(results, 'totalPrice')
    total_price_elem.text = str(total_price)

    # Criar novo arquivo XML de saída
    result_tree = ET.ElementTree(results)
    result_tree.write(output_file, encoding='utf-8', xml_declaration=True)

    print(f'Arquivo XML de resultados gerado: {output_file}')

if __name__ == "__main__":
    input_file = 'books.xml'
    output_file = 'output.xml'

    process_xml(input_file, output_file)
