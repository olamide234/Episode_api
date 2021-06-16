# BLOG'S EPISODE API
This collect information of Episodes; characters involved, their location; and user's comments on individual episodes.

There are 8 endpoints altogether <br>
http://127.0.0.1:8000/api/characters/ endpoint have GET, POST requests for characters,<br>
http://127.0.0.1:8000/api/episodes/ endpoint have GET, POST requests for episodes,<br>
http://127.0.0.1:8000/api/comments/ endpoint have GET, POST requests for comments,<br>
http://127.0.0.1:8000/api/locations/ endpoint have GET requests for locations,<br>
http://127.0.0.1:8000/api/episodes/{id} endpoint have GET, PUT, PATCH, DELETE requests for individual episode,<br>
http://127.0.0.1:8000/api/characters/{id} endpoint have GET, PUT, PATCH, DELETE requests for individual character,<br>
http://127.0.0.1:8000/api/comments/{id} endpoint have GET, PUT, PATCH, DELETE requests for individual comment, <br>
http://127.0.0.1:8000/api/locations/{id} endpoint have GET, PUT, PATCH requests for individual location, <br>

On deleting a character, the location attached is also deleted. On deleting an episode, all comments attached are deleted.

## Data Requirement
Model a scenario involving the following objects, payload and relationships.

**CHARACTER DATA** : firstName ( String ) ,lastName ( String ), status ( String – 'ACTIVE' or 'DEAD' or 'UNKNOWN'), stateOfOrigin ( String ), 
 gender (String – 'MALE' or 'FEMALE'), location ( Location Data Type ) , episodes (Episode Data Type ) , created (DateTime)
 
**LOCATION DATA** : name ( String ) , latitude ( double ) , longitude (double) ,created (DateTime)

**EPISODE DATA** : name ( String ) , releaseDate ( dateTime ) , episodeCode ( String ) , characters ( Character Data Type ),
 episodeComments ( Comment Data Type ) , created (DateTime)
 
**COMMENTS DATA** : comment (String < 250 characters) , ipAddressLocation (String) ,created (DateTime)

#### NB : 
* A 'CHARACTER OBJECT' has only 'ONE LOCATION' and can feature in 'MANY EPISODES'.
* An 'EPISODE OBJECT' can have 'MANY CHARACTERS' featured in it.
* An 'EPISODE OBJECT' can have 'MANY COMMENTS' .
* “created” column refers to time at which the record was saved in the database.
* Ensure that the dateTime fields have some differences in there values so that u can do a sort in Ascending order on the data based on the column.

#### Task
* Episode list endpoint should be sorted by “releaseDate” from oldest to newest and each episode should be listed along with it the count of comments.
* Comment list Endpoint should be retrieved in reverse chronological order with the public IP address of the commenter and DateTime they were stored.
* Character Endpoint should accept sort parameters to sort by one of name, gender in ascending or descending order.
* Character Endpoint should also accept a filter parameter to filter by gender or status or location
* Search for a List of Episodes a Character featured in .
* Add a comment to an Episode Object.
