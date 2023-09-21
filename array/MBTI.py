eiAnswers = []
eiAAnswers = 0
eiBAnswers = 0

snAnswers = []
snCounterA = 0
snCounterB = 0

tfAnswers = []
tfCounterA = 0
tfCounterB = 0

jpAnswers = []
jpCounterA = 0
jpCounterB = 0

personalityOutput = ""
user_name = " "


def question1():
    global user_name
    user_name = input("Enter your name: ")
    print("Hello " + user_name + " your entry should be  A or B")
    print("""
           1.   
                A. expend energy, enjoy groups  
                B. conserve energy, enjoy one-on-one
            """)

    user_entry = input("Enter A  or B : ")
    global eiAnswers
    global eiAAnswers
    global eiBAnswers
    letter = "A"
    letters = "B"
    if user_entry.casefold() == letter.casefold():
        eiAnswers.append("A: expend energy, enjoy groups")
        eiAAnswers += 1
        question2()

    elif user_entry.casefold() == letters.casefold():
        eiAnswers.append("B: conserve energy, enjoy one-on-one")
        eiBAnswers += 1
        question2()

    else:
        print("""   The expected answer should be  A or B 
                    I know this is an error, Please retry again
                    """)
        question1()


def question2():
    print("""
        2.  
            A. interpret literally   
            B.look for meaning and possibilities
            """)
    user_entry = input("Enter A  or B : ")
    global snAnswers
    global snCounterA
    global snCounterB
    letter = "A"
    letters = "B"

    if user_entry.casefold() == letter.casefold():
        snAnswers.append("A: interpret literally")
        snCounterA += 1
        questions3()

    elif user_entry == letters.casefold():
        snAnswers.append("B: look for meaning and possibilities")
        snCounterB += 1
        questions3()

    else:
        print("""   The expected answer should be  A or B 
                     I know this is an error, Please retry again
                           """)
        question2()


def questions3():
    print("""
        3.    
                A. logical, thinking, questioning    
                B. empathetic, feeling, accommodating""")

    userEntry = input("Enter an option: ")
    global tfCounterA
    global tfCounterB
    global tfAnswers
    letter = "A"
    letters = "B"

    if userEntry.casefold() == letter.casefold():
        tfAnswers.append("A: logical, thinking, questioning")
        tfCounterA += 1
        question4()

    elif userEntry.casefold() == letters.casefold():
        tfAnswers.append("B: empathetic, feeling, accommodating")
        tfCounterB += 1
        question4()

    else:
        print("""   The expected answer should be  A or B 
                     I know this is an error, Please retry again
                           """)
        questions3()


def question4():
    print("""
        4.    
             A. organized, orderly   
               B. flexible, adaptable
               """)

    userEntry = input("Enter an option: ")

    global jpAnswers
    global jpCounterA
    global jpCounterB
    letter = "A"
    letters = "B"

    if userEntry.casefold() == letter.casefold():
        jpAnswers.append("A: organized, orderly ")
        jpCounterA += 1
        question5()


    elif userEntry == letters.casefold():
        jpAnswers.append("B: flexible, adaptable")
        jpCounterB += 1
        question5()


    else:
        print("""   The expected answer should be  A or B 
                     I know this is an error, Please retry again
                          """)
        question4()


def question5():
    print("""
           5.  
                A. more outgoing, think out loud   
                 B. more reserved, think to yourself 
                  """)

    userEntry = input("Enter an option: ")
    global eiAnswers
    global eiAAnswers
    global eiBAnswers
    letter = "A"
    letters = "B"

    if userEntry.casefold() == letter.casefold():
        eiAnswers.append("A: more outgoing, think out loud ")
        eiAAnswers += 1
        question6()

    elif userEntry.casefold() == letters.casefold():
        eiAnswers.append("B: more reserved, think to yourself ")
        eiBAnswers += 1
        question6()

    else:
        print("""
                    The expected answer should be  A or B 
                    I know this is an error, Please retry again
                    """)
        question5()



def question6():
    print("""
             6.  
                    A. practical, realistic, experiential   
                    B. imaginative, innovative, theoretical 
                """)

    userEntry = input("Enter an option: ")
    global snAnswers
    global snCounterA
    global snCounterB
    letter = "A"
    letters = "B"

    if userEntry.casefold() == letter.casefold():
        snAnswers.append("A: practical, realistic, experiential  ")
        snCounterA += 1
        question7()




    elif userEntry.casefold() == letters.casefold():
        snAnswers.append("B: imaginative, innovative, theoretical ")
        snCounterB += 1
        question7()

    else:
        print("""
        Expected answer is A or B
        I know this is an error, please try again
        """)
        question6()


def question7():
    print("""
        7. 
            A. candid, straight forward, frank       
            B. tactful, kind, encouraging
            """)

    userEntry = input("Enter an option: ")

    global tfCounterB
    global tfAnswers
    global tfCounterA
    letter = "A"
    letters = "B"

    if userEntry.casefold() == letter.casefold():
        tfAnswers.append("A: candid, straight forward, frank ")
        tfCounterA += 1
        question8()


    elif userEntry.casefold() == letters.casefold():
        tfAnswers.append("B: tactful, kind, encouraging")
        tfCounterB += 1
        question8()


    else:
        print("""
          Expected answer is A or B
          I know this is an error, please try again
          """)
        question7()


def question8():
    print("""
       8.  
            A. plan, schedule   
            B. unplanned, spontaneous""")

    userEntry = input("Enter an option: ")
    global jpAnswers
    global jpCounterA
    global jpCounterB
    letter = "A"
    letters = "B"

    if userEntry.casefold() == letter.casefold():
        jpAnswers.append("A: plan, schedule")
        jpCounterA += 1
        question9()


    elif userEntry.casefold() == letters.casefold():
        jpAnswers.append("B: unplanned, spontaneous ")
        jpCounterB += 1
        question9()


    else:
        print("""
                 Expected answer is A or B
                 I know this is an error, please try again
                 """)
        question8()


