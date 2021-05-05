from aiogram.dispatcher import FSMContext


async def menu():
    return ("""Привет👋

☑ Опираясь на личный опыт лидеров студенческого самоуправления Беларуси, мы создали эту платформу для тех, кто хотел бы попробовать себя в качестве руководителя студенческой организации😎

☑ Надеемся, наш проект подтолкнет тебя не только проверить свои силы в онлайне, но и применить полученные знания в реальной жизни💪 Если ты уже являешься руководителем или представителем какой-либо студенческой организации, то здесь мы можем помочь тебе переосмыслить накопленный опыт, посмотреть на некоторые ситуации под другим углом🤗

Будем рады любому фидбэку и помощи в модернизации & пиаре платформы🤝
""")


async def set_name():
    return ("Как мы можем к тебе обращаться?")


async def set_avatar():
    return ("Выбери свой аватар:?(отправьте эмоджи)")


async def set_pers():
    return ("""Выбери направление студенческой активности, в котором тебе хотелось бы себя испытать. Не волнуйся, после завершения игры ты сможешь пройти ее и за других персонажей.

1. 🎨🎭 Творчество и культура – стань главой Творческого объединения  студентов. Как правило, такие организации занимаются культурно-массовой и досуговой деятельностью: организуют концерты, капустники, творческие вечера, фестивали, КВН и т.п.

2. 🧪🖥️ Наука и учебный процесс – займи должность главы Совета по науке и качеству образования. Обычно, такие организации занимаются исследованиями в области качества образования, выдвигают рекомендации по улучшению учебного процесса и т.п.

3. 🛡⚖ Защита прав и интересов студентов – выбери пост главы Студенческого совета. Задачами таких организаций является защита прав и представление интересов студентов.
""")


async def start_act_1():
    return ("""🎮 Вся игра состоит из (20) вопросов, на которые тебе предстоит ответить. Подходи к ответу максимально ответственно, ставь себя на место своего игрового аватара.

📈 Твои ответы будут влиять на рост или падение игровых метрик: лояльности студентов, лояльности коллег и лояльности администрации. Помни, что ответы могут как увеличить значение метрик до max (50 очков), так и сбить их до min (0 очков). 

Что-ж, настало время определить: станешь ли ты легендой факультета или покинешь пост с подмоченной репутацией? 🤔
""")


async def recruiting_method(state: FSMContext):
    data = await state.get_data()
    return (f"""Итак, сегодня твой первый день в новой должности. 😉
Первоочередная задача - сформировать команду, чтобы орган мог приступить к работе 🕰️. Какой метод набора людей в {data['pers']} тебе ближе?
1) Посоветуюсь с деканатом, у администрации факультета наверняка есть хорошие ребята на примете.
2) Возьму на работу своих друзей - я хорошо знаю их возможности, да и я же теперь главный, мне решать.
3) Объявлю открытый набор в {data['pers']}. Право проявить себя должно быть у каждого!
4) Где там прошлый состав {data['pers']}? Они ребята опытные – позову их обратно.""")


async def act1(state: FSMContext):
    data = await state.get_data()
    return f"Декан🧙‍♂️: Поздравляю {data['name']}, теперь ты - глава {data['pers']}. Факультет рассчитывает, что ты " \
           f"станешь мудрым руководителем и не совершишь глупых ошибок на своем посту. Что ж, удачи тебе! 💫 "


async def set_recruiting_method():
    return f"""Так или иначе, список кандидатов сформирован 📝, пора бы познакомиться с ними поближе."""


async def positions_of_people(state: FSMContext):
    data = await state.get_data()
    text = "Деканат посоветовал тебе этих ребят"
    if data["recruiting_method"] == "2":
        text = "Вот список твоих друзей"
    elif data["recruiting_method"] == "4" or data["recruiting_method"] == "3":
        text = "Вот список людей, которые откликнулись на вакансию"
    return (
        f"""{text}. Тебе как руководителю нужно назначить людей на должности. Кого куда назначишь?

1) Твой заместитель 👥
2) Менеджер соцсетей 🤳
3) Секретарь 📑
4) Менеджер проектов 📊

а) Маша, у которой 5 тысяч подписчиков в инстаграме и 118 сториз ежедневно 🤳. Всё, что интересует Машу - это соцсети, в которых она проводит много времени. Категорически против работы руками, при этом обожает быть в центре событий 💫
б) Слава, который является круглым отличником. Ответственный и трудолюбивый, на него всегда можно положиться 🙏. Предпочитает выполнять работу самостоятельно, поскольку по натуре своей - интроверт, при этом обладает завышенным ЧСВ (чувством собственной важности). 🤖. 
в) Ира. Прирожденный переговорщик и дипломат 👩‍💼. Умеет убеждать людей, однако, иногда не справляется со своим “пылом”, невольно агрессирует в сложных ситуациях 😤.
г) Макс, который работает волонтером вне университета, к тому же является старостой группы и профоргом🙋🏽‍♂️. Опыта ему точно не занимать, однако не всегда успеет все сделать вовремя. Не удивляйся потом, если нужное мероприятие пройдет 10 апреля вместо 10 февраля. Ну, зато совет дельный может дать👌.""")


