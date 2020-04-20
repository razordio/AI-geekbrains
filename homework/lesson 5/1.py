out_f = open("out_file.txt", "w")
while True:
    text = input('Enter text:')
    itext = text + '\n'
    out_f.write(itext)
    if itext == '\n':
        break
out_f.close()