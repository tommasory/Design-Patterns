class Image:
   def __init__( self, filename ):
      self._filename = filename
   
   def load_image_from_disk( self ):
      print("L. loading " + self._filename )
   
   def display_image( self ):
      print("D. display " + self._filename)

class Proxy:
   def __init__( self, subject ):
      self._subject = subject
      self._proxystate = None

class ProxyImage( Proxy ):

   def display_image( self ):
      if self._proxystate == None:
         self._subject.load_image_from_disk()
         self._proxystate = 1
      print("1. display " + self._subject._filename )