[![Article DOI:10.1038/s41597-022-01878-2](https://img.shields.io/badge/Article%20DOI-10.1038%2Fs41597.022.01878.2-blue)](https://doi.org/10.1038/s41597-022-01878-2) [![Article DOI:10.1016/j.dib.2024.110852](https://img.shields.io/badge/Article%20DOI-10.1016%2Fj.dib.2024.110852-blue)](https://doi.org/10.1016/j.dib.2024.110852)  [![PyPI](https://img.shields.io/pypi/v/cloudsen12_models)](https://pypi.org/project/cloudsen12_models/) [![PyPI - License](https://img.shields.io/pypi/l/cloudsen12_models)](https://github.com/spaceml-org/cloudsen12_models/blob/main/LICENSE) [![HF](https://img.shields.io/badge/%F0%9F%A4%97-Datasets-yellow)](https://huggingface.co/datasets/isp-uv-es/CloudSEN12Plus) [![HF](https://img.shields.io/badge/%F0%9F%A4%97-Models-yellow)](https://huggingface.co/isp-uv-es/cloudsen12_models)

<h1> <img src="https://raw.githubusercontent.com/IPL-UV/cloudsen12_models/main/notebooks/logo.webp" alt="Logo" width='5%'> 
	<a href="https://cloudsen12.github.io/"> CloudSEN12 </a> 
</h1>

This package contains minimum code to run the CloudSEN12 models proposed in [Aybar et al. 2022](https://www.nature.com/articles/s41597-022-01878-02) and [Aybar et al. 2024](https://www.sciencedirect.com/science/article/pii/S2352340924008163). The main dependencies of this package are pytorch and the [georeader](https://github.com/spaceml-org/georeader) package which only depends on rasterio and geopandas libraries.

The notebook [run_in_gee_image.ipynb](https://github.com/IPL-UV/cloudsen12_models/blob/main/notebooks/run_in_gee_image.ipynb) has an example of running the model on a Sentinel-2 image downloaded from the Google Earth Engine:

 <img src="https://raw.githubusercontent.com/IPL-UV/cloudsen12_models/main/notebooks/example_flood_dubai_2024.png">

For examples about dataset use and training see [cloudsen12.github.io](https://cloudsen12.github.io/).

## models
With this package, the following models can be loaded: (with the function [`cloudsen12.load_model_by_name()`](https://github.com/IPL-UV/cloudsen12_models/blob/main/cloudsen12_models/cloudsen12.py#L167))

* **cloudsen12** Model trained on the 13 bands of Sentinel-2 L1C in the CloudSEN12 dataset.
* **cloudsen12l2a**  Model trained on the 12 bands of Sentinel-2 L2A in the CloudSEN12 dataset.
* **dtacs4bands** Model trained on the NIR, RED, GREEN and BLUE bands of Sentinel-2 L1C in the CloudSEN12 dataset. Bands: `["B08", "B04", "B03", "B02"]`
* **landsat30** Model trained on the common bands of Sentinel-2 L1C and Landsat 8 and 9 in the CloudSEN12 dataset. Bands: `['B01', 'B02', 'B03', 'B04', 'B08', 'B10', 'B11', 'B12']`.
* **UNetMobV2_V1** Model trained on the 13 bands of Sentinel-2 L1C in the CloudSEN12 dataset. The cloud masks of this model are included in CloudSEN12+ dataset.
* **UNetMobV2_V2** Model trained on the 13 bands of Sentinel-2 L1C in the CloudSEN12+.

## Citation

If you find this code useful please cite:

```
@article{aybar_cloudsen12_2024,
	title = {{CloudSEN12}+: {The} largest dataset of expert-labeled pixels for cloud and cloud shadow detection in {Sentinel}-2},
	issn = {2352-3409},
	url = {https://www.sciencedirect.com/science/article/pii/S2352340924008163},
	doi = {10.1016/j.dib.2024.110852},
	journal = {Data in Brief},
	author = {Aybar, Cesar and Bautista, Lesly and Montero, David and Contreras, Julio and Ayala, Daryl and Prudencio, Fernando and Loja, Jhomira and Ysuhuaylas, Luis and Herrera, Fernando and Gonzales, Karen and Valladares, Jeanett and Flores, Lucy A. and Mamani, Evelin and Quiñonez, Maria and Fajardo, Rai and Espinoza, Wendy and Limas, Antonio and Yali, Roy and Alcántara, Alejandro and Leyva, Martin and Loayza-Muro, Raúl and Willems, Bram and Mateo-García, Gonzalo and Gómez-Chova, Luis},
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

## Acknowledgments

This research has been funded by the DEEPCLOUD project (PID2019-109026RB-I00) funded by the Spanish Ministry of Science and Innovation (MCIN/AEI/10.13039/501100011033) and the European Union (NextGenerationEU).

<img width="300" title="DEEPCLOUD project (PID2019-109026RB-I00, University of Valencia) funded by MCIN/AEI/10.13039/501100011033." alt="DEEPCLOUD project (PID2019-109026RB-I00, University of Valencia) funded by MCIN/AEI/10.13039/501100011033." src="https://www.uv.es/chovago/logos/logoMICIN.jpg">

