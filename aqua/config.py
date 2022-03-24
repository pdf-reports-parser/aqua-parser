import types

TOC_HEADING = 2
TOC_BOTTOM = 3

SMD_ERROR = ('SMD', None, '')

TOC = types.MappingProxyType({
    'smd': 0,
    'status': 1,
    'value_description': 2,
    'single_value': 3,
    'trial_object': 4,
})

toc_table_settings = {
    'edge_min_length': 200,  # this param get clean toc table default 3
}
