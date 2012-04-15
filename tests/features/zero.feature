Feature: Get a thumbnail
  To get a thumbnail of an image
  As a user
  I want to send access an url and get my thumbnail

  Scenario: With an url
    Given /<engine>/?url=<url>&width=<width>&height=<height>
	When I access the api url
	Then I get my image at size <width>x<height>
    
	Examples:
      | engine | url                            | width | height |
      | resize | http://localhost:8000/toto.jpg |  800  |  600   |
