import random

def generator_pass(length):
    symbols = "abcdefghiklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = "".join(random.sample(symbols, length))
    return password

pass_length = int(input("Введите размер вашего пароля: "))
print("Вот твой пароль!: " + generator_pass(pass_length))