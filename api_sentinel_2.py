
# connect to the API
# import api as api
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
from collections import OrderedDict


#api = SentinelAPI('user', 'password', 'https://scihub.copernicus.eu/dhus')
api = SentinelAPI('rafa99', 'Rafa030898', 'https://scihub.copernicus.eu/dhus')


# Download cena única por id de produto conhecido


#product_id = 'S2A_MSIL2A_20171015T113321_N0205_R080_T29TNG_20171015T113318'

#product_id = 'S2_OFFLINE-2557d1a6-b29e-4100-aaf1-148fd7fc4211'

# https://scihub.copernicus.eu/userguide/LongTermArchive


# pesquisar por polígono, hora e palavras-chave de consulta SciHub
footprint = geojson_to_wkt(read_geojson('map.geojson'))
products = api.query(footprint,
                     #date= (date(2017, 7, 15), date(2019, 7, 15)),
                     #date= (date(2019, 7, 15), 'NOW'),
                     date= (date(2017, 7, 15), date(2018, 7, 15)),
                     platformname='Sentinel-2',
                     cloudcoverpercentage=(0, 30))

print('\nNumero de produtos encontrados= ', (len(products)))

#print('\nProdutos= ', products, '\n')    # print corrido de todos os produtos disponiveis


# convert to Pandas DataFrame
products_df = api.to_dataframe(products)
print('\nProdutos= ', products_df, '\n')  # Retorna os produtos de uma resposta de consulta como um Pandas DataFrame


# GeoJSON FeatureCollection containing footprints and metadata of the scenes
api.to_geojson(products)


# GeoPandas GeoDataFrame with the metadata of the scenes and the footprints as geometries
#api.to_geodataframe(products)
#print('\nProd= ', products_geodf, '\n')


# baixar todos os resultados da pesquisa
api.download_all(products)





# Get basic information about the product: its title, file size, MD5 sum, date, footprint and its download url
api.get_product_odata(product_id)

# Get the product's full metadata available on the server
api.get_product_odata(product_id, full=True)
