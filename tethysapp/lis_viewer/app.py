from tethys_sdk.base import TethysAppBase, url_map_maker


class LisObservationsExplorer(TethysAppBase):
    """
    Tethys app class for LIS Observations Explorer.
    """

    name = 'LIS Observations Explorer'
    index = 'lis_viewer:home'
    icon = 'lis_viewer/images/logo.png'
    package = 'lis_viewer'
    root_url = 'lis-viewer'
    color = '#00a1ff'
    description = 'View LIS Model data'
    tags = ''
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='lis-viewer',
                           controller='lis_viewer.controllers.home'),
                    UrlMap(name='api',
                           url='lis-viewer/api',
                           controller='lis_viewer.controllers.api'),
                    UrlMap(name='get-ts',
                           url='lis-viewer/get-ts',
                           controller='lis_viewer.controllers.get_ts'),
                    UrlMap(name='upload-shp',
                           url='lis-viewer/upload-shp',
                           controller='lis_viewer.ajax_controllers.upload_shp'),
                    UrlMap(name='api_get_var_list',
                           url='lis-viewer/api/GetVariableList',
                           controller='lis_viewer.api.api_get_var_list'),
                    UrlMap(name='api_get_point_values',
                           url='lis-viewer/api/GetPointValues',
                           controller='lis_viewer.api.api_get_point_values'),
                    UrlMap(name='api_get_polygon_values',
                           url='lis-viewer/api/GetPolygonValues',
                           controller='lis_viewer.api.api_get_polygon_values'),
                    )

        return url_maps