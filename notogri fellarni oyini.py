import random,os
import datetime as dt

author = f"Muallif: Saydullayev Asadbek"

fayl1 = ['be', 'bear', 'beat', 'become', 'begin', 'bite', 'blow', 'break', 'bring', 'build', 'burn', 'burst', 'buy', 'can', 'catch', 'choose', 'come', 'cost', 'cut', 'deal', 'dig', 'do', 'draw', 'dream', 'drink', 'drive', 'eat', 'fall', 'feed', 'feel', 'fight', 'find', 'fly', 'forbid', 'forget', 'forgive', 'freeze', 'get', 'give', 'go', 'grow', 'hang', 'have', 'hear', 'hide', 'hit', 'hold', 'hurt', 'keep', 'know', 'lay', 'lead', 'learn', 'leave', 'lend', 'let', 'lie', 'light', 'lose', 'make', 'mean', 'meet', 'pay', 'put', 'read', 'ride', 'ring', 'rise', 'run', 'say', 'see', 'seek', 'sell', 'send', 'sew', 'shake', 'shine', 'shoot', 'show', 'shut', 'sing', 'sit', 'sleep', 'smell', 'speak', 'spell', 'spend', 'spill', 'split', 'spoil', 'spread', 'spring', 'stand', 'steal', 'stick', 'sting', 'strike', 'swear', 'sweep', 'swim', 'take', 'teach', 'tear', 'tell', 'think', 'throw', 'understand', 'wake', 'wear', 'win', 'write']
fayl2 = {'be': ['was', "Bo'lmoq"], 'bear': ['bore', "Tug'ulmoq, tug'ulgan"], 'beat': ['beat', 'Urmoq'], 'become': ['became', "Bo'lmoq,erishmoq"], 'begin': ['began', 'Boshlamoq'], 'bite': ['bit', 'Tishlamoq'], 'blow': ['blew', 'Esmoq, puflamoq'], 'break': ['broke', 'Sindirmoq'], 'bring': ['brought', 'Olib kelmoq'], 'build': ['built', 'Qurmoq'], 'burn': ['burnt', 'Yonmoq'], 'burst': ['burst', 'Portlamoq'], 'buy': ['bought', 'Sotib olmoq'], 'can': ['could', 'Qila olmoq'], 'catch': ['caught', 'Tutmoq, ushlamoq'], 'choose': ['chose', 'Tanlamoq'], 'come': ['came', 'Kelmoq'], 'cost': ['cost', 'Narxi turmoq'], 'cut': ['cut', 'Kesmoq'], 'deal': ['dealt', 'Kelishuv, bitim'], 'dig': ['dug', 'Qazimoq'], 'do': ['did', 'Qilmoq, bajarmoq'], 'draw': ['drew', 'Chizmoq'], 'dream': ['dreamt', "Tush ko'rmoq"], 'drink': ['drank', 'Ichmoq'], 'drive': ['drove', 'Minmoq'], 'eat': ['ate', 'Yemoq'], 'fall': ['fell', 'Yiqilmoq'], 'feed': ['fed', 'Ovqatlantirmoq, boqmoq'], 'feel': ['felt', 'His qilmoq'], 'fight': ['fought', 'Urushmoq, kurashmoq'], 'find': ['found', 'Topmoq'], 'fly': ['flew', 'Uchmoq'], 'forbid': ['forbade', 'Taqiqlamoq'], 'forget': ['forgot', 'Unutmoq'], 'forgive': ['forgave', 'Kechirmoq'], 'freeze': ['froze', 'Muzlatmoq'], 'get': ['got', 'Olmoq'], 'give': ['gave', 'Bermoq'], 'go': ['went', 'Bormoq'], 'grow': ['grew', "O'smoq"], 'hang': ['hung', 'Osmoq, ilmoq'], 'have': ['had', "Bor bo'lmoq"], 'hear': ['heard', 'Eshitmoq'], 'hide': ['hid', 'Yashirinmoq, berkitmoq'], 'hit': ['hit', 'Urmoq, zarba bermoq'], 'hold': ['held', 'Ushlamoq'], 'hurt': ['hurt', 'Jarohatlamoq, zarar yetkazmoq'], 'keep': ['kept', 'Saqlamoq'], 'know': ['knew', 'Bilmoq'], 'lay': ['laid', "Qo'ymoq"], 'lead': ['led', 'Yetaklamoq, boshlab bormoq'], 'learn': ['learnt', "O'rganmoq"], 'leave': ['left', 'Tark etmoq'], 'lend': ['lent', 'Qarz bermoq'], 'let': ['let', 'Ruxsat bermoq'], 'lie': ['lay', 'Yotmoq, aldamoq'], 'light': ['lit', 'Yoqmoq (chiroqni)'], 'lose': ['lost', "Yo'qotmoq"], 'make': ['made', 'Bajarmoq, yaratmoq, qilmoq'], 'mean': ['meant', 'Anglatmoq'], 'meet': ['met', 'Uchratmoq, uchrashmoq'], 'pay': ['paid', "To'lamoq"], 'put': ['put', "Qo'ymoq"], 'read': ['read', "O'qimoq"], 'ride': ['rode', 'Minmoq (ot yoki velosiped)'], 'ring': ['rang', 'Jiringlamoq'], 'rise': ['rose', "Ko'tarilmoq"], 'run': ['ran', 'Yugurmoq'], 'say': ['said', 'Aytmoq'], 'see': ['saw', "Ko'rmoq"], 'seek': ['sought', 'Qidirmoq'], 'sell': ['sold', 'Sotmoq'], 'send': ['sent', "Jo'natmoq"], 'sew': ['sewed', 'Tikmoq'], 'shake': ['shook', 'Titramoq, silkitmoq'], 'shine': ['shone', 'Nur sochmoq'], 'shoot': ['shot', 'Otmoq'], 'show': ['showed', "Ko'rsatmoq"], 'shut': ['shut', 'Yopmoq, berkitmoq'], 'sing': ['sang', 'Kuylamoq'], 'sit': ['sat', "O'tirmoq"], 'sleep': ['slept', 'Uxlamoq'], 'smell': ['smelt', 'Xidlamoq'], 'speak': ['spoke', 'Gapirmoq'], 'spell': ['spelt', "Xariflab o'qimoq"], 'spend': ['spent', 'Sarflamoq'], 'spill': ['spilt', "To'kmoq"], 'split': ['split', "Uzunasiga bo'lmoq, yorilish, tilinish"], 'spoil': ['spoilt', 'Buzmoq'], 'spread': ['spread', 'Tarqalmoq, yoymoq, surtmoq, surkamoq, solmoq'], 'spring': ['sprang', 'Sakramoq'], 'stand': ['stood', 'Turmoq'], 'steal': ['stole', "O'g'rilamoq"], 'stick': ['stuck', 'Sanchmoq, suqmoq'], 'sting': ['stung', 'Nayzasini suqmoq'], 'strike': ['struck', 'Urmoq, gugurt chaqmoq'], 'swear': ['swore', "So'kinmoq, qasam ichmoq"], 'sweep': ['swept', 'Supurmoq'], 'swim': ['swam', 'Suzmoq'], 'take': ['took', 'Olmoq'], 'teach': ['taught', "O'qitmoq"], 'tear': ['tore', 'Yirtmoq'], 'tell': ['told', 'Aytmoq'], 'think': ['thought', "O'ylamoq"], 'throw': ['threw', 'Otmoq, uloqtirmoq'], 'understand': ['understood', 'Tushunmoq'], 'wake': ['woke', "Uyg'onmoq"], 'wear': ['wore', 'Kiymoq'], 'win': ['won', "G'alaba qilmoq, yutmoq"], 'write': ['wrote', 'Yozmoq']}
fayl3 = {'be': ['been', "Bo'lmoq"], 'bear': ['born', "Tug'ulmoq, tug'ulgan"], 'beat': ['beaten', 'Urmoq'], 'become': ['become', "Bo'lmoq,erishmoq"], 'begin': ['begun', 'Boshlamoq'], 'bite': ['bitten', 'Tishlamoq'], 'blow': ['blown', 'Esmoq, puflamoq'], 'break': ['broken', 'Sindirmoq'], 'bring': ['brought', 'Olib kelmoq'], 'build': ['built', 'Qurmoq'], 'burn': ['burnt', 'Yonmoq'], 'burst': ['burst', 'Portlamoq'], 'buy': ['bought', 'Sotib olmoq'], 'can': ['been able to', 'Qila olmoq'], 'catch': ['caught', 'Tutmoq, ushlamoq'], 'choose': ['chosen', 'Tanlamoq'], 'come': ['come', 'Kelmoq'], 'cost': ['cost', 'Narxi turmoq'], 'cut': ['cut', 'Kesmoq'], 'deal': ['dealt', 'Kelishuv, bitim'], 'dig': ['dug', 'Qazimoq'], 'do': ['done', 'Qilmoq, bajarmoq'], 'draw': ['drawn', 'Chizmoq'], 'dream': ['dreamt', "Tush ko'rmoq"], 'drink': ['drunk', 'Ichmoq'], 'drive': ['driven', 'Minmoq'], 'eat': ['eaten', 'Yemoq'], 'fall': ['fallen', 'Yiqilmoq'], 'feed': ['fed', 'Ovqatlantirmoq, boqmoq'], 'feel': ['felt', 'His qilmoq'], 'fight': ['fought', 'Urushmoq, kurashmoq'], 'find': ['found', 'Topmoq'], 'fly': ['flown', 'Uchmoq'], 'forbid': ['forbidden', 'Taqiqlamoq'], 'forget': ['forgotten', 'Unutmoq'], 'forgive': ['forgiven', 'Kechirmoq'], 'freeze': ['frozen', 'Muzlatmoq'], 'get': ['got', 'Olmoq'], 'give': ['given', 'Bermoq'], 'go': ['gone', 'Bormoq'], 'grow': ['grown', "O'smoq"], 'hang': ['hung', 'Osmoq, ilmoq'], 'have': ['had', "Bor bo'lmoq"], 'hear': ['heard', 'Eshitmoq'], 'hide': ['hidden', 'Yashirinmoq, berkitmoq'], 'hit': ['hit', 'Urmoq, zarba bermoq'], 'hold': ['held', 'Ushlamoq'], 'hurt': ['hurt', 'Jarohatlamoq, zarar yetkazmoq'], 'keep': ['kept', 'Saqlamoq'], 'know': ['known', 'Bilmoq'], 'lay': ['laid', "Qo'ymoq"], 'lead': ['led', 'Yetaklamoq, boshlab bormoq'], 'learn': ['learnt', "O'rganmoq"], 'leave': ['left', 'Tark etmoq'], 'lend': ['lent', 'Qarz bermoq'], 'let': ['let', 'Ruxsat bermoq'], 'lie': ['lain', 'Yotmoq, aldamoq'], 'light': ['lit', 'Yoqmoq (chiroqni)'], 'lose': ['lost', "Yo'qotmoq"], 'make': ['made', 'Bajarmoq, yaratmoq, qilmoq'], 'mean': ['meant', 'Anglatmoq'], 'meet': ['met', 'Uchratmoq, uchrashmoq'], 'pay': ['paid', "To'lamoq"], 'put': ['put', "Qo'ymoq"], 'read': ['read', "O'qimoq"], 'ride': ['ridden', 'Minmoq (ot yoki velosiped)'], 'ring': ['rung', 'Jiringlamoq'], 'rise': ['risen', "Ko'tarilmoq"], 'run': ['run', 'Yugurmoq'], 'say': ['said', 'Aytmoq'], 'see': ['seen', "Ko'rmoq"], 'seek': ['sought', 'Qidirmoq'], 'sell': ['sold', 'Sotmoq'], 'send': ['sent', "Jo'natmoq"], 'sew': ['sewn', 'Tikmoq'], 'shake': ['shaken', 'Titramoq, silkitmoq'], 'shine': ['shone', 'Nur sochmoq'], 'shoot': ['shot', 'Otmoq'], 'show': ['shown', "Ko'rsatmoq"], 'shut': ['shut', 'Yopmoq, berkitmoq'], 'sing': ['sung', 'Kuylamoq'], 'sit': ['sat', "O'tirmoq"], 'sleep': ['slept', 'Uxlamoq'], 'smell': ['smelt', 'Xidlamoq'], 'speak': ['spoken', 'Gapirmoq'], 'spell': ['spelt', "Xariflab o'qimoq"], 'spend': ['spent', 'Sarflamoq'], 'spill': ['spilt', "To'kmoq"], 'split': ['split', "Uzunasiga bo'lmoq, yorilish, tilinish"], 'spoil': ['spoilt', 'Buzmoq'], 'spread': ['spread', 'Tarqalmoq, yoymoq, surtmoq, surkamoq, solmoq'], 'spring': ['sprung', 'Sakramoq'], 'stand': ['stood', 'Turmoq'], 'steal': ['stolen', "O'g'rilamoq"], 'stick': ['stuck', 'Sanchmoq, suqmoq'], 'sting': ['stung', 'Nayzasini suqmoq'], 'strike': ['struck', 'Urmoq, gugurt chaqmoq'], 'swear': ['sworn', "So'kinmoq, qasam ichmoq"], 'sweep': ['swept', 'Supurmoq'], 'swim': ['swum', 'Suzmoq'], 'take': ['taken', 'Olmoq'], 'teach': ['taught', "O'qitmoq"], 'tear': ['torn', 'Yirtmoq'], 'tell': ['told', 'Aytmoq'], 'think': ['thought', "O'ylamoq"], 'throw': ['thrown', 'Otmoq, uloqtirmoq'], 'understand': ['understood', 'Tushunmoq'], 'wake': ['woken', "Uyg'onmoq"], 'wear': ['worn', 'Kiymoq'], 'win': ['won', "G'alaba qilmoq, yutmoq"], 'write': ['written', 'Yozmoq']}


