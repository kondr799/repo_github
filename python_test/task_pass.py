import random

def generator_pass(lenght):
    symbols = "abcdefghiklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = "".join(random.sample(symbols,lenght))
    return password


pass_lenght = int(input("Введите размер вашего желаемого пароля: "))
print("Вот ваш новый пароль!!: " + generator_pass(pass_lenght))