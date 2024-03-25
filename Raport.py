import os
from datetime import datetime
import sys

def wczytaj(plik):
    with open(plik, "r") as f:
        return [str(line.rstrip()) for line in f]

now = datetime.now()
fulldate = now.strftime("%d-%m-%Y %H:%M:%S")

outputfile = open("raport.html", "w")

outputfile.write(f"""
<html>
<head>
<title>Raport programu</title>
</head>
<body>
<h1>Raport {fulldate}</h1>

<table border="1">
<tr>
<th>Plik wejściowy</th>
<th>Dane wejściowe</th>
<th>Dane wyjściowe</th>
</tr>
""")

input_dir = r"C:\Users\lenovo\Desktop\studia\Języki Systemowe-projekt\wejscie"
output_dir = r"C:\Users\lenovo\Desktop\studia\Języki Systemowe-projekt\wyniki"

try:
    input_files = [f for f in os.listdir(input_dir) if f.endswith(".txt")]
    output_files = [f"{os.path.splitext(f)[0]}_wynik.txt" for f in input_files]
except FileNotFoundError:
    sys.exit()

if len(input_files) != len(output_files):
    raise ValueError("Liczba plików wejściowych nie jest równa liczbie plików wyjściowych.")

for input_file, output_file in zip(input_files, output_files):
    input_file_path = os.path.join(input_dir, input_file)
    output_file_path = os.path.join(output_dir, output_file)

    if not os.path.isfile(output_file_path):
        #print(f"Ostrzeżenie: Brak pliku wynikowego dla pliku wejściowego {input_file}")
        continue

    lines_input = wczytaj(input_file_path)
    lines_output = wczytaj(output_file_path)

    lines_input_html = "<br>".join(lines_input)
    lines_output_html = "<br>".join(lines_output)

    numer_pliku = os.path.splitext(input_file)[0]

    outputfile.write(f"""<tr>
                          <td>{numer_pliku}</td>
                          <td>{lines_input_html}</td>
                          <td>{lines_output_html}</td>
                       </tr>""")

outputfile.write("""
</table>
</body>
</html>
""")

outputfile.close()