date = dt.datetime.now()

kun = f"Kun: {date.date()}\nSoat: {date.hour}:{date.minute}\n"
try:
    os.mkdir("C:\\Users\\saydu\\fellar")
    fayl_locate = "C:\\Users\\saydu\\felar\\topolmagan fellaringiz.txt"
    with open(fayl_locate,'a') as file:
        file.write("  -- Topolmagan fellaringiz --\n")
except:
    pass
fayl_locate = "C:\\Users\\saydu\\Downloads\\Telegram Desktop\\felar\\topolmagan fellaringiz.txt"
with open(fayl_locate,'a') as file:
    file.write("======================================\n")
    file.write(f"{kun}\n")

def random_fel():
    ran_fel = random.choice(fayl1)
    return ran_fel


def get_fel2 (rand_fel):
    for k,s in fayl2.items():
        if rand_fel == k:
                asosiy_fel = s
    for ka,so in fayl3.items():
        if rand_fel == ka:
            asosiy_fel3 = so
                
    while True:
        print ()
        print ("Ortga qaytish uchun ( back ) sozini yozing\nTopolmasangiz ( no ) so'zini yozing\n")
        fel2 = input(f" {rand_fel} ning 2 shaklini kiriting: ").lower()
        fel2 = fel2.rstrip()
        print ()
        if fel2 == asosiy_fel[0]:
            print ("===================================")
            print(f"Siz to'gri topdingiz tabrikleman :)\n {rand_fel}: ( {asosiy_fel[0]} ),{asosiy_fel3[0]} = {asosiy_fel[-1]} ")
            print ("===================================")
            break
        if fel2 == "no":
            print ("===================================")
            print ("Eslab qoling")
            print(f" {rand_fel} : ( {asosiy_fel[0]} ),{asosiy_fel3[0]} = {asosiy_fel[-1]} ")
            print ("===================================")
            no_fel (rand_fel,asosiy_fel[0],asosiy_fel3[0],asosiy_fel[-1])
            break
        elif fel2 == 'back':
            return fel2
        else:
            print ("===================================")
            print ("Siz topolmadingiz :(")
            print ("===================================")


