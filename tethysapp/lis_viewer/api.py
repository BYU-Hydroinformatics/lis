from django.http import JsonResponse
from utilities import *
import json
LIS_DIRECTORY = "/lis/"

def api_get_var_list(request):
    '''
    Return a JSON object that contains the list of all the available variables. Needs to be changed to be more dynamic.
    '''
    json_obj = {}
    if request.method == 'GET':

        variable_options = get_lis_variables(LIS_DIRECTORY)

        json_obj = {"variable_options":variable_options}

    return  JsonResponse(json_obj)

def api_get_point_values(request):
    '''
        Return a JSON object that contains the list of all the values for a given point.
    '''
    json_obj = {}

    if request.method == 'GET':
        json_obj = {}

        latitude = None
        longitude = None
        variable = None

        #Check if the parameters exist, if they do, define them
        if request.GET.get('latitude'):
            latitude = request.GET['latitude']
        if request.GET.get('longitude'):
            longitude = request.GET['longitude']
        if request.GET.get('variable'):
            variable = request.GET['variable']

        coords = str(longitude)+','+str(latitude) #Creating the coordinates string so that it can be passed into the get_ts_plot function. See utilities.py

        try:
            graph = get_pt_timeseries(LIS_DIRECTORY,variable,coords)
            graph = json.loads(graph)
            json_obj = graph

            return JsonResponse(json_obj) #Return the json object with a list of the time and corresponding values

        except:
            json_obj ={"Error":"Error Processing Request"} #Show an error if there are any problems executing the script.

            return JsonResponse(json_obj)

    return JsonResponse(json_obj)

def api_get_polygon_values(request):
    '''
        Return a JSON object that contains the list of all the values for a given bounds.
    '''
    json_obj = {}

    # Check if the parameters exist, if they do, define them
    if request.method == 'GET':
        json_obj = {}

        minx = None
        miny = None
        maxx = None
        maxy = None
        variable = None

        if request.GET.get('minx'):
            minx = request.GET['minx']
        if request.GET.get('miny'):
            miny = request.GET['miny']
        if request.GET.get('maxx'):
            maxx = request.GET['maxx']
        if request.GET.get('maxy'):
            maxy = request.GET['maxy']
        if request.GET.get('variable'):
            variable = request.GET['variable']

        bounds = [minx,miny,maxx,maxy] #Creating the bounds list, so that it can be passed into the get_mean function. See utilities.py

        try:
            graph = get_poly_timeseries(LIS_DIRECTORY,variable,bounds)
            graph = json.loads(graph)
            json_obj = graph
            return JsonResponse(json_obj) #Return the json object with a list of the time and corresponding values

        except:
            json_obj = {"Error": "Error Processing Request"}

            return JsonResponse(json_obj) #Throw an error for any exceptions

    return JsonResponse(json_obj)
