from functions import convert, checkout


class Player:
    """ Class describes player """

    def __init__(self, name):
        self.name = name
        self.score_remain = 189

    def throws(self):
        # total sum of 3 throws is going to deducted
        score = 0
        # total sum of 3 throws (temporary)
        pre_score = 0
        if checkout(self.score_remain - pre_score):
            print(f'Остаток: {self.score_remain} = {checkout(self.score_remain)} \n')
        else:
            print(f'Остаток: {self.score_remain}\n')

        for attempt in range(3):
            # receives a list of [k, v] where k - multiply and v - sector
            throw = convert(input(f'Дротик #{attempt + 1}: '))
            # throw score
            throw_score = throw[0] * throw[1]
            pre_score += throw_score
            if not self.is_end_of_turn(pre_score):

                if checkout(self.score_remain - pre_score):
                    print(f'Остаток: {self.score_remain - pre_score} = {checkout(self.score_remain - pre_score)}\n')
                else:
                    print(f'Остаток: {self.score_remain - pre_score}\n')
                score = pre_score if attempt == 2 else 0
            else:
                if self.is_checkout(throw, (self.score_remain - pre_score)):
                    print('Победа!')
                    score = pre_score
                    self.score_remain -= score
                    break
                print(f'Перебор!\nОстаток: {self.score_remain}\n')
                break
            self.score_remain -= score
        print(f'Игрок {self.name} выбил {score}')

    def show_results(self):
        if self.score_remain != 0:
            print(f'У {self.name} ещё осталось закрыть {self.score_remain}')

    def is_end_of_turn(self, pre_score):
        return True if self.score_remain - pre_score <= 1 else False

    def is_checkout(self, throw, remain):
        """
        Detect is a leg is done with checkout
        :param throw: a list of multiply and value of throw
        :param remain: remain score to checkout
        :return:
        """
        if throw[0] == 2:
            if remain == 0:
                return True
        else:
            return False
