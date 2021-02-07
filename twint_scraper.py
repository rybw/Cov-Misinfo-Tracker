import nest_asyncio
nest_asyncio.apply()

import twint

c = twint.Config()
#c.Username = "KarenBot17"
c.Lang = "en"


c.Search = ["plandemic" or "masksoffamerica" or "pandemichoax"]
c.Limit = 600
c.Since = "2020-10-06 13:00:00"
c.Store_csv = True
c.Output = "none.csv"

# Run
twint.run.Search(c)