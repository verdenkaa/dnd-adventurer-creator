from pypdf import PdfReader, PdfWriter

def pdf_make(race, clas, path):
    reader = PdfReader("./static/images/template.pdf")  # шаблон которы не трогаем, сохраняем записи в другой файл
    writer = PdfWriter()

    page = reader.pages[0]  # страница первая
    fields = reader.get_fields()
    #print(fields['ClassLevel'])  # это для отладки, пока менял тольки их
    #print(fields['Race '])
    #print(fields)  # тут можно посмотреть названия всех полей для ввода
    writer.add_page(page)  # добавляем в метод записи
    
    writer.update_page_form_field_values(  # вписываем новые значения в поля
        writer.pages[0], {'ClassLevel': clas, 'Race ': race}
    )
    
    with open(path, "wb") as output_stream:
        writer.write(output_stream)  # сохраняем