def question9():
    print("""
                9. 
                    A. seek many tasks, public activities 
                     B. seek private, solitary activities with quiet to concentrate""")

    userEntry = input("Enter an option: ")
    global eiAnswers
    global eiBAnswers
    global eiAAnswers
    letter = "A"
    letters = "B"

    if userEntry.casefold() == letter.casefold():
        eiAnswers += ["A: seek many tasks, public activities "]
        eiAAnswers += 1
        question10()


    elif userEntry.casefold() == letters.casefold():
        eiAnswers.append("B: seek private, solitary activities with quiet to concentrate")
        eiBAnswers += 1
        question10()


    else:
        print("""
                         Expected answer is A or B
                         I know this is an error, please try again
                         """)

        question9()


def question10():
    print("""
            10.  
                A. standard, usual, conventional       
                B. different, novel, unique """)

    userEntry = input("Enter an option: ")
    global snAnswers
    global snCounterA
    global snCounterB
    letter = "A"
    letters = "B"
    if userEntry.casefold() == letter.casefold():
        snAnswers.append("A: standard, usual, conventional ")
        snCounterA += 1
        question11()


    elif userEntry.casefold() == letters.casefold():
        snAnswers.append("B: different, novel, unique")
        snCounterB += 1
        question11()


    else:
        print("""
                         Expected answer is A or B
                         I know this is an error, please try again
                         """)

        question10()


def question11():
    print("""
        11.   
                A. firm, tend to criticize, hold the line
                B. gentle, tend to appreciates with quiet to concentrate """)
    global tfCounterA
    global tfCounterB
    global tfAnswers
    letter = "A"
    letters = "B"
    userEntry = input("Enter an option: ")
    if userEntry.casefold() == letter.casefold():
        tfAnswers += ["A: firm, tend to criticize, hold the lin "]
        tfCounterA += 1
        question12()


    elif userEntry.casefold() == letters.casefold():
        tfAnswers += ["B: gentle, tend to appreciates with quiet to concentrate "]
        tfCounterB += 1
        question12()


    else:
        print("""
                               Expected answer is A or B
                               I know this is an error, please try again
                               """)
        question11()


def question12():
    print("""
    12.     
            A. regulated, structured  
            B. easygoing,\"live\" and \"let live\"""")

    userEntry = input("Enter an option: ")
    global jpCounterB
    global jpCounterA
    global jpAnswers
    letter = "A"
    letters = "B"

    if userEntry.casefold() == letter.casefold():
        jpAnswers += ["A: regulated, structured  "]
        jpCounterA += 1
        question13()

    elif userEntry == letters.casefold():
        jpAnswers += ["B: easygoing,\" live\"and \"let live\""]
        jpCounterB += 1
        question13()

    else:
        print("""
                      The expected answer should be  A or B
                     I know this is an error, Please retry again""")
        question12()


def question13():
    print("""
    13.
            A. external, communicative, express yourself   
            B. internal, reticent, keep to yourself """);

    userEntry = input("Enter an option: ")
    global eiAnswers
    global eiAAnswers
    global eiBAnswers
    letter = "A"
    letters = "B"
    if userEntry.casefold() == letter.casefold():
        eiAnswers += ["A: external, communicative, express yourself "]
        eiAAnswers += 1
        question14()


    elif userEntry.casefold() == letters.casefold():
        eiAnswers += ["B: internal, reticent, keep to yourself"]
        eiBAnswers += 1
        question14()


    else:
        print("""

                       The expected answer should be  A or B
                       I know this is an error, Please retry again""")
        question13()


def question14():
    print("""   
        14.  
                A. focus on here-and-now  
                B. look to the future , global perspective, \"big picture\"""")

    userEntry = input("Enter an option: ")
    global snCounterB
    global snCounterA
    global snAnswers
    letter = "A"
    letters = "B"
    if userEntry.casefold() == letter.casefold():
        snAnswers += ["A: focus on here-and-now "]
        snCounterA += 1
        question15()


    elif userEntry.casefold() == letters.casefold():
        snAnswers += ["B: look to the future , global perspective, \"big picture\""]
        snCounterB += 1
        question15()


    else:
        print("""

                       The expected answer should be  A or B
                       I know this is an error, Please retry again""")
        question14()


def question15():
    print("""
            15.   
                A. tough-minded,just  
                B. tender-hearted, merciful""")

    userEntry = input("Enter an option: ")
    global tfAnswers
    global tfCounterA
    global tfCounterB
    letter = "A"
    letters = "B"
    if userEntry.casefold() == letter.casefold():
        tfAnswers += ["A:  tough-minded,just"]
        tfCounterA += 1
        question16()


    elif userEntry.casefold() == letters.casefold():
        tfAnswers += ["B:  tender-hearted, merciful"]
        tfCounterB += 1
        question16()


    else:
        print("""

                       The expected answer should be  A or B
                       I know this is an error, Please retry again""")
        question15()


def question16():
    print("""
        16. 
            A. preparation,plan ahead   
            B. go with the flow, adapt as you go""")

    userEntry = input("Enter an option: ")
    global jpAnswers
    global jpCounterA
    global jpCounterB
    letter = "A"
    letters = "B"
    if userEntry.casefold() == letter.casefold():
        jpAnswers += ["A:  preparation,plan ahead     "]
        jpCounterA += 1
        question17()


    elif userEntry.casefold() == letters.casefold():
        jpAnswers += ["B: go with the flow, adapt as you go"]
        jpCounterB += 1
        question17()

    else:
        print("""
                The expected answer should be  A or B 
                I know this is an error, Please retry again""")
        question16()


def question17():
    print("""
    17.
                A. active, initiate     
                 B. reflective, deliberate""")

    userEntry = input("Enter an option: ")
    global eiAnswers
    global eiAAnswers
    global eiBAnswers
    letter = "A"
    letters = "B"

    if userEntry.casefold() == letter.casefold():
        eiAnswers += ["A: active, initiate "]
        eiAAnswers += 1
        question18()


    elif userEntry.casefold() == letters.casefold():
        eiAnswers += ["B: reflective, deliberate "]
        eiBAnswers += 1
        question18()


    else:
        print("""
                        The expected answer should be  A or B
                        I know this is an error, Please retry again
                          """)
        question17()