def get_fel3 (rand_fel):
    for k,s in fayl3.items():
        if rand_fel == k:
                asosiy_fel3 = s
    for ka,so in fayl2.items():
        if rand_fel == ka:
            asosiy_fel2 = so
                
    while True:
        print ()
        print ("Ortga qaytish uchun ( back ) sozini yozing\nTopolmasangiz ( no ) so'zini yozing\n")
        fel3 = input(f" {rand_fel} ning 3 shaklini kiriting: ").lower()
        fel3 = fel3.rstrip()
        print ()
        if fel3 == asosiy_fel3[0]:
            print ("===================================")
            print(f"Siz to'gri topdingiz tabrikleman :)\n {rand_fel}: {asosiy_fel2[0]}, ( {asosiy_fel3[0]} ) = {asosiy_fel2[-1]} ")
            print ("===================================")
            break
        if fel3 == "no":
            print ("===================================")
            print ("Eslab qoling")
            print(f" {rand_fel} : {asosiy_fel2[0]}, ( {asosiy_fel3[0]} ) = {asosiy_fel2[-1]} ")
            print ("===================================")
            no_fel (rand_fel,asosiy_fel2[0],asosiy_fel3[0],asosiy_fel2[-1])
            break
        elif fel3 == 'back':
            return fel3
        else:
            print ("===================================")
            print ("Siz topolmadingiz :(")
            print ("===================================")

