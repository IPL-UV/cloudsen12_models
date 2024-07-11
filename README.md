[![Article DOI:10.1038/s41597-022-01878-2](https://img.shields.io/badge/Article%20DOI-10.1038%2Fs41597.022.01878.2-blue)](https://doi.org/10.1038/s41597-022-01878-2)  [![PyPI](https://img.shields.io/pypi/v/cloudsen12_models)](https://pypi.org/project/cloudsen12_models/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cloudsen12_models)](https://pypi.org/project/cloudsen12_models/) [![PyPI - License](https://img.shields.io/pypi/l/cloudsen12_models)](https://github.com/spaceml-org/cloudsen12_models/blob/main/LICENSE)

# cloudsen12_models

This package contains minimum code to run the CloudSEN12 models proposed in [Aybar et al. 2023](https://www.nature.com/articles/s41597-022-01878-02). It uses the [georeader](https://github.com/spaceml-org/georeader) package which only depends on rasterio and geopandas libraries.

The notebook [run_in_gee_image.ipynb]() has a minimum example of running the model.


## Citation

If you find this code useful please cite:

```
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