def question18():
    print("""
            18.
                A. facts, things, what is   
                B. ideas, dreams,\" what cloud be,\" philosophical""")
    global snCounterB
    global snAnswers
    global snCounterA
    letter = "A"
    letters = "B"

    userEntry = input("Enter an option: ")
    if userEntry.casefold() == letter.casefold():
        snAnswers += ["A: facts, things, what is  "]
        snCounterA += 1
        question19()


    elif userEntry.casefold() == letters.casefold():
        snAnswers += ["B: ideas, dreams,\" what cloud be,\" philosophical "]
        snCounterB += 1
        question19()

    else:
        print("""
                           The expected answer should be  A or B
                           I know this is an error, Please retry again
                             """)
        question18()


def question19():
    print("""      
          19.      
                    A. Matter of fact, issue-oriented  
                    B. sensitive, people-oriented, compassionate""")

    global tfAnswers
    global tfCounterA
    global tfCounterB
    letter = "A"
    letters = "B"

    userEntry = input("Enter an option: ")
    if userEntry.casefold() == letter.casefold():
        tfAnswers += ["A: facts, things, what is  "]
        tfCounterA += 1
        question20()

    elif userEntry.casefold() == letters.casefold():
        tfAnswers += ["B: ideas, dreams,\" what cloud be,\" philosophical "]
        tfCounterB += 1
        question20()


    else:
        print("""

                       The expected answer should be  A or B\s
                       I know this is an error, Please retry again""")
        question19()


def question20():
    print("""
            20.  
                    A. control, govern   
                    B. latitude, freedom""")
    global jpCounterB
    global jpCounterA
    global jpAnswers

    letter = "A"
    letters = "B"
    userEntry = input("Enter an option: ")
    if userEntry.casefold() == letter.casefold():
        jpAnswers += ["A: control, govern  "]
        jpCounterA += 1
        Answer()

    elif userEntry.casefold() == letters.casefold():
        jpAnswers += ["B: latitude, freedom "]
        jpCounterB += 1
        Answer()

    else:
        print("""

                      The expected answer should be  A or B
                      I know this is an error, Please retry again
                      """)
        question20()


def Answer():
    global user_name
    global eiAnswers
    global eiAAnswers
    global eiBAnswers

    print("\nHello " + user_name + " you selected ")
    for i in eiAnswers:
        print(i)
    print(f" number of A selected:{eiAAnswers}")
    print(f" number of B selected:{eiBAnswers}")
    answer2()


def answer2():
    global snAnswers
    global snCounterA
    global snCounterB
    for i in snAnswers:
        print(i)
    print(f" number of A selected:{snCounterA}")
    print(f" number of B selected:{snCounterB}")

    answer3()


def answer3():
    global tfAnswers
    global tfCounterA
    global tfCounterB
    for i in tfAnswers:
        print(i)
    print(f" number of A selected:{tfCounterA}")
    print(f" number of B selected:{tfCounterB}")
    answer4()


def answer4():
    global jpAnswers
    global jpCounterA
    global jpCounterB

    for i in jpAnswers:
        print(i)
    print(f" number of A selected:{jpCounterA}")
    print(f" number of B selected:{jpCounterB}")

    personlity()


