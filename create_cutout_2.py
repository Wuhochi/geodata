
# In this example we assume you have set in config.py

# ncep_dir = '/path/to/weather_data/'

# where the files have format e.g.

# 'ncep_dir/{year}{month:0>2}/tmp2m.*.grb2'

import logging
logging.basicConfig(level=logging.DEBUG)

import atlite

cutout = atlite.Cutout(name="europe-sub-2011-01",
                       module="era5",
                       xs=slice(30, 41.56244222),
                       ys=slice(40, 33.56459975),
                       years=slice(2011, 2011),
                       months=slice(1,1,1) )

#this is where all the work happens - it took 105 minutes on FIAS'
#beast resi, with 16 cores; the resulting cutout takes 57 GB
cutout.prepare()
