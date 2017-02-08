import urllib2
import json


def render_output_data(data):

    json_response = json.loads(data) # Use the json module input data into a dictionary
    if "title" in json_response["metadata"]:        # to access the contents in the JSON
        print json_response["metadata"]["title"]
        print "=" * 50

    count = json_response["metadata"]["count"]
    events_recorded = str(count) + " events recorded"
    print events_recorded.center(50)
    print "_" * 50          # print a line for goo display of title before the main data


    for i in json_response["features"]: # looping through all content of the USGS data
        print i["properties"]["place"]      # print the properties which are map positions and place it occured.

    for i in json_response["features"]:     # print the events that only have a magnitude greater than 7
        if i["properties"]["mag"] >= 7.0:
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]

    print     # print blank line to create spacing

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