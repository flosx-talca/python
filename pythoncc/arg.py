import argparse

varibale = argparse.ArgumentParser(description = "Primer comando por argumento python3")
varibale.add_argument('-s','--ser',help='por ejemplo: locahost')
argumento= varibale.parse_args()
print(argumento.ser)
if argumento.ser:
    print('el valor es  {argumento.ser}')
else:
    print('No se recibio valor')