async def set_positions_of_people():
    return (f"""Окей, теперь есть ясность, кто за что отвечает в твоей команде, двигаемся дальше 🆙️""")


async def strategy():
    return (f"""Какую стратегию работы ты выберешь?

1) рок-н-ролл - юху, полная свобода действий, никаких ограничений и компромиссов 😝!
2) консервативную - буду делать то, что делали до меня, зачем заморачиваться, если все работает 🤓?
3) компромиссную - разберусь с тем, что было до меня: эффективные и полезные решения оставлю, а в остальном буду работать на улучшение, привнося в работу что-то новое 😌.
""")


async def set_strategy():
    return (f"""В чем сила, брат? Сила - в гибкости. Кто умеет комбинировать сразу несколько стратегий, тот и сильный лидер. Так что попробуй всё, чтобы подобрать удобный тебе и команде способ работы. """)


async def tactics(state: FSMContext):
    data = await state.get_data()
    return (
        f"""Теперь тебе предстоит первое собрание с составом {data['pers']}, где вы должны определиться с конкретной программой своей деятельности😯. Какой тактики ты будешь придерживаться?
1) Подсмотрю идеи у других студенческих организаций - а что, не пропадать же добру🤥!
2) Устрою мозговой штурм с командой - это всегда работает🤯.
3) Устрою опрос среди студентов, чего они хотят. Как говорится, глас народа - глас божий😇.
4) Буду искать идеи в интернете - в гугле уж точно что-то найдется🤓.
""")


async def set_tactics():
    return (f"""Вы только посмотрите! Такой программе обзавидовались бы даже Отцы-основатели...но это не точно😂. Тырить идеи - это не солидно. Лучше используй возможности non-formal education: изучай новые форматы, развивай нетворкинг и ищи вдохновение. Ну и гугол тебе в помощь😉""")


async def delete_item():
    return (
        f"""Фух, вроде прошло нормально. Тебя вызвали в деканат, чтобы обсудить ваш план🏃. В разговоре декан предлагает исключить пару пунктов из вашей программы🛑. Что ты ему ответишь?
1) Соглашусь без вопросов, ему виднее🙍.
2) Буду вести переговоры и торговаться - попытаюсь отстоять хоть что-нибудь🗣️.
3) Отвечу категорическим отказом - меня избрали студенты, значит, они мне доверяют🙅🏽‍♀️.
4) Сделаю вид, что у меня звонит телефон, и выйду в коридор, чтобы избежать ответов на неудобные вопросы🙉.
""")


async def end_act1():
    return (
        f"""Худо-бедно ты сформировал_а команду и определился_лась со своей программой. Что же, пора приступать к работе!

⭐️Сводка по акту⭐️

Если ты приходишь на менеджерскую позицию, то наиболее ценными ресурсами для тебя становятся информация и взаимоотношения с окружающими. Старайся как можно больше общаться с людьми - от них ты будешь получать нужную информацию (даже если сначала тебе кажется, что она бесполезна), а позже и трансформировать новые знакомства в прочные и полезные связи. Не забывай и о том, что получать бесценный опыт можно и на ошибках - просто пробуй! 💫
""")


# -----------------------------------------------------------


async def organizers():
    return (
        f"""На носу важное мероприятие - фестиваль для первокурсников💥. Курировать все номера и отвечать за постановку хотят два разных человека. Ты понимаешь, что следствием твоего выбора может быть конфликт внутри Творческого объединения. Кому отдашь проведение мероприятия🤔?
1) Конечно Нике – она талантливая организаторка, к тому же моя подруга🤛.
2) Паше – он хоть и новичок, но я же ему давно уже обещал_а дать возможность себя проявить и не важно, что он глухонемой.
3) Попытаюсь объединить их усилия, они хоть и не ладят, но я в своих менеджерских качествах уверен_а💯!
4) Это очень важное мероприятие, чтобы его кому-то делегировать, “запороть” его = лишиться авторитета. Проведу сам, а ребятам пообещаю “в следующий раз”🤥.
""")


async def set_organizers():
    return (f"""Делегирование - наше всё. Научись доверять и распределять обязанности между подчиненными, ведь в одиночку ты вряд ли вывезешь всю работу. Однако делай это постепенно. Кидать  новичков под танки - не лучшая идея.""")


