import flickrapi
import image_scrape


class FlickrAPI:
    def __init__(self):
        self.api_key = u'YOUR API KEY'
        self.api_secret = u'YOUR API SECRET'

    def main(self):
        flickr = flickrapi.FlickrAPI(self.api_key, self.api_secret, format='parsed-json')
        photos = flickr.photos.search(
            has_geo=1,
            per_page=250,
            tags="programming",
            license=1,
            media="photos",
            extras="original_format"
        )
        context = photos["photos"]["photo"]
        for photo in range(len(context)):
            innerContext = context[photo]
            farmID = innerContext["farm"]
            serverID = innerContext["server"]
            photoID = innerContext["id"]
            photoSecret = innerContext["originalsecret"]
            photoFormat = innerContext["originalformat"]
            # Divide creation of url to make pep8 calm down
            url = "https://farm" + str(farmID) + ".staticflickr.com/" + str(serverID)
            url += "/"+photoID+"_"+photoSecret+"_o."+photoFormat
            imageScraper = image_scrape.ImageScraper()
            try:
                imageScraper.save_image(url)
            finally:
                print url
                imageScraper.commitObject()
        imageScraper.closeSession()
if __name__ == "__main__":
    flickrAPI = FlickrAPI()
    flickrAPI.main()

# http://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg
# farmID = photos["photos"]["photo"][photo]["farm"]
#                                         ["server"]
#                                         ["id"]
#                                         ["secret"]
