import chardet
# pip install chardet - w terminalu możemy wydac taką komendę

file_path = 'test.log'
with open(file_path, 'rb') as file:  # musi być odczytane binarnie - rb
    raw_data = file.read()

# print(raw_data)
result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.7093334047673798, 'language': 'Turkish'}
# dla większej próbki
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
kodowanie = result['encoding']
confidence = result['confidence']
print(kodowanie, confidence)  # utf-8 0.99
print(raw_data.decode(encoding=kodowanie))
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
# utf-8 0.99
# Radek
# dodane
# dośdane
# dośćdane
# dośąńdane
