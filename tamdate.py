#!/usr/bin/python

import time
from datetime import datetime
from optparse import OptionParser

es_game = {'arena': {'era': 3, 'year': 399, 'release': 1994},
           'daggerfall': {'era': 3, 'year': 405, 'release': 1996},
           'morrowind': {'era': 3, 'year': 427, 'release': 2002},
           'oblivion': {'era': 3, 'year': 433, 'release': 2006},
           'skyrim': {'era': 4, 'year': 201, 'release': 2011}}

month = {'January': 'Morning Star',
         'February': "Sun's Dawn",
         'March': 'First Seed',
         'April': "Rain's Hand",
         'May': 'Second Seed',
         'June': 'Mid Year',
         'July': "Sun's Height",
         'August': 'Last Seed',
         'September': 'Hearthfire',
         'October': 'Frostfall',
         'November': "Sun's Dusk",
         'December': 'Evening Star'}

weekday = {'Monday': 'Morndas',
           'Tuesday': 'Tirdas',
           'Wednesday': 'Middas',
           'Thursday': 'Turdas',
           'Friday': 'Fredas',
           'Saturday': 'Loredas',
           'Sunday': 'Sundas'}

holiday = {'01-01': {'name': 'New Life Festival', 'desc': "Today the people of Tamriel are having the New Life Festival in celebration of a new year. The Emperor has ordered yet another tax increase in his New Life Address, and there is much grumbling about this. Still, despite financial difficulties, the New Life tradition of free ale at all the taverns of Tamriel continues."},
           '02-01': {'name': 'Scour Day', 'desc': "Scour Day is a celebration held in most High Rock villages on the day after New Life. It was once the day one cleans up after New Life, but has changed into a party of its own."},
           '12-01': {'name': "Ovank'a", 'desc': "Ovank'a is the day the people of the Alik'r Desert offer prayers to Stendarr in the hopes of a mild and merciful year. It is considered very holy."},
           '15-01': {'name': "South Wind's Prayer", 'desc': "The 15th of Morning Star is a holiday taken very seriously in Tamriel, where they call it South Wind's Prayer, a plea by all the religions of Tamriel for a good planting season. Citizens with every affliction known in Tamriel flock to services in the every temples, as the clergy is known to perform free healings on this day. Only a few will be judged worthy of this service, but few can afford the temples usual price."},
           '16-01': {'name': 'The Day of Lights', 'desc': "The Day of Lights is celebrated as a holy day by most villages in Hammerfell on the Iliac Bay. It is a prayer for a good farming and fishing year, and is taken very seriously."},
           '18-01': {'name': 'Waking Day', 'desc': "The people in Yeorth Burrowland invented Waking Day in prehistoric times to wake the spirits of nature after a long, cold winter. It has evolved into a sort of orgiastic celebration of the end of winter."},
           '02-02': {'name': 'Mad Pelagius', 'desc': "Mad Pelagius is a silly little tradition in High Rock in a mock memorial to Pelagius Septim II, one of the maddest emperors in recent history. He died about 350 years ago, so the Septims since have taken it with good humor."},
           '05-02': {'name': 'Othroktide', 'desc': "The people of Dwynnen have a huge party to celebrate Othroktide, the day when Baron Othrok took Dwynnen from the undead forces who claimed it in the Battle of Wightmoor."},
           '08-02': {'name': 'Day of Release', 'desc': "The people of Glenumbra Moors may be the only people to remember or care about the battle between Aiden Direnni and the Alessian Army in the first era. They celebrate it vigorously on the Day of Release."},
           '16-02': {'name': "Heart's Day", 'desc': "Today is the 16th of Sun's Dawn, a holiday celebrated all over Tamriel as Heart's Day. It seems that in every house, the Legend of the Lovers is being sung for the younger generation. In honor of these Lovers, Polydor and Eloisa, the inns of all Tamriel offer a free room for visitors. If such kindness had been given the Lovers, it is said, it would always be springtime in the world."},
           '27-02': {'name': 'Perseverance Day', 'desc': "Perseverance Day is quite a party in Ykalon. It was originally held as a solemn memorial to those killed in battle, resisting the Camoran Usurper, but has since become a boisterous festival."},
           '28-02': {'name': 'Aduros Nau', 'desc': "The villages in the Bantha celebrate the baser urges that come with Springtide on Aduros Nau. The traditions vary from village to village, but none of them are for the overly virtuous."},
           '07-03': {'name': 'First Planting', 'desc': "On the 7th of First Seed every year, the people of Tamriel celebrate First Planting, symbolically sowing the seeds for the autumn harvest. It is a festival of fresh beginnings, both for the crops and for the men and women of the celebrated city. Neighbors are reconciled in their disputes, resolutions are formed, bad habits dropped, the diseased cured. The clerics at the temples run a free clinic all day long to cure people of poisoning, different diseases, paralyzation, and the other banes found in the world of Tamriel."},
           '09-03': {'name': 'The Day of Waiting', 'desc': "The Day of Waiting is a very old holy day among certain settlements in the Dragontail Mountains. Every year at that time, a dragon is supposed to come out of the desert and devour the wicked, so everyone locks himself up inside."},
           '21-03': {'name': 'Hogithum', 'desc': "Hogithum, the day that all dark elven priests summon Daedra Prince Azura for her guidance and support."},
           '25-03': {'name': 'Flower Day', 'desc': "Flower Day is another of the frivolous celebrations of High Rock. Children pick the new flowers of spring while older Bretons, cooped up all winter, come out to welcome the season with dancing and singing."},
           '26-03': {'name': 'Festival of Blades', 'desc': "During the Festival of Blades, the people of the Alik'r Desert celebrate the victor of the first Redguard over a race of giant goblins. The story is considered a myth by most scholars, but the holiday is still very popular in the desert."},
           '01-04': {'name': 'Gardtide', 'desc': "On Gardtide, the people of Tamarilyn Point hold a festival to honor Druagaa, the old goddess of flowers. Worship of the goddess is all but dead, but the celebration is always a great success."},
           '13-04': {'name': 'The Day of the Dead', 'desc': "The Day of the Dead is one of the more peculiar holidays of Daggerfall. The superstitious say that the dead rise on this holiday to wreak vengeance on the living. It is a fact that King Lysandus's spectre began its haunting on the Day of the Dead, 3E 404."},
           '20-04': {'name': 'The Day of Shame', 'desc': "All along the seaside of Hammerfell, no one leaves their houses on the Day of Shame. It is said that the Crimson Ship, a vessel filled with victims of the Knahaten Plague who were refused refuge hundreds of years ago, will return on this day."},
           '28-04': {'name': "Jester's Day", 'desc': "Be warned that today is Jester's Day in the all cities of Tamriel, and pranks are being set up from one end of town to the other. It is as if a spell has been cast over the community, for even the most taciturn and dignified councilman might attempt to play a joke. The Thieves Guild finds particular attention as everyone looks for pickpockets in particular."},
           '07-05': {'name': 'Second Planting', 'desc': "The celebration of Second Planting is in full glory this day. It is a holiday with traditions similar to First Planting, improvements on the first seeding symbolically to suggest improvements on the soul. The free clinics of the temples are open for the second and last time this year, offering cures for those suffering from any kind of disease or affliction. Because peace and not conflict is stressed at this time, battle injuries are healed only at full price."},
           '09-05': {'name': "Marukh's Day", 'desc': "Marukh's Day is only observed by certain communities in Skeffington Wood. By comparing themselves to the virtuous prophet Marukh, the people of Skeffington Wood pray for the strength to resist temptation."},
           '20-05': {'name': 'The Fire Festival', 'desc': "The Fire Festival in Northmoor is one of the most attended celebrations in High Rock. It began as a pompous display of magic and military strength in ancient days and has become quite a festival."},
           '30-05': {'name': 'Fishing Day', 'desc': "Fishing Day is a big celebration for the Bretons who live off the bounty of the Iliac Bay. They are not a usually flamboyant people, but on Fishing Day, they make so much noise, fish have been scared away for weeks."},
           '01-06': {'name': "Drigh R'Zimb", 'desc': "The festival of Drigh R'Zimb, held in the hottest time of year in Abibon-Gora, is a jubilation held for the sun Daibethe itself. Scholars do not know how long Drigh R'Zimb has been held, but it is possible the Redguards brought the festival with them when they came in the first era."},
           '16-06': {'name': 'Mid Year Celebration', 'desc': "Today is the 16th of Mid Year, the traditional day for the Mid Year Celebration. Perhaps to alleviate the annual news of the Emperor's latest tax increase, the temples offer blessings for only half the donation they usually suggest. Many so blessed feel confident enough to enter the dungeons when they are not fully prepared, so this joyous festival has often been known to turn suddenly into a day of defeat and tragedy."},
           '23-06': {'name': 'Dancing Day', 'desc': "Dancing Day is a time-honored holiday in Daggerfall. Who started it is questionable, but the Red Prince Atryck popularized it in the second era. It is an occasion of great pomp and merriment for all the people of Daggerfall, from the nobles down."},
           '24-06': {'name': 'Tibedetha', 'desc': "Tibedetha is middle Tamrielic for \"Tibers Day\". It is not surprising that the lorddom of Alcaire celebrates its most famous native with a great party. Historically, Tiber Septim never returned once to his beloved birthplace."},
           '10-07': {'name': "Merchant's Festival", 'desc': "The bargain shoppers of the known world are out in force today and it is little wonder, for the 10th of Sun's Height is a holiday called the Merchants's Festival. Every marketplace and equipment store has dropped their prices to at least half. The only shop not being patronized today is the Mages Guild, where prices are as exorbitant as usual. Most citizens in need of a magical item are waiting two months for the celebration of Tales and Tallows when prices will be more reasonable."},
           '12-07': {'name': "Divad Etep't", 'desc': "During Divad Etep't, the people of Antiphyllos mourn the death of the one of the greatest of the early Redguard heroes, Divad, son of Frandar of the Hel Ansei. His deeds are questioned by historians, but his tomb in Antiphyllos is almost certainly genuine."},
           '20-07': {'name': "Sun's Rest", 'desc': "You will have to wait until tomorrow if you are planning on making any equipment purchases, for all stores are closed in observance of Sun's Rest. Of course, the temples, taverns, and Mages Guild in all cities are still open their regular hours, but most citizens chose to devote this day to relaxation, not commerce or prayer. This is not a convenient arrangement for all, but the Merchants's Guild heavily fines any shop that stays open, so everyone complies."},
           '29-07': {'name': 'Fiery Night', 'desc': "Few besides the natives of the Alik'r Desert would venture out on the hottest day of the year, Fiery Night. It's a lively celebration with a meaning lost in antiquity."},
           '02-08': {'name': 'The day of Maiden Katrica', 'desc': "On the day of Maiden Katrica, the people of Ayasofya show their appreciation for the warrior that saved their county with the biggest party of the year."},
           '11-08': {'name': "Koomu Alezer'i", 'desc': "Koomu Alezer'i means simply \"We Acknowledge\" in old Redguard, and it has been a tradition in Sentinel for thousands of years. No matter the harvest, the people of Sentinel solemnly thank the gods for their bounty, and pray to be worthy of the graces of the gods."},
           '14-08': {'name': 'The Feast of the Tiger', 'desc': "The Feast of the Tiger in the Bantha rainforest is like other holidays in praise of a bountiful harvest. It is not, however, a solemn occasion for introspection and thanksgiving, but a great celebration and festival from village to village."},
           '21-08': {'name': 'Appreciation Day', 'desc': "Appreciation Day in Anticlere is an ancient holiday of thanksgiving for a bountiful harvest for the people of Anticlere. It is considered a holy and contemplative day, devoted to Mara, the goddess-protector of Anticlere."},
           '27-08': {'name': "Harvest's End", 'desc': "Perhaps no other festival fires the spirit of Tamriel as much as the one held today, Harvest's End. The work of the year is over, the seeding, sowing, and reaping. Now is the time to celebrate and enjoy the fruits of the harvest, and even visitors to the celebrated region are invited to join the farmers. The taverns offer free drinks all day long, an extravagance before the economy of the coming winter months. Underfed farm hands gorging themselves and then getting sick in the town square are the most common sights of the celebration of Harvest's End."},
           '03-09': {'name': 'Tales and Tallows', 'desc': "No other holiday divides the people of Tamriel like the 3rd of Hearth Fire. A few of the oldest, more superstitious men and women do not speak all day long for fear that the evil spirits of the dead will enter their bodies. Most citizens enjoy the holiday, calling it Tales and Tallows, but even the most lighthearted avoid the dark streets of Tamriel cities, for everyone knows the dead do walk tonight. Only the Mages Guild completely thrives on this day. In celebration of the oldest magical science, necromancy, all magical items are half price today."},
           '06-09': {'name': 'Khurat', 'desc': "Every town and fellowship in the Wrothgarian Mountains celebrates Khurat, the day when the finest young scholars are accepted into the various priesthoods. Even those people without children of age go to pray for the wisdom and benevolence of the clergy."},
           '12-09': {'name': 'Riglametha', 'desc': "Riglametha is celebrated on the twelfth of Hearth Fire every year in Lainlyn as a celebration of Lainlyns many blessings. Pageants are held on such themes as the Ghraewaj, when the daedra worshippers in Lainlyn were changed to harpies for their blasphemy."},
           '19-09': {'name': "Children's Day", 'desc': "Children's Day in Betony is a festive occasion with a grim history. All know though few choose to recall that Children's Day began as a memorial to the dozens of children in Betony who were stolen from their homes by vampires one night never to be seen again. This happened over a hundred years ago, and the holiday has since become a celebration of youth."},
           '05-10': {'name': 'Dirij Tereur', 'desc': "The fifth of Frost Fall marks Dirij Tereur for the people of the Alik'r Desert. It is a sacred day honoring Frandar Hunding, the traditional spiritual leader of the Redguards who led them to Hammerfell in the first era. Stories are read from Hunding's Book of Circles, and the temples in the region are filled to capacity."},
           '13-10': {'name': "Witches's Festival", 'desc': "Today is the 13th of Frost Fall, known throughout Tamriel as the Witches's Festival when the forces of sorcery and religion clash. The Mages Guild gets most of the business since weapons and items are evaluated for their mystic potential free of charge and magic spells are one half their usual price. Demonologists, conjurers, lamias, warlocks, and thaumaturgists meet in the wilderness outside city, and the creatures created or summoned there may plague Tamriel for eons. Most wise men choose not to wander this night."},
           '23-10': {'name': 'Broken Diamonds', 'desc': "On the 23rd of Frost Fall in the 121st year of the third era, the empress Kintyra Septim II met her death in the imperial dungeons in Glenpoint on the orders of her cousin and usurper Cephorus I. Her death is remembered in Glenpoint as the day called Broken Diamonds. It is a day of silent prayer for the wisdom and benevolence of the imperial family of Tamriel."},
           '30-10': {'name': "The Emperor's Birthday", 'desc': "On the 30th of Frostfall, the Emperor's Birthday was the most popular holiday of the year. Great traveling carnivals entertained the masses, while the aristocracy of Tamriel enjoyed the annual Goblin Chase on horseback."},
           '03-11': {'name': 'The Serpents Dance', 'desc': "The Serpents Dance in Satakalaam may or may not have begun as a serious religious holiday dedicated to a snake god, but this day is a reason for a great street festival."},
           '08-11': {'name': 'Moon Festival', 'desc': "On the 8th of Suns Dusk, the Bretons of Glenumbra Moors hold the Moon Festival, a joyous holiday in honor of Secunda, goddess of the moon. Although the goddess has no active worshippers, the traditional celebration has continued through the ages as a time of feasting and merriment."},
           '18-11': {'name': 'Hel Anseilak', 'desc': "Hel Anseilak, which means \"Communion with the Saints of the Sword\" in Old Redguard, is the most serious of holy days for the people of Pothago. The ancient way of Hel Ansei is never practiced by modern Redguards, but its rich heritage is remembered and honored on this day."},
           '20-11': {'name': 'Warriors Festival', 'desc': "Today is the 20th of Sun's Dusk, the Warriors Festival in Tamriel. Most all the local warriors, spellswords, and rogues come to the equipment stores and blacksmiths where all weapons are half price. Unfortunately, the low prices also tempt many an untrained boy to buy his first sword and the normally quiet streets ring with amateur skirmishes."},
           '15-12': {'name': "North Wind's Prayer", 'desc': "Today is the 15th of Evening Star, a holiday reverently observed by the temples as North Wind's Prayer. It is a thanksgiving to the Gods for a good harvest and a mild winter. The temples offer all their services blessing, curing, healing for half the donation usually requested."},
           '18-12': {'name': "Baranth Do is celebrated on the 18th of Evening. Star by the Redguards of the Alik'r Desert. Its meaning is \"Goodbye to the Beast of Last Year\". Pageants featuring demonic representations of the old year are popular, and revelry to honor the new year is everywhere."},
           '21-12': {'name': "Chil'a", 'desc': "Chil'a, the blessing of the new year in the barony of Kairou, is both a sacred day and a festival. The archpriest and the baroness each consecrate the ashes of the old year in solemn ceremony, then street parades, balls, and tournaments conclude the event."},
           '25-12': {'name': "The New Life festival comes a few days early in Wayrest with Saturalia, traditionally held on the 25th of Evening Star. Originally a holiday for a long forgotten god of debauchery, it has become a time of gift giving, parties, and parading. Visitors are encouraged to participate."},
           '30-12': {'name': 'Old Life', 'desc': "On the last day of the year the Empire celebrates the holiday called Old Life. Many go to the temples to reflect on their past. Some go for more than this, for it is rumored that priests will, as the last act of the year, perform resurrections on beloved friends and family members free of the usual charge. Worshippers know better than to expect this philanthropy, but they arrive in a macabre procession with the recently deceased nevertheless."}}


