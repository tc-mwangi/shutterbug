# Click™

**click**, is a fan website dedicated to the epic MIRROR'S EDGE™ CATALYST Game Franchise. User's are able to view images and profiles of the characters in the game.


##Screenshots

![image](https://github.com/tc-mwangi/shutterbugg-Django/blob/master/static/screenshots/screencapture-figma-proto-YY7ptjpqnZURS5wsZkVD1I4M-Untitled-2019-03-05-07_48_20%20copy.png)

![image](https://github.com/tc-mwangi/shutterbugg-Django/blob/master/static/screenshots/screencapture-figma-proto-YY7ptjpqnZURS5wsZkVD1I4M-Untitled-2019-03-05-07_51_51%20copy.png)

![image](https://github.com/tc-mwangi/shutterbugg-Django/blob/master/static/screenshots/screencapture-figma-proto-YY7ptjpqnZURS5wsZkVD1I4M-Untitled-2019-03-05-07_52_21%20copy.png)

![image](https://github.com/tc-mwangi/shutterbugg-Django/blob/master/static/screenshots/screencapture-figma-proto-YY7ptjpqnZURS5wsZkVD1I4M-Untitled-2019-03-05-07_53_01%20(1)%20copy.png)


## Installation
OS X

### Pre-requisites
* [Python 3](https://www.python.org/)
* [Django version 1.11.17](https://www.djangoproject.com/download/)
* IDE of your choice.


### Steps

* Clone the app to a directory.
```
git clone https://github.com/tc-mwangi/shutterbugg-Django.git
```

* Build Locally

```
$ python -m venv virtual
$ source virtual/bin/activate
$ pip install -r requirements.txt
$ DEVELOPMENT=1 python manage.py runserver
```

* Serve

```
Then visit http://localhost:8000 to view the app. 
```

### User Stories

* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page. 
* Search for different categories of photos. Categories are based on the characters of the game.
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.


### BDD
|     | Behaviour    |          Input                | Output    | 
|--- | ---         |     ---      |          --- |
|  1. | display menu options |     | home, characters, locations, search      |
|  2. | display images on homepage |    | on click , open image modal  with image details and share button option  |
|  3. | diplay images based on characters  |  -  |  redirect to selected character's page  |
|  4. | diplay images based on locations found in the game  |  -  |  redirect to selected location page  |
|  5. | display search bar |  search_term based on categories  | redirect to search results page |


## Author

**@top-cat** - *Initial work* - [Click™](https://github.com/tc-mwangi/shutterbugg-Django)


## Credits

**Powered by** [-](/)

## License
MIT © [Click™]()