async def inactive():
    return (
        f"""Ты видишь, что один из твоих подчиненных стал работать хуже 📉: на собраниях не появляется, инициативу не проявляет, работу выполняет неохотно. Что будешь с ним делать?

1) Мне бездельники не нужны - уволю его без разговоров 😠.
2) Поговорю с ним и узнаю причину спада активности - возможно, ему стоит поручить другую работу 🤔.
3) Мне без разницы, пусть числится в организации, авось когда-нибудь пригодится 😏.
""")


async def set_inactive():
    return (f"""Говорить с подчиненными необходимо - это факт. И наш совет: не затягивай с этим. Однако, что бы ты не выбрал_а – знай, что ты потрясающий_ая, потому что не боишься принимать сложных решений! ❤""")


async def strange_number():
    return (
        f"""Творческий коллектив студентов целый месяц готовил номер 🥁 для концерта в честь дня университета, который состоится уже на следующей неделе. Есть вероятность, что администрация универа такому номеру не обрадуется, твоя должность под угрозой. Допустишь номер к программе 🤔?

1) Я за свободу творчества! 🔓 Допускаем, ребята все-таки готовились.
2) Не допущу номер. Зачем нам эти проблемы? ⛔
3) Попытаюсь согласовать номер с администрацией. Вдруг я ошибаюсь насчет их мнения. 🗣
4) Придумаю причину, почему концепцию номера нужно изменить, и предложу ребятам поставить другой номер. 👀

""")


async def set_strange_number():
    return (f"""Принимать сложные решения – удел каждого лидера. Не бойся брать на себя ответственность, в конце концов, ты же главый🤷.""")


async def artistic_director():
    return (
        f"""Один из твоих топовых худруков прислал тебе сообщение в телеге: “Я ухожу в другую студенческую организацию, мне надоело работать в Творческом объединении”📳. Ты навел_а справки и выяснилось, что, на самом деле, глава другой студенческой организации предложил худруку больше плюшек (премия раз в месяц и путевка в санаторий)💲. У вас в организации таких возможностей нет. Что делать?\

1) Пойду к администрации и попробую выбить плюх 🆘.
2) Да ну его, он предатель, лучше найду нового худрука 🤦‍♂️.
3) Поговорю с главой-переманщиком – это недопустимо, устрою скандал на весь универ 👺.
4) Извинюсь и попробую выяснить реальную причину ухода у худрука, позову обратно 🌚.
""")


async def set_artistic_director():
    return (
        f"""Ну, чё там с деньгами? Студенческая инициатива держится, в основном, на голом энтузиазме. Но не стоит забывать, что в самоуправлении ты получаешь нечто большее, чем деньги – друзей, опыт работы, интересные знакомства и эмоции😊""")


async def muslim():
    return (
        f"""На факультете готовится творческий вечер, где каждая учебная группа должна представить номер. Одна из групп обратилась с предложением сделать номер, где девушки должны быть одеты в славянские кокошники. При этом в группе есть студентка-мусульманка 🧕, которая отказывается снимать хиджаб и надевать кокошник. Ты знаешь, что другие студенты группы относятся к этой ситуации с недовольством и не хотят менять концепцию. Как поступишь 😮?

1) У нас демократия. Большая часть студентов решила, что будет номер с кокошниками, значит, так тому и быть. Попрошу ее отказаться от участия 🚷.
2) Жестко отреагирую на попытку дискриминации 😤. Право участия должно быть у всех, независимо от вероисповедания, гендера, внешнего вида и культурных особенностей. Настою на ее участии в номере.
3) Я должен прислушиваться к мнению большинства студентов 🧚‍♂️. Придется предложить студентке поставить собственный номер, если она этого хочет, а ребята пусть танцуют в кокошниках.
""")


async def set_muslim():
    return (
        f"""Рекомендуем, кстати, освежить в памяти Всеобщую декларацию прав человека📖. Однако, однозначного решения этой ситуации, безусловно, не существует.""")


async def striptease():
    return (
        f"""К тебе пришли три первачка с сумасшедшей идеей - они хотят станцевать стриптиз&вог (да, там, где парни танцуют на каблуках) на ближайшем факультетском празднике👯. По личным убеждениям ты категорически против и считаешь, что это недопустимо, т.к. нарушает традиционные ценности Республики Беларусь❎. Откажешь им?

1) Конечно откажу! Подобному не место в стенах высшего учебного заведения🚷.
2) Посоветуюсь с администрацией, стоит ли пропускать этот номер. Как они решат, так и будет⚖️.
3) Попытаюсь переступить через свои взгляды. Право самовыражаться должно быть у всех. Не хочу, чтобы меня запомнили авторитарным лидером👴🏻.
4) Вынесу вопрос на голосование в актив творческого союза – мы должны принимать такие решения коллегиально👐.
""")


