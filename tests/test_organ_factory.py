import json

organs = {'organs': [{'name': 'Heart',
                      'args': [['aorta'],
                               ['KDO', 'aorta + LP * 2'],
                               ['OAK'],
                               ['LP'],
                               ['MGP', 'aorta + OAK + bsa'],
                               ['KDRLG']],
                      },
                     {'name': 'Pancreas',
                      'args': [['arg0', 'arg1+arg2+arg3*arg4'],
                               ['arg1', 'arg2 + arg1 + from_mediator'],
                               ['arg2'],
                               ['arg3'],
                               ['arg4']]}]}

organs = organs['organs']

organ_factory = OrganFactory(organs)
print(organ_factory)