def get_umumiy_fel (rand_fel):
    for k,s in fayl2.items():
        if rand_fel == k:
                asosiy_fel = s
    for ka,so in fayl3.items():
        if rand_fel == ka:
            asosiy_fel3 = so
                
    while True:
        print ()
        print ("Ortga qaytish uchun ( back ) sozini yozing\nTopolmasangiz ( no ) so'zini yozing\n")
        fel2 = input(f" {rand_fel} ning 2 shaklini kiriting: ").lower()
        fel2 = fel2.rstrip()
        print ()
        if fel2 == asosiy_fel[0]:
            print ("===================================")
            print(f"Siz to'gri topdingiz tabrikleman :)")
            print ("===================================")
        elif fel2 == "no":
            print ("===================================")
            print ("Eslab qoling")
            print(f" {rand_fel} : {asosiy_fel[0]} = {asosiy_fel[-1]} ")
            print ("===================================")
            no_fel (rand_fel,asosiy_fel[0],asosiy_fel3[0],asosiy_fel[-1])
        elif fel2 == 'back':
            return fel2
        else:
            print ("===================================")
            print ("Siz topolmadingiz :(")
            print ("===================================")
            continue
        
        print ("Ortga qaytish uchun ( back ) sozini yozing\nTopolmasangiz ( no ) so'zini yozing\n")
        fel3 = input(f" {rand_fel} ning 3 shaklini kiriting: ").lower()
        fel3 = fel3.rstrip()
        if fel3 == asosiy_fel3[0]:
            print ("===================================")
            print(f"Siz to'gri topdingiz tabrikleman :)\n {rand_fel}: {asosiy_fel[0]}, {asosiy_fel3[0]} = {asosiy_fel[-1]} ")
            print ("===================================")
            break
        elif fel3 == "no":
            print ("===================================")
            print ("Eslab qoling")
            print(f" {rand_fel} : {asosiy_fel[0]} ,{asosiy_fel3[0]} = {asosiy_fel[-1]} ")
            print ("===================================")
            no_fel (rand_fel,asosiy_fel[0],asosiy_fel3[0],asosiy_fel[-1])
            break
        elif fel3 == "back":
            return f"back"
        else:
            print ("===================================")
            print ("Siz topolmadingiz :(")
            print ("===================================")
            