async def set_striptease():
    return (f""" А как ты хотел_а? Ведь с творческими людьми работаешь

⭐️Сводка по акту⭐️
Не бойся дискутировать как со студентами, так и с администрацией на самые разные темы. Посредством диалога можно решить даже то, что кажется на первый взгляд неразрешимым.
При этом, помни, что в творческой сфере, как правило, работает множество “нестандартных” личностей. Будь аккуратнее в общении, давай фидбэк только хорошо взвесив “за” и “против”, чтобы случайно не отвернуть от себя талантливого человека 👽.
""")


# --------------------------------------------------


async def bell():
    return (
        f"""Ночь, ты спокойно спишь и никого не трогаешь. Вдруг - звонок, это твой однокурсник Вася Пупкин, он попался слегка выпившим 🤪 службе порядка в общежитии. Вася просит помочь ему избежать выселения из общаги, потому что жить ему, кроме общаги, негде. До этого момента Вася в подобных ситуациях уличен не был, характеризуется однокурсниками положительно, защищал честь факультета на шахматном турнире ♟ (хоть и занял первое место с конца). Будешь ли его защищать?

1) Да, для этого позвоню декану - у него явно есть связи с администрацией общаги, он поможет 🥺.
2) Приду впрягаться за бедолагу сам - кроме меня ему никто не поможет 😇.
3) У  меня же был знакомый в службе порядка - напишу ему, он отмажет 😎.
4) Ничего не буду делать, сам вляпался - сам пусть и разгребает 😐.
""")


async def set_bell():
    return (
        f"""Эх, это была отличная ночка, ты всегда мечтал_а о том, чтобы разруливать проблемы накосячивших студентов вместо того, чтобы спать. Но что поделать? Самоуправление - работа ДЛЯ студентов.""")


async def discrimination():
    return (
        f"""Группа студентов жалуется тебе на неоднократные акты дискриминации со стороны конкретного преподавателя😠. Ты поговорил_а с преподавателем – он говорит, что жалобы студентов абсолютно необоснованны и являются вымыслом🤡. Как ты будешь разруливать ситуацию?

1) Проведу анкетные опросы среди студентов, узнаю их мнение и передам преподавателю рекомендации по разрешению конфликта📝.
2) Выступлю медиатором между оскорбленными студентами и преподавателем - в споре рождается истина⚔️.
3) Попрошу вмешаться в инцидент декана - у меня мало авторитета для таких дел🏽‍♂️.
4)Это их личное дело, им стоит разобраться в этом самостоятельно, не вынося сор из избы🙈.
""")


async def set_discrimination():
    return (f"""Тут мы бы могли сказать, что тебе стоит быть объективным, беспристрастным и разбираться в каждом конкретном случае. Но ты ведь и так это знаешь, да?""")


async def interview():
    return (
        f"""Ты замутил_а опрос в инстаграме студсовета с целью узнать, что студенты хотели бы изменить в работе факультета. Как выяснилось, многим студентам не нравится качество обслуживания в столовой 🍱, и они просят тебя разобраться. Твои действия:

1) Мне все нравится, ничего не знаю, я вообще контейнер ношу из дома ☺️.
2) Пойду разговаривать сам_а с заведующей столовой, предупрежу ее, что в случае, если ситуация не улучшится, студенты начнут питаться в соседнем кафе “Европа” 🤨.
3) Подниму вопрос на Совете факультета, попрошу администрацию разобраться 🤓.
4) Напишем со студентами коллективное обращение заведующей, припугну ее санстанцией 🤫.
""")


async def set_interview():
    return (
        f"""Угу. Наш тебе совет – общайся со студентами 🙋‍♂️💁‍♀️ (даже с теми, с кем не хочется!) как можно чаще. От них можно получить ценные инсайты, которые часто бывают скрыты от твоих глаз.""")


async def petitions():
    return (
        f"""У тебя есть возможность выписать 10 ходатайств на заселение в общежитие студентов на следующий год✍️. Как определишься со счастливчиками?

1) Создам опрос на странице студсовета в соц. сети: “Ребята, кому нужно ходатайство на общагу, плюсуйте!” Кто плюсанет первый, тому и напишу📳.
2) Выпишу ходатайства самым нуждающимся по мнению деканата и коллег🙏.
3) Выпишу только тем, кто проявил себя в научной/общественной/культурной жизни☝️.
4) No money, no honey. Напишу ходатайства тем, кто угостит меня вкусным обедом, например🍝.
""")


async def set_petitions():
    return (f"""Ты же знаешь, что пользоваться служебным положением в своих личных целях не комильфо 🙇‍♂️? """)


async def lazy():
    return (
        f"""Ты видишь, что один из твоих подчиненных стал работать хуже: на собраниях не появляется, инициативу не проявляет, работу выполняет неохотно💩. Что будешь с ним делать?

1) Мне бездельники не нужны - уволю его без разговоров 🆓.
2) Поговорю с ним и узнаю причину спада активности - возможно, ему стоит поручить другую работу 🙇.
3) Мне без разницы, пусть числится в организации, авось когда-нибудь пригодится 🧘.
""")


