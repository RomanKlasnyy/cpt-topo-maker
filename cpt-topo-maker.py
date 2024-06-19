"""
Supported topologies: mesh, star, tree, ring, bus
At least 1 switch per topology!
2 to 10 end devices per topology!
Mesh: 4, 6, 8, 10 | Calc con: x * 2.5  | Switches: y = x
Star: 2-10        | Calc con: x        | Switches: y = 1
Tree: 2-10        | Cal con: x + 2     | Switches: y = 3
Ring: 3-10        | Cal con: x * 2     | Switches: y = x
Bus: 2-10         | Cal con: x * 2 - 1 | Switches: y = x
Mesh > Ring > Bus > Tree > Star
Suggestions per dev amount: 3-5
"""
import os
import random


def main():
    devices = int(input('Amount of devices (2-10): '))
    assert 2 <= devices <= 10
    switches = int(input('Amount of switches (1-10): '))
    assert 1 <= switches <= 10
    cables = int(input('Amount of cables (2-25): '))
    assert 2 <= cables <= 25
    topos = []
    if devices in [4, 6, 8, 10] and switches >= devices and cables >= devices * 2.5:
        topos.append('mesh')
    if 2 <= devices <= 10 and switches >= 1 and cables >= devices:
        topos.append('star')
    if 2 <= devices <= 10 and switches >= 3 and cables >= devices + 2:
        topos.append('tree')
    if 3 <= devices <= 10 and switches >= devices and cables >= devices * 2:
        topos.append('ring')
    if 2 <= devices <= 10 and switches >= devices and cables >= devices * 2 - 1:
        topos.append('bus')
    if topos:
        ans = input(f'Choose a topology from the list: {topos}')
        if ans in topos:
            os.startfile(rf".\topos\{ans}{devices}.pkt")
        else:
            print('Choosing a topology randomly...')
            os.startfile(rf".\topos\{random.choice(topos)}{devices}.pkt")
    else:
        print('Impossible to build a topology from the given input')


if __name__ == '__main__':
    main()