def main():
    while True:
        print("Dasturni tugatish uchun ( end ) sozini yozing: ")
        print ("Fellarni ikkala shaklini topish uchun ( 1 ) bosing: ")
        print("Felning 2 yoki 3 shaklini topish uchun (2 yoki 3) bosing:")
        print ("Topolmagan fellaringizni ko'rish uchun ( 4 ) bosing: ")
        print ("Topolmagan fellaringizni o'chirish uchun ( 5 ) bosing: ")
        print ("Topolmagan fellaringizni qayerdaligini topish uchun( 6 ) bosing: ")
        javob = input(">>> ").lower()
        javob = javob.rstrip()
        print ("---------------")
        if javob == "1": 
            print ("Tartib bo'yicha so'rash -> 1 bosing: ")
            print ("Taxminiy so'rash -> 2 bosing: ")
            print ("Pro darajadegilar uchun -> 3 bosing: ")
            natija = input(">>> ").strip()
            if natija == "1":
                while True:
                    for f in fayl1:
                        j = get_umumiy_fel(f)
                        if j == "back":
                            break
                    break
                        

            if natija == "2":
                while True:
                    rand_fel = random_fel()
                    j = get_umumiy_fel(rand_fel)
                    if j == "back":
                        break
                    
                        
            if natija == "3":
                ran_fellar = []
                while True:
                    rand_fel = random_fel()
                    if rand_fel not in ran_fellar:
                        ran_fellar.append(rand_fel)
                        j = get_umumiy_fel(rand_fel)
                        if j == "back":
                            break
                    else:
                        if len(ran_fellar) == 111:
                            print ("================")
                            print ("Tabrikleman barchasini topdingiz :)")
                            print ("================")
                            break
                        continue
                    
        if javob == "4":
            print ("     Topolmagan fellaringiz")
            with open(fayl_locate,'r') as file:
                fayl = file.read()
            print (fayl)
            print ("===================================")
            
        if javob == "5":
            print ("Topolmagan fellaringiz muvafaqiyatli o'chirildi.")
            print ("===================================")
            with open(fayl_locate,'w') as file:
                pass
       
        if javob == "6":
            print("Topolmagan fellaringiz joylashuvi C:\\Users\\saydu\\fellar.")
            print ("===================================")
       
        if javob == "end":
            break
       
        if javob == "2" or javob == "3":
            
            print ("Tartib bo'yicha so'rash -> 1 bosing: ")
            print ("Taxminiy so'rash -> 2 bosing: ")
            print ("Pro darajadegilar uchun -> 3 bosing: ")
            natija = input(">>> ").strip()
            if natija == "1":
                while True:
                    for f in fayl1:
                        if javob == "2":
                            j = get_fel2(f)
                            if j == "back":
                                break
                        if javob == "3":
                            j = get_fel3(f)
                            if j == "back":
                                break
                    if j == "back":
                        break

            if natija == "2":
                while True:
                    rand_fel = random_fel()
                    if javob == "2":
                        j = get_fel2(rand_fel)
                        if j == "back":
                            break
                    if javob == "3":
                        j = get_fel3(rand_fel)
                        if j == "back":
                            break
                        
            if natija == "3":
                ran_fellar = []
                while True:
                    rand_fel = random_fel()
                    if rand_fel not in ran_fellar:
                        ran_fellar.append(rand_fel)
                    else:
                        if len(ran_fellar) == 111:
                            print ("================")
                            print ("Tabrikleman barchasini topdingiz :)")
                            print ("================")
                            break
                        continue
                    if javob == "2":
                        j = get_fel2(rand_fel)
                        if j == "back":
                            break
                    if javob == "3":
                        j = get_fel3(rand_fel)
                        if j == "back":
                            break
       
        elif javob != "end" and javob != "2" and javob != "3" and javob != "4" and javob != "5" and javob != "6" and javob != "1": 
                    print ("Noto'g'ri kiritdingiz, qaytadan kiriting")
                    print ("---------------")

topil_fel = []
def no_fel(rand_fel,fel2,fel3,tarj):
    if rand_fel not in topil_fel:
        with open(fayl_locate,'a') as file:
            file.write(f"{rand_fel}: {fel2}, {fel3} = {tarj}\n")
        topil_fel.append(rand_fel)


print ("\nNoto'g'ri fellarni topish o'yiniga xush kelibsiz")
print (author)
print ("===================================")

def play():
    main()
play()
print ('=============================')
print ("Dastur yakunlandi")
        
    

