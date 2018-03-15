import random
import string


class TxtGenerator:
    def generate(self, amount):
        def gen_word():
            return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randrange(3, 10)))
        with open('test_data.txt', 'w') as file:
            for i in range(amount):
                file.write(gen_word() + ';')
            file.write(gen_word())