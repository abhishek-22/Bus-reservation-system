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
  var sheet = SpreadsheetApp.getSheetByName("people_in_hall");
  
  for (var i = 0; i < data.length; i++) {
    var row = data[i];
    sheet.appendRow([row.field1, row.field2, row.field3]);
  }
}

function getCondition() {
  var sheet = SpreadsheetApp.getSheetByName("token");
  var cellA1 = sheet.getRange("A1");
  var value = new Date(cellA1.getValue());
  var currentTime = new Date();
  var twentyHoursLater = new Date(currentTime.getTime() + 20*60*60*1000);
  
  if (value < twentyHoursLater || !value) {
    var url = "API_URL";
    var headers = {
      "username": "YOUR_USERNAME",
      "password": "YOUR_PASSWORD"
    };
    var options = {
      "headers": headers
    };
    var response = UrlFetchApp.fetch(url, options);
    var json = response.getContentText();
    var data = JSON.parse(json);
    var date = new Date(data.date);
    cellA1.setValue(date);
    var cellB1 = sheet.getRange("B1");
    cellB1.setValue(data.token);
    return data.token;
  } else {
    var cellB1 = sheet.getRange("B1");
    return cellB1.getValue();
  }
}
