[![Article DOI:10.1038/s41597-022-01878-2](https://img.shields.io/badge/Article%20DOI-10.1038%2Fs41597.022.01878.2-blue)](https://doi.org/10.1038/s41597-022-01878-2)  [![PyPI](https://img.shields.io/pypi/v/cloudsen12_models)](https://pypi.org/project/cloudsen12_models/) [![PyPI - License](https://img.shields.io/pypi/l/cloudsen12_models)](https://github.com/spaceml-org/cloudsen12_models/blob/main/LICENSE)

<h1> <img src="https://raw.githubusercontent.com/IPL-UV/cloudsen12_models/main/notebooks/logo.webp" alt="Logo" width='5%'> 
	<a href="https://cloudsen12.github.io/"> CloudSEN12 </a> 
</h1>

This package contains minimum code to run the CloudSEN12 models proposed in [Aybar et al. 2022](https://www.nature.com/articles/s41597-022-01878-02) and [Aybar et al. 2024](https://www.sciencedirect.com/science/article/pii/S2352340924008163). The main dependencies of this package are pytorch and the [georeader](https://github.com/spaceml-org/georeader) package which only depends on rasterio and geopandas libraries.

The notebook [run_in_gee_image.ipynb](https://github.com/IPL-UV/cloudsen12_models/blob/main/notebooks/run_in_gee_image.ipynb) has an example of running the model on a Sentinel-2 image downloaded from the Google Earth Engine:

 <img src="https://raw.githubusercontent.com/IPL-UV/cloudsen12_models/main/notebooks/example_flood_dubai_2024.png">

For more examples see [cloudsen12.github.io](https://cloudsen12.github.io/).

## Citation

If you find this code useful please cite:

```
@article{aybar_cloudsen12_2024,
	title = {{CloudSEN12}+: {The} largest dataset of expert-labeled pixels for cloud and cloud shadow detection in {Sentinel}-2},
	issn = {2352-3409},
	url = {https://www.sciencedirect.com/science/article/pii/S2352340924008163},
	doi = {10.1016/j.dib.2024.110852},
	journal = {Data in Brief},
	author = {Aybar, Cesar and Bautista, Lesly and Montero, David and Contreras, Julio and Ayala, Daryl and Prudencio, Fernando and Loja, Jhomira and Ysuhuaylas, Luis and Herrera, Fernando and Gonzales, Karen and Valladares, Jeanett and Flores, Lucy A. and Mamani, Evelin and Quiñonez, Maria and Fajardo, Rai and Espinoza, Wendy and Limas, Antonio and Yali, Roy and Alcántara, Alejandro and Leyva, Martin and Loayza-Muro, Rau´l and Willems, Bram and Mateo-García, Gonzalo and Gómez-Chova, Luis},
	month = aug,
	year = {2024},
	pages = {110852},
}

@article{aybar_cloudsen12_2022,
	title = {{CloudSEN12}, a global dataset for semantic understanding of cloud and cloud shadow in {Sentinel}-2},
	volume = {9},
	issn = {2052-4463},
	url = {https://www.nature.com/articles/s41597-022-01878-2},
	doi = {10.1038/s41597-022-01878-2},
	number = {1},
	urldate = {2023-01-02},
	journal = {Scientific Data},
	author = {Aybar, Cesar and Ysuhuaylas, Luis and Loja, Jhomira and Gonzales, Karen and Herrera, Fernando and Bautista, Lesly and Yali, Roy and Flores, Angie and Diaz, Lissette and Cuenca, Nicole and Espinoza, Wendy and Prudencio, Fernando and Llactayo, Valeria and Montero, David and Sudmanns, Martin and Tiede, Dirk and Mateo-García, Gonzalo and Gómez-Chova, Luis},
	month = dec,
	year = {2022},
	pages = {782},
}
```
