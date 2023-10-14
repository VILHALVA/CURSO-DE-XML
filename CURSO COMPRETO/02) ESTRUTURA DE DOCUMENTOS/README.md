# ESTRUTURA DE DOCUMENTOS
1. **Declaração XML**:
   
   A declaração XML é uma parte opcional, mas frequentemente usada, que aparece no início de um documento XML. Ela fornece informações sobre a versão do XML usada e a codificação de caracteres do documento. A declaração XML é escrita no seguinte formato:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   ```

   - `<?xml`: Indica o início da declaração XML.
   - `version="1.0"`: Especifica a versão do XML utilizada no documento.
   - `encoding="UTF-8"`: Define a codificação de caracteres, que indica como os caracteres especiais são codificados no documento. UTF-8 é amplamente utilizado e suporta uma ampla gama de caracteres.

2. **Elementos e Aninhamento**:

   Elementos são os blocos de construção fundamentais do XML. Eles representam dados ou estruturas no documento. Os elementos são delimitados por tags, como `<elemento>` e `</elemento>`. Os elementos podem conter outros elementos, formando uma estrutura hierárquica. Por exemplo:

   ```xml
   <pessoa>
      <nome>João</nome>
      <idade>30</idade>
   </pessoa>
   ```

   Neste exemplo, "pessoa" é um elemento pai que contém dois elementos filhos, "nome" e "idade".

3. **Atributos**:

   Os atributos são informações adicionais associadas a elementos e são definidos dentro das tags dos elementos. Eles têm um nome e um valor. Por exemplo:

   ```xml
   <livro categoria="romance">Orgulho e Preconceito</livro>
   ```

   Aqui, "categoria" é um atributo do elemento "livro" com o valor "romance".

4. **Comentários**:

   Comentários em XML são usados para adicionar notas ou informações que não devem ser processadas pelo sistema que lê o XML. Comentários são escritos entre `<!--` e `-->`. Por exemplo:

   ```xml
   <!-- Este é um comentário XML -->
   <exemplo>Conteúdo do elemento</exemplo>
   ```

   Os comentários são úteis para documentação ou anotações dentro do XML.

5. **Entidades Especiais**:

   Entidades especiais em XML são usadas para representar caracteres que têm significados especiais na marcação. Por exemplo, o caractere `<` é usado para iniciar um elemento, mas se você deseja usá-lo como parte do conteúdo de um elemento, você deve usar a entidade `&lt;` para representá-lo.

   Algumas entidades especiais comuns incluem:
   - `&lt;` para `<`
   - `&gt;` para `>`
   - `&amp;` para `&`
   - `&quot;` para `"`
   - `&apos;` para `'`

   Por exemplo:

   ```xml
   <texto>Este é um exemplo de entidade especial: &lt;dados&gt;</texto>
   ```

   O resultado será: "Este é um exemplo de entidade especial: <dados>"

Espero que esta explicação tenha ajudado a esclarecer a estrutura de documentos XML e os elementos que a compõem. 