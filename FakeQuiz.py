class MultipleChoiceQuestion:
    def __init__(self, question, options, answer, points):
        self.question = question
        self.options = options
        self.answer = answer
        self.points = points

    def display_question(self):
        print(self.question)
        for i, option in enumerate(self.options):
            print(f"{chr(ord('A') + i)}. {option}")

    def check_answer(self, user_answer):
        return user_answer == self.answer


def main():
    questions = [
        MultipleChoiceQuestion("What lambda function has two inputs and one output?", ["lambda x,y:x,y", "lambda y:x,y", "lambda x,y:x", "lambda x,y:z"], "C", 1),
        MultipleChoiceQuestion("\n""Consider the following code snippet:\n"
                               "people_list = [\n"
                               "    {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},\n"
                               "    {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},\n"
                               "    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3}\n"
                               "]\n"
                               "\n"
                               "people_list.sort(key=lambda x, p: p['age'], reverse=True)\n"
                               "print(people_list)""]\n""\n"
                               "What if anything is wrong with the lambda function?""\n"
                               ,
                                 ["Nothing is wrong", "Named Parameter is wrong", "Lambda input parameters are not corret", "Invalid Key Name"], "C", 1),

        MultipleChoiceQuestion("\n""Consider the following code snippet:\n"
                               "people_list = [\n"
                               "    {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},\n"
                               "    {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},\n"
                               "    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3}\n"
                               "]\n"
                               "\n"
                               "new_list = list(filter(lambda p:p['age'] > 15))\n""\n"
                    
                               "What if anything is wrong with the lambda function?\n""\n"
                               ,
                                 ["Nothing", "Inavlid Key", "Missing Argument for filter function", "Missin argument for list function"], "C", 1)
    

    ]

    total_points = 0

    for question in questions:
        question.display_question()
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        if question.check_answer(user_answer):
            total_points += question.points

    print(f"Total points: {total_points}")


if __name__ == "__main__":
    main()