async def set_lazy():
    return (
        f"""Не забывай контролировать такие вопросы. Иначе организация может разрастись до неприличных размеров, а ответственность между ее членами “размоется” 🏄‍♀️ и доверить важное поручение можно будет единицам. Будь в тонусе, оптимизируй процессы! 🆗️""")


async def characteristic():
    return (
        f"""Твоего друга отчисляют - у него 0 сданных контрольных и посещено только несколько пар за семестр (а ведь ты говорил_а ему, что в универе нужно появляться хотя бы иногда)🤦🏾‍♀️. Тебе, как представителю студентов, декан предлагает написать характеристику твоего друга для заседания комиссии. Что ты туда впишешь?

1) Ничего не буду писать. Лучше сохранить нейтралитет🏄.
2) Вступлюсь за друга и напишу ему крутую характеристику, даже преукрашу - надо же своего спасать👼.
3) Напишу правду - он же действительно не учился, так будет справедливо🤞.
""")


async def set_characteristic():
    return (f"""Пусть этот выбор будет на твоей совести - слушай ее хотя бы время от времени.""")


async def stock():
    return (
        f"""Вы в студсовете провели благотворительную акцию 💚, собрав достаточно крупную денежную сумму. Ты поручил_а своему заму передать собранные деньги приюту для животных 🐕. Когда через неделю ты позвонил_а директорке приюта, чтобы услышать слова благодарности, она сказала, что к ней никто не приходил и никаких денег она не получала. При этом, твой зам отчитался, что деньги приюту были переданы 🤓 Как поступить в такой ситуации?

1) В смысле “как поступить?”. Я же в доле - жить в шоколаде и пожинать плоды, конечно 😈.
2) Расскажу об этом администрации факультета - пусть его “прышчучыншать” по всей строгости 👮‍♂️.
3) Попрошу его вернуть все деньги людям и уволю - это же полный беспредел 🔚.
4) Ничего не делать. Студентам норм? Норм. Ему норм? Норм. Лучше сделать вид, что ничего не произошло, иначе пострадает и мой имидж тоже, если ситуация вскроется 🤫.
""")


async def set_stock():
    return (f"""#animalslivesmatter

⭐️Сводка по акту⭐️

Самоуправление, как и вся наша жизнь, штука неоднозначная. Часто здесь не бывает “правильных/неправильных” решений, все зависит от последствий, к которым ты готов_а, принимая какое-либо решение. Став лидером, ты обязан_а продумывать все на несколько шагов вперед и учитывать интересы всех сторон. 

Мы считаем, что ключевой навык для лидеров студенческого самоуправления сегодня - это умение проводить “гарвардские переговоры”. Если не слышал_а о таком, то Гугл в помощь или можешь прочитать книгу “Договориться можно обо всем” Г. Кеннеди! P.S. друзьям рассказать не забудь!🤝

""")


# --------------------------------------------------


async def competitor():
    return (
        f"""Твой бывший конкурент на должность председателя СНКО сообщил, что один из преподавателей факультета отказывается поставить ему зачет по выдуманной причине🥵. Как оказалось, этот преподаватель - твой близкий родственник. И как быть?
1. Не буду принимать участия в разрешении конфликта, потому что у меня есть личный интерес в этом споре. Поручу дело своему заму👀.
2. Семья превыше всего, своим близким надо помогать в трудную минуту. Попытаюсь “замять” конфликт👊.
3. Мутная история. Я хорошо знаю этого преподавателя, это компетентный и непредвзятый сотрудник. Так что займу сторону препода - на провокации конкурентов я не ведусь🙅🏽‍♀️.
4. Отстаивать права студентов на получение качественного преподавателем и деканом. Буду разбираться сам, а не образования – мой долг, поэтому организую встречу с замалчивать проблему⚖️.
""")


async def set_competitor():
    return (f"""Мда, хорошенькое начало. С другой стороны, а кто говорил, что будет легко 🤯?
""")


async def pandemic():
    return (
        f"""Мир неожиданно захлестнула пандемия коровавируса, в связи с чем всех обучающихся оперативно (ха!) перевели на дистанционку💻. Один из студентов, который прослыл главным хейтером на факультете и известен мнением, о том, что в мире не существует совершенных вещей, кроме него самого, написал в инсте такой постец: “Нас, очников, перевели учиться на ДО, за что платники тогда платят такие деньги? Почему бы универу не произвести перерасчет и не снизить стоимость платы до уровня заочной формы? Куда смотрит @главаСНКО, может сделаете что-нибудь?” 
В какой форме ты ему ответишь?

1. Напишу ему в личные сообщения с предложением обратиться напрямую в Минобр. СНКО такими вопросами не занимается😈.
2. Мало ли, что он там пишет в своих соцсетях, его мнение вообще мало кого интересует, все знают, что он просто на этой теме “хайпует”🐀.
3. Напишу ему ответный пост на официальной странице СНКО. Подвергну его “мнение” критике, попрошу информационной поддержки у коллег в комментариях. Пусть неповадно будет☠️.
4. Попытаюсь пригласить его на личную встречу, пусть выскажет свое недовольство в лицо. А дальше мы уж разберемся🤼.
""")


