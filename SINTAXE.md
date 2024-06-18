# SINTAXE
XML utiliza tags para estruturar e organizar dados de maneira hierárquica e semântica. Cada tag define um elemento que pode conter dados ou outros elementos aninhados. Aqui estão as principais tags do XML com exemplos e explicações:

## 1. TAG DE DECLARAÇÃO XML:
A declaração XML define a versão do XML utilizada no documento e opcionalmente a codificação de caracteres.

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

- `<?xml version="1.0" encoding="UTF-8"?>`: Declara que o documento XML está na versão 1.0 e usa a codificação UTF-8 para caracteres.

## 2. ELEMENTOS:
Os elementos são os blocos básicos de construção do XML. Eles são delimitados por tags de abertura (`<tag>`) e tags de fechamento (`</tag>`).

```xml
<book>
    <title>Harry Potter and the Philosopher's Stone</title>
    <author>J.K. Rowling</author>
    <genre>Fantasy</genre>
    <price>10.99</price>
</book>
```

- `<book>` e `</book>`: Definem o elemento `book`, que contém informações sobre um livro, como título, autor, gênero e preço.

## 3. ATRIBUTOS:
Atributos são informações adicionais associadas a elementos que fornecem detalhes específicos sobre o elemento.

```xml
<book category="fiction">
    <title>Harry Potter and the Philosopher's Stone</title>
    <author>J.K. Rowling</author>
    <year>1997</year>
    <price>10.99</price>
</book>
```

- `category="fiction"`: Atributo `category` do elemento `book`, que especifica a categoria do livro como "fiction".

## 4. TEXTO:
Texto é o conteúdo dentro dos elementos XML que não é parte de uma tag. No exemplo abaixo, "Harry Potter and the Philosopher's Stone" é o texto dentro do elemento `<title>`.

```xml
<title>Harry Potter and the Philosopher's Stone</title>
```

- `Harry Potter and the Philosopher's Stone`: Texto dentro do elemento `<title>`, que é o título do livro.

## 5. COMENTÁRIOS:
Comentários são usados para adicionar anotações no código XML que não são processadas pelo parser XML.

```xml
<!-- Este é um comentário XML -->
```

- `<!-- Este é um comentário XML -->`: Um comentário que fornece uma explicação ou nota sobre o conteúdo XML.

## 6. ELEMENTOS VAZIOS:
Elementos vazios são aqueles que não têm conteúdo e fechamento explícito. Eles são representados usando a sintaxe `<tag/>`.

```xml
<emptyElement/>
```

- `<emptyElement/>`: Um elemento vazio sem conteúdo.

## 7. NAMESPACE:
Namespaces são usados para evitar conflitos de nome entre elementos XML de diferentes fontes.

```xml
<book xmlns="http://example.com/books">
    <title>Harry Potter and the Philosopher's Stone</title>
    <author>J.K. Rowling</author>
    <genre>Fantasy</genre>
    <price>10.99</price>
</book>
```

- `xmlns="http://example.com/books"`: Define o namespace padrão para o elemento `book`, garantindo que ele seja único dentro do contexto especificado.

## 8. DOCUMENT TYPE DECLARATION (DTD) E XML SCHEMA:
Document Type Declaration (DTD) e XML Schema são usados para definir a estrutura e validar documentos XML contra regras específicas.

```xml
<!DOCTYPE library SYSTEM "books.dtd">
```

- `<!DOCTYPE library SYSTEM "books.dtd">`: Declaração que referencia um arquivo DTD chamado `books.dtd`, que define a estrutura esperada para o documento XML.

Estas são as principais tags e conceitos utilizados em XML para estruturar e organizar dados de forma eficiente e legível. Cada um desses elementos desempenha um papel crucial na definição e manipulação de documentos XML em diferentes contextos e aplicações.