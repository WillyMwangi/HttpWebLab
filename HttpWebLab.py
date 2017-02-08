import urllib2
import json


def render_output_data(data):

    json_response = json.loads(data) # Use the json module input data into a dictionary


def main():

    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib2.urlopen(urlData)       # Open the URL and read the data
    print webUrl.getcode()
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        render_output_data(data)
    else:
        print "Retrieving results failed try again.Error" + str(webUrl.getcode())


if __name__ == "__main__":
    main()