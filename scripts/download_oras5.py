import cdsapi

c = cdsapi.Client()

years = ['19%d' % i for i in range(58, 100)] + ['200%d' % i for i in range(0,10)] + ['20%d' % i for i in range(10,23)]
months = ['0%d' % i for i in range(1,10)] + ['10','11','12']
variables = ['net_downward_heat_flux', 'net_upward_water_flux', 'ocean_heat_content_for_the_total_water_column',
                'ocean_heat_content_for_the_upper_300m','ocean_heat_content_for_the_upper_700m', 'sea_surface_height',
                'sea_surface_temperature']
for year in years:
    print('Downloading data for %s:' % year)
    if int(year) < 2015:
        product_type = 'consolidated'
    else:
        product_type = 'operational'
    c.retrieve(
        'reanalysis-oras5',
        {
            'format': 'zip',
            'product_type': [product_type],
            'vertical_resolution': 'single_level',
            'variable': variables,
            'year': [year],
            'month': months,
        },
        '/scratch/zt1/project/edott-prj/user/awikner1/denso/ORAS5/%s.zip' % year)

