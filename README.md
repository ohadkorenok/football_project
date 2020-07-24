# football_project
Tornado - Mongo based backend for managing football association


## Running the environment:
If you don't have docker-compose installed, please install docker compose. I use it in linux via `pip install docker-compose`.

Next, run the following command to initialize the environment : `docker-compose up -d --build`


### API examples:
https://documenter.getpostman.com/view/3989244/T1DpCdE8?version=latest

In addition, attached the postman collection of this API for easy testing. For using it, please open Postman, and 
import the BeamUp.postman_collection.json file.
####Please notice:
The DB will be empty so use:
Create_league to generate league_id for the creation of teams.

Create_team to generate teams for the creation of match.
  
After that, you can set the postman environment variables {{league_id}}, {{team_id}}, {{match_id}} and the requests will work easily.

### DB Management and UI (Mongo Express):
localhost:8081


Enjoy!