def mday(day):
    if 11 <= int(day) <= 13:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(int(day) % 10, 'th')
    return str(day)+suffix


def es_year(date, game):
    if not game:
        return ''
    game = es_game[game.lower()]
    game['year'] = game['year'] + int(date.strftime('%Y')) - game['release']

    if game['era'] is 3 and game['year'] > 433:
        game['era'] = 4
        game['year'] = game['year'] - 433

    return '{era}E {year}'.format(**game)


def tamriellic(date, game):
    tamriel = dict()
    tamriel['mday'] = mday(date.strftime('%d'))
    tamriel['month'] = month[date.strftime('%B')]
    tamriel['wday'] = weekday[date.strftime('%A')]
    try:
        tamriel['hday'] = holiday.get(date.strftime('%d-%m')).get('name')
        tamriel['hdesc'] = holiday.get(date.strftime('%d-%m')).get('desc')
    except:
        tamriel['hday'] = None
        tamriel['hdesc'] = None
    tamriel['year'] = es_year(date, game)
    return tamriel


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--date",
                      action="store",
                      dest="date",
                      help="specify date to convert, format DD-MM-YYYY")
    parser.add_option("--template",
                      action="store",
                      dest="template",
                      help="specify your own output template")
    parser.add_option("--holiday",
                      action="store_true",
                      dest="holiday",
                      default=False,
                      help="Print holiday name")
    parser.add_option("--hdesc",
                      action="store_true",
                      dest="hdesc",
                      default=False,
                      help="Print holiday description")
    parser.add_option("--game",
                      action="store",
                      dest="game",
                      help="Elder Scrolls game, used to generate year")

    opts, args = parser.parse_args()

    if opts.date:
        try:
            tamriel = tamriellic(datetime.strptime(opts.date, '%d-%m-%Y'),
                                 opts.game)
        except ValueError:
            print "date must be in the following format: DD-MM-YYYY"
            exit(1)
    else:
        tamriel = tamriellic(time, opts.game)

    if opts.template:
        print opts.template.format(**tamriel)
    else:
        if opts.holiday and tamriel['hday']:
            print tamriel['hday']
        print '{wday}, {mday} of {month} {year}'.format(**tamriel)
        if opts.hdesc and tamriel['hdesc']:
            print '\n'+tamriel['hdesc']