async def set_pandemic():
    return (
        f"""“Вы думаете, что я вас не переиграю? Что я вас не уничтожу?” 😈 – примерно с таких слов ты мог_ла начать свой ответ студенту, но это лишь фантазии… Будь вежливым в общении с другими студентами. По крайней мере, старайся.""")


async def remote():
    return (
        f"""Студенты жалуются, что с переходом на дистанционное обучение качество преподавания существенно снизилось: пары не проводятся, преподаватели не умеют пользоваться компьютерами🤢. Как будешь реагировать на жалобу?

1) Оставлю эти выдумки без внимания, такого просто не может быть, я такого не замечал_а🙊.
2) Попрошу студентов принести доказательства - видеозаписи, скриншоты, когда преподаватель явно не справляется с новыми технологиями. Потом отнесу весь материал администрации, там пусть разбираются💽.
3) Вместе со студентами разработаю рекомендации по улучшению качества дистанционного преподавания, предоставим результат преподавателям📑.
""")


async def set_remote():
    return (f"""*здесь может быть ваш мем про айти страну*""")


async def reluctantly():
    return (
        f"""Ты видишь, что один из твоих подчиненных стал работать хуже: на собраниях не появляется, инициативу не проявляет, работу выполняет неохотно🥵. Что будешь с ним делать?

1) Мне бездельники не нужны - уволю его без разговоров🙅🏽‍♀️.
2) Поговорю с ним и узнаю причину спада активности - возможно, ему стоит поручить другую работу🙇.
3) Мне без разницы, пусть числится в организации, авось когда-нибудь пригодится🧘.
""")


async def set_reluctantly():
    return (f"""Иногда с людьми приходится расставаться и не всегда это легко.
Просто прими это.""")


async def polls():
    return (
        f"""Семестр почти подходит к концу, а это значит, что настала пора проводить очередные анкетные опросы ✍ по качеству преподавания курсов. Как будешь его пиарить? 💬

1) С применением административного ресурса “попрошу” 🤭 всех студентов пройти анкетирование. Нам необходима максимальная репрезентативность, не важно, какими методами. Цель оправдывает средства.
2) Размещу информационно-агитационный контент во всех возможных “айфонах, плафонах, интернетах, тиктоках” о предстоящем анкетировании – попробую заинтересовать студентов на их же языке 😛
3) Размещу объявление на информационных стендах факультета, сайте и попрошу преподавателей рассказать об этом на парах. Кто придет - тот придет 🙏
4) А чего париться? У старост есть контакты всех студентов - пусть напишут инфу в чатах 🤞
""")


async def set_polls():
    return (
        f"""Как минимум, не стесняйся спрашивать совета у студентов, которые учатся не специальностях 👨‍🎓👩‍🎓, связанных с пиаром&коммуникациями. 
""")


async def traffic():
    return (f"""Окей, трафики пошли 🎰 Как организуешь процесс анкетирования?

1) Сброшу студентам ссылку на анкету, пусть проходят в удобное время и в удобном месте 🚀 У нас ответственные студенты, я уверен_а, что ссылка не уйдет “налево”. 
2) Буду проводить анкетирование в компьютерном классе. Предварительно назначу конкретное место и время ⏰ прохождения анкетирования, соберу список желающих и буду запускать в аудиторию только по списку. Порядок должен быть везде 🧹
3) Распечатаю анкету и передам преподавателям, чтобы они провели анкетирование после своих пар. Они в этом заинтересованы, вот пусть и проводят 😁
4) Поручу это дело старостам 😏 Они со студентами близко общаются, они пиарили анкетирование - кому как не им довести дело до конца?
""")


async def set_traffic():
    return (f"""Запомни! В наше время студенты ценят свободу выбора, анонимность и свое свободное время. А, ну и листни наш гайд по проведению анкетирований.
""")


async def meaning():
    return (
        f"""К тебе пришел твой заместитель. Он говорит, что студенты одной из групп отказываются проходить анкетирование🤮. “Да это все равно ни на что не повлияет, какой от этого смысл?” - говорят они. Твои действия?

1. Не хотят - пусть не проходят, это дело добровольное, буду я еще кого-то уговаривать🤨.
2. Попрошу преподавателей/администрацию провести разъяснительную беседу со строптивыми студентами. Это всегда работает💯.
3. Проведу разъяснительный стрим в соцсетях, где отвечу на все интересующие вопросы студентов. Ну, а что, все же уже в инстаграме зарегались📲
4. Отправлю своих подчиненных в массы – пусть заходят в аудитории на переменах и рекламируют анкетирование! Метод дедовский, но работает, да и коллеги ораторское мастерство прокачают🗣️.
""")


