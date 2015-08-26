from models import Question, Theme, Answer
import json

def test():
    theme = Theme.objects.all()

    # question = Question.objects.all()
    print theme.question_set.all()
    # for i in question:
    #     print i.name
    # print question
    return 'vxb'


def question(**kwargs):
    th = Theme.objects.get(id=kwargs.get('object').pk)
    q = Question.objects.filter(theme=th)
    for i in q:
        question = i.name
    return q


def answer(**kwargs):
    th = Theme.objects.get(id=kwargs.get('object').pk)
    q = Question.objects.filter(theme=th)
    a = Answer.objects.all()
    # print 'aaaa', Answer.objects.filter(question__in=q)

    # print 'bbbbb', Answer.objects.select_related('question__name').get(id=kwargs.get('object').pk)
    # print Answer.objects.select_related('question__name').get(id=value[0])
    all = {}
    for foo in q:
        local = {foo: Answer.objects.filter(question=foo).values('answer', 'status', 'pk')}
        all.update(local)
    print all
    return all
    # answer = []
    # for j in q:
    #     n = j.answer_set
    #     print n
    #
    #     for k in n:
    #         print k.answer
    #         answer.append(k.answer)
    # #     print answer
    # return answer
