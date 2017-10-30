# ACROM

[![Licence](http://img.shields.io/badge/license-GPLv3-blue.svg?style=flat)](https://www.gnu.org/licenses/gpl-3.0.en.html)

ACROM
** Tools (Beta version) for analysis of Light Curves from CoRoT **


A set of python scripts in beta version for analysis of chromatic COROT Light Curves. Contains functionalities for filtering, detrending and plotting  the chromatic light curves registered by the COROT Satellite.
This tools may be utils for treat with chromatic light curves (coming from COROT or other surveys) with purpose to study the  achromatic nature of exoplanetary transits.
This code was developed as part of thesis "Transitos de exoplanetas con CoRoT en diferentes colores" (Exoplanet´s Transits with CoRoT in different colors) in the Valencian International university (2014).  

If you use Acrom in your research, please cite:

Dorado-Daza, D.J. 2014. Exoplanet´s Transits with CoRoT in different colors. Valencian International University, Valencia, Spain.

### Filtering:
From a raw COROT light curve in ASCII Format (i.e, corot-2b.txt), this script allows to filter bad points (status > 0) and to generate sub light curves Red (R), Green (G) and Blue (B) in their respective files.
<img src="img/Corot 2b_raw.jpg" width="700" />

### Detrending: 
From the sub light curves (R,G,B), this script runs a moving average algorithm  (a type of Convolution) to deal  with the COROT Light Curves ’ s long-term trend.
<img src="img/R_LC_FilteredDetrend.jpg" width="700" />
<img src="img/G_LC_FilteredDetrend.jpg" width="700" />
<img src="img/B_LC_FilteredDetrend.jpg" width="700" />

### Folding Phase: 
Applies folding phase to sub light curves (R,G,B).
<img src="img/R_LC_FilteredDetrendedFoldingPhase.png" width="700" />
<img src="img/G_LC_FilteredDetrendedFoldingPhase.png" width="700" />
<img src="img/B_LC_FilteredDetrendedFoldingPhase.png" width="700" />

### Plotting: 
This scripts allows to show the graphs of sub light curves generated.


# Author

Derian Jesús Dorado-Daza (2014). If you have a sugesttion or observation, please write to derianjesus.dorado@campusviu.es 
