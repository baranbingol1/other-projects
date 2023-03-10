#Bu modül xml dosyalarını parse etmemize yarayacak ancak kötü amaçlı yazılmış xml dosyaları için güvenli değildir!
import xml.etree.ElementTree as ET

def xml_to_markdown(xml_string):
    root = ET.fromstring(xml_string)
    markdown_string = ""
    #Her bir tag'in child'ını markdown'a çevirme fonksiyonuna atıyoruz.
    for child in root:
        markdown_string += element_to_markdown(child)
    return markdown_string

#Bu fonksiyon bir xml nesnesinin her bir tagini parse ederek xml nesnesini markdown tipi nesneye çevirecektir.
def element_to_markdown(element):
    markdown_string = ""
    if element.tag == "h1":
        markdown_string += "# " + element.text + "\n"
    elif element.tag == "h2":
        markdown_string += "## " + element.text + "\n"
    elif element.tag == "h3":
        markdown_string += "### " + element.text + "\n"
    elif element.tag == "p":
        markdown_string +=  element.text + "\n\n"
    elif element.tag == "i":
        markdown_string += "* " + element.text + " *" + "\n\n"
    elif element.tag == "b":
        markdown_string += "** " + element.text + " **" + "\n\n"
    elif element.tag == "ul":
        for item in element:
            markdown_string += "- " + item.text + "\n"
        markdown_string += "\n"
    elif element.tag == "ol":
        for i, item in enumerate(element):
            markdown_string += str(i+1) + ". " + item.text + "\n"
        markdown_string += "\n"
    return markdown_string

#Test edelim.
html = "<html>\
    \
    <body>\
        <h1>Baslik</h1>\
            <p>Paragraf</p>\
            <i>Italik yazi</i>\
            <b>Bold yazi</b>\
                <ul>\
                    <li>Duzensiz Liste Madde 1</li>\
                        <li>Duzensiz Liste Madde 2</li>\
                    </ul>\
                <ol>\
                    <li>Duzenli Liste Madde 1</li>\
                        <li>Duzenli Liste Madde 2</li>\
                    </ol>\
        </body>\
        </html>"

#Manuel olarak yaparsak

#HTML'i XML'e dönüştürelim.
xml = ET.fromstring(html)
#XML dosyamızı markdown dosyasına çevirelim.
markdown_string = ""
for element in xml.iter():
    markdown_string += element_to_markdown(element)
with open("ornek.md", "w") as file:
    file.write(markdown_string)

#############################################

#Fonksiyonu kullanırsak.
xml_to_markdown(html)
with open("ornek2.md", "w") as file:
    file.write(markdown_string)