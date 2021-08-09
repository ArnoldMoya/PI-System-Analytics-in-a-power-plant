# -*- coding: utf-8 -*-
"""
Spyder Editor

Written by AM
"""

import PIconnect as PI

with PI.PIServer() as server:
    points = server.search('*CDA*')
    print("Amount of PI points in CDA:", len(points))
    for point in points[:5]:
        print(point)