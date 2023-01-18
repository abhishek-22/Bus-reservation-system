function importData() {
  var condition = getCondition();
  var url = "API_URL";
  var headers = {
    "Authorization": "Bearer "+condition,
  };
  var options = {
    "headers": headers
  };
  var response = UrlFetchApp.fetch(url, options);
  var json = response.getContentText();
  var data = JSON.parse(json);
  var sheet = SpreadsheetApp.getActiveSheet();
  
  for (var i = 0; i < data.length; i++) {
    var row = data[i];
    sheet.appendRow([row.field1, row.field2, row.field3]);
  }
}

function getCondition() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var cell = sheet.getRange("A1");
  var value = new Date(cell.getValue());
  var currentTime = new Date();
  var twentyHoursLater = new Date(currentTime.getTime() + 20*60*60*1000);
  
  if (value < twentyHoursLater) {
    return "token_1";
  } else {
    return "token_2";
  }
}
