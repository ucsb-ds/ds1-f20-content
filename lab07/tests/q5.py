test = {   'name': 'q5',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> round(training.take(0).column("Claw Width").item(0), 4) == 13.0142\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> #training.take(159);\n>>> round(training.take(159).column("Tail Length").item(0), 3) == 11.041\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> round(testing.take(0).column("Claw Width").item(0), 4) == 15.3296\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> round(testing.take(39).column("Claw Width").item(0), 4) == 11.9751\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> testing.num_rows * training.num_rows + testing.num_rows**2 * training.num_rows**2 == 40966400\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}