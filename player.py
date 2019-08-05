from functions import convert, checkout


class Player:
    """ Class describes player """

    def __init__(self, name):
        self.name = name
        self.score_remain = 189

    def throws(self):
        score = 0
        pre_score = 0
        if checkout(self.score_remain):
            print(f'Остаток: {self.score_remain} = {checkout(self.score_remain - score)} \n')
        else:
            print(f'Остаток: {self.score_remain}\n')

        for attempt in range(3):
            throw = convert(input(f'Дротик #{attempt + 1}: '))
            throw_score = throw[0] * throw[1]
            pre_score += throw_score
            if not self.is_end_of_turn(pre_score):
                score = pre_score
                if checkout(self.score_remain - pre_score):
                    print(f'Остаток: {self.score_remain - pre_score} = {checkout(self.score_remain - pre_score)}\n')
                else:
                    print(f'Остаток: {self.score_remain - pre_score}\n')
                self.score_remain -= score
            else:
                break

        return print(f'Игрок {self.name} выбил {score}')

    def show_results(self):
        return print(f'У {self.name} ещё осталось закрыть {self.score_remain}')

    def is_end_of_turn(self, pre_score):
        return True if self.score_remain - pre_score <= 1 else False



