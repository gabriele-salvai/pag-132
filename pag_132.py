reddito= float(input("insersci il tuo reddito annuo:\t"))
imponibile=0
imposta=0
aliquota1=0
aliquota2=12/100
aliquota3=18/100
aliquota4=27/100
aliquota5=48/100
aliquota6=60/100
if reddito<=10000:
    imponibile+=reddito
    imposta=imponibile*aliquota1
    print("il tuo reddito imponibile è:",imponibile)
    print("l'imposta è:",imposta)
elif reddito>10000 and reddito<=20000:
    imponibile= 10000
    imposta=imponibile*aliquota1
    print("il primo imponibile è:",imponibile)
    print("la prima imposta è:",imposta)
    imponibile=reddito-imponibile
    imposta=imponibile*(aliquota2)
    print("il secondo imponibile è:",imponibile)
    print("la seconda imposta è:",imposta)
    print("il totale di imposta che devi pagare è",imposta)
elif reddito>20000 and reddito<=35000:
    imponibile=10000
    imposta=imponibile*aliquota1
    c=imponibile
    print("il primo imponibile è:",imponibile)
    print("la prima imposta è:",imposta)
    imposta=imponibile*(aliquota2)
    c=imponibile+10000
    print("il secondo imponibile è:",imponibile)
    print("la seconda imposta è:",imposta)
    imponibile=reddito-c
    c=imponibile*(aliquota3)
    imposta+=c
    print("il terzo imponibile è:",imponibile)
    print("la terza imposta è:",c)
    print("il totale di imposta che devi pagare è",imposta)
elif reddito>35000 and reddito<=60000:
    imponibile=10000
    imposta=imponibile*aliquota1
    c=imponibile
    print("il primo imponibile è:",imponibile)
    print("la prima imposta è:",imposta)
    imposta=imponibile*(aliquota2)
    c=imponibile+10000
    print("il secondo imponibile è:",imponibile)
    print("la seconda imposta è:",imposta)
    imponibile=15000
    imposta=imponibile*(aliquota3)
    c+=imposta
    print("il terzo imponibile è:",imponibile)
    print("la terza imposta è:",imposta)
    c+=imposta
    imponibile=reddito-35000
    imposta=imponibile*(aliquota4)
    c+=imposta
    print("il quarto imponibile è:",imponibile)
    print("la quarta imposta è:",imposta)
    print("il totale di imposta che devi pagare è",c)
elif reddito>60000 and reddito<=100000:
    c=0
    imponibile=10000
    imposta=imponibile*aliquota1
    print("il primo imponibile è:",imponibile)
    print("la prima imposta è:",imposta)
    imposta=imponibile*(aliquota2)
    imponibile=10000
    c+=imposta
    print("il secondo imponibile è:",imponibile)
    print("la seconda imposta è:",imposta)
    imponibile=15000
    imposta=imponibile*(aliquota3)
    c+=imposta
    print("il terzo imponibile è:",imponibile)
    print("la terza imposta è:",imposta)
    imponibile=25000
    imposta=imponibile*aliquota4
    c+=imposta
    print("il quarto imponibile è:",imponibile)
    print("la quarta imposta è:",imposta) 
    imponibile=reddito-60000
    imposta=imponibile*aliquota5
    c+=imposta
    print("il quinto imponibile è:",imponibile)
    print("la quinta imposta è:", imposta)
    print("il totale di imposta che devi pagare è",c)
else:
    c=0
    imponibile=10000
    imposta=imponibile*aliquota1
    print("il primo imponibile è:",imponibile)
    print("la prima imposta è:",imposta)
    imposta=imponibile*(aliquota2)
    imponibile=10000
    c+=imposta
    print("il secondo imponibile è:",imponibile)
    print("la seconda imposta è:",imposta)
    imponibile=15000
    imposta=imponibile*(aliquota3)
    c+=imposta
    print("il terzo imponibile è:",imponibile)
    print("la terza imposta è:",imposta)
    imponibile=25000
    imposta=imponibile*aliquota4
    c+=imposta
    print("il quarto imponibile è:",imponibile)
    print("la quarta imposta è:",imposta) 
    imponibile=40000
    imposta=imponibile*aliquota5
    c+=imposta
    print("il quinto imponibile è:",imponibile)
    print("la quinta imposta è:", imposta)
    imponibile=reddito-10000
    imposta=imponibile*aliquota6
    c+=imposta
    print("il sesto imponibile è:",imponibile)
    print("la sesta imposta è:", imposta)
    print("il totale di imposta che devi pagare è",c)



  