<!-- transform.xslt -->
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
            <head>
                <title>Documentos</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                    }
                    .document {
                        margin-bottom: 20px;
                        border: 1px solid #ccc;
                        padding: 10px;
                    }
                    .title {
                        font-size: 18px;
                        font-weight: bold;
                    }
                    .info {
                        font-style: italic;
                        color: #666;
                    }
                    .content {
                        margin-top: 10px;
                    }
                </style>
            </head>
            <body>
                <h1>Documentos</h1>
                <xsl:apply-templates/>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="document">
        <div class="document">
            <div class="title"><xsl:value-of select="title"/></div>
            <div class="info">Tipo: <xsl:value-of select="type"/>, Autor: <xsl:value-of select="author"/>, Data: <xsl:value-of select="date"/></div>
            <div class="content"><xsl:value-of select="content"/></div>
        </div>
    </xsl:template>

</xsl:stylesheet>
