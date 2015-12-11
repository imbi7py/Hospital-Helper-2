# -*- coding: UTF-8 -*-


STRUCTURE_KEY = 'structure'

INIT_STRUCTURE = """[{
    "name": "Клиент",
    "verbose_name": "",
    "db": true,
    "group": "Клиент", 
    "relations": ["doctor"],
        "args": [{
        "name": "Фамилия",
        "type": "str"
    }, {
        "name": "Имя",
        "type": "str"
    }, {
        "name": "Отчество",
        "type": "str"
    }, {
        "name": "Возраст",
        "type": "str"
    }, {
        "name": "Чсс",
        "type": "str"
    }, {
        "name": "Рост",
        "type": "str"
    }, {
        "name": "Вес",
        "type": "str"
    }, {
        "name": "_ППТ",
        "calculation": "sqrt(Рост * Вес / 3600)"
    }]
}, {
    "name": "Сердце",
    "db": true,
    "relations": ["Клиент"],
    "args": [{
        "name": "Аорта"
    }, {
        "name": "ОАК"
    }, {
        "name": "ЛП"
    }, {
        "name": "КДРЛЖ"
    }, {
        "name": "КСРЛЖ"
    }, {
        "name": "ЗСЛЖ"
    }, {
        "name": "МЖП"
    }, {
        "name": "АК"
    }, {
        "name": "КЛА"
    }, {
        "name": "ПП"
    }, {
        "name": "ПЖ"
    }, {
        "name": "НПВ"
    }, {
        "name": "КДО",
        "calculation": "7 / (2.4 + (0.1 * КДРЛЖ)) * (0.1 * КДРЛЖ) ** 3"
    }, {
        "name": "КСО",
        "calculation": "7 / (2.4 + 0.1 * КСРЛЖ) * 0.1 * КСРЛЖ ** 3"
    }, {
        "name": "ФВ",
        "calculation": "((КДО - КСО) / КДО) * 100"
    }, {
        "name": "ИММЛЖ",
        "calculation": "(0.8 * (1.04 * (sum((КДРЛЖ, МЖП, ЗСЛЖ)) ** 3) - КДРЛЖ ** 3) + 0.6) / Клиент._ППТ"
    }, {
        "name": "ОТС",
        "calculation": "(2 * ЗСЛЖ) / КДРЛЖ"
    }]
}, {
    "name": "Печень",
    "group": "Брюшная полость", 
    "db": true,
    "relations": ["Клиент"],
    "args": [{
        "name": "КВР"
    }, {
        "name": "ВВ"
    }, {
        "name": "НПВ"
    }, {
        "name": "Холедох"
    }]
}, {
    "name": "Желчный",
    "group": "Брюшная полость", 
    "db": true,
    "relations": ["Клиент"],
    "args": [{
        "name": "Длина"
    }, {
        "name": "Ширина"
    }, {
        "name": "Толщина"
    }, {
        "name": "Стенка"
    }, {
        "name": "Объем",
        "calculation": "0.00052 * (Длина * Ширина * Толщина)"
    }]
}, {
    "name": "Поджелудочная",
    "verbose_name": "Поджелудочная железа",
    "group": "Брюшная полость", 
    "db": true,
    "relations": ["Клиент"],
    "args": [{
        "name": "Головка"
    }, {
        "name": "Тело"
    }, {
        "name": "Хвост"
    }, {
        "name": "Вирсунгов"
    }]
}, {
    "name": "Селезенка",
    "group": "Брюшная полость", 
    "db": true,
    "relations": ["Клиент"],
    "args": [{
        "name": "Длина"
    }, {
        "name": "Ширина"
    }, {
        "name": "Толщина"
    }, {
        "name": "Площадь"
    }]
}, {
    "name": "Почки",
    "db": true,
    "relations": ["Клиент"],
    "args": [{
        "name": "Длина"
    }, {
        "name": "Ширина"
    }, {
        "name": "Паренхим"
    }, {
        "name": "Чашечки"
    }, {
        "name": "Лоханка"
    }, {
        "name": "Длина_2"
    }, {
        "name": "Ширина_2"
    }, {
        "name": "Паренхим_2"
    }, {
        "name": "Чашечки_2"
    }, {
        "name": "Лоханка_2"
    }]
}, {
    "name": "Щитовидная",
    "verbose_name": "Щитовидная железа",
    "db": true,
    "relations": ["Клиент"],
    "args": [{
        "name": "Перешеек"
    }, {
        "name": "Длина"
    }, {
        "name": "Ширина"
    }, {
        "name": "Толщина"
    }, {
        "name": "Объем",
        "calculation": "0.00048 * (Длина * Ширина * Толщина)"
    }, {
        "name": "Длина_2"
    }, {
        "name": "Ширина_2"
    }, {
        "name": "Толщина_2"
    }, {
        "name": "Объем_2",
        "calculation": "0.00048 * (Длина_2 * Ширина_2 * Толщина_2)"
    }, {
        "name": "V_общ",
        "calculation": "Объем + Объем_2"
    }]
}, {
    "name": "Предстательная",
    "verbose_name": "Предстательная железа",
    "db": true,
    "relations": ["Клиент"],
    "args": [{
        "name": "Длина"
    }, {
        "name": "Ширина"
    }, {
        "name": "Толщина"
    }, {
        "name": "Объем",
        "calculation": "0.00052 * (Длина * Ширина * Толщина)"
    }]
}, {
    "name": "М.Пузырь",
    "verbose_name": "Мочевой пузырь",
    "db": true,
    "relations": ["Клиент"],
    "args": [{
        "name": "Длина"
    }, {
        "name": "Ширина"
    }, {
        "name": "Толщина"
    }, {
        "name": "Стенка"
    }, {
        "name": "Объем",
        "calculation": "0.00052 * (Длина * Ширина * Толщина)"
    }]
}, {
    "name": "Гинекология",
    "db": true,
    "relations": ["Клиент"],
    "args": []
}, {
    "name": "Образование",
    "db": true,
    "relations": ["Клиент"],
    "args": [{
        "name": "Длина_1"
    }, {
        "name": "Длина_2"
    }, {
        "name": "Длина_3"
    }, {
        "name": "Длина_4"
    }, {
        "name": "Длина_5"
    }, {
        "name": "Длина_6"
    }]
}, {
    "name": "Киста",
    "db": true,
    "relations": ["Клиент"],
    "args": [{
        "name": "Длина_1"
    }, {
        "name": "Длина_2"
    }, {
        "name": "Длина_3"
    }, {
        "name": "Длина_4"
    }, {
        "name": "Длина_5"
    }, {
        "name": "Длина_6"
    }, {
        "name": "Длина_7"
    }, {
        "name": "Длина_8"
    }]
}]"""

DATABASE = 'data.db'
