def health_rate(age, apples_ate, cig_smoked):
    rating = (age * 1.2) + (apples_ate * 3.9) - (cig_smoked * 1.5)
    if rating > 50:
        print(rating, 'indicates thats you are healthy')
    else:
        print(rating, 'means, you should take care of health')


habbit1 = [30, 20, 0]
habbit2 = [35, 10, 20]
habbit3 = [25, 0, 70]

health_rate(*habbit1)
health_rate(*habbit2)
health_rate(*habbit3)