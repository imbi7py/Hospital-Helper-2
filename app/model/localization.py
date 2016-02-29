# -*- coding: UTF-8 -*-

import json

from model import db, logic, exceptions
import options


class Localization:

    __translation = {}

    @classmethod
    def install(cls, lang):

        if lang not in [c.name for c in db.Translation.__table__.columns]:
            raise exceptions.NoSuchTranslation

        cls.create_init_translation()

        strings = db.SESSION.query(db.Translation).all()

        for s in strings:
            transl = getattr(s, lang)
            cls.__translation[s.sys] = transl

        import builtins
        builtins.__dict__['_'] = cls.get_text

    @classmethod
    def get_text(cls, text):
        try:
            return cls.__translation[text]
        except KeyError:
            return text

    @staticmethod
    def add_system_label(label):

        t, _ = db.Translation.get_or_create(sys=logic.Parser.unidecode(label),
                                            defaults={
            'ru': label.replace('_', ' ').lstrip()
        })

        db.SESSION.add(t)

    @classmethod
    def create_init_translation(cls):

        structure = db.SESSION.query(db.KeyValue).filter(
            db.KeyValue.key == options.STRUCTURE_KEY).first()

        try:
            structure = json.loads(structure.value)
        except AttributeError:
            raise exceptions.AppNotReady

        for item in structure:
            for arg in item['args']:
                cls.add_system_label(arg['name'])

            for l in ('group', 'name', 'verbose_name'):
                s = item.get(l)
                if s:
                    cls.add_system_label(s)