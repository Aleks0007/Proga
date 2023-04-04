import main as gh #grasshopper

textInput = "1101011010001100101101101011100111111010011110001101100100011011" # Ввод исходного текста
password = "strongPassword" # Ввод пароля

# Получение ключей для шифрования и расшифрования
K = gh.getKeys(password)

# Шифрование
textEncrypt = gh.encrypt(textInput, K)

# Расшифрование
textDecrypt = gh.decrypt(textEncrypt, K)

print('Сообщение:',textDecrypt)
print('Зашифрованное сообщение:', textEncrypt)
