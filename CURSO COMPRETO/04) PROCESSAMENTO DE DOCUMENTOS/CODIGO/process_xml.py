import lxml.etree as ET

def transform_xml(xml_file, xslt_file, output_file):
    # Carrega o arquivo XSLT
    xslt = ET.parse(xslt_file)
    transform = ET.XSLT(xslt)

    # Carrega o arquivo XML
    xml = ET.parse(xml_file)

    # Aplica a transformação
    result = transform(xml)

    # Salva o resultado em um arquivo HTML
    with open(output_file, 'wb') as f:
        f.write(result)

if __name__ == "__main__":
    xml_file = 'documents.xml'
    xslt_file = 'transform.xslt'
    output_file = 'output.html'

    transform_xml(xml_file, xslt_file, output_file)
    print(f'Arquivo HTML gerado com sucesso: {output_file}')
