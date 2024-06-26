import fitz
import os


def add_table_to_pdf(input_pdf_path, output_pdf_path, table_data, x, y, cell_width, cell_height, font_size=10):
    # Abre o documento PDF
    doc = fitz.open(input_pdf_path)

    # Seleciona a primeira página
    page = doc[0]

    # Define a posição inicial da tabela
    start_x, start_y = x, y

    for row in table_data:
        current_x = start_x
        current_y = start_y

        for cell in row:
            # Desenha o retângulo da célula
            rect = fitz.Rect(current_x, current_y, current_x +
                             cell_width, current_y + cell_height)
            page.draw_rect(rect, color=(0, 0, 0), width=1)

            # Insere o texto da célula
            text_position = fitz.Point(current_x + 10, current_y + 15)
            page.insert_text(text_position, cell,
                             fontsize=font_size, color=(0, 0, 0))

            # Move para a próxima célula na linha
            current_x += cell_width

        # Move para a próxima linha
        start_y += cell_height

    # Salva o PDF modificado
    doc.save(output_pdf_path)
    doc.close()


def process_all_pdfs_in_folder(folder_path, output_folder_path):
    x, y = 158, 40  # Coordenadas para o texto

    cell_width, cell_height = 110, 25
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            input_pdf_path = os.path.join(folder_path, filename)
            nome_do_arquivo = filename.split(".")
            table_data = [
                ["", "Autorização", "Data"],
                [nome_do_arquivo[0], nome_do_arquivo[1], nome_do_arquivo[2]],
            ]
            output_pdf_path = os.path.join(
                output_folder_path, f"Editado_{filename}")

            add_table_to_pdf(input_pdf_path, output_pdf_path,
                             table_data, x, y, cell_width, cell_height)


folder_path = "arquivos"
output_folder_path = "arquivos/editados"

if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

process_all_pdfs_in_folder(folder_path, output_folder_path)
