money = 0;
gameIsOn=1;
while (gameIsOn==1):
    answer = int(input("what would you like to do? \n 1. do a job \n 2. buy food \n3. End game\n choice(number):"));
    
    if(answer == 1):
        print("nice JOB... hahahhaha, you earned 10 dollars at McDonalds");
        money = money + 10;
    elif(answer == 2):
        chocoorvanilla = input("would you prefer vanilla or chocolate ice cream?");
        if(chocoorvanilla == "vanilla"):
            if(money >=1):
                print("you bought vanilla ice cream! money \n -$1.00 \n new balance:");
                money = money - 1;
                print(money);
            else:
                print("not enough money, go get a job at McDonalds, \n new balance:");
                print(money);
        elif(chocoorvanilla == "chocolate"):
            if(money >=1.5):
                print("you bought chocolate ice cream! money \n -$1.50\n new balance:");
                money = money - 1.5;
                print(money);
            else:
                print("not enough money, go get a job at McDonalds, \n balance:");
                print(money);
    elif(answer == 3):
        gameIsOn=0;
