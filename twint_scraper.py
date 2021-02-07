# -*- coding: utf-8 -*-
"""
Created on Sat Feb 6 10:03:47 2021
@author: adi
"""

import nest_asyncio
nest_asyncio.apply()

import twint

c = twint.Config()
c.Lang = "en"

c.Search = ["plandemic" or "masksoffamerica" or "pandemichoax"]
c.Limit = 600
c.Since = "2020-10-06 13:00:00"
c.Store_csv = True
c.Output = "none.csv"

twint.run.Search(c)
