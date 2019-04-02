import random



# 보유 돈 입력

money = int(input("보유 돈 입력: "))



while(1):

#     자판기 이용 선택

    buy_or_not = int(input("자판기 이용 1.한다 2.안한다. "))

    if(buy_or_not == 1):

        product = random.randrange(1,5)

        

#         상품1일 경우

        if(product == 1):

            if(money > 100):

                money -= 100

                print("보유 돈:", money)

            else:

                print("돈이 부족합니다.")

                print("보유 돈:", money)

                

#                 상품2일 경우

        elif(product == 2):

            if(money > 200):

                money -= 200

                print("보유 돈:", money)

            else:

                print("돈이 부족합니다.")

                print("보유 돈:", money)

                

#                 상품3일 경우

        elif(product == 3):

            if(money > 300):

                money -= 300

                print("보유 돈:", money)

            else:

                print("돈이 부족합니다.")

                print("보유 돈:", money)

                

#                 상품4일 경우

        elif(product == 4):

            if(money > 400):

                money -= 400

                print("보유 돈:", money)

            else:

                print("돈이 부족합니다.")

                print("보유 돈:", money)

                

#                 자판기 이용 안할 경우

    elif(buy_or_not == 2):

        print("잔돈:", money)

        break

    

#     1이나 2이외의 숫자를 입력할 경우

    else:

        print("유효하지 않은 값입니다.")



print("프로그램을 종료합니다.")