def personlity():
    global eiAAnswers
    global eiBAnswers
    global snCounterA
    global snCounterB
    global tfCounterA
    global tfCounterB
    global jpCounterA
    global jpCounterB
    global personalityOutput

    if eiAAnswers > eiBAnswers:
        personalityOutput += "E"
    else:
        personalityOutput += "I"

    if snCounterA > snCounterB:
        personalityOutput += "S"
    else:
        personalityOutput += "N"

    if tfCounterA > tfCounterB:
        personalityOutput += "T"
    else:
        personalityOutput += "F"
    if jpCounterA > jpCounterB:
        personalityOutput += "J"
    else:
        personalityOutput += "P"

    print("your personality is: " + personalityOutput)
    match personalityOutput:
        case "ESTJ":
            print(""" 
                         ESTJ

                         An ESTJ (ESTJ) is someone with the Extraverted, Observant, Thinking, and Judging personality traits. 
                         They possess great fortitude, emphatically following their own sensible judgment. They often serve 
                         as a stabilizing force among others, able to offer solid direction amid adversity.
                         Good order is the foundation of all things.

                         EDMUND BURKE
                         ESTJs are representatives of tradition and order, utilizing their understanding of what is right, 
                         wrong and socially acceptable to bring families and communities together. Embracing the values 
                         of honesty, dedication and dignity, people with the ESTJ personality type are valued for their clear advice 
                         and guidance, and they happily lead the way on difficult paths. Taking pride in bringing people 
                         together, ESTJs often take on roles as community organizers, working hard to bring everyone 
                         together in celebration of cherished local events, or in defense of the traditional values that hold 
                         families and communities together.

                         ESTJ (ESTJ) personality
                         Leading by Example
                         Demand for such leadership is high in democratic societies, and forming no less than 11% of the 
                         population, it’s no wonder that many of America’s presidents have been ESTJs. Strong believers 
                         in the  rule of law and authority that must be earned, ESTJ personalities lead by example, 
                         demonstrating dedication and purposeful honesty, and an utter rejection of laziness and cheating, 
                         especially in work. If anyone declares hard, manual work to be an excellent way to build character,
                         it is ESTJs.

                         ESTJs are aware of their surroundings and live in a world of clear, verifiable facts – the surety 
                         of their knowledge means that even against heavy resistance, they stick to their principles and 
                         push an unclouded vision of what is and is not acceptable. Their opinions aren’t just empty talk e
                         ither, as ESTJs are more than willing to dive into the most challenging projects, improving action 
                         plans and sorting details along the way, making even the most complicated tasks seem easy and a
                         pproachable.

                         However, ESTJs don’t work alone, and they expect their reliability and work ethic to be reciprocated 
                         – people with this personality type meet their promises, and if partners or subordinates jeopardize 
                         them through incompetence or laziness, or worse still, dishonesty, they do not hesitate to show 
                         their wrath. This can earn them a reputation for inflexibility, a trait shared by all Sentinel 
                         personalities, but it’s not because ESTJs are arbitrarily stubborn, 
                         but because they truly believe that these values are what make society work.

                         A Greater Responsibility
                         ESTJs are classic images of the model citizen: they help their neighbors, 
                         uphold the law, and try to make sure that everyone participates in the communities and 
                         organizations they hold so dear.
                         The main challenge for ESTJs is to recognize that not everyone follows the same path or contributes 
                         in the same way. A true leader recognizes the strength of the individual, as well as that of the 
                         group, and helps bring those individuals’ ideas to the table. That way, ESTJs really do have all the 
                         facts, and are able to lead the charge in directions that work for everyone.  """)
        case "ENTP":
            print("""
                         ENTP personalities

                         An (ENTP) is a person with the Extraverted, Intuitive, Thinking, and Prospecting personality traits. 
                         They tend to be bold and creative, deconstructing and rebuilding ideas with great mental agility. 
                         They pursue their goals vigorously despite any resistance they might encounter.
                         Quick-witted and audacious, ENTP aren’t afraid to disagree with the status quo. In fact, they’re not 
                         afraid to disagree with pretty much anything or anyone. Few things light up people with this personality 
                         type more than a bit of verbal sparring – and if the conversation veers into controversial terrain, 
                         so much the better.

                         ENTP are known for their rebellious streak. For this personality type, no belief is too sacred 
                         to be questioned, no idea is too fundamental to be scrutinized, and no rule is too important to 
                         be broken, or at least thoroughly tested. Sometimes ENTP even rebel against their own beliefs by 
                         arguing the opposing viewpoint – just to see how the world looks from the other side.
                         some of the weakness of the ENTP are that they have mental exercise of debating and to them, nothing
                          is sacred. They often misjudge others feelings and push their debtates well past others tolerance level. 
                          sometimes this personalities find it difficult to focus.
                         some of the Strength of this personality is that hey are very knowledgeable, they are quick thinkers, 
                         and excellent brainstormers. Their confidence, quick thought and ability to connect disparate ideas 
                         in novel ways create a style of communication that is charming, even entertaining, and informative 
                         at the same time.
                         """)

        case "ESFJ":
            print("""
                         ESFJ

                         A ESFJ (ESFJ) is a person with the Extraverted, Observant, Feeling, and Judging personality traits. 
                         They are attentive and people-focused, and they enjoy taking part in their social community. 
                         Their achievements are guided by decisive values, and they willingly offer guidance to others.

                         Encourage, lift, and strengthen one another. For the positive energy spread to one will be felt by us all.

                         DEBORAH DAY
                         For ESFJs, life is sweetest when it’s shared with others. People with this personality type form 
                         the bedrock of many communities, opening their homes – and their hearts – to friends, loved ones,
                          and neighbors.

                         This doesn’t mean that ESFJs like everyone, or that they’re saints. But ESFJs do believe in the power of 
                         hospitality and good manners, and they tend to feel a sense of duty to those around them. 
                         Generous and reliable, people with this personality type often take it upon themselves – in ways 
                         both large and small – to hold their families and their communities together.

                         ESFJs have a talent for making the people in their lives feel supported, cared for, and secure.

                         The Beauty of a Responsible Life
                         ESFJs are altruists. They take seriously their responsibilities to give back, serve others, and do 
                         the right thing.

                         And ESFJs believe that there is a clear right thing to do in nearly every situation. While some 
                         personality types adopt a more lenient, live-and-let-live attitude, ESFJs may find it difficult 
                         not to judge when someone takes a path that strikes them as misguided. As a result, ESFJs often 
                         struggle to accept it when someone – particularly someone they care about – disagrees with them.

                         ESFJs have a clear moral compass – and it can be nothing short of baffling to them when other people’s 
                         actions don’t align with it.
                         With their definite views on right and wrong, ESFJs tend to be on the opinionated side. But these 
                         opinions aren’t arbitrary – they’re often based on a deep respect for tradition. ESFJs know that 
                         everything they do affects someone else, and they trust that established laws, protocols, and 
                         social norms will help them navigate their everyday lives in a way that is considerate and 
                         responsible toward others.

                         Building Relationships That Last
                         Supportive and outgoing, ESFJs can always be spotted at a party – they’re the ones fluttering around 
                         making sure that everyone else is having a good time! But make no mistake: ESFJs don’t just breeze through 
                         other people’s lives. Loyal to the core, they build lasting relationships, and they can be counted on 
                         to show up whenever a helping hand – or a listening ear – is needed.

                         ESFJs rarely miss a birthday or holiday. Devoted to their relationships, they commit even the smallest 
                         details of their friends’ and loved ones’ lives to memory.
                         With their love of order and structure, ESFJs prefer planned events to open-ended activities or 
                         spontaneous get-togethers – and they’re happy to host in order to ensure that everything goes smoothly. 
                         People with this personality type put a great deal of energy into making other people feel special and 
                         celebrated, and they may take it personally when someone doesn’t seem to appreciate their efforts.

                         For many people with the ESFJ personality type, one of life’s greatest challenges is accepting that 
                         they can’t control anyone else’s thoughts or behavior – not even those who are nearest and dearest to them. 
                         Fortunately, ESFJs can find peace and fulfillment by focusing on what they do best: setting an example of care,
                          consideration, and responsibility – and bringing people together in the process.
                         """)

        case "ESTP":
            print("""
                        An ESTP 
                        ESTP is someone with the Extraverted, Observant, Thinking, and Prospecting personality traits. 
                        They tend to be energetic 
                        and action-oriented, deftly navigating whatever is in front of them. They love uncovering life’s 
                        opportunities, whether socializing with others or in more personal pursuits.

                       ESTPs always have an impact on their immediate surroundings – the best way to spot them at a party
                       is to look for the whirling eddy of people flitting about them as they move from group to group. 
                       Laughing and entertaining with a blunt and earthy humor, ESTP personalities love to be the center of attention.
                       If an audience member is asked to come on stage, ESTPs volunteer – or volunteer a shy friend.

                       Theory, abstract concepts and plodding discussions about global issues and their implications don’t 
                       keep ESTPs interested for long. ESTPs keep their conversation energetic, with a good dose of intelligence, 
                       but they like to talk about what is – or better yet, to just go out and do it. ESTPs leap before they look,
                       fixing their mistakes as they go, rather than sitting idle, preparing contingencies and escape clauses.


                       Diving Right In
                       ESTPs are the likeliest personality type to make a lifestyle of risky behavior. They live in the 
                       moment and dive into the action – they are the eye of the storm. People with the ESTP personality 
                       type enjoy drama, passion, and pleasure, not for emotional thrills, but because it’s so stimulating to their 
                       logical minds. They are forced to make critical decisions based on factual, immediate reality in a process 
                       of rapid-fire rational stimulus response.

                       This makes school and other highly organized environments a challenge for ESTPs. It certainly isn’t 
                       because they aren’t smart, and they can do well, but the regimented, lecturing approach of formal 
                       education is just so far from the hands-on learning that ESTPs enjoy. It takes a great deal of maturity to see
                       this process as a necessary means to an end, something that creates more exciting opportunities.

                       Also challenging is that to ESTPs, it makes more sense to use their own moral compass than someone 
                       else’s. Rules were made to be broken. This is a sentiment few high school instructors or corporate 
                       supervisors are likely to share, and can earn ESTP personalities a certain reputation. But if they minimize 
                       the trouble-making, harness their energy, and focus through the boring stuff, ESTPs are a force to be reckoned
                        with.

                      The Path Less Traveled
                      With perhaps the most perceptive, unfiltered view of any type, ESTPs have a unique skill in 
                      noticing small changes. Whether a shift in facial expression, a new clothing style, or a broken habit, 
                      people with this personality type pick up on hidden thoughts and motives where most types would be lucky 
                      to pick up anything specific at all. ESTPs use these observations immediately, calling out the change and
                      asking questions, often with little regard for sensitivity. ESTPs should remember that not everyone wants 
                      their secrets and decisions broadcast.
                         """)

        case "INFJ":
            print("""
                         An Advocate (INFJ) is someone with the Introverted, Intuitive, Feeling, and Judging personality traits. 
                         They tend to approach life with deep thoughtfulness and imagination. Their inner vision, personal values, 
                         and a quiet, principled version of humanism guide them in all things.

                         “Treat people as if they were what they ought to be and you help them to become what they are capable 
                         of being.”

                         (INFJs) may be the rarest personality type of all, but they certainly leave their mark on the world. 
                         Idealistic and principled, they aren’t content to coast through life – they want to stand up and make 
                         a difference. For Advocate personalities, success doesn’t come from money or status but from seeking 
                         fulfillment, helping others, and being a force for good in the world.

                         While they have lofty goals and ambitions, INFJs shouldn’t be mistaken for idle dreamers. People with 
                         this personality type care about integrity, and they’re rarely satisfied until they’ve done what 
                         they know to be right. Conscientious to the core, they move through life with a clear sense of their values, 
                         and they aim never to lose sight of what truly matters – not according to other people or society at large,
                          but according to their own wisdom and intuition.

                         Perhaps because their personality type is so uncommon, INFJs tend to carry around a sense – whether 
                         conscious or not – of being different from most people. With their rich inner lives and their deep, 
                         abiding desire to find their life purpose, they don’t always fit in with those around them. This isn’t 
                         to say that Advocates can’t enjoy social acceptance or close relationships – only that they sometimes 
                         feel misunderstood or at odds with the world.

                         INFJ may be Introverted, but they value deep, authentic relationships with others. Few things bring 
                         these personalities as much joy as truly knowing another person – and being known in return. 
                         Advocates enjoy meaningful conversations far more than small talk, and they tend to communicate 
                         in a way that is warm and sensitive
                         """)

        case "INFP":
            print("""
                            A  (INFP) is someone who possesses the Introverted, Intuitive, Feeling, and Prospecting personality 
                         traits. These rare personality types tend to be quiet, open-minded, and imaginative, and they 
                         apply a caring and creative approach to everything they do.

                         Although they may seem quiet or unassuming,  (INFPs) have vibrant, passionate inner lives.
                         Creative and imaginative, they happily lose themselves in daydreams, inventing all sorts of stories 
                         and conversations in their minds. These personalities are known for their sensitivity – INFP can 
                         have profound emotional responses to music, art, nature, and the people around them.

                         Idealistic and empathetic, INFP long for deep, soulful relationships, and they feel called to
                         help others. But because this personality type makes up such a small portion of the population, 
                         INFPs may sometimes feel lonely or invisible, adrift in a world that doesn’t seem to appreciate 
                         the traits that make them unique.

                         Empathy is among this personality type’s greatest gifts, but at times it can be a liability. 
                         The troubles of the world weigh heavily on INFP’ shoulders, and these personalities can be 
                         vulnerable to internalizing other people’s negative moods or mindsets. Unless they learn to set 
                         boundaries, INFP may feel overwhelmed by just how many wrongs there are that need to be set right.

                         People with this personality type tend to feel directionless or stuck until they connect with 
                         a sense of purpose for their lives. For many INFP, this purpose has something to do with 
                         uplifting others and their ability to feel other people’s suffering as if it were their own. 
                         While INFP want to help everyone, they need to focus their energy and efforts – otherwise, they 
                         can end up exhausted.
                         """)

        case "INTJ":
            print("""
                            A (INFP) is someone who possesses the Introverted, Intuitive, Feeling, and Prospecting personality 
                         traits. These rare personality types tend to be quiet, open-minded, and imaginative, and they apply 
                         a caring and creative approach to everything they do.

                         Although they may seem quiet or unassuming,  (INFPs) have vibrant, passionate inner lives. Creative 
                         and imaginative, they happily lose themselves in daydreams, inventing all sorts of stories and 
                         conversations in their minds. These personalities are known for their sensitivity – INFP can have 
                         profound emotional responses to music, art, nature, and the people around them.

                         Idealistic and empathetic, INFP long for deep, soulful relationships, and they feel called to help 
                         others. But because this personality type makes up such a small portion of the population, INFPs 
                         may sometimes feel lonely or invisible, adrift in a world that doesn’t seem to appreciate the traits 
                         that make them unique.

                         Empathy is among this personality type’s greatest gifts, but at times it can be a liability. 
                         The troubles of the world weigh heavily on INFP’ shoulders, and these personalities can be vulnerable 
                         to internalizing other people’s negative moods or mindsets. Unless they learn to set boundaries, 
                         INFP may feel overwhelmed by just how many wrongs there are that need to be set right.

                         People with this personality type tend to feel directionless or stuck until they connect with a 
                         sense of purpose for their lives. For many INFP, this purpose has something to do with uplifting 
                         others and their ability to feel other people’s suffering as if it were their own. While INFP want to 
                         help everyone, they need to focus their energy and efforts – otherwise, they can end up exhausted.
                         """)

        case "INTP":
            print("""
                         INTP personalities
                         A (INTP) is someone with the Introverted, Intuitive, Thinking, and Prospecting personality traits. 
                         These flexible thinkers enjoy taking an unconventional approach to many aspects of life. 
                         They often seek out unlikely paths, mixing willingness to experiment with personal creativity.
                         INTP often lose themselves in thought – which isn’t necessarily a bad thing. People with this 
                         personality type hardly ever stop thinking. From the moment they wake up, their minds buzz with ideas, 
                         questions, and insights. At times, they may even find themselves conducting full-fledged debates 
                         in their own heads.
                         People with this personality type want to understand everything in the universe, but one area 

                         in particular tends to mystify them: human nature. As their name suggests, Logicians feel 
                         most at home in the realm of logic and rationality. As a result, they can find themselves 
                         baffled by the illogical, irrational ways that feelings and emotions influence people’s behavior
                         – including their own.

                         Some of this personality strength is that they analyze everything that they come across, 
                         from research data to the behavior of the people around them. Thanks to their unrelenting 
                         imagination, Logicians can come up with creative, counterintuitive ideas that wouldn’t occur 
                         to most people. Logicians are driven by curiosity and an intense desire to learn everything that 
                         they can. These personalities are always casting about for new pursuits, hobbies, and areas of research. 
                         they care about the truth. Rather than taking comfort in ideology or received ideas, they want to understand 
                         what’s really going on beneath the surface of things.
                         """)
        case "ISFJ":
            print("""
                         ISFJ
                         A ISFJ () is someone with the Introverted, Observant, Feeling, and Judging personality traits. 
                         These people tend to be warm and unassuming in their own steady way. They’re efficient and responsible, 
                         giving careful attention to practical details in their daily lives.

                         Love only grows by sharing. You can only have more for yourself by giving it away to others.

                         BRIAN TRACY
                         In their unassuming, understated way, ISFJs help make the world go round. Hardworking and devoted, 
                         people with this personality type feel a deep sense of responsibility to those around them. 
                         ISFJs can be counted on to meet deadlines, remember birthdays and special occasions, uphold traditions, 
                         and shower their loved ones with gestures of care and support. But they rarely demand recognition for 
                         all that they do, preferring instead to operate behind the scenes.

                         This is a capable, can-do personality type, with a wealth of versatile gifts. Though sensitive 
                         and caring, ISFJs also have excellent analytical abilities and an eye for detail. And despite their 
                         reserve, they tend to have well-developed people skills and robust social relationships. 
                         ISFJs are truly more than the sum of their parts, and their varied strengths shine in even the most 
                         ordinary aspects of their daily lives.

                         ISFJs are true altruists, meeting kindness with kindness-in-excess and engaging with the work 
                         and people they believe in with enthusiasm and generosity.

                         The Gift of Loyalty
                         Among ISFJs’ most distinctive traits is loyalty. Rare is the ISFJ who allows a friendship or 
                         relationship to fade away from lack of effort. Instead, they invest a great deal of energy into 
                         maintaining strong connections with their loved ones – and not just by sending “How are you doing?” texts.
                         People with this personality type are known for dropping everything and lending a hand whenever a 
                         friend or family member is going through a hard time.

                         ISFJs tend to feel most energized and effective when they’re showing up for someone who needs their help.
                         ISFJs’ sense of loyalty doesn’t stop with their nearest and dearest – it often extends to their communities,
                         their employers, and even family traditions. But the intensity of their commitment and desire to 
                         serve can have its downsides. Other people may take advantage of ISFJs’ helpful, hardworking nature, 
                         leaving them feeling burned out and overworked. And ISFJs may feel guilty or stressed when they 
                         contemplate changes – even necessary changes – to themselves, their relationships, or the way 
                         they’ve done things in the past.

                         The Highest of Standards
                         For ISFJs, “good enough” is rarely good enough. People with this personality type can be 
                         meticulous to the point of perfectionism. They take their responsibilities personally, consistently 
                         going above and beyond and doing everything that they can to exceed others’ expectations.

                         ISFJ personalities are known for their humility, and they rarely seek the spotlight.
                         But what happens when ISFJs’ efforts go unnoticed or unappreciated? While ISFJs tend to underplay
                          their accomplishments, that doesn’t mean that they don’t enjoy recognition – or that they’re fine 
                          with being taken for granted. Unless they learn to stand up for themselves, ISFJs may find 
                          themselves quietly losing their enthusiasm and motivation, eventually becoming resentful toward 
                          the people who just don’t seem to appreciate them.

                         Showing Up for Others – and Themselves
                         Although they’re Introverted, ISFJs have a deeply social nature. Thanks to their ability to remember 
                         the details of other people’s lives, ISFJs have a special talent for making their friends and 
                         acquaintances feel seen, known, and cherished. Few personality types can match ISFJs’ ability to choose 
                         just the right gift for any occasion, whether large or small.

                         Dedicated and thoughtful, ISFJs find great joy in helping those around them build stable, secure, 
                         and happy lives. It may not be easy for people with this personality type to show up for themselves 
                         in the way that they show up for other people, but when they do, they often find themselves with 
                         even more energy and motivation to do good in the world.
                         """)

        case "ISTJ":
            print("""
                         ISTJ
                         A Logistician (ISTJ) is someone with the Introverted, Observant, Thinking, and Judging personality 
                         traits. These people tend to be reserved yet willful, with a rational outlook on life. 
                         They compose their actions carefully and carry them out with methodical purpose.

                         ISTJ pride themselves on their integrity. People with this personality type mean what they say, 
                         and when they commit to doing something, they make sure to follow through.

                         This personality type makes up a good portion of the overall population, and 
                         while ISTJ may not be particularly flashy or attention-seeking, they do more than their share to 
                         keep society on a sturdy, stable foundation. In their families and their communities, ISTJ 
                         often earn respect for their reliability, their practicality, and their ability to stay grounded and logical, 
                         even in the most stressful situations.

                         The core of ISTJ’ self-respect comes from a sense of personal integrity. People with this personality 
                         type believe that there is a right way to proceed in any situation – and that anyone who pretends 
                         otherwise is probably trying to bend the rules to suit their own purposes. ISTJ have a deep respect 
                         for structure and tradition, and they are often drawn to organizations, workplaces, and educational 
                         settings that offer clear hierarchies and expectations.

                         For many ISTJ, a lack of structure offers not freedom, but chaos.
                         People with the Logistician personality type rarely hesitate to take responsibility for their actions 
                         and choices. Generally speaking, they are quick to own up to their own mistakes, admitting the truth 
                         even if it doesn’t make them look good. To ISTJ, honesty is far more important than showmanship, 
                         and they’d rather satisfy their own conscience than lie to impress someone else.

                         ISTJ’ dedication is an admirable quality, and it drives many of their accomplishments. 
                         But it can also become a weakness that other people take advantage of. With their strong work ethic 
                         and sense of duty, ISTJ may routinely find themselves shouldering other people’s responsibilities. 
                         Even if they don’t complain about the situation, ISTJ can end up exhausted or discouraged if they’re 
                         constantly expected – or taking it upon themselves – to pick up the slack for their colleagues, 
                         friends, or loved ones.
                         """)

        case "ISTP":
            print("""
                          An ISFP (ISFP) is a person with the Introverted, Observant, Feeling, and Prospecting personality traits. 
                         They tend to have open minds, approaching life, new experiences, and people with grounded warmth. 
                         Their ability to stay in the moment helps them uncover exciting potentials.

                         I change during the course of a day. I wake and I’m one person, and when I go to sleep I know for 

                         certain I’m somebody else.

                         BOB DYLAN
                         ISFPs are true artists – although not necessarily in the conventional sense. For this personality type, 
                         life itself is a canvas for self-expression. From what they wear to how they spend their free time, 
                         ISFPs act in ways that vividly reflect who they are as unique individuals.

                         And every ISFP is certainly unique. Driven by curiosity and eager to try new things, people with this 
                         personality often have a fascinating array of passions and interests. With their exploratory spirits and 
                         their ability to find joy in everyday life, ISFPs can be among the most interesting people you’ll ever meet. 
                         The only irony? Unassuming and humble, ISFPs tend to see themselves as “just doing their own thing,” 
                         so they may not even realize how remarkable they really are.


                         The Beauty of an Open Mind
                         ISFPs embrace a flexible, adaptable approach to life. Some personality types thrive on strict schedules 

                        and routines – but not ISFPs. ISFPs take each day as it comes, doing what feels right to them in the moment. 
                        And they make sure to leave plenty of room in their lives for the unexpected – with the result that many of 
                        their most cherished memories are of spontaneous, spur-of-the-moment outings and adventures, whether by themselves 
                        or with their loved ones.

                         This flexible mindset makes ISFPs remarkably tolerant and open-minded. These personalities genuinely
                          love living in a world filled with all kinds of people – even people who disagree with them or choose 
                          radically different lifestyles. It’s no surprise, then, that ISFPs are unusually open to changing their minds 
                          and rethinking their opinions. If any personality type believes in giving something (or someone) a second chance,
                           it’s ISFPs.

                         ISFPs want to live in a world where they – and everyone else – have the freedom to live as they see fit, 
                         without judgment.
                         That said, ISFPs’ go-with-the-flow mentality can have its downsides. People with this personality type 
                         may struggle to set long-term plans – let alone stick with them. As a result, ISFPs tend to have 
                         a pretty cloudy view of their ability to achieve their goals, and they often worry about letting other 
                         people down. ISFPs may find that adding a little structure to their lives goes a long way toward helping 
                         them feel more capable and organized – without quashing their independent spirits.

                         Living in Harmony
                         In their relationships, ISFPs are warm, friendly, and caring, taking wholehearted enjoyment in the
                          company of their nearest and dearest. But make no mistake: this is an Introverted personality type, 
                          meaning that ISFPs need dedicated alone time to recharge their energy after socializing with others.
                           This alone time is what allows ISFPs to reestablish a sense of their own identity – in other words, 
                           to reconnect with who they truly are.
                         """)
        case "ISFP":
            print("""
                         An ISFP (ISFP) is a person with the Introverted, Observant, Feeling, and Prospecting personality traits. 
                         They tend to have open minds, approaching life, new experiences, and people with grounded warmth. 
                         Their ability to stay in the moment helps them uncover exciting potentials.

                         I change during the course of a day. I wake and I’m one person, and when I go to sleep I know for 
                         certain I’m somebody else.

                         BOB DYLAN
                         ISFPs are true artists – although not necessarily in the conventional sense. For this personality type, 
                         life itself is a canvas for self-expression. From what they wear to how they spend their free time, 
                         ISFPs act in ways that vividly reflect who they are as unique individuals.

                         And every ISFP is certainly unique. Driven by curiosity and eager to try new things, people with this personality 
                         often have a fascinating array of passions and interests. With their exploratory spirits and their 
                         ability to find joy in everyday life, ISFPs can be among the most interesting people you’ll ever meet. 
                         The only irony? Unassuming and humble, ISFPs tend to see themselves as “just doing their own thing,” 
                         so they may not even realize how remarkable they really are.


                         The Beauty of an Open Mind
                         ISFPs embrace a flexible, adaptable approach to life. Some personality types thrive on strict schedules 
                         and routines – but
                         not ISFPs. ISFPs take each day as it comes, doing what feels right to them in the moment. And they make sure to 
                         leave plenty of room in their lives for the unexpected – with the result that many of their most cherished memories 
                         are of spontaneous, spur-of-the-moment outings and adventures, whether by themselves or with their loved ones.

                         This flexible mindset makes ISFPs remarkably tolerant and open-minded. These personalities genuinely love living in 
                         a world filled with all kinds of people – even people who disagree with them or choose radically different lifestyles. 
                         It’s no surprise, then, that ISFPs are unusually open to changing their minds and rethinking their opinions.
                         If any personality type believes in giving something (or someone) a second chance, it’s ISFPs.

                         ISFPs want to live in a world where they – and everyone else – have the freedom to live as they see fit, 
                         without judgment.
                         That said, ISFPs’ go-with-the-flow mentality can have its downsides. People with this personality 
                         type may struggle to set long-term plans – let alone stick with them. As a result, ISFPs tend to 
                         have a pretty cloudy view of their ability to achieve their goals, and they often worry about letting 
                         other people down. ISFPs may find that adding a little structure to their lives goes a long way toward 
                         helping them feel more capable and organized – without quashing their independent spirits.

                         Living in Harmony
                         In their relationships, ISFPs are warm, friendly, and caring, taking wholehearted enjoyment in
                         the company of their nearest and dearest. But make no mistake: this is an Introverted personality type,
                         meaning that ISFPs need dedicated alone time to recharge their energy after socializing with others. 
                         This alone time is what allows ISFPs to reestablish a sense of their own identity – in other words,
                          to reconnect with who they truly are.
                         """)

        case "ENTJ":
            print("""
                         ENTJ personalities
                         A (ENTJ) is someone with the Extraverted, Intuitive, Thinking, and Judging personality traits. 
                         They are decisive people who love momentum and accomplishment. They gather information to construct 
                         their creative visions but rarely hesitate for long before acting on them.
                         If there’s anything ENTJs love,it’s a good challenge, big or small, and they firmly
                         believe that given enough time and resources, they can achieve any goal. This quality makes people
                         with the Commander personality type brilliant entrepreneurs, and their ability to think strategically
                          and hold a long-term focus while executing each step of their plans with determination and precision 
                          makes them powerful business leaders.

                          ENTJs see inefficiency not just as a problem in its own right, but as something that pulls time and 
                          energy away from all their future goals, an elaborate sabotage consisting of irrationality and laziness. 
                          People with the Commander personality type will root out such behavior wherever they go.
                         Energetic – Rather than finding this process taxing Commanders are energized by it, genuinely enjoying 
                         leading their teams forward as they implement their plans and goals.
                         ENTJ couldn’t do this if they were plagued by self-doubt – they trust their abilities, make known 
                         their opinions, and believe in their capacities as leaders.
                         Strong-Willed – Nor do they give up when the going gets tough – Commander personalities strive 
                         to achieve their goals, but really nothing is quite as satisfying to them as rising to the challenge
                          of each obstacle in their run to the finish line.
                         ENTJ exemplify the difference between moment-to-moment crisis management and navigating the challenges 
                         and steps of a bigger plan, and are known for examining every angle of a problem and not just 
                         resolving momentary issues, but moving the whole project forward with their solutions. 
                         These qualities combine to create individuals who are able to inspire and invigorate others,
                          who people actually want to be their leaders, and this in turn helps Commanders to accomplish 
                          their often ambitious goals that could never be finished alone.
                          """)
        case "ESFP":
            print("""
                         An ESFP\s
                         ESFP is a person with the Extraverted, Observant, Feeling, and Prospecting personality traits. 
                         These people love vibrant experiences, engaging in life eagerly and taking pleasure in discovering 
                         the unknown. They can be very social, often encouraging others into shared activities.


                         If anyone is to be found spontaneously breaking into song and dance, it is the ESFP personality type. 
                         ESFPs get caught up in the excitement of the moment, and want everyone else to feel that way, 
                         too. No other personality type is as generous with their time and energy as ESFPs when it comes to 
                         encouraging others, and no other personality type does it with such irresistible style.

                         Living with Passion
                         ESFPs love the spotlight, and all the world’s a stage. Many famous people with the ESFP personality 
                         type are indeed actors, but they love putting on a show for their friends too, chatting with a 
                         unique and earthy wit, soaking up attention and making every outing feel a bit like a party. Utterly social, 
                         ESFPs enjoy the simplest things, and there’s no greater joy for them than just having fun with a good group 
                         of friends.

                         It’s not just talk either – ESFPs have the strongest aesthetic sense of any personality type. 
                         From grooming and outfits to a well-appointed home, ESFP personalities have an eye for fashion. 
                         Knowing what’s attractive the moment they see it, ESFPs aren’t afraid to change their surroundings 
                         to reflect their personal style. ESFPs are naturally curious, exploring new designs and styles with ease.

                         Though it may not always seem like it, ESFPs know that it’s not all about them – they are observant,
                         and very sensitive to others’ emotions. People with this personality type are often the first to 
                         help someone talk out a challenging problem, happily providing emotional support and practical advice. 
                         However, if the problem is about them, ESFPs are more likely to avoid a conflict altogether than to address 
                         it head-on. ESFPs usually love a little drama and passion, but not so much when they are the focus of the 
                         criticisms it can bring.

                         A Spontaneous Spirit
                         The biggest challenge ESFPs face is that they are often so focused on immediate pleasures that 
                         they neglect the duties and responsibilities that make those luxuries possible. Complex analysis, 
                         repetitive tasks, and matching statistics to real consequences are not easy activities for ESFPs. 
                         They’d rather rely on luck or opportunity, or simply ask for help from their extensive circle of friends. 
                         It is important for ESFPs to challenge themselves to keep track of long-term things like their retirement 
                         plans or sugar intake – there won’t always be someone else around who can help to keep an eye on these things.

                         ESFPs recognize value and quality, which on its own is a fine trait. In combination with their 
                         tendency to be poor planners though, this can cause them to live beyond their means, and credit cards 
                         are especially dangerous. More focused on leaping at opportunities than in planning out long-term goals, 
                         ESFPs may find that their inattentiveness has made some activities unaffordable.

                         There’s nothing that makes ESFPs feel quite as unhappy as realizing that they are boxed in by
                          circumstance, unable to join their friends.
                         ESFPs are welcome wherever there’s a need for laughter, playfulness, and a volunteer to try 
                         something new and fun – and there’s no greater joy for ESFP personalities than to bring everyone else 
                         along for the ride. ESFPs can chat for hours, sometimes about anything but the topic they meant to talk about,
                          and share their loved ones’ emotions through good times and bad. If they can just remember to keep their 
                          ducks in a row, they’ll always be ready to dive into all the new and exciting things the world has to offer, 
                          friends in tow.

                         """)


def main():
    question1()



if __name__ == "__main__":
    main()
