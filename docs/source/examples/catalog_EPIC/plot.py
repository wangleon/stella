#!/usr/bin/env python3
import os
import numpy as np
import astropy.io.fits as fits
from stella.catalog.utils import plot_skymap, plot_histogram, plot_histogram2d

def main():

    ra_lst  = np.array([])
    dec_lst = np.array([])
    kp_lst  = np.array([])
    teff_lst = np.array([])
    logg_lst = np.array([])
    for i in range(1,7):
        # read data file
        catfile = os.path.join(os.getenv('STELLA_DATA'), 'catalog/EPIC_%d.fits'%i)
        data = fits.getdata(catfile)
        mask = data['EPIC']>0

        # plot skymap
        ra_lst  = np.append(ra_lst, data[mask]['RAdeg'])
        dec_lst = np.append(dec_lst, data[mask]['DEdeg'])
        kp_lst  = np.append(kp_lst, data[mask]['kepmag'])
        mask1 = data['Teff']>0
        teff_lst = np.append(teff_lst, data[mask1]['Teff'])
        logg_lst = np.append(logg_lst, data[mask1]['logg'])

    plot_skymap(ra_lst, dec_lst, 'skymap_epic.png', size=1, alpha=0.01)

    plot_histogram(kp_lst,
            bins    = np.arange(0, 20),
            figfile = 'maghist_epic.png',
            xlabel  = '$K_\mathrm{p}$',
            xticks  = np.arange(0, 21, 2),
            )

    # plot Kiel histogram
    plot_histogram2d(teff_lst, logg_lst,
            xbins     = np.arange(2000, 12001, 100),
            ybins     = np.arange(0, 6.01, 0.1),
            xlabel    = '$T_\mathrm{eff}$ (K)',
            ylabel    = '$\log{g}$',
            figfile   = 'kielhist_epic.png',
            reverse_x = True,
            reverse_y = True,
            scale     = 'log',
            )

if __name__=='__main__':
    main()
