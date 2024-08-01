from clovax import ClovaX

c = ClovaX()
c.get_cookie("./cookies.txt")
log = c.start("'우리 학교의 이름이 뭐야?' 이 질문과 같은 똑같은 뜻의 질문을 10개를 ,로 나눠서 적어줘 다른건 적지마 10개 만든 질문만 적어")
print(log["text"])