async def set_meaning():
    return (f"""К сожалению, люди любят, когда результат виден сразу. Поэтому используй все доступные методы, чтобы наверняка донести до студентов ценность анкетирований.

Давай, не расслабляйся, финал уже близко!🔜

⭐️Сводка по акту⭐️
Ведь не всегда результат оправдывает средства, не так ли? От решений лидера часто зависит “маленькое” или “большое” будущее окружающих. К каждой ситуации нужно подходить индивидуально и вдумчиво, попробуй докопаться до сути - это же до жути интересно! Советуем изучить метод “5 почему” и прочитать книгу “Спроси маму” Фитцпатрика.
Рекомендуем почаще проводить исследования, в т.ч. анкетирования и опросы. Но ни в коем случае не делай “ради сделать”! 
Схема Plan-Do-Check-Act тебе в помощь🚀.
""")


# -----------------------------------------------------------------------------------------------------------------------------------------------


async def management():
    return (f"""Итак, полгода пролетело незаметно и вот настал новый семестр. Что будешь делать с командой? 😯

1) Продолжу работать со своей командой, они крутые ребята! 🤜🤛
2) Администрация советует присмотреться к первокурсникам 👶 - пожалуй, позовем парочку к себе.
3) Где-то прочитал, что нужно кардинально обновлять состав раз в полгода, так что уволю всех и наберу новичков 🆕️
""")


async def set_management():
    return (f"""Устойчивое развитие - это ж не только про планету Земля. Старайся сохранять баланс между “дедушками” и новичками. """)


async def femki():
    return (
        f"""Тебе прилетает претензия от студентов о том, что в  вашей организации работает больше парней, чем девушек🦸🏼‍♀️. Как ты ответишь на такие обвинения в сексизме?

1) Проигнорирую - я глава организации и не обязан_а объяснять, кто и почему работает со мной в команде😾
2) Объявлю новый набор к нам в команду, приглашу больше представительниц прекрасного пола и установлю квоту на количество девушек в организации - баланс полов должен соблюдаться везде👫
3) В мою организацию попадают только профессионалы, независимо от пола и гендерной принадлежности. Какие тут могут быть претензии🌚?
4) Приглашу критиков к нам на работу. Пусть сначала поработают, а то пороху не нюхали, а языками уже чешут🎃.""")


async def set_femki():
    return (f"""#metoo не попал в студсовет из-за дискриминации 😞""")


async def ignore(state: FSMContext):
    data = await state.get_data()
    return (
        f"""Тебе с председателями {data['pers']} всех факультетов университета поручили совместно организовать мероприятие🎉. По какой-то причине твои коллеги полностью игнорируют подготовку к мероприятию, де-факто, работаешь ты один. Твои действия:

1. Сделаю всё сам. В конце расскажу администрации всю правду о сложившейся ситуации😏.
2. Сделаю всё сам. В конце скажу администрации, что это была слаженная командная работа – мало ли какая ситуация была у ребят🤫.
3. Всячески буду “пинать” ребят и мотивировать их выполнять свою работу🔝. 
4. А мне что, больше всех надо? Никто ничего не делает, вот и я не буду🗿.
""")


async def set_ignore():
    return (
        f"""Ничего умнее, чем “ситуация неоднозначная”, мы не придумали. Быть успешным выскочкой, командным игроком или ябедой-карьеристом - решать тебе.""")


async def event(state: FSMContext):
    data = await state.get_data()
    return (
        f"""День обещал быть беззаботным 🤤, но вдруг к тебе приходит несколько студентов с идеей по ивенту. Они утверждают, что большинство студентов факультета поддерживают идею, но твоя команда в этом сомневается. Как ты на это отреагируешь?

1) Поддержу и помогу с реализацией мероприятия - для чего же еще я на этом посту? 😎 Пусть сами потом разбираются, если кому-то не понравится.
2) Дам поручение своим подчиненным провести исследование 🤓 и узнать точное мнение масс по поводу данной идеи. Исходя из результатов исследования, дам положительный или отрицательный ответ студентам-активистам.
3) Откажусь от проведения 🤐 - у [название органа] есть свой план мероприятий, работы и так выше крыши. Надо было вступать в орган, когда объявляли набор, а не отсиживаться на задних партах.
4) Я и так много поработал_а за этот год, пожалуй, лучше отдохну 😴. Отдам вопрос на рассмотрение своему заму.""")


async def set_event():
    return (
        f"""Кстати, а ты держишь связь с алюмни твоей организации?🎓 Неплохо было бы узнать их мнение, вдруг кто-то из них сталкивался с похожими сложностями в своей карьере.""")


async def putin(state: FSMContext):
    data = await state.get_data()
    return (f"""Год у власти пролетел незаметно, вот-вот грядут выборы. Идешь на второй срок?

1) Да, буду активно участвовать в предвыборной гонке, чтобы остаться у власти. Кто лучше меня справится с этой ролью?👤
2) Внесу поправки в Регламент {data['pers']}, чтобы продлить срок своих полномочий на посту председателя, ведь у меня еще так много идей и энергии. Мы провели опрос в наших соцсетях - меня там все поддерживают📊.
3) Не буду участвовать в выборах. Уйду на пике, как настоящая рок-звезда👨‍🎤.
""")


async def set_putin():
    return (f"""Мы уважаем твой выбор в любом случае. А как насчет студентов?""")


async def putinFOREVOR():
    return (f"""Что будешь делать на предвыборке? 😱
1) Пообещаю сохранить все то, что уже сделано, стабильность - наше все! 🇧🇾
2) Наобещаю всего нового - а что, главное выиграть, там разберемся. 😏
3) Да мне все равно, приду на предвыборные дебаты неготовым - меня и так люди любят. 😍
4) Нарою в соцсетях компромат на конкурентов и представлю его публике - грязно, но действенно! 😈
""")


async def end():
    return (f"""Окей, давай подведем итоги 🤖

⭐️Сводка по акту⭐️

Не засиживайся - иди дальше, ведь впереди так много прекрасного и неизведанного! 🌄 Но не стоит разрывать все накопленные связи, будь активным Alumni своего органа: помогай молодым советом, а иногда и рублем. Нетворкинг и комьюнити - это не просто модные англицизмы, а весьма полезные и одновременно приятные вещи. 
""")


async def putinLOX():
    return (f"""Что скажешь напоследок? 🗣
1) Поблагодарю администрацию&студентов&команду, с которой работал. Это был крутой опыт, который поможет мне в дальнейшей карьере👏.
2) Отдам должное деканату - без них у меня ничего бы не получилось👻.
3) Похвалю себя (сам себя не похвалишь - никто не похвалит), а вину за неудачи скину на команду😌.
4) Не люблю я этот официоз, лучше ничего не буду говорить😑.
""")


async def ALLEND(state: FSMContext):
    data = await state.get_data()
    return (f"""Спасибо тебе за участие! Вот твои метрики 📊:

❤ Лояльность студентов: {data['Students_love']}
💚 Лояльность коллег: {data['Respect_for_colleagues']}
💙 Лояльность администрации: {data['Loyalty_to_the_administration']}

Поделись результатом с друзьями в соц. сетях 💫, чтобы проверить кто из вас топовый менеджер! 🤟
""")

async def creators():
    return(f"""Бот создан студенческой группой по самоуправлению и качеству образованию, действующей в рамках академического сотрудничества белорусских университетов и Института прав человека и гуманитарного права им. Р. Валленберга (Лунд, Швеция)



В программе принимают участие:

🔷Юридический факультет БГУ

🔷Факультет международных отношений БГУ

🔷Факультет права БГЭУ

🔷Факультет технологий управления и гуманитаризации БНТУ

🔷Юридический факультет Полоцкого государственного университета

🔷Факультет экономики и права Могилевского государственного университета им. Кулешова

🔷Юридический факультет Гомельского государственного университета им. Скорины


Подробнее о программе: https://rwi.lu.se/where-we-work/regions/europe/europe-office/
""")


async def users():
    return(f"""😺 Для студентов и студенток белорусских вузов, которые уже вовлечены в студенческое самоуправление или только хотят им заняться в ближайшем будущем.

✅ Пройди тренировку в нашем симуляторе и вперед в оффлайн, творить!
""")

async def exit():
    return(f"""😺Выход обнулит твои результаты🗿. Ты точно хочешь выйти?
""")

async def rule():
    return (f"""Я хочу сыграть с тобой в одну игру 🤡...Ты станешь руководителем одного из трех органов студенческого самоуправления и возьмешь ответственность за каждое принятое тобой решение.



Каждое твое действие влияет на изменение игровых метрик, о которых ты узнаешь в конце игры. Три акта. Три персонажа. Три метрики.



Игра начинается 🎲""")


async def link():
    return (f"""⚙️ Что-то не понравилось, возник вопрос или предложение? Лови ссылку на форму обратной связи😉
https://forms.gle/qrCcYmWroMqmTV1bA""")
async def share_bot(bot):
    return (f"""Привет👋 Я LuchNoNeZavodBot, – симулятор студенческого самоуправления.

Попробуй свои силы на посту лидера студенческой организации💪. 👇😉

https://t.me/{(await bot.me).username}\n""")