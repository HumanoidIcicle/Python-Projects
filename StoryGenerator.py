import random
print(
    )

print('                                                                       *=*=*=*=*Choose your own adventure*=*=*=*=*=*')
print('                                                                   *=*=*=*=*=*=*Destiny Is In Your Hands *=*=*=*=*=*=*')
print(
    )

while True:
    gender = str(input ('Välj karaktärs kön; kille eller tjej: '))
    karaktär = str(input('Karaktärs namn: '))
    cappron1 = ''
    small = ''
    pron2 = ''
    pron3 = ''
    crush = ''
    crushcap = ''
    crushsmall = ''
    crushpron3 = ''
    fling = ''
    fling_gender = ''
    hood = ''
    tv_show = str(input('Vad är din favorit serie?: '))
    flick_namn = ['Amelie', 'Ellie', 'Melanie', 'Annalyse', 'Bella', 'Emma', 'Anna', 'Hailey', 'Felicia', 'Viktoria', 'Lisbeth', 'Alice', 'Elin', 'Ann',
                'Selma','Sonja', 'Elvira', 'Melina', 'Louisa', 'Amanda', 'Olivia', 'Emmi', 'Maj', 'Elyse', 'Elise', 'Myrto', 'Isadora', 'Desiree', 'Jonna', 'Chloe', 'Sandra',
                'Isabella', 'Kathleen', 'Mikaela', 'Julia', 'Celia', 'Rebecka', 'Melissa', 'Evin', 'Lea', 'Katja', 'Suzanne', 'Josefin', 'Samantha']
    kill_namn = ['Viktor', 'Jonathan', 'Ethan', 'Luka', 'William', 'Julian', 'Damian', 'Michael', 'Daniel', 'Jovan', 'Loke', 'Felix', 'Noah', 'Viggo', 'Gustav', 'Oskar', 'Benjamin', 'Karl']

    if gender == 'kille':
        cappron1 = 'Han'
        small = 'han'
        pron2 = 'hans'
        pron3 = 'honom'
        crush = random.choice(flick_namn)
        crushcap = 'Hon'
        crushsmall = 'hon'
        crushpron2 = 'hennes'
        crushpron3 = 'henne'
        fling = 'pokvän'
        fling_gender = 'kille'
        hood = '''en mjukblå huvtröja med en bild Halsey på
    baksidan. Den köpte han innan resan tillbaka. Inte för att han gillar Halsey men för att hon är {} favorit artist.'''.format(crush)
        crush_dress = ''', vacker i en kort röd-vit klänning, en dryck i
    hand och hennes långt krulligt brunt hår fallande längs axlar.'''

    elif gender == 'tjej':
        
        cappron1 = 'Hon'
        small = 'hon'
        pron2 = 'hennes'
        pron3 = 'henne'
        crush = random.choice(kill_namn)
        crushcap = 'Han'
        crushsmall = 'han'
        crushpron2 = 'hans'
        crushpron3 = 'honom'
        fling = 'flickvän'
        fling_gender = 'tjej'
        hood = '''en ny mjukblå huvtröja med vita ränder på
    botten och längs armar och en bild på {} favorit band the Crawlers. '''.format(crush)
        crush_dress = '.'
    print(        
        )
    print('            =================================== Ödets Mästare: {}s Berättelse ==================================='.format(karaktär))
    print(
            )

    print('''        Det är en varm fredag kväll. Vinden blåser mjukt ute och några barn leker i skolgården framför {}s hus.
    {} sitter på balkongen med ett glas juice bredvid sig och tittar på solnedgången. I den lilla byn verkar
    tiden gå långsammare än i staden. Men idag går den ännu långsammare. Det är i slutet av juli och idag
    ska {} på fest hos {}. {} är {}s bästa kompis. De har känt varandra sedan födseln. Deras föräldrar har
    varit nära vänner sedan gymnasiet. Men {} och {} har inte setts sedan i julas därför att {} går nu
    gymnasiet i staden och då bor {} med sin farmor and farfar.

    Dessutom är idag {}s födelsedag. Skolan slutade för en vecka sedan men {} reste tillbaka natten innan.
    {} vet inte ännu att {} är tillbaka och {} vill hålla det så för att överraska {} på festen. Där tänker {} också
    berätta om sina känslor för {}, ingen bättre tid att göra det än dagen {} är gladast. Antingen känner {}
    samma och blir gladare att {} uttrycker sina känslor eller...
    Det sista undviker {} tänka om.
    '''.format(karaktär, cappron1, small, crush, crush, karaktär, karaktär, crush,karaktär, small, crush, karaktär,
                crush, small, small, crushpron3, small, crushpron3, crushsmall, crushsmall, karaktär, small))

    print('''        När glaset är tomt går {} till vardagsrumet och sätter på en säsong av {} för att hålla sig upptagen medan
    {} väntar. När det är dags att åka tar {} på sig ett par svarta jeans och {}
    Genom stora hörlurarna sätter {} på Yellow Claw på högt volym för att lugna sig. {}s hus ligger inte så långt
    ifrån {}  så {} tänker promenera dit. {} kan antingen ta den långa vägen dit så att {} är framme när de flesta
    gästerna redan kommit, då är det bara att ta {} någonstans tystare, ensamma. Eller tar {} genvägen som ta {}
    dit när bara några människor har kommit och {} är fortfarande fräsch och energetisk.
    '''.format(karaktär, tv_show, small, small, hood, small, crush, pron2, small, cappron1, small, crush, small, pron3, crush))

    väg = str(input('Vilken väg? Skriv genväg eller långväg: '))

    if väg == 'genväg':
        print(
            )
        print('''        Problemet med genvägen är att på ena sidan av den är en väldigt tät skog och på den andra en kyrkogård. Båda
    lika skrämmande till {}. Speciellt när solen har gått ner. {} har alltid hatat kyrkogårdar. Sedan {} var barn har {}
    undvikat ta genvägen och alltid tagit den långa vägen till {}s. De otaliga skräckfilmer om zombies och spöken {} har
    sett hjälpte inte rädslan. Men idag är en speciell dag. Det handlar inte om {} utan om {}. {} tar ett djupt andetag
    och börjar gå så fort {} kan.
    "Tänk inte på filmerna," tröstar {} sigsjälv. "Sådant händer inte i verkligheten. Det vet du väl. Och du går gymnasiet nu,
    vilken 16 åring är rädd för spöken?"

        När {} går förbi kyrkogårdens portuppgång börjar {} höra röster, viskande röster i mörkret. Först tror {} att det är
    rädslan som gör att {} hör saker som inte är verkliga. Men rösterna fortsätter. Och ju närmare {} kommer  desto
    högre och tydligare blir rösterna. Månen är täckt av moln och det är svårt för {} att se vem som pratar.
    '''.format(karaktär, karaktär, small, small, crush, small, pron3, crush, cappron1, small, small, small, small, small, small, small, pron3))
        
        choice1 = str(input(' undersök eller fortsätt?: '))

        if choice1 == 'undersök':
            
            print(
                )
            print('''        Tvekande bestämmer {} sig för att undersöker vad som pågår.
        "Det kan inte vara en begravning så här sent på kvällen." tänker {}.
    {} hoppar över den korta väggen för att inte riskera grindens rusty noises. Långsammt smyger {} genom
    gravstenarna och följer rösterna. Det låter som det är flera personer som pratar samtidigt. {} gömmer
    sig bakom en av de större gravstenar och stänger av hörlurarna.
    
        Nu ser {} sex personer, alla klädda i långa svarta kappor. Från {} synpunkt ser {}  att de står i en cirkel
    runt ett hål. De har huvar på sig så {} kan inte ser om {} känner någon av dem. En man läser någonting från en
    stor gammal bok med grekiska symboler medan de andra upprepar samma fras om och om igen på vad {}
    antar är grekiska också. Symbolerna på boken känner {} igen från grekiska kursen i sjuan som {} avslutade
    när det kändes så svårt. {} har naturligtvis glömt det mesta. Men i frasen männen upprepar hör {} orden
    "...av bloden...". {} behöver inte vara Einstein för att begripa att det här är en ond kult. Det är en ond kult i {}
    lilla by. Byn där ingenting händer och alla känner alla.
        Men någonting annat gör {} ännu mer uneasy. Mannen med boken, hans röst. Den låter bekant av någon anledning.
    "Johan!!" insikten slår honom plötsligt och kraftigt. {} skulle känna igen {}s pappas röst var som helst. Ju längre
    {} lyssnar desto säkrare blir {} på att det verkligen är {}s pappa.
    {} fryser. {} vill springa därifrån och skrika om hjälp men {} kan inte röra på sig. {} blundar och leans på gravstenen
    och alla möjliga tankar flood {} mind.
    "Tänk om ett odjur hoppar ut ur hålet. Det kommer  kunna lukta ut mig. Då hittar de mig." "Ska de offrar mig till Hedis?"
    "De kan döda mig eller kasta en förtrolling som förvandlar mig till en groda, en snigel eller ännu värre en förstrolling som
    radera hela mitt minne. Då glömmer jag vem jag är. Mitt liv. {}."
    Det skulle {} aldrig låta hända.
    "Nej." tänker {} determinedly. "Jag kan inte glömma {}."

        {} ta några djupa andetag, samlar sina tankar och då märker att det blivit tyst i kyrkogården. Så tyst att {} hör sigsjälv
    andas och en uggla uppe i ett träd.
    "Är männen borta?" undrar {} och kollar upp för att se. Ingen syns till.
    '''.format(small, small, cappron1, small, cappron1, small, pron2, karaktär, small, small, small, small, small, cappron1, small,
                cappron1, pron2, pron3, cappron1, crush, small, small, crush, cappron1, cappron1, small, cappron1, pron2, crush,
                small, small, crush, cappron1, small, small))

            break


