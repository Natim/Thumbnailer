Feature: Get a thumbnail
  To get a thumbnail of an image
  As a user
  I want to send access an url and get my thumbnail

  Scenario: With an image to resize into a box
    Given /<engine>/?url=<url>&width=<width>&height=<height>
	When I access the api url
	Then I get my image at max size <width>x<height>
    
	Examples:
      | engine    | url												| width | height |
      | scale     | http://localhost:8000/images/horizontal.jpg 	|  800  |  600   |
      | scale     | http://localhost:8000/images/vertical.jpg		|  200  |  300   |
      | scale	  | http://localhost:8000/images/vertical.jpg		|  200  |    0   |
      | scale     | http://localhost:8000/images/vertical.jpg		|    0  |  200   |
      | document  | http://localhost:8000/documents/document.pdf	|  500  |  500   |

  Scenario: With an image to crop
    Given /<engine>/?url=<url>&width=<width>&height=<height>
	When I access the api url
	Then I get my image at size <width>x<height>
    
	Examples:
      | engine    | url                                         	| width | height |
      | crop      | http://localhost:8000/images/horizontal.jpg 	|  800  |  600   |
      | crop      | http://localhost:8000/images/vertical.jpg   	|  200  |  300   |
      | upscale   | http://localhost:8000/images/horizontal.jpg 	|  600  |  600   |
      | upscale   | http://localhost:8000/images/vertical.jpg   	|  600  |  500   |
