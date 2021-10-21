from proxy import Image, ProxyImage

img1 = Image("HiRes_10Mb_Photo1")
proxy_image1 = ProxyImage (img1)

img2 = Image("HiRes_10Mb_Photo2")
proxy_image2 = ProxyImage (img2)

proxy_image1.display_image() # loading necessary
proxy_image1.display_image() # loading unnecessary
proxy_image1.display_image() # loading unnecessary

#proxy_image2.display_image() # loading necessary
#proxy_image2.display_image() # loading unnecessary
