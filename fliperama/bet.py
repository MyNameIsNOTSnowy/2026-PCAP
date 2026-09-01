import random
from telas import linha

banco = 100
def jogar_bet():

    banco = 100

    while banco > 0:
        print(f"Você tem: {banco}")
        reais = float(input("Quanto quer apostar? 🤑: "))
        uh = ["🔪", "🤑", "🍒", "🐱"]

        if reais > banco:
            linha()
            print("Você não tem esse dinheiro saia daqui 😡")
            break
        else:
            banco = (banco - reais)
            randomBS1 = random.choice(uh)
            randomBS2 = random.choice(uh)
            randomBS3 = random.choice(uh)

            print("................")
            print(f"| {randomBS1} | {randomBS2} | {randomBS3} |")
            print("''''''''''''''''")

            if randomBS1 == "🔪" or randomBS2 == "🔪" or randomBS3 == "🔪":
                print("perdeu seu dinheiro lol")
            elif randomBS1 == "🤑" and randomBS2 == "🤑" and randomBS3 == "🤑":
                print(f"JACKPOT → {(reais * 10)}")
                reais2 = (reais * 10)
                banco = (banco + reais2)
            elif randomBS1 == "🤑" and randomBS2 == "🤑" and randomBS3 == "🐱":
                print(f"você ganhou {(reais * 8)}")
                reais2 = (reais * 8)
                banco = (banco + reais2)
            elif randomBS1 == "🤑" and randomBS2 == "🤑" and randomBS3 == "🍒":
                print(f"você ganhou {(reais * 7.5)}")
                reais2 = (reais * 7.5)
                banco = (banco + reais2)
            elif randomBS1 == "🤑" and randomBS2 == "🍒" and randomBS3 == "🍒":
                print(f"você ganhou {(reais * 6)}")
                reais2 = (reais * 6)
                banco = (banco + reais2)
            elif randomBS1 == "🤑" and randomBS2 == "🍒" and randomBS3 == "🤑":
                print(f"você ganhou {(reais * 7.5)}")
                reais2 = (reais * 7.5)
                banco = (banco + reais2)
            elif randomBS1 == "🤑" and randomBS2 == "🍒" and randomBS3 == "🐱":
                print(f"você ganhou {(reais * 6.5)}")
                reais2 = (reais * 6.5)
                banco = (banco + reais2)
            elif randomBS1 == "🤑" and randomBS2 == "🐱" and randomBS3 == "🤑":
                print(f"você ganhou {(reais * 8)}")
                reais2 = (reais * 8)
                banco = (banco + reais2)
            elif randomBS1 == "🤑" and randomBS2 == "🐱" and randomBS3 == "🐱":
                print(f"você ganhou {(reais * 7)}")
                reais2 = (reais * 7)
                banco = (banco + reais2)
            elif randomBS1 == "🤑" and randomBS2 == "🐱" and randomBS3 == "🍒":
                print(f"você ganhou {(reais * 6.5)}")
                reais2 = (reais * 6.5)
                banco = (banco + reais2)
            elif randomBS1 == "🐱" and randomBS2 == "🐱" and randomBS3 == "🐱":
                print(f"você ganhou {(reais * 6)}")
                reais2 = (reais * 6)
                banco = (banco + reais2)
            elif randomBS1 == "🐱" and randomBS2 == "🐱" and randomBS3 == "🤑":
                print(f"você ganhou {(reais * 7)}")
                reais2 = (reais * 7)
                banco = (banco + reais2)
            elif randomBS1 == "🐱" and randomBS2 == "🐱" and randomBS3 == "🍒":
                print(f"você ganhou {(reais * 5.5)}")
                reais2 = (reais * 5.5)
                banco = (banco + reais2)
            elif randomBS1 == "🐱" and randomBS2 == "🤑" and randomBS3 == "🐱":
                print(f"você ganhou {(reais * 7)}")
                reais2 = (reais * 7)
                banco = (banco + reais2)
            elif randomBS1 == "🐱" and randomBS2 == "🤑" and randomBS3 == "🍒":
                print(f"você ganhou {(reais * 6.5)}")
                reais2 = (reais * 6.5)
                banco = (banco + reais2)
            elif randomBS1 == "🐱" and randomBS2 == "🤑" and randomBS3 == "🤑":
                print(f"você ganhou {(reais * 8)}")
                reais2 = (reais * 8)
                banco = (banco + reais2)
            elif randomBS1 == "🐱" and randomBS2 == "🍒" and randomBS3 == "🐱":
                print(f"você ganhou {(reais * 5.5)}")
                reais2 = (reais * 5.5)
                banco = (banco + reais2)
            elif randomBS1 == "🐱" and randomBS2 == "🍒" and randomBS3 == "🤑":
                print(f"você ganhou {(reais * 6.5)}")
                reais2 = (reais * 6.5)
                banco = (banco + reais2)
            elif randomBS1 == "🐱" and randomBS2 == "🍒" and randomBS3 == "🍒":
                print(f"você ganhou {(reais * 5)}")
                reais2 = (reais * 5)
                banco = (banco + reais2)
            elif randomBS1 == "🍒" and randomBS2 == "🍒" and randomBS3 == "🍒":
                print(f"você ganhou {(reais * 4.5)}")
                reais2 = (reais * 4.5)
                banco = (banco + reais2)
            elif randomBS1 == "🍒" and randomBS2 == "🍒" and randomBS3 == "🤑":
                print(f"você ganhou {(reais * 6)}")
                reais2 = (reais * 6)
                banco = (banco + reais2)
            elif randomBS1 == "🍒" and randomBS2 == "🍒" and randomBS3 == "🐱":
                print(f"você ganhou {(reais * 5)}")
                reais2 = (reais * 5)
                banco = (banco + reais2)
            elif randomBS1 == "🍒" and randomBS2 == "🐱" and randomBS3 == "🍒":
                print(f"você ganhou {(reais * 5)}")
                reais2 = (reais * 5)
                banco = (banco + reais2)
            elif randomBS1 == "🍒" and randomBS2 == "🐱" and randomBS3 == "🤑":
                print(f"você ganhou {(reais * 6.5)}")
                reais2 = (reais * 6.5)
                banco = (banco + reais2)
            elif randomBS1 == "🍒" and randomBS2 == "🐱" and randomBS3 == "🐱":
                print(f"você ganhou {(reais * 5.5)}")
                reais2 = (reais * 5.5)
                banco = (banco + reais2)
            elif randomBS1 == "🍒" and randomBS2 == "🤑" and randomBS3 == "🤑":
                print(f"você ganhou {(reais * 7.5)}")
                reais2 = (reais * 7.5)
                banco = (banco + reais2)
            elif randomBS1 == "🍒" and randomBS2 == "🤑" and randomBS3 == "🐱":
                print(f"você ganhou {(reais * 6.5)}")
                reais2 = (reais * 6.5)
                banco = (banco + reais2)
            elif randomBS1 == "🍒" and randomBS2 == "🤑" and randomBS3 == "🍒":
                print(f"você ganhou {(reais * 6)}")
                reais2 = (reais * 6)
                banco = (banco + reais2)