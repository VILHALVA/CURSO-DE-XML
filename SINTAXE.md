# SINTAXE
Abaixo está um exemplo simples de um documento XML que descreve informações sobre livros:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<library>
    <book>
        <title>Harry Potter and the Philosopher's Stone</title>
        <author>J.K. Rowling</author>
        <genre>Fantasy</genre>
        <year>1997</year>
        <pages>223</pages>
    </book>
    <book>
        <title>The Great Gatsby</title>
        <author>F. Scott Fitzgerald</author>
        <genre>Classic</genre>
        <year>1925</year>
        <pages>180</pages>
    </book>
</library>
```

**Explicação:**

- A primeira linha `<?xml version="1.0" encoding="UTF-8"?>` define a versão do XML e a codificação de caracteres usada no documento.
- `<library>` é o elemento raiz que contém todos os outros elementos do documento.
- `<book>` é um elemento que representa informações sobre um livro específico. Existem dois elementos `<book>` neste exemplo, cada um descrevendo um livro diferente.
- Dentro de cada `<book>`, há vários elementos que representam diferentes atributos do livro, como título (`<title>`), autor (`<author>`), gênero (`<genre>`), ano de publicação (`<year>`) e número de páginas (`<pages>`).

Este é apenas um exemplo simples de como o XML pode ser usado para estruturar e representar dados de forma hierárquica e legível por máquina. O XML é amplamente utilizado em uma variedade de contextos, como configuração de software, troca de dados entre sistemas e armazenamento de informações estruturadas.