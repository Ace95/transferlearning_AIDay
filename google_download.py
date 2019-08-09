from google_images_download import google_images_download

# Dowload images from Google 

response = google_images_download.googleimagesdownload()

arguments = {
            "keywords" : "pikachu",
            "limit" : 100,
            "print_urls" : False,
            "format" : "jpg",
            "size" : ">400*300",
            "output_directory" : "images"
            }

paths = response.download(arguments)

response = google_images_download.googleimagesdownload()

arguments = {
                "keywords" : "charizard",
                "limit" : 100,
                "print_urls" : False,
                "format" : "jpg",
                "size" : ">400*300",
                "output_directory" : "images"
}

paths = response.download(arguments)
