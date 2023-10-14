# XPATH E XSLT
Vamos explorar XPath e XSLT, duas tecnologias fundamentais para navegar e transformar documentos XML:

1. **XPath para Navegação em Documentos XML**:

   - **XPath** é uma linguagem que permite selecionar elementos e atributos específicos em documentos XML, facilitando a navegação e extração de dados de documentos XML. É frequentemente usado em combinação com linguagens de programação e bibliotecas para acessar informações em documentos XML.

   - Com XPath, você pode criar expressões que descrevem os elementos que deseja selecionar com base em sua localização na árvore do documento XML. As expressões XPath são usadas em várias linguagens de programação, como Python, Java e JavaScript, para consultar e manipular documentos XML.

   Exemplo de expressão XPath:

   Considere o seguinte documento XML:

   ```xml
   <pessoas>
      <pessoa>
         <nome>João</nome>
         <idade>30</idade>
      </pessoa>
      <pessoa>
         <nome>Maria</nome>
         <idade>25</idade>
      </pessoa>
   </pessoas>
   ```

   Para selecionar todos os elementos `<nome>` dentro de `<pessoa>`, a expressão XPath seria: `/pessoas/pessoa/nome`

2. **Transformação de XML usando XSLT (Extensible Stylesheet Language Transformations)**:

   - **XSLT** é uma linguagem usada para transformar documentos XML em outros formatos, como HTML, XML ou texto. Ele é frequentemente usado para converter documentos XML em páginas da web com aparência específica ou para extrair dados de documentos XML e aplicar transformações.

   - Um documento XSLT contém regras e templates que descrevem como a transformação deve ocorrer. Essas regras são aplicadas ao documento XML de origem para criar o documento de saída transformado.

   Exemplo de um arquivo XSLT simples que transforma um documento XML em HTML:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
      <xsl:template match="/">
         <html>
            <body>
               <h1>Lista de Pessoas</h1>
               <ul>
                  <xsl:for-each select="pessoas/pessoa">
                     <li>
                        <xsl:value-of select="nome"/> - <xsl:value-of select="idade"/> anos
                     </li>
                  </xsl:for-each>
               </ul>
            </body>
         </html>
      </xsl:template>
   </xsl:stylesheet>
   ```

   Quando aplicado a um documento XML, o XSLT geraria uma página HTML com a lista de pessoas.

No geral, XPath é usado para navegar e selecionar dados em documentos XML, enquanto o XSLT é usado para transformar documentos XML em outros formatos, aplicando regras de transformação definidas em um documento XSLT separado. Ambas as tecnologias são fundamentais para o processamento avançado de XML.