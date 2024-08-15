from flask import Flask, request, render_template, send_file
import os
from brazilfiscalreport.danfe import (
    Danfe,
    DanfeConfig,
    DecimalConfig,
    FontType,
    InvoiceDisplay,
    Margins,
    ReceiptPosition,
    TaxConfiguration,
)
from config import UPLOAD_FOLDER, OUTPUT_FOLDER, LOGO_PATH

app = Flask(__name__)

# Criar os diretórios, se não existirem
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Verifica se o arquivo foi enviado
        if 'file' not in request.files:
            return 'Nenhum arquivo foi enviado', 400
        file = request.files['file']
        if file.filename == '':
            return 'Nenhum arquivo selecionado', 400

        # Salva o arquivo XML
        xml_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(xml_path)

        # Ler o conteúdo do XML
        with open(xml_path, "r", encoding="utf8") as f:
            xml_content = f.read()

        # Configurar o DANFE
        config = DanfeConfig(
            logo=LOGO_PATH,
            margins=Margins(top=10, right=10, bottom=10, left=10),
            receipt_pos=ReceiptPosition.BOTTOM,
            decimal_config=DecimalConfig(price_precision=2, quantity_precision=2),
            tax_configuration=TaxConfiguration.ICMS_ST,
            invoice_display=InvoiceDisplay.FULL_DETAILS,
            font_type=FontType.TIMES
        )

        # Gerar o DANFE
        output_pdf_path = os.path.join(OUTPUT_FOLDER, 'output_danfe.pdf')
        danfe = Danfe(xml_content, config=config)
        danfe.output(output_pdf_path)

        # Enviar o PDF gerado para o navegador
        return send_file(output_pdf_path, as_attachment=False)

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
