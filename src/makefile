all:

flask_run:
	export FLASK_APP=run.py ; export FLASK_ENV=development ; flask run 

post_session:
	curl -X post localhost:5000/session -d '{"password":"098f6bcd4621d373cade4e832627b4f6","email": "valtair.juior@unemat.br"}' -H 'content-type:application/json'

post_usercontroller:

get_usercontroller:
	curl -X get localhost:5000/user -H 'authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxLCJleHAiOjE1ODA0ODk4NTcuMDg3MzI2NX0.xjusbNPzsFMX9Qf8fBYapg9aMd1fV2VPeDPslnJHglY'
put_usercontroller:
	curl -X put localhost:5000/user -d '{"password":"123","email": "valtair.juior@unemat.br"}' -H 'content-type:application/json' -H 'authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxLCJleHAiOjE1ODA0ODk4NTcuMDg3MzI2NX0.xjusbNPzsFMX9Qf8fBYapg9aMd1fV2VPeDPslnJHglY'
delete_usercontroller: