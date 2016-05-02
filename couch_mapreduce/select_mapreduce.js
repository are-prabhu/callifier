//This script will allow to select the doc for the token 
//Command to use select 
//curl  -X GET http://admin:admin@172.17.0.2:5984/callifi/_design/test/_view/test?key="[\"foneall\"]" --globoff

function(doc) {
  if (doc.account_token && doc._id)
  emit([doc._id], {"account_token":doc.account_